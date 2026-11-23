"""Model — дані та бізнес-логіка. Нічого не знає ні про View, ні про Presenter."""
from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TaskModel:
    def __init__(self):
        self._tasks: list[Task] = []
        self._next_id = 1

    def add(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Назва задачі не може бути порожньою")
        task = Task(self._next_id, title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def complete(self, task_id: int) -> None:
        self._find(task_id).done = True

    def remove(self, task_id: int) -> None:
        self._tasks.remove(self._find(task_id))

    def all(self) -> list[Task]:
        return list(self._tasks)

    def _find(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise KeyError(f"Задачу з id={task_id} не знайдено")
