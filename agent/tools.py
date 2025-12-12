"""
MCP Tools for THE ARXIV SYNDICATE
In-process tools for data acquisition and persistence.
"""
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET


class SyndicateTools:
    """Collection of tools for the Syndicate pipeline."""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize SQLite database schema."""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS papers (
                arxiv_id TEXT PRIMARY KEY,
                title TEXT,
                authors TEXT,
                summary TEXT,
                categories TEXT,
                published TEXT,
                pdf_url TEXT,
                fetched_at TEXT
            );

            CREATE TABLE IF NOT EXISTS cell_state (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                cell_name TEXT NOT NULL,
                output TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS graveyard (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                paper_id TEXT,
                reason TEXT,
                cell_name TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS zines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_id TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );

            CREATE INDEX IF NOT EXISTS idx_cell_state_run ON cell_state(run_id);
            CREATE INDEX IF NOT EXISTS idx_graveyard_run ON graveyard(run_id);
        """)
        conn.commit()
        conn.close()

    def get_tool_definitions(self) -> list[dict]:
        """Return tool definitions for Claude."""
        return [
            {
                "name": "arxiv_search",
                "description": "Search ArXiv for papers. Returns titles, abstracts, authors, dates, and arxiv IDs.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query (supports boolean operators, field prefixes like ti:, au:, abs:)"
                        },
                        "max_results": {
                            "type": "integer",
                            "description": "Maximum papers to return (default 25, max 100)",
                            "default": 25
                        },
                        "sort_by": {
                            "type": "string",
                            "enum": ["relevance", "lastUpdatedDate", "submittedDate"],
                            "default": "submittedDate"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "fetch_paper",
                "description": "Fetch detailed metadata for a specific ArXiv paper by ID.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "arxiv_id": {
                            "type": "string",
                            "description": "ArXiv paper ID (e.g., '2301.07041' or 'cs.LG/2301.07041')"
                        }
                    },
                    "required": ["arxiv_id"]
                }
            },
            {
                "name": "semantic_scholar_search",
                "description": "Search Semantic Scholar for papers with citation data.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query"
                        },
                        "limit": {
                            "type": "integer",
                            "default": 20
                        },
                        "fields": {
                            "type": "string",
                            "description": "Comma-separated fields to return",
                            "default": "title,authors,year,citationCount,abstract,url"
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "save_state",
                "description": "Persist cell output to database for handoff to next cell.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "cell_name": {"type": "string"},
                        "output": {"type": "string"}
                    },
                    "required": ["run_id", "cell_name", "output"]
                }
            },
            {
                "name": "load_state",
                "description": "Retrieve previous cell output from database.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "cell_name": {"type": "string"}
                    },
                    "required": ["run_id", "cell_name"]
                }
            },
            {
                "name": "add_to_graveyard",
                "description": "Record a paper sent to the graveyard (filtered out) with reason.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "paper_id": {"type": "string"},
                        "reason": {"type": "string"},
                        "cell_name": {"type": "string"}
                    },
                    "required": ["run_id", "paper_id", "reason", "cell_name"]
                }
            },
            {
                "name": "save_zine",
                "description": "Save the final zine output.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "required": ["run_id", "content"]
                }
            }
        ]

    def execute(self, tool_name: str, args: dict[str, Any]) -> str:
        """Execute a tool and return result as string."""
        handlers = {
            "arxiv_search": self._arxiv_search,
            "fetch_paper": self._fetch_paper,
            "semantic_scholar_search": self._semantic_scholar,
            "save_state": self._save_state,
            "load_state": self._load_state,
            "add_to_graveyard": self._add_to_graveyard,
            "save_zine": self._save_zine,
        }

        handler = handlers.get(tool_name)
        if not handler:
            return json.dumps({"error": f"Unknown tool: {tool_name}"})

        try:
            return handler(args)
        except Exception as e:
            return json.dumps({"error": str(e)})

    def _arxiv_search(self, args: dict) -> str:
        """Search ArXiv API."""
        query = args.get("query", "")
        max_results = min(args.get("max_results", 25), 100)
        sort_by = args.get("sort_by", "submittedDate")

        base_url = "http://export.arxiv.org/api/query"
        params = {
            "search_query": f"all:{query}",
            "start": 0,
            "max_results": max_results,
            "sortBy": sort_by,
            "sortOrder": "descending"
        }

        url = f"{base_url}?{urllib.parse.urlencode(params)}"

        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read().decode('utf-8')

        # Parse Atom feed
        ns = {
            'atom': 'http://www.w3.org/2005/Atom',
            'arxiv': 'http://arxiv.org/schemas/atom'
        }
        root = ET.fromstring(data)

        papers = []
        for entry in root.findall('atom:entry', ns):
            arxiv_id = entry.find('atom:id', ns).text.split('/abs/')[-1]
            title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            published = entry.find('atom:published', ns).text

            authors = [
                author.find('atom:name', ns).text
                for author in entry.findall('atom:author', ns)
            ]

            categories = [
                cat.get('term')
                for cat in entry.findall('atom:category', ns)
            ]

            pdf_link = None
            for link in entry.findall('atom:link', ns):
                if link.get('title') == 'pdf':
                    pdf_link = link.get('href')
                    break

            papers.append({
                "arxiv_id": arxiv_id,
                "title": title,
                "authors": authors,
                "summary": summary[:500] + "..." if len(summary) > 500 else summary,
                "published": published,
                "categories": categories,
                "pdf_url": pdf_link
            })

            # Cache in database
            self._cache_paper(arxiv_id, title, authors, summary, categories, published, pdf_link)

        return json.dumps({"count": len(papers), "papers": papers}, indent=2)

    def _fetch_paper(self, args: dict) -> str:
        """Fetch single paper by ID."""
        arxiv_id = args.get("arxiv_id", "").replace("arXiv:", "")

        # Check cache first
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM papers WHERE arxiv_id = ?", (arxiv_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return json.dumps({
                "arxiv_id": row[0],
                "title": row[1],
                "authors": json.loads(row[2]) if row[2] else [],
                "summary": row[3],
                "categories": json.loads(row[4]) if row[4] else [],
                "published": row[5],
                "pdf_url": row[6],
                "cached": True
            }, indent=2)

        # Fetch from API
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"

        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read().decode('utf-8')

        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        root = ET.fromstring(data)
        entry = root.find('atom:entry', ns)

        if entry is None:
            return json.dumps({"error": f"Paper not found: {arxiv_id}"})

        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        summary = entry.find('atom:summary', ns).text.strip()
        published = entry.find('atom:published', ns).text

        authors = [
            author.find('atom:name', ns).text
            for author in entry.findall('atom:author', ns)
        ]

        categories = [
            cat.get('term')
            for cat in entry.findall('atom:category', ns)
        ]

        pdf_link = None
        for link in entry.findall('atom:link', ns):
            if link.get('title') == 'pdf':
                pdf_link = link.get('href')
                break

        self._cache_paper(arxiv_id, title, authors, summary, categories, published, pdf_link)

        return json.dumps({
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": authors,
            "summary": summary,
            "categories": categories,
            "published": published,
            "pdf_url": pdf_link
        }, indent=2)

    def _semantic_scholar(self, args: dict) -> str:
        """Search Semantic Scholar API."""
        query = args.get("query", "")
        limit = min(args.get("limit", 20), 100)
        fields = args.get("fields", "title,authors,year,citationCount,abstract,url")

        base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            "query": query,
            "limit": limit,
            "fields": fields
        }

        url = f"{base_url}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url, headers={"User-Agent": "ArxivSyndicate/1.0"})

        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode('utf-8'))

            papers = data.get("data", [])
            return json.dumps({"count": len(papers), "papers": papers}, indent=2)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                return json.dumps({"error": "Rate limited. Try again in a few seconds."})
            return json.dumps({"error": f"HTTP {e.code}: {e.reason}"})

    def _cache_paper(self, arxiv_id, title, authors, summary, categories, published, pdf_url):
        """Cache paper in database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO papers
            (arxiv_id, title, authors, summary, categories, published, pdf_url, fetched_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            arxiv_id, title, json.dumps(authors), summary,
            json.dumps(categories), published, pdf_url,
            datetime.now().isoformat()
        ))
        conn.commit()
        conn.close()

    def _save_state(self, args: dict) -> str:
        """Save cell state to database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cell_state (run_id, cell_name, output)
            VALUES (?, ?, ?)
        """, (args["run_id"], args["cell_name"], args["output"]))
        conn.commit()
        conn.close()
        return json.dumps({"status": "saved", "cell": args["cell_name"]})

    def _load_state(self, args: dict) -> str:
        """Load cell state from database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT output FROM cell_state
            WHERE run_id = ? AND cell_name = ?
            ORDER BY created_at DESC LIMIT 1
        """, (args["run_id"], args["cell_name"]))
        row = cursor.fetchone()
        conn.close()

        if row:
            return row[0]
        return json.dumps({"error": f"No state found for {args['cell_name']}"})

    def _add_to_graveyard(self, args: dict) -> str:
        """Add paper to graveyard."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO graveyard (run_id, paper_id, reason, cell_name)
            VALUES (?, ?, ?, ?)
        """, (args["run_id"], args["paper_id"], args["reason"], args["cell_name"]))
        conn.commit()
        conn.close()
        return json.dumps({"status": "buried", "paper": args["paper_id"]})

    def _save_zine(self, args: dict) -> str:
        """Save final zine."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO zines (run_id, content) VALUES (?, ?)
        """, (args["run_id"], args["content"]))
        conn.commit()
        conn.close()
        return json.dumps({"status": "zine_saved", "run_id": args["run_id"]})
