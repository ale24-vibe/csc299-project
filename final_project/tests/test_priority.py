from tasks_app import storage
from tasks_app import cli
from pathlib import Path


def test_set_priority_updates_task(tmp_path: Path):
    store = tmp_path / "s.json"
    storage.DEFAULT_STORE = store
    t = cli.add_task("Priority test", "set-priority", priority="medium")
    # change to high
    assert cli.set_priority(t.id[:8], "high")
    # reload and verify
    tasks = cli.list_tasks()
    found = [x for x in tasks if x.id == t.id]
    assert len(found) == 1
    assert found[0].priority == "high"
