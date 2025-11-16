# 001 — Build a tasks manager "built in class"

## Summary

Create a small, well-tested tasks manager application that mirrors the "built in class" assignment used in the course. The application should provide a clear domain model for tasks, support adding/listing/updating tasks, and include a minimal CLI (and optionally a small HTTP API) so the resulting project can be used for teaching and extension. The implementation will prioritize clarity, automated tests, and straightforward developer setup.

## Goals

- Provide a compact, documented tasks manager that students can read and extend.
- Include a clear Task model, persistent storage (file-based or SQLite), and basic operations: create, list, update (status), delete.
- Ship a small CLI that demonstrates the core operations and a tiny test-suite verifying behavior.
- Keep third-party dependencies minimal and prefer standard library when reasonable.

## Non-Goals

- Not a full-featured production task tracking product (no multi-user auth, no web UI beyond minimal API).

## Users & Personas

- Student / Learner: wants a small, readable codebase to learn from.
- Instructor: wants reproducible tests and deterministic behavior for grading.

## Requirements / Acceptance Criteria

1. The repo exposes a clear Task model with the following fields: id (uuid), title, description, created_at, due_date (optional), priority (low/medium/high), status (open/done), tags (list).
2. Persistent storage: a JSON file or SQLite database with simple migration path.
3. CLI: commands `add`, `list`, `done <id>`, `remove <id>` and `search <keyword>` with clear output.
4. Tests: unit tests covering model, storage, and CLI glue logic with >= 80% coverage for core modules.
5. README with run instructions, tests, and examples.

## Constraints

- Keep the code size small (target ~200–500 LOC for the core app).
- Prefer Python 3.10+ or the project's configured Python runtime.

## Data model (Task)

- id: string (uuid)
- title: string (required)
- description: string (optional)
- created_at: ISO-8601 timestamp
- due_date: ISO-8601 timestamp or null
- priority: enum {low, medium, high}
- status: enum {open, done}
- tags: list[string]

## Developer workflow

1. Create a feature branch (done): `001-build-tasks-manager`.
2. Populate `spec.md` (this file) and `plan.md` (implementation plan).
3. Implement core modules under `src/` and tests under `tests/`.
4. Run tests and ensure they pass: `python -m pytest`.

## Minimal Milestones / Tasks

- M1: Initialize project structure (src/, tests/, pyproject) and add README.
- M2: Implement Task model and in-memory operations with tests.
- M3: Implement storage (file-based JSON) and tests.
- M4: Implement CLI and glue tests for CLI behavior.
- M5: Add basic documentation and examples.

## Acceptance / Demo

- Show sample run: `python -m tasks_manager add "Buy milk" "2 liters"` then `python -m tasks_manager list`.

## Risks / Open Questions

- Choose JSON vs SQLite for storage. JSON is easiest for teaching; SQLite is more realistic. We'll default to JSON, but keep storage layer pluggable.

## Next steps for implementation

1. Populate `plan.md` with a task breakdown (I can do this next).
2. Implement M1–M3 in small commits, run unit tests, and open a PR for review.

