
# tasks-final

Final consolidated tasks manager used as a compact, teachable example. This README gives quick runnable examples you can use for a short demo.

Highlights
- Task model: `id` (UUID), `title`, `description`, `created_at` (timezone-aware ISO), `due_date`, `priority`, `status`, `tags`.
- JSON-backed storage (pluggable) with a dynamic `DEFAULT_STORE` so tests and demos can override it.
- Programmatic CLI helpers and a module entrypoint (`python -m tasks_app`).
- Tests for model, storage and CLI included under `Final Project/tests`.

Quick start (commands you can copy/paste)

1) Run the package tests (verifies core behavior)

```bash
# from repository root (uses the repo venv)
REPO=/Users/alexle/csc299-project
VENV=$REPO/.venv/bin/python
PYTHONPATH="Final Project/src" $VENV -m pytest -q "Final Project/tests"
```

2) Programmatic smoke run (safe — uses a temporary store and leaves repo unchanged)

```bash
PYTHONPATH=tasks_final/src $VENV - <<'PY'
from pathlib import Path
from tasks_app import storage, cli

tmp = Path('tmp_demo_store.json')
try:
	storage.DEFAULT_STORE = tmp
	t = cli.add_task('Demo task', 'short demo')
	print('Added:', t.id, t.title)
	print('List:', [(x.id, x.title, x.status) for x in cli.list_tasks()])
	cli.mark_done(t.id[:8])
	print('After done:', [(x.id, x.title, x.status) for x in cli.list_tasks()])
	cli.remove_task(t.id[:8])
	print('Final list:', [x.title for x in cli.list_tasks()])
````markdown

# Final Project

Final consolidated tasks manager used as a compact, teachable example. This README gives quick runnable examples you can use for a short demo.

Highlights
- Task model: `id` (UUID), `title`, `description`, `created_at` (timezone-aware ISO), `due_date`, `priority`, `status`, `tags`.
- JSON-backed storage (pluggable) with a dynamic `DEFAULT_STORE` so tests and demos can override it.
- Programmatic CLI helpers and a module entrypoint (`python -m tasks_app`).
- Tests for model, storage and CLI included under `Final Project/tests`.

Quick start (commands you can copy/paste)

Environment notes
- These examples assume macOS zsh and a repo-local virtualenv at `/Users/alexle/csc299-project/.venv` as used in the project. If you don't have that venv, substitute your Python executable for `$VENV` below.

```bash
# from repository root (adjust REPO if different)
REPO=/Users/alexle/csc299-project
VENV=$REPO/.venv/bin/python
# directory containing the package source
PKG_DIR="Final Project"
```

1) Run the package tests (verifies core behavior)

```bash
# runs pytest for the final package
PYTHONPATH="$PKG_DIR/src" $VENV -m pytest -q "$PKG_DIR/tests"
```

2) Programmatic smoke run (safe — uses a temporary store and leaves repo unchanged)

```bash
PYTHONPATH="$PKG_DIR/src" $VENV - <<'PY'
from pathlib import Path
from tasks_app import storage, cli

tmp = Path('tmp_demo_store.json')
try:
    storage.DEFAULT_STORE = tmp
    t = cli.add_task('Demo task', 'short demo')
    print('Added:', t.id, t.title)
    print('List:', [(x.id, x.title, x.status) for x in cli.list_tasks()])
    cli.mark_done(t.id[:8])
    print('After done:', [(x.id, x.title, x.status) for x in cli.list_tasks()])
    cli.remove_task(t.id[:8])
    print('Final list:', [x.title for x in cli.list_tasks()])
finally:
    try: tmp.unlink()
    except: pass
PY
```

3) Use the module CLI interactively

```bash
# add a task
PYTHONPATH="$PKG_DIR/src" $VENV -m tasks_app add "Buy snacks" "For demo"

# list tasks
PYTHONPATH="$PKG_DIR/src" $VENV -m tasks_app list

# mark done (use full id or prefix)
PYTHONPATH="$PKG_DIR/src" $VENV -m tasks_app done <id-or-prefix>

# search
PYTHONPATH="$PKG_DIR/src" $VENV -m tasks_app search "snack"

# remove
PYTHONPATH="$PKG_DIR/src" $VENV -m tasks_app remove <id-or-prefix>
```

Install editable (optional)

```bash
# install in your venv so you can run without PYTHONPATH
$VENV -m pip install -e "$PKG_DIR"
# then run without PYTHONPATH
$VENV -m tasks_app list
```

Notes on storage
- Default file: `final_project_store.json` in the repo root. For demos and tests set `storage.DEFAULT_STORE` to a temp path (see the smoke/script examples) or pass a path to `load_tasks`/`save_tasks`.
- To avoid committing local demo state, remove and ignore the store file before committing changes:

```bash
git rm --cached final_project_store.json || true
echo "final_project_store.json" >> .gitignore
git add .gitignore && git commit -m "chore: ignore local tasks store" || true
```

Developer tips
- If you see timezone warnings, the package uses timezone-aware datetimes; this is intentional. When serializing/deserializing in other systems, prefer UTC-aware parsing.
- For CI: add `pytest-cov` and a coverage badge if you want to enforce coverage thresholds.

How to create a quick rehearsal script

Below is an example `scripts/demo.sh` you can copy that runs tests, a smoke snippet, and a short module-CLI flow. It uses a temporary store so the repo is unchanged.

```bash
#!/usr/bin/env bash
set -euo pipefail
REPO=/Users/alexle/csc299-project
VENV=$REPO/.venv/bin/python
PKG_DIR="Final Project"

echo "Running tests..."
PYTHONPATH="$PKG_DIR/src" $VENV -m pytest -q "$PKG_DIR/tests"

echo "Running smoke script..."
PYTHONPATH="$PKG_DIR/src" $VENV - <<'PY'
from pathlib import Path
from tasks_app import storage, cli
tmp = Path('tmp_demo_store.json')
try:
    storage.DEFAULT_STORE = tmp
    t = cli.add_task('Demo run', 'auto')
    print('OK added:', t.id)
    cli.mark_done(t.id[:8])
    print('Search:', [x.title for x in cli.search_tasks('Demo')])
    cli.remove_task(t.id[:8])
finally:
    try: tmp.unlink()
    except: pass
PY

echo "Done demo run."
```


````

