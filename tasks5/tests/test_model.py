from tasks_manager.model import Task


def test_task_to_from_dict():
    t = Task(title="Test", description="desc")
    d = t.to_dict()
    t2 = Task.from_dict(d)
    assert t2.title == "Test"
    assert t2.description == "desc"
    assert t2.id
