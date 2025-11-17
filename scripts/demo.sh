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
