from typing import List
from .model import Task
from . import storage


def add_task(title: str, description: str = "", deadline=None, priority: str = "medium", tags=None) -> Task:
    tasks = storage.load_tasks()
    task = Task(title=title, description=description, deadline=deadline, priority=priority, tags=tags or [])
    tasks.append(task)
    storage.save_tasks(tasks)
    return task


def list_tasks() -> List[Task]:
    return storage.load_tasks()


def mark_done(task_id: str) -> bool:
    tasks = storage.load_tasks()
    matched = 0
    for t in tasks:
        if str(t.id).startswith(str(task_id)):
            if t.status != "done":
                t.status = "done"
            matched += 1
    if matched:
        storage.save_tasks(tasks)
        return True
    return False


def search_tasks(keyword: str) -> List[Task]:
    kw = keyword.lower()
    return [t for t in storage.load_tasks() if kw in t.title.lower() or kw in t.description.lower()]
