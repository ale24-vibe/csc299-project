---
title: "Tasks for 001 — Build a tasks manager"
---

# Tasks for feature: Build a tasks manager "built in class"

## Phase 1: Setup (M1)

- [ ] T001 Create project skeleton under `tasks5/src/tasks_manager/` and `tasks5/tests/` (pyproject optional)
- [ ] T002 Add README.md with run/test instructions
- [ ] T003 Configure simple developer workflow in README (how to run tests and run CLI)

## Phase 2: Foundational (M2, M3)

- [ ] T004 Implement `Task` model in `tasks_manager/model.py` (id, title, description, created_at, due_date, priority, status, tags)
- [ ] T005 Implement JSON file storage in `tasks_manager/storage.py` with `load_tasks()` and `save_tasks()`
- [ ] T006 Unit tests for model and storage in `tasks5/tests/test_model.py` and `tests/test_storage.py`

## Phase 3: CLI (M4)

- [ ] T007 Implement CLI functions in `tasks_manager/cli.py`: `add`, `list`, `done`, `remove`, `search` (programmatic API)
- [ ] T008 Add small integration tests for CLI glue in `tasks5/tests/test_cli.py`

## Phase 4: Polish (M5)

- [ ] T009 Update README with examples and sample runs
- [ ] T010 Minor refactor and ensure tests pass
