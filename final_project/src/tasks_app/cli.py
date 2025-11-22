from typing import List
from .model import Task
from .storage import load_tasks, save_tasks


def add_task(title: str, description: str = "", **kwargs) -> Task:
    if not title:
        raise ValueError("title is required")
    tasks = load_tasks()
    t = Task(title=title, description=description, **kwargs)
    tasks.append(t)
    save_tasks(tasks)
    return t


def list_tasks() -> List[Task]:
    return load_tasks()


def mark_done(task_id: str) -> bool:
    tasks = load_tasks()
    matched = 0
    for t in tasks:
        if str(t.id).startswith(str(task_id)):
            if t.status != "done":
                t.status = "done"
            matched += 1
    if matched:
        save_tasks(tasks)
        return True
    return False


def remove_task(task_id: str) -> bool:
    tasks = load_tasks()
    new = [t for t in tasks if not str(t.id).startswith(str(task_id))]
    if len(new) != len(tasks):
        save_tasks(new)
        return True
    return False


def search_tasks(keyword: str) -> List[Task]:
    kw = keyword.lower()
    return [t for t in load_tasks() if kw in t.title.lower() or kw in t.description.lower()]


def set_priority(task_id: str, priority: str) -> bool:
    """Set the priority for tasks matching the given id prefix.

    Returns True if at least one task was updated, False otherwise.
    """
    tasks = load_tasks()
    matched = 0
    for t in tasks:
        if str(t.id).startswith(str(task_id)):
            if t.priority != priority:
                t.priority = priority
            matched += 1
    if matched:
        save_tasks(tasks)
        return True
    return False
