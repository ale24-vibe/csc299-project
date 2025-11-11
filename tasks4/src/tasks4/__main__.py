"""Make the package executable with `python -m tasks4`.

This module simply calls the package `main()` entrypoint.
"""
import argparse
from . import run


def _parse_args():
    p = argparse.ArgumentParser(description="Summarize paragraph-length task descriptions.")
    p.add_argument("--model", default="gpt-5.0-mini", help="Model name to use (default: gpt-5.0-mini)")
    p.add_argument("--temperature", type=float, default=0.2, help="Temperature for the model (default: 0.2)")
    p.add_argument("--input-file", help="Path to a text file containing paragraphs separated by blank lines")
    return p.parse_args()


def _load_paragraphs_from_file(path: str):
    text = open(path, "r", encoding="utf-8").read()
    # split on two or more newlines
    parts = [p.strip() for p in text.split("\n\n") if p.strip()]
    return parts


if __name__ == "__main__":
    args = _parse_args()
    paragraphs = None
    if args.input_file:
        paragraphs = _load_paragraphs_from_file(args.input_file)
    run(paragraphs=paragraphs, model=args.model, temperature=args.temperature)
