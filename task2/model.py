from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import uuid

@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    deadline: Optional[str] = None   # ISO format string
    priority: str = "medium"         # low, medium, high
    status: str = "todo"             # todo, done
    tags: List[str] = field(default_factory=list)

    def is_overdue(self) -> bool:
        """Return True if the task deadline (ISO string) is before now.

        This method is defensive: any parsing error returns False (not overdue).
        """
        if not self.deadline:
            return False
        try:
            dt = datetime.fromisoformat(self.deadline)
            if dt.tzinfo is None:
                now = datetime.now()
            else:
                from datetime import timezone
                now = datetime.now(dt.tzinfo)
            return dt < now
        except Exception:
            # If the stored deadline isn't a valid ISO string, consider it not overdue
            return False

    def to_dict(self) -> dict:
        """Convert Task to a serializable dictionary."""
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
        """Create a Task from a dict, providing safe defaults for missing fields."""
        if data is None:
            raise ValueError("None data passed to Task.from_dict")
        return cls(
            id=str(data.get("id", str(uuid.uuid4()))),
            title=data.get("title", ""),
            description=data.get("description", ""),
            deadline=data.get("deadline", None),
            priority=data.get("priority", "medium"),
            status=data.get("status", "todo"),
            tags=list(data.get("tags", [])) if data.get("tags") is not None else [],
        )