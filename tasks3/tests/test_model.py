from datetime import datetime, timedelta
from tasks3.model import Task


def test_is_overdue_future():
    future = (datetime.now() + timedelta(days=1)).isoformat()
    t = Task(title="future", deadline=future)
    assert t.is_overdue() is False


def test_is_overdue_past():
    past = (datetime.now() - timedelta(days=1)).isoformat()
    t = Task(title="past", deadline=past)
    assert t.is_overdue() is True
