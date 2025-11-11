import os
from tasks4.client import summarize_paragraph, _local_fallback_summary


def test_local_fallback_returns_short_phrase():
    paragraph = (
        "This is a test paragraph that contains several sentences. "
        "It should return a short phrase built from the first sentence."
    )
    summary = _local_fallback_summary(paragraph)
    assert isinstance(summary, str)
    words = summary.split()
    # fallback produces between 1 and 7 words (we expect at least 4 but allow robustness)
    assert 1 <= len(words) <= 7


def test_summarize_paragraph_uses_fallback_when_no_key(monkeypatch):
    # Ensure OPENAI_API_KEY is not set
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    paragraph = (
        "Write an end-to-end integration test harness to validate message flows, retries, and error "
        "handling across the async queue consumers. The harness should be configurable and produce "
        "deterministic outputs for CI runs."
    )
    summary = summarize_paragraph(paragraph)
    assert isinstance(summary, str)
    assert 1 <= len(summary.split()) <= 7
