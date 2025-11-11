tasks4 — OpenAI Chat Completions experiment

This small package demonstrates calling the OpenAI Chat Completions API to summarize paragraph-length task descriptions into short phrase summaries.

Usage
- Set your OpenAI API key in the environment: `export OPENAI_API_KEY=...`
- Run with uv (from the repository root): `uv run tasks4`

If `OPENAI_API_KEY` is not set the script falls back to a lightweight local summarizer so you can still test the flow.
