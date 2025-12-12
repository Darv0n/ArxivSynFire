"""
THE SYNDICATE PIPELINE
Orchestrates the 5-cell autonomous research intelligence system.
"""
import json
import os
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional

from anthropic import Anthropic

from .cells import (
    CELLS,
    get_scanner_prompt,
    get_weaver_prompt,
    get_hyperlexic_prompt,
    get_architect_prompt,
    get_orchestra_prompt,
)
from .tools import SyndicateTools


class SyndicatePipeline:
    """
    The Arxiv Syndicate - Autonomous Research Intelligence Pipeline

    5 cells execute sequentially:
    SCANNER → WEAVER → HYPERLEXIC → ARCHITECT → ORCHESTRA → ZINE
    """

    def __init__(
        self,
        workspace: Path,
        model: str = "claude-sonnet-4-20250514",
        api_key: Optional[str] = None
    ):
        self.workspace = Path(workspace)
        self.model = model
        self.client = Anthropic(api_key=api_key)

        # Initialize tools with database
        db_path = self.workspace / "data" / "syndicate.db"
        self.tools = SyndicateTools(db_path)

        # Pipeline state
        self.run_id = None
        self.state = {}

        self._setup_workspace()

    def _setup_workspace(self):
        """Create workspace directory structure."""
        dirs = [
            self.workspace / "data",
            self.workspace / "output" / "zines",
            self.workspace / "output" / "evidence",
            self.workspace / "logs",
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)

    def run(self, query: str, verbose: bool = True) -> str:
        """
        Execute the full 5-cell pipeline.

        Args:
            query: Research topic/query to investigate
            verbose: Print progress to stdout

        Returns:
            The final zine as markdown string
        """
        self.run_id = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
        self.state = {"query": query, "run_id": self.run_id, "cells": {}}

        if verbose:
            print(f"\n{'='*60}")
            print("THE ARXIV SYNDICATE")
            print(f"Run ID: {self.run_id}")
            print(f"Query: {query}")
            print(f"{'='*60}\n")

        # CELL 1: SCANNER
        if verbose:
            print("[1/5] SCANNER - Gathering intelligence...")
        scanner_output = self._run_cell(
            "scanner",
            get_scanner_prompt(query)
        )
        self.state["cells"]["scanner"] = scanner_output
        if verbose:
            print(f"      {CELLS['scanner']['handoff_signal']}\n")

        # CELL 2: WEAVER
        if verbose:
            print("[2/5] WEAVER - Finding correlations...")
        weaver_output = self._run_cell(
            "weaver",
            get_weaver_prompt(scanner_output)
        )
        self.state["cells"]["weaver"] = weaver_output
        if verbose:
            print(f"      {CELLS['weaver']['handoff_signal']}\n")

        # CELL 3: HYPERLEXIC
        if verbose:
            print("[3/5] HYPERLEXIC - Seeing through time...")
        hyperlexic_output = self._run_cell(
            "hyperlexic",
            get_hyperlexic_prompt(weaver_output)
        )
        self.state["cells"]["hyperlexic"] = hyperlexic_output
        if verbose:
            print(f"      {CELLS['hyperlexic']['handoff_signal']}\n")

        # CELL 4: ARCHITECT
        if verbose:
            print("[4/5] ARCHITECT - Mapping paradigms...")
        architect_output = self._run_cell(
            "architect",
            get_architect_prompt(hyperlexic_output)
        )
        self.state["cells"]["architect"] = architect_output
        if verbose:
            print(f"      {CELLS['architect']['handoff_signal']}\n")

        # CELL 5: ORCHESTRA
        if verbose:
            print("[5/5] ORCHESTRA - Synthesizing emergence...")
        full_context = json.dumps(self.state["cells"], indent=2)
        zine = self._run_cell(
            "orchestra",
            get_orchestra_prompt(architect_output, full_context)
        )
        self.state["cells"]["orchestra"] = zine
        if verbose:
            print(f"      {CELLS['orchestra']['handoff_signal']}\n")

        # Save outputs
        self._save_outputs(zine)

        if verbose:
            print(f"{'='*60}")
            print("TRANSMISSION COMPLETE")
            print(f"{'='*60}\n")

        return zine

    def _run_cell(self, cell_name: str, prompt: str) -> str:
        """
        Execute a single cell with tool access.

        Args:
            cell_name: Name of the cell (scanner, weaver, etc.)
            prompt: The prompt for this cell

        Returns:
            Cell output as string
        """
        cell = CELLS[cell_name]

        # Build system prompt
        system = f"""You are {cell['name']} in THE ARXIV SYNDICATE.

Role: {cell['role']}

Personality:
{cell['personality']}

You are part of a 5-cell autonomous research intelligence pipeline.
Execute your function with precision. Stay in character.
Use the tools available to you to gather and process information.
"""

        # Filter tools for this cell
        allowed_tools = cell["allowed_tools"]
        tool_defs = [
            t for t in self.tools.get_tool_definitions()
            if t["name"] in allowed_tools
        ]

        messages = [{"role": "user", "content": prompt}]

        # Agentic loop with tool use
        max_iterations = 10
        for _ in range(max_iterations):
            response = self.client.messages.create(
                model=self.model,
                max_tokens=8192,
                system=system,
                messages=messages,
                tools=tool_defs if tool_defs else None
            )

            # Check if we're done (no tool use)
            if response.stop_reason == "end_turn":
                # Extract text response
                for block in response.content:
                    if hasattr(block, "text"):
                        return block.text
                return ""

            # Process tool calls
            tool_results = []
            assistant_content = []

            for block in response.content:
                if block.type == "text":
                    assistant_content.append(block)
                elif block.type == "tool_use":
                    assistant_content.append(block)

                    # Execute tool
                    result = self.tools.execute(
                        block.name,
                        {**block.input, "run_id": self.run_id}
                    )

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            # Add assistant response and tool results to messages
            messages.append({"role": "assistant", "content": assistant_content})
            messages.append({"role": "user", "content": tool_results})

        # If we hit max iterations, return what we have
        return "MAX_ITERATIONS_REACHED"

    def _save_outputs(self, zine: str):
        """Save zine and evidence to files."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save zine
        zine_path = self.workspace / "output" / "zines" / f"zine_{timestamp}.md"
        with open(zine_path, "w") as f:
            f.write(zine)

        # Save full state as evidence pack
        evidence_path = self.workspace / "output" / "evidence" / f"evidence_{timestamp}.json"
        with open(evidence_path, "w") as f:
            json.dump(self.state, f, indent=2)

        # Log run
        log_path = self.workspace / "logs" / "runs.log"
        with open(log_path, "a") as f:
            f.write(f"{timestamp} | {self.run_id} | {self.state['query']}\n")


def run_pipeline(
    query: str,
    workspace: str = "./workspace",
    model: str = "claude-sonnet-4-20250514",
    verbose: bool = True
) -> str:
    """
    Convenience function to run the pipeline.

    Args:
        query: Research topic to investigate
        workspace: Path to workspace directory
        model: Claude model to use
        verbose: Print progress

    Returns:
        The zine as markdown
    """
    pipeline = SyndicatePipeline(
        workspace=Path(workspace),
        model=model
    )
    return pipeline.run(query, verbose=verbose)
