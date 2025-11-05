import json
from pathlib import Path
from typing import List
from .model import Task

DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks() -> List[Task]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
    tasks: List[Task] = []
    for item in data:
        try:
            tasks.append(Task.from_dict(item))
        except Exception:
            # skip malformed
            continue
    return tasks


def save_tasks(tasks: List[Task]) -> None:
    tmp = DATA_FILE.with_suffix(".tmp")
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
    tmp.replace(DATA_FILE)
