import json
from pathlib import Path
from models import Task

DATA_FILE = Path("tasks.json")

def load_tasks() -> list[Task]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return [Task(**t) for t in data]

def save_tasks(tasks: list[Task]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump([t.__dict__ for t in tasks], f, indent=2)
