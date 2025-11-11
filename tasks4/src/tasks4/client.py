import os
from typing import Optional


def _local_fallback_summary(paragraph: str) -> str:
    """Very small heuristic fallback: return a short phrase built from the first sentence (4-7 words).

    This keeps the demo runnable without network access or an API key.
    """
    # crude: take first sentence
    first = paragraph.split(".")[0]
    words = first.strip().split()
    if not words:
        return "(no summary available)"
    # take between 4 and 7 words
    cut = min(max(4, len(words)), 7)
    return " ".join(words[:cut])


def summarize_paragraph(paragraph: str, model: str = "gpt-5.0-mini", temperature: float = 0.2) -> str:
    """Summarize a paragraph into a short phrase using OpenAI Chat Completions API.

    - Reads `OPENAI_API_KEY` from environment. If missing, returns a local fallback summary.
    - On API errors, falls back to local summary.
    """
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return _local_fallback_summary(paragraph)

    try:
        import openai

        openai.api_key = key

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a concise summarizer. Return a short phrase (4-7 words) that captures the task." 
                ),
            },
            {
                "role": "user",
                "content": (
                    "Summarize the following task description as a short phrase (4-7 words):\n\n" + paragraph
                ),
            },
        ]

        resp = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=32,
        )

        # extract content safely
        choices = resp.get("choices") or []
        if not choices:
            return _local_fallback_summary(paragraph)

        content = choices[0].get("message", {}).get("content", "").strip()
        if not content:
            return _local_fallback_summary(paragraph)
        # return single-line short phrase
        return " ".join(content.splitlines()).strip()

    except Exception:
        # On any error, return a local fallback summary
        return _local_fallback_summary(paragraph)
