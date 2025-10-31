from model import Task
import storage

def add_task(title, description="", deadline=None, priority="medium", tags=None):
    tasks = storage.load_tasks()
    task = Task(title=title, description=description, deadline=deadline,
                priority=priority, tags=tags or [])
    tasks.append(task)
    storage.save_tasks(tasks)
    return task

def list_tasks():
    return storage.load_tasks()

def mark_done(task_id):
    tasks = storage.load_tasks()
    for task in tasks:
        if str(task.id).startswith(str(task_id)):
            task.status = "done"
            storage.save_tasks(tasks)
            return True
    return False

def search_tasks(keyword):
    tasks = storage.load_tasks()
    keyword_lower = keyword.lower()
    return [task for task in tasks if keyword_lower in task.title.lower()]
