```markdown
# Implementation plan — Tasks Manager (001-build-tasks-manager)

This plan breaks the work into small, testable steps that implement the milestones from `spec.md`.

## Objectives
- Deliver a compact, well-tested tasks manager suitable for teaching.
- Keep the storage layer pluggable (default JSON file). CLI implements add/list/done/remove/search.

## Timeline & phases

Phase A — Plan & scaffolding (this file)
- Deliverable: `plan.md` (this file) populated with tasks, acceptance criteria, and estimates.

Phase B — Core model & in-memory ops (M2)
- Implement `Task` dataclass in `src/tasks_manager/model.py` with `to_dict`/`from_dict`.
- Unit tests: creation, serialization, required/optional fields, and status transitions.
- Estimate: 1–2 hours.

Phase C — Storage layer (M3)
- Implement JSON file storage in `src/tasks_manager/storage.py`.
- API: `load_tasks(path=None) -> list[Task]` and `save_tasks(tasks, path=None) -> None`.
- Keep default path configurable (not bound at import time) to allow test monkeypatching.
- Unit tests: read/write round-trip, missing file handling (return empty list), concurrent writes (basic atomic write via temp file + rename).
- Estimate: 1–2 hours.

Phase D — CLI and glue (M4)
- Implement programmatic CLI functions in `src/tasks_manager/cli.py`: `add_task(title, description, ...)`, `list_tasks()`, `mark_done(id)`, `remove_task(id)`, `search_tasks(keyword)`.
- Provide `__main__.py` to expose `python -m tasks_manager <cmd>` and produce stable, parseable output for tests.
- Unit/integration tests: call CLI functions directly and test `__main__` via subprocess or `runpy` (use PYTHONPATH in tests).
- Estimate: 2–3 hours.

Phase E — Docs, examples & polish (M5)
- Update `README.md` with run instructions, examples, and developer notes (how to run tests, how to change storage backend).
- Add a small example in `examples/` (optional) demonstrating add/list flow.
- Estimate: 1 hour.

Phase F — CI & optional storage migration
- Add GitHub Actions workflow to run pytest on push/PR to feature branches and main.
- Optional: implement SQLite backend in `storage_sqlite.py` and migration helpers.
- Estimate: 1–3 hours depending on scope.

## Acceptance criteria (mapping to spec)
- Task model fields are present and serializable (tests pass).
- CLI commands behave as described and tests cover add/list/done/remove/search.
- Storage read/write round-trip covered by tests; default store file is not committed to the repo.
- README contains usage with `python -m tasks_manager` examples.

## Risks & mitigations
- Binding a default file path at import time prevents test isolation — mitigate by resolving defaults at call time and allowing explicit `path` params in storage API.
- Simultaneous writes: implement atomic write (write to temp file + rename) to reduce corruption risk.

## Quick checklist for the next commit
1. Add/verify `Task` dataclass and unit tests (already present in `tasks5/src/tasks_manager/model.py`).
2. Ensure `storage.load_tasks` / `save_tasks` accept `path=None` and resolve a module-level default dynamically.
3. Add/verify CLI tests and `__main__.py` (already present). Run `pytest` and fix any failures.
4. Update `README.md` with usage examples and note that `OPENAI_API_KEY` or similar are not required (project uses JSON storage by default).

## Who does what (if needed)
- I can generate and push the `plan.md` (done now).
- Next I can: add CI, or create a PR from `001-build-tasks-manager` to `main` with the checklist.

``` 
