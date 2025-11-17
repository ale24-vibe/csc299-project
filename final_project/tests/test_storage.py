from pathlib import Path
from tasks_app.model import Task
from tasks_app import storage


def test_storage_roundtrip(tmp_path: Path):
    p = tmp_path / "store.json"
    t = Task(title="A")
    storage.save_tasks([t], path=p)
    loaded = storage.load_tasks(path=p)
    assert len(loaded) == 1
    assert loaded[0].id == t.id
