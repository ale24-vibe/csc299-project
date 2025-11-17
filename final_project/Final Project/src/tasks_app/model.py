from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import List, Optional
import uuid


def _now_iso() -> str:
    # timezone-aware UTC ISO format
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    created_at: str = field(default_factory=_now_iso)
    due_date: Optional[str] = None
    priority: str = "medium"
    status: str = "open"
    tags: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(d: dict) -> "Task":
        return Task(
            id=d.get("id") or str(uuid.uuid4()),
            title=d.get("title", ""),
            description=d.get("description", ""),
            created_at=d.get("created_at") or _now_iso(),
            due_date=d.get("due_date"),
            priority=d.get("priority", "medium"),
            status=d.get("status", "open"),
            tags=d.get("tags", []) or [],
        )
