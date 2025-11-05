import os
from pathlib import Path

from tasks3 import services
from tasks3 import storage


def test_add_and_list(tmp_path):
    # isolate storage to temp file
    storage.DATA_FILE = tmp_path / "tasks.json"
    # add a task
    t = services.add_task("T1", "desc")
    tasks = services.list_tasks()
    assert any(x.id == t.id for x in tasks)


def test_mark_done(tmp_path):
    storage.DATA_FILE = tmp_path / "tasks.json"
    t = services.add_task("T2")
    assert services.mark_done(t.id[:8]) is True
    # second call should still return True (id matched)
    assert services.mark_done(t.id[:8]) is True
