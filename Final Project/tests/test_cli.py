from tasks_app import storage
from tasks_app import cli
from pathlib import Path


def test_cli_add_list_remove(tmp_path: Path):
    store = tmp_path / "s.json"
    storage.DEFAULT_STORE = store
    t = cli.add_task("Demo", "d")
    ls = cli.list_tasks()
    assert any(x.id == t.id for x in ls)
    assert cli.mark_done(t.id[:8])
    assert cli.remove_task(t.id[:8])
