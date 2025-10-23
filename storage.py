import json
from pathlib import Path
from model import Task

DATA_FILE = Path("tasks.json")

def load_tasks() -> list[Task]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Warning: tasks.json is corrupted or contains invalid JSON. Returning an empty task list.")
            return []
    return [Task(**t) for t in data]


def save_tasks(tasks: list[Task]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump([t.__dict__ for t in tasks], f, indent=2)
