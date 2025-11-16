import json
from typing import List
from pathlib import Path
from .model import Task

DEFAULT_STORE = Path("tasks5_store.json")


def load_tasks(path: Path | str = DEFAULT_STORE) -> List[Task]:
    p = Path(path)
    if not p.exists():
        return []
    data = json.loads(p.read_text(encoding="utf-8"))
    return [Task.from_dict(d) for d in data]


def save_tasks(tasks: List[Task], path: Path | str = DEFAULT_STORE) -> None:
    p = Path(path)
    p.write_text(json.dumps([t.to_dict() for t in tasks], indent=2), encoding="utf-8")
