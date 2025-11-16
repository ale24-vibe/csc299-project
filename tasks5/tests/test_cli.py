from tasks_manager.cli import add_task, list_tasks, mark_done, remove_task, search_tasks
from tasks_manager.storage import DEFAULT_STORE
from pathlib import Path


def test_cli_add_list_remove(tmp_path, monkeypatch):
    # use tmp file for storage
    monkeypatch.setattr('tasks_manager.storage.DEFAULT_STORE', tmp_path / 's.json')
    t = add_task("Buy milk", "2 liters")
    items = list_tasks()
    assert any(i.title == "Buy milk" for i in items)
    assert mark_done(t.id)
    assert any(i.status == "done" for i in list_tasks())
    assert remove_task(t.id)
    assert not list_tasks()
