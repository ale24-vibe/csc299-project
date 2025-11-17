#!/usr/bin/env bash
set -euo pipefail

REPO=/Users/alexle/csc299-project
# Auto-detect venv python: prefer repo .venv, else system python3
if [ -x "$REPO/.venv/bin/python" ]; then
    VENV=$REPO/.venv/bin/python
else
    VENV=$(which python3 || which python || echo python)
fi

# We assume package is in "Final Project" directory (as requested).
PKG_DIR="Final Project"
if [ ! -d "$PKG_DIR" ]; then
    echo "Error: expected package directory '$PKG_DIR' not found."
    exit 1
fi

run_py() {
    PYTHONPATH="$PKG_DIR/src" $VENV -m "$@"
}

MODE=${1:-all}

echo "Using package dir: $PKG_DIR"

if [ "$MODE" = "all" ] || [ "$MODE" = "test" ]; then
    echo "Running tests..."
    run_py pytest -q "$PKG_DIR/tests"
fi

if [ "$MODE" = "all" ] || [ "$MODE" = "smoke" ]; then
    echo "Running smoke script (uses a temporary store)..."
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

    echo "Smoke run complete."
fi

if [ "$MODE" = "all" ] || [ "$MODE" = "interactive" ]; then
    echo "Example interactive steps (shown but not run):"
    echo "  $VENV -m tasks_app add \"Buy snacks\" \"For demo\""
    echo "  $VENV -m tasks_app list"
fi

if [ "$MODE" = "all" ] || [ "$MODE" = "final" ]; then
    echo "\n--- Final project module CLI demo using a temporary store ---"
    PYTHONPATH="$PKG_DIR/src" $VENV - <<'PY'
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
fi

if [ "$MODE" = "all" ] || [ "$MODE" = "install" ]; then
    echo "Optional: install $PKG_DIR in editable mode (so you can run without PYTHONPATH)"
    echo "  $VENV -m pip install -e \"$PKG_DIR\""
fi
