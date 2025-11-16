# tasks5 — Tasks manager scaffold (from spec-kit)

This directory contains a small, teaching-focused tasks manager implementation created from the spec-kit scaffold. It is intentionally minimal: a Task model, a JSON-backed storage layer, and a tiny programmatic CLI interface used for tests and examples.

Project layout (important files)
- `tasks5/src/tasks_manager/` — package source
  - `model.py` — `Task` dataclass (id, title, description, created_at, due_date, priority, status, tags)
  - `storage.py` — simple JSON `load_tasks()` / `save_tasks()` helpers (default file: `tasks5_store.json`)
  - `cli.py` — programmatic functions: `add_task`, `list_tasks`, `mark_done`, `remove_task`, `search_tasks`
- `tasks5/tests/` — unit tests for model, storage, and CLI

Quick start (run locally)

1. From the repository root, run tests using the repo venv or your preferred Python:

```bash
# Use your venv python or system python. Example using the repo venv:
/Users/alexle/csc299-project/.venv/bin/python -m pytest -q tasks5/tests

# Or with PYTHONPATH so the package in tasks5/src is importable:
PYTHONPATH=tasks5/src python3 -m pytest -q tasks5/tests
```

2. Run example usage (programmatic CLI)

```python
# Run in a Python REPL or script with PYTHONPATH=tasks5/src
from tasks_manager.cli import add_task, list_tasks, mark_done, remove_task

# Add a task
t = add_task("Buy milk", "2 liters")
print('Added:', t.id, t.title)

# List tasks
for it in list_tasks():
    print(it.id, it.title, it.status)

# Mark done (pass prefix of id allowed)
mark_done(t.id[:8])

# Remove
remove_task(t.id[:8])
```

Command-line usage notes
- The package is not installed by default. You can either set `PYTHONPATH=tasks5/src` or install the package in editable mode:

```bash
python3 -m pip install -e tasks5
# then: python -c "from tasks_manager.cli import add_task; print(add_task('x').id)"
```

Storage
- Default storage path (when using the CLI helpers) is `tasks5_store.json` in the repository root. Tests use temporary paths so they do not modify the default file.
- To persist to a different file in your scripts, call `save_tasks()`/`load_tasks()` with a path argument.

Development notes
- The implementation is intentionally small for teaching purposes. If you'd like a console entrypoint (like `python -m tasks_manager`) or a small HTTP API, I can add that.
- Consider switching to SQLite for more realistic persistence once the exercises are stable.

How this was created
- This project was scaffolded with GitHub's Spec Kit templates and then a minimal tasks manager implementation (model, storage, CLI, and tests) was added to demonstrate the feature flow.
