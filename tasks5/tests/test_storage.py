from tasks_manager.model import Task
from tasks_manager.storage import load_tasks, save_tasks
from pathlib import Path


def test_storage_roundtrip(tmp_path):
    p = tmp_path / "store.json"
    tasks = [Task(title="A"), Task(title="B")]
    save_tasks(tasks, path=p)
    loaded = load_tasks(path=p)
    assert len(loaded) == 2
    assert loaded[0].title == "A"
