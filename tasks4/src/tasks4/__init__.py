"""tasks4 package

Entry point: `main()` — when run via `uv run tasks4` this will summarize sample paragraph descriptions
using the OpenAI Chat Completions API (ChatGPT-5-mini by default). If no API key is present a small
local fallback summarizer is used.
"""
from .client import summarize_paragraph


SAMPLE_PARAGRAPHS = [
    (
        "Implement a background job that periodically scans user activity logs, detects patterns of "
        "suspicious behavior (such as rapid failed logins from a single IP or large numbers of password "
        "reset requests), and writes alerts to the monitoring queue with a severity tag and contextual "
        "metadata for downstream analysts. The job should be configurable for frequency, thresholds, "
        "and target queues."
    ),
    (
        "Design and build an onboarding flow for new users that collects minimal required profile data, "
        "walks them through a three-step setup wizard (preferences, notification settings, and a short "
        "tour), and stores their choices in the user profile in a transactional way so incomplete setups "
        "can be resumed. The flow must be accessible and responsive on mobile devices."
    ),
]


def run(paragraphs=None, model: str = "gpt-5.0-mini", temperature: float = 0.2) -> None:
    """Run summarization over provided paragraphs.

    If `paragraphs` is None, use `SAMPLE_PARAGRAPHS`. `model` and `temperature` are passed to the
    summarizer and can be overridden from the CLI.
    """
    paragraphs = paragraphs or SAMPLE_PARAGRAPHS

    print("tasks4 — OpenAI Chat Completions experiment\n")

    for i, paragraph in enumerate(paragraphs, start=1):
        print(f"Description #{i}:")
        print(paragraph)
        print("\nSummary:")
        summary = summarize_paragraph(paragraph, model=model, temperature=temperature)
        print(f"- {summary}\n")


def main() -> None:
    """Backward-compatible main() that runs with default model & sample paragraphs."""
    run()

