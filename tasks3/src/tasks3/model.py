from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import uuid


@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    deadline: Optional[str] = None  # ISO format string
    priority: str = "medium"
    status: str = "todo"
    tags: List[str] = field(default_factory=list)

    def is_overdue(self) -> bool:
        if not self.deadline:
            return False
        try:
            dt = datetime.fromisoformat(self.deadline)
            return dt < datetime.now()
        except Exception:
            return False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "priority": self.priority,
            "status": self.status,
            "tags": list(self.tags) if self.tags is not None else [],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            id=str(data.get("id", str(uuid.uuid4()))),
            title=data.get("title", ""),
            description=data.get("description", ""),
            deadline=data.get("deadline", None),
            priority=data.get("priority", "medium"),
            status=data.get("status", "todo"),
            tags=list(data.get("tags", [])) if data.get("tags") is not None else [],
        )
