# final_project — compact task manager

A small, teachable task manager with a simple REPL and a module CLI. This README shows the essential commands to run and demo the project.

Prerequisites
- Python 3.10+
- (Optional) a repo-local virtualenv at /Users/alexle/csc299-project/.venv — examples below assume it exists.

Quick variables

```bash
REPO=/Users/alexle/csc299-project
VENV=$REPO/.venv/bin/python
PKG_DIR=final_project
```

Run tests

```bash
PYTHONPATH="$PKG_DIR/src" $VENV -m pytest -q "$PKG_DIR/tests"
```

Interactive REPL

Start the built-in REPL (friendly commands):

```bash
$VENV final_project/main.py
```

REPL commands (short)
- help
- add <title> [| description]
- list
- done <id-or-prefix>
- search <keyword>
- remove <id-or-prefix>
- exit

Module CLI (one-shot)

Run single commands without starting the REPL:

```bash
PYTHONPATH="$PKG_DIR/src" $VENV -m tasks_app add "Buy snacks" "For demo"
PYTHONPATH="$PKG_DIR/src" $VENV -m tasks_app list
PYTHONPATH="$PKG_DIR/src" $VENV -m tasks_app search "snack"
```

Safe smoke demo

Quick non-destructive smoke snippet that uses a temporary store:

```bash
PYTHONPATH="$PKG_DIR/src" $VENV - <<'PY'
from pathlib import Path
from tasks_app import storage, cli

tmp = Path('tmp_demo_store.json')
try:
    storage.DEFAULT_STORE = tmp
    t = cli.add_task('Demo task', 'short demo')
    print('Added:', t.id)
    cli.mark_done(t.id[:8])
    cli.remove_task(t.id[:8])
finally:
    try: tmp.unlink()
    except: pass
PY
```

Editable install (optional)

```bash
$VENV -m pip install -e final_project
# then run without PYTHONPATH
$VENV -m tasks_app list
```

Storage notes
- Default store: `final_project_store.json` (repo root).
- Override in code/tests: `storage.DEFAULT_STORE = Path('tmp.json')`.

If you want a longer README, CI integration, or a demo script tuned for a timed presentation, tell me and I will add it.
````markdown

# Final Project

Final consolidated tasks manager used as a compact, teachable example. This README gives quick runnable examples you can use for a short demo.

Highlights
- Task model: `id` (UUID), `title`, `description`, `created_at` (timezone-aware ISO), `due_date`, `priority`, `status`, `tags`.
- JSON-backed storage (pluggable) with a dynamic `DEFAULT_STORE` so tests and demos can override it.
- Programmatic CLI helpers and a module entrypoint (`python -m tasks_app`).
- Tests for model, storage and CLI included under `final_project/tests`.

Quick start (commands you can copy/paste)

Environment notes
- These examples assume macOS zsh and a repo-local virtualenv at `/Users/alexle/csc299-project/.venv` as used in the project. If you don't have that venv, substitute your Python executable for `$VENV` below.

```bash
# from repository root (adjust REPO if different)
REPO=/Users/alexle/csc299-project
VENV=$REPO/.venv/bin/python
# directory containing the package source
PKG_DIR="final_project"
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

Interactive tools

This project exposes two interactive ways to use the task manager:

- REPL: a small, friendly Read–Eval–Print Loop you can start with the script `final_project/main.py`. This is similar to the `task1` behavior: it prints a short welcome, accepts commands like `help`, `add`, `list`, `done`, `search`, `remove`, and `exit`.
- Module CLI: a standard module entrypoint `python -m tasks_app` for scripted or one-shot commands (add/list/done/search/remove).

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
$VENV -m pip install -e "final_project"
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

How to run the REPL (interactive)

You can run the small REPL shipped with the project. It automatically adds `final_project/src` to sys.path so it imports the package in-place.

```bash
# using the project venv (recommended)
REPO=/Users/alexle/csc299-project
VENV=$REPO/.venv/bin/python
$VENV final_project/main.py
```

REPL commands (short):
- help — show a single-line command summary
- add <title> [| description] — add a new task; you can separate a title and description with a `|` for convenience
- list — list all tasks (id prefix, title, priority, due date)
- done <id-or-prefix> — mark matching task(s) as done
- search <keyword> — case-insensitive search over title and description
- remove <id-or-prefix> — delete matching task(s)
- exit — quit the REPL

Example REPL session:

```
Welcome to Task Manager (type 'help' for commands)
> help
Commands: add <title> [| description], list, done <id|prefix>, search <keyword>, remove <id|prefix>, exit
> add Buy snacks | For demo
Added task: Buy snacks (id=8f3a2b1c)
> list
[OPEN] 8f3a2b1c | Buy snacks | Priority: medium
> done 8f3a2b1c
Marked done: True
> exit
```

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
