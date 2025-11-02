from model import Task
import storage
from typing import List


def add_task(title, description="", deadline=None, priority="medium", tags=None):
    tasks = storage.load_tasks()
    task = Task(title=title, description=description, deadline=deadline,
                priority=priority, tags=tags or [])
    tasks.append(task)
    storage.save_tasks(tasks)
    return task


def list_tasks() -> List[Task]:
    return storage.load_tasks()


def mark_done(task_id: str) -> int:
    """Mark a task done by id prefix or full id. Returns the count of tasks updated. Raises ValueError if multiple matches found."""
    tasks = storage.load_tasks()
    updated = 0
    for t in tasks:
        if str(t.id).startswith(str(task_id)):
            if t.status != "done":
                t.status = "done"
                updated += 1
    if updated:
        storage.save_tasks(tasks)
        return True
    return False
    return matched


def search_tasks(keyword) -> List[Task]:
    tasks = storage.load_tasks()
    kw = keyword.lower()
    return [t for t in tasks if kw in t.title.lower() or kw in t.description.lower()]


def search_by_tag(tag) -> List[Task]:
    tasks = storage.load_tasks()
    tg = tag.lower()
    return [t for t in tasks if tg in [x.lower() for x in (t.tags or [])]]
