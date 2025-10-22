from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import uuid

@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    deadline: Optional[str] = None   # store as ISO string
    priority: str = "medium"         # low, medium, high
    status: str = "todo"             # todo, in-progress, done
    tags: List[str] = field(default_factory=list)

    def is_overdue(self) -> bool:
        if not self.deadline:
            return False
        return datetime.fromisoformat(self.deadline) < datetime.now()
