PY?=python3
PKG_DIR := final_project

.PHONY: help test smoke final demo install

help:
	@echo "Makefile targets:"
	@echo "  make test    - run pytest for the final project package"
	@echo "  make smoke   - run quick smoke demo (uses tmp store)"
	@echo "  make final   - run the module CLI demo (uses tmp store)"
	@echo "  make demo    - runs smoke + final (full demo)"
	@echo "  make install - optional: pip install -e 'Final Project'"

test:
	@echo "Running tests for '${PKG_DIR}'..."
	PYTHONPATH="${PKG_DIR}/src" $(PY?) -m pytest -q "${PKG_DIR}/tests"

smoke:
	@echo "Running smoke script (temporary store)..."
	./scripts/demo.sh smoke

final:
	@echo "Running final module CLI demo (temporary store)..."
	./scripts/demo.sh final

demo: smoke final
	@echo "Demo complete."

install:
	@echo "Install '${PKG_DIR}' in editable mode (optional)"
	$(PY?) -m pip install -e "${PKG_DIR}"
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
