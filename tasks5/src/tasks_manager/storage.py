import json
from typing import List, Optional
from pathlib import Path
from .model import Task

DEFAULT_STORE = Path("tasks5_store.json")


def load_tasks(path: Optional[Path | str] = None) -> List[Task]:
    """Load tasks from the given path or the dynamic DEFAULT_STORE.

    Use `path=None` to pick up the current value of `DEFAULT_STORE` at runtime
    (this makes it possible for tests to monkeypatch `DEFAULT_STORE`).
    """
    p = Path(path or DEFAULT_STORE)
    if not p.exists():
        return []
    data = json.loads(p.read_text(encoding="utf-8"))
    return [Task.from_dict(d) for d in data]


def save_tasks(tasks: List[Task], path: Optional[Path | str] = None) -> None:
    p = Path(path or DEFAULT_STORE)
    p.write_text(json.dumps([t.to_dict() for t in tasks], indent=2), encoding="utf-8")
