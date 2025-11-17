from tasks_app.model import Task


def test_task_to_from_dict():
    t = Task(title="X", description="Y")
    d = t.to_dict()
    t2 = Task.from_dict(d)
    assert t.id == t2.id
    assert t.title == t2.title
    assert t.description == t2.description
