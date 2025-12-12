#!/usr/bin/env python3
"""
THE ARXIV SYNDICATE - Command Line Interface

Usage:
    syndicate "mechanistic interpretability"
    syndicate --topic "vision transformers" --workspace ./runs
    syndicate --cron --topic "weekly ML digest"
"""
import argparse
import sys
from pathlib import Path

from .pipeline import SyndicatePipeline


def main():
    parser = argparse.ArgumentParser(
        prog="syndicate",
        description="THE ARXIV SYNDICATE - Autonomous Research Intelligence",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  syndicate "mechanistic interpretability"
  syndicate --topic "diffusion models" --model claude-opus-4-1-20250805
  syndicate --topic "RL from human feedback" --workspace ./custom_workspace
  syndicate --cron --topic "weekly AI digest"

The pipeline executes 5 cells sequentially:
  SCANNER   → Gathers papers from ArXiv, Semantic Scholar
  WEAVER    → Finds hidden connections and correlations
  HYPERLEXIC → Identifies patterns, novelty, and historical echoes
  ARCHITECT → Maps paradigms and epoch positions
  ORCHESTRA → Synthesizes THE ZINE
        """
    )

    parser.add_argument(
        "query",
        nargs="?",
        help="Research topic/query (alternative to --topic)"
    )

    parser.add_argument(
        "-t", "--topic",
        type=str,
        help="Research topic/query to investigate"
    )

    parser.add_argument(
        "-w", "--workspace",
        type=Path,
        default=Path("./workspace"),
        help="Workspace directory for outputs (default: ./workspace)"
    )

    parser.add_argument(
        "-m", "--model",
        type=str,
        default="claude-sonnet-4-20250514",
        help="Claude model to use (default: claude-sonnet-4-20250514)"
    )

    parser.add_argument(
        "--cron",
        action="store_true",
        help="Run in cron mode (minimal output, suitable for scheduled jobs)"
    )

    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output file for the zine (default: stdout in cron mode)"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    args = parser.parse_args()

    # Determine query
    query = args.query or args.topic
    if not query:
        parser.error("Query required. Use positional argument or --topic")

    # Run pipeline
    try:
        pipeline = SyndicatePipeline(
            workspace=args.workspace,
            model=args.model
        )

        verbose = not args.cron
        zine = pipeline.run(query, verbose=verbose)

        # Output handling
        if args.output:
            with open(args.output, "w") as f:
                f.write(zine)
            if verbose:
                print(f"Zine saved to: {args.output}")
        elif args.cron:
            # In cron mode, output zine to stdout
            print(zine)
        else:
            # In interactive mode, zine is already saved to workspace
            print(f"\nZine saved to: {args.workspace}/output/zines/")

        return 0

    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        return 130

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if not args.cron:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
