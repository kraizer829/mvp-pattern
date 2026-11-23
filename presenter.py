"""Presenter — посередник між Model і View.

Отримує дії від View, змінює Model і сам оновлює View, форматуючи дані.
View і Model одне про одного не знають.
"""
from model import TaskModel
from view import TaskView


class TaskPresenter:
    def __init__(self, model: TaskModel, view: TaskView):
        self.model = model
        self.view = view
        view.presenter = self

    # ----- обробники дій користувача -----
    def on_add(self, title: str) -> None:
        try:
            task = self.model.add(title)
        except ValueError as e:
            self.view.show_error(str(e))
            return
        self.view.show_message(f"Додано задачу #{task.id}")
        self.on_show()

    def on_complete(self, raw_id: str) -> None:
        self._with_id(raw_id, self.model.complete, "виконано")

    def on_remove(self, raw_id: str) -> None:
        self._with_id(raw_id, self.model.remove, "видалено")

    def on_show(self) -> None:
        lines = [
            f"{t.id}. [{'x' if t.done else ' '}] {t.title}"
            for t in self.model.all()
        ]
        self.view.show_tasks(lines)

    # ----- допоміжне -----
    def _with_id(self, raw_id: str, action, verb: str) -> None:
        if not raw_id.strip().isdigit():
            self.view.show_error("id має бути числом")
            return
        task_id = int(raw_id)
        try:
            action(task_id)
        except KeyError as e:
            self.view.show_error(e.args[0])
            return
        self.view.show_message(f"Задачу #{task_id} {verb}")
        self.on_show()
