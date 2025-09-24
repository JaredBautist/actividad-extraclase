from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Literal, List
Priority = Literal["high", "medium", "low"]
@dataclass(slots=True)
class Task:
    id: int
    title: str
    priority: Priority = "medium"
    description: Optional[str] = None
    done: bool = False
class ToDo:
    __slots__ = ("_tasks", "_next_id")
    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1
    # Create
    def add(self, title: str, *, priority: Priority = "medium", description: Optional[str] = None) -> Task:
        title = (title or "").strip()
        if not title: raise ValueError("title required")
        if priority not in ("high","medium","low"): raise ValueError("invalid priority")
        t = Task(self._next_id, title, priority, description, False)
        self._tasks.append(t); self._next_id += 1; return t
    # Read
    def list(self, *, priority: Optional[Priority] = None, done: Optional[bool] = None) -> List[Task]:
        out: List[Task] = []
        for t in self._tasks:
            if priority is not None and t.priority != priority: continue
            if done is not None and t.done != done: continue
            out.append(t)
        return out
    def get(self, task_id: int) -> Optional[Task]:
        for t in self._tasks:
            if t.id == task_id: return t
        return None
    # Update
    def toggle_done(self, task_id: int) -> bool:
        t = self.get(task_id)
        if t is None: return False
        t.done = not t.done; return True
    def update(self, task_id: int, *, title: Optional[str] = None,
               priority: Optional[Priority] = None, description: Optional[str] = None,
               done: Optional[bool] = None) -> bool:
        t = self.get(task_id)
        if t is None: return False
        if title is not None:
            title = title.strip()
            if not title: raise ValueError("title required")
            t.title = title
        if priority is not None:
            if priority not in ("high","medium","low"): raise ValueError("invalid priority")
            t.priority = priority
        if description is not None: t.description = description
        if done is not None: t.done = done
        return True
    # Delete
    def remove(self, task_id: int) -> bool:
        before = len(self._tasks); self._tasks = [t for t in self._tasks if t.id != task_id]
        return len(self._tasks) < before
    # Helpers
    def __len__(self) -> int: return len(self._tasks)
    def next_id(self) -> int: return self._next_id
