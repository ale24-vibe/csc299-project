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
    found = False
    for task in tasks:
        if str(task.id).startswith(task_id):
            task.status = "done"
            found = True
    if found:
        storage.save_tasks(tasks)
    return found
