#!/usr/bin/env bash
set -euo pipefail

REPO=/Users/alexle/csc299-project
VENV=$REPO/.venv/bin/python

echo "Running tests for tasks_final..."
PYTHONPATH=tasks_final/src $VENV -m pytest -q tasks_final/tests

echo "Running smoke script (uses a temporary store)..."
PYTHONPATH=tasks_final/src $VENV - <<'PY'
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

echo "Smoke run complete."

echo "Example interactive steps (shown but not run):"
echo "  $VENV -m tasks_app add \"Buy snacks\" \"For demo\""
echo "  $VENV -m tasks_app list"

echo "\n--- Final project (tasks_final) module CLI demo using a temporary store ---"
PYTHONPATH=tasks_final/src $VENV - <<'PY'
from pathlib import Path
from tasks_app import storage
from tasks_app.__main__ import main
from tasks_app import cli

tmp = Path('tmp_demo_tasks_final.json')
try:
    storage.DEFAULT_STORE = tmp
    print('Running: add via module')
    main(['add', 'Final demo task', 'from module'])
    print('Running: list via module')
    main(['list'])
    t = cli.list_tasks()[0]
    print('Running: done via module (prefix)')
    main(['done', t.id[:8]])
    print('Running: search via module')
    main(['search', 'Final'])
    print('Running: remove via module')
    main(['remove', t.id[:8]])
finally:
    try: tmp.unlink()
    except: pass
PY

echo "Optional: install tasks_final in editable mode (so you can run without PYTHONPATH)"
echo "  $VENV -m pip install -e tasks_final"
