import json
from pathlib import Path
from typing import List
from model import Task

# Store the data file next to this module for predictable behavior
DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks() -> List[Task]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Warning: tasks.json is corrupted or contains invalid JSON. Returning an empty task list.")
            return []

    tasks: List[Task] = []
    for item in data:
        try:
            tasks.append(Task.from_dict(item))
        except Exception:
            # skip malformed entries but continue loading others
            print("Warning: skipping malformed task entry in tasks.json")
    return tasks


def save_tasks(tasks: List[Task]) -> None:
    # Write atomically: write to a temp file then rename
    tmp = DATA_FILE.with_suffix(".tmp")
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(tmp, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
    tmp.replace(DATA_FILE)
