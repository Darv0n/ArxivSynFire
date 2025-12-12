# THE ARXIV SYNDICATE

<div align="center">

```
╔═══════════════════════════════════════════════════════════════════╗
║                     THE ARXIV SYNDICATE                           ║
║           "Where the future leaks before it's announced"          ║
╚═══════════════════════════════════════════════════════════════════╝
```

[![License: MIT](https://img.shields.io/badge/License-MIT-00ff88.svg)](https://opensource.org/licenses/MIT)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

**Underground research intelligence network with emergence synthesis for tracking technological acceleration, semantic paper correlation, and paradigm shift detection.**

[View Demo](https://arxivsyndicate.dev) · [Report Bug](https://github.com/yourusername/ArxivSynFire/issues) · [Request Feature](https://github.com/yourusername/ArxivSynFire/issues)

</div>

---

## About

The Arxiv Syndicate is an underground research intelligence network that tracks the future before it's announced. This repository contains the website/landing page for the Syndicate, showcasing its 5-cell intelligence pipeline and methodology.

### The Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                     THE ARXIV SYNDICATE                         │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
   [NEWS FEED]          [ARXIV FIREHOSE]      [PATENT DUMPS]
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    THE SCANNER    │  ← Daily Intelligence Intake
                    └─────────┬─────────┘
                              │
                    ┌───────────────────┐
                    │    THE WEAVER     │  ← Semantic Correlation Engine
                    └─────────┬─────────┘
                              │
                    ┌───────────────────┐
                    │   THE HYPERLEXIC  │  ← Deep Pattern Seer
                    └─────────┬─────────┘
                              │
                    ┌───────────────────┐
                    │    THE ARCHITECT  │  ← Paradigm Mapper
                    └─────────┬─────────┘
                              │
                    ┌───────────────────┐
                    │   THE ORCHESTRA   │  ← Shadow Savant
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │     THE ZINE      │
                    │ + EVIDENCE PACK   │
                    └───────────────────┘
```

### The Cells

| Cell | Role | Vector | Personality |
|------|------|--------|-------------|
| **THE SCANNER** | Daily Intelligence Intake | GATHERING | Obsessive, paranoid, FOMO weaponized |
| **THE WEAVER** | Semantic Correlation Engine | CORRELATION | Pattern-addicted, citation-graph romantic |
| **THE HYPERLEXIC** | Deep Pattern Seer | DEPTH | Pre-internet pattern brain, information-sexual |
| **THE ARCHITECT** | Paradigm Mapper | STRUCTURE | Epoch-aware, dreams in phase transitions |
| **THE ORCHESTRA** | Shadow Savant | EMERGENCE | Wounded genius, arctic pragmatist |

---

## Features

### Website Features

- **Cyberpunk Aesthetic** - Dark theme with neon green accents and terminal-style typography
- **Animated Pipeline** - Interactive visualization of the 5-cell architecture
- **Cell Cards** - Detailed breakdowns of each cell's personality, voice, and function
- **Pattern Library** - Reference section for mathematical equivalences
- **Epochs Timeline** - ML/AI paradigm evolution visualization
- **Terminal Animation** - Interactive typing effect demonstrating activation
- **Responsive Design** - Optimized for all screen sizes
- **Easter Egg** - Konami code unlocks secret mode

### Technical Features

- Pure HTML/CSS/JavaScript (no frameworks)
- CSS custom properties for theming
- Intersection Observer for scroll animations
- Smooth scroll navigation
- Parallax grid effect
- Glitch text animations
- Console easter egg for developers

---

## The Agent (NEW)

**The Syndicate is now autonomous.** The `agent/` directory contains a fully functional CLI tool that runs the 5-cell pipeline using Claude.

### Quick Start

```bash
# Install
pip install -e .

# Set your API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Run
syndicate "mechanistic interpretability"
```

### Usage

```bash
# Basic query
syndicate "vision transformers, multimodal models"

# Custom workspace
syndicate --topic "RL from human feedback" --workspace ./my_runs

# Cron mode (quiet, outputs zine to stdout)
syndicate --cron --topic "weekly AI digest" > zine.md

# Use Opus for deeper analysis
syndicate "quantum computing" --model claude-opus-4-1-20250805
```

### Cron Example

```bash
# Every Monday at 9am, generate weekly digest
0 9 * * MON ANTHROPIC_API_KEY=sk-... /usr/local/bin/syndicate --cron "weekly ML digest" >> /var/log/syndicate/zines.md
```

### Architecture

```
USER/CRON
    │
    ▼
┌───────────────────────────────────────────┐
│           SYNDICATE CORE                   │
│  ┌─────────────────────────────────────┐  │
│  │         Claude SDK Client           │  │
│  └─────────────────────────────────────┘  │
│  ┌─────────────────────────────────────┐  │
│  │    MCP Tools (arxiv, semantic       │  │
│  │    scholar, persistence)            │  │
│  └─────────────────────────────────────┘  │
└───────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────┐
│              5-CELL PIPELINE                 │
│  SCANNER → WEAVER → HYPERLEXIC → ARCHITECT  │
│                    → ORCHESTRA              │
└─────────────────────────────────────────────┘
    │
    ▼
┌───────────────────────────────────────────┐
│              OUTPUTS                       │
│  • THE ZINE (markdown)                    │
│  • Evidence Pack (JSON)                   │
│  • Graveyard (SQLite)                     │
└───────────────────────────────────────────┘
```

---

## The Website

A cyberpunk landing page showcasing the Syndicate's methodology.

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge)
- Optional: Node.js for local development server

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Darv0n/ArxivSynFire.git
   cd ArxivSynFire
   ```

2. **Open directly in browser**
   ```bash
   open src/index.html
   # or on Linux
   xdg-open src/index.html
   ```

3. **Or use a local server** (recommended)
   ```bash
   # With npm
   npm install
   npm start

   # With Python
   python -m http.server 8000 -d src

   # With PHP
   php -S localhost:8000 -t src
   ```

4. **Visit** `http://localhost:8000`

---

## Project Structure

```
ArxivSynFire/
├── agent/                  # AUTONOMOUS AGENT (NEW)
│   ├── __init__.py
│   ├── cli.py              # Command-line interface
│   ├── pipeline.py         # 5-cell orchestrator
│   ├── cells.py            # Cell prompts & personalities
│   ├── tools.py            # MCP tools (arxiv, semantic scholar, etc)
│   └── requirements.txt
├── src/                    # WEBSITE
│   ├── index.html          # Main HTML file
│   ├── styles.css          # All styles
│   ├── script.js           # Interactivity & animations
│   └── favicon.svg
├── docs/
│   ├── PIPELINE.md         # Detailed pipeline documentation
│   ├── CELLS.md            # Cell specifications
│   ├── PATTERNS.md         # Pattern library reference
│   └── ZINE_STRUCTURE.md   # Zine output format
├── workspace/              # Runtime outputs (gitignored)
│   └── output/
│       ├── zines/          # Generated zines
│       └── evidence/       # Evidence packs
├── pyproject.toml          # Python package config
├── vercel.json             # Vercel deployment config
├── .gitignore
├── LICENSE
├── README.md
├── CONTRIBUTING.md
└── package.json
```

---

## The Zine Output

The Syndicate produces a structured intelligence zine with the following sections:

```
═══════════════════════════════════════════════════════════════════
              THE ARXIV SYNDICATE — SIGNAL ZINE
                 [DATE] — TRANSMISSION #[N]
           "Where the future leaks before it's announced"
═══════════════════════════════════════════════════════════════════

▓▓▓ THE DROP ▓▓▓         → What landed this week that matters
▓▓▓ THE GEMS ▓▓▓         → Hidden papers everyone should read
▓▓▓ THE HYPE CHECK ▓▓▓   → What's overblown vs. what's real
▓▓▓ THE PATTERN ▓▓▓      → Convergences and echoes forming
▓▓▓ THE PARADIGM ▓▓▓     → Where we are in the epoch
▓▓▓ THE EMERGENCE ▓▓▓    → What forms in the spaces between
▓▓▓ THE MACHIAVELLI ▓▓▓  → Power plays and money flows
▓▓▓ THE CALLS ▓▓▓        → Dated, specific predictions
▓▓▓ THE GRAVEYARD ▓▓▓    → Past predictions, scored
▓▓▓ THE READING LIST ▓▓▓ → Subversive curriculum
```

Every zine ships with an **Evidence Pack** — full chain of analysis from intake to synthesis.

---

## Pattern Library

Core equivalences the Hyperlexic recognizes:

| Pattern | Meaning |
|---------|---------|
| *"Attention is matrix factorization"* | Self-attention = softmax over dot products = learned factorization |
| *"Diffusion is score matching is denoising"* | Three names, one idea, decades apart |
| *"Transformers are Hopfield networks"* | 1982 → 2017, same core mechanics |
| *"RL is just search with gradients"* | Policy gradient = differentiable search |
| *"Everything is optimization"* | Training, inference, evolution, markets |
| *"Everything is compression"* | Learning = compression = intelligence |

---

## Epochs

Know where you are in the cycle:

| Era | Years | Signal |
|-----|-------|--------|
| **PRE-DEEP** | before 2012 | "features matter more than models" |
| **DEEP LEARNING I** | 2012-2017 | "depth matters" |
| **DEEP LEARNING II** | 2017-2022 | "scale is all you need" |
| **FOUNDATION MODELS** | 2022-2024 | "generalists beat specialists" |
| **???** | emerging | [watch the indicators] |

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## Acknowledgments

- Font: [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
- Font: [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk)
- Inspiration: The PhDs who publish before the press release

---

<div align="center">

```
Stay paranoid. Stay curious. Stay ahead.

— The Syndicate
```

*The math is in the margins. The predictions are dated. Check the receipts.*

</div>
