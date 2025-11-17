REPO := /Users/alexle/csc299-project
VENV := $(REPO)/.venv/bin/python

.PHONY: test smoke final demo install

demo: test smoke final

test:
	./scripts/demo.sh test

smoke:
	./scripts/demo.sh smoke

final:
	./scripts/demo.sh final

install:
	./scripts/demo.sh install
PYTHON := $(shell [ -x .venv/bin/python ] && echo .venv/bin/python || echo python3)

.PHONY: help test smoke demo install

help:
	@echo "Makefile targets:"
 	@echo "  make test   - run Final Project tests"
 	@echo "  make smoke  - run smoke script (temporary store)"
 	@echo "  make demo   - run full demo (tests + smoke + module demo)"
 	@echo "  make install - install Final Project in editable mode"

test:
	@echo "Running Final Project tests..."
	PYTHONPATH="Final Project/src" $(PYTHON) -m pytest -q "Final Project/tests"

smoke:
	@echo "Running smoke script (safe temporary store)..."
	 	PYTHONPATH="Final Project/src" $(PYTHON) - <<'PY'
		from pathlib import Path
		from tasks_app import storage, cli
		tmp = Path('tmp_demo_store.json')
		try:
		    storage.DEFAULT_STORE = tmp
		    t = cli.add_task('SmokeTask', 'from make')
		    print('Added:', t.id)
		    cli.remove_task(t.id[:8])
		finally:
		    try: tmp.unlink()
		    except: pass
		print('Smoke done')
		PY

demo: test smoke

install:
	$(PYTHON) -m pip install -e "Final Project"
