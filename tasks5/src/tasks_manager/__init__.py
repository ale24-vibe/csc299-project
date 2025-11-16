"""Simple tasks manager package used for the spec-kit implementation demo.

This package is intentionally small and focused on teaching: a Task model, JSON
storage, and a minimal programmatic CLI.
"""

from .model import Task
from .storage import load_tasks, save_tasks
from .cli import add_task, list_tasks, mark_done, remove_task, search_tasks

__all__ = [
    "Task",
    "load_tasks",
    "save_tasks",
    "add_task",
    "list_tasks",
    "mark_done",
    "remove_task",
    "search_tasks",
]
