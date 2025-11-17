import json
from pathlib import Path
from typing import List, Optional
from .model import Task

DEFAULT_STORE = Path("final_project_store.json")


def load_tasks(path: Optional[Path | str] = None) -> List[Task]:
    p = Path(path or DEFAULT_STORE)
    if not p.exists():
        return []
    data = json.loads(p.read_text(encoding="utf-8"))
    return [Task.from_dict(d) for d in data]


def save_tasks(tasks: List[Task], path: Optional[Path | str] = None) -> None:
    p = Path(path or DEFAULT_STORE)
    # atomic-ish write
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps([t.to_dict() for t in tasks], indent=2), encoding="utf-8")
    tmp.replace(p)
