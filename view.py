"""View — лише відображення та введення. Жодної логіки: усі дії передає Presenter."""
from abc import ABC, abstractmethod


class TaskView(ABC):
    """Інтерфейс View. Presenter працює лише з ним, тому View легко підмінити."""

    @abstractmethod
    def show_tasks(self, lines: list[str]) -> None: ...

    @abstractmethod
    def show_message(self, text: str) -> None: ...

    @abstractmethod
    def show_error(self, text: str) -> None: ...


class ConsoleTaskView(TaskView):
    """Консольна реалізація View."""

    def __init__(self):
        self.presenter = None  # встановлюється Presenter'ом

    def show_tasks(self, lines: list[str]) -> None:
        print("\n--- Список задач ---")
        print("\n".join(lines) if lines else "(порожньо)")

    def show_message(self, text: str) -> None:
        print(f"[OK] {text}")

    def show_error(self, text: str) -> None:
        print(f"[Помилка] {text}")

    def run(self) -> None:
        """Цикл введення: View лише передає команди користувача Presenter'у."""
        print("Команди: add <назва> | done <id> | del <id> | list | exit")
        while True:
            command, _, arg = input("> ").strip().partition(" ")
            if command == "exit":
                break
            elif command == "add":
                self.presenter.on_add(arg)
            elif command == "done":
                self.presenter.on_complete(arg)
            elif command == "del":
                self.presenter.on_remove(arg)
            elif command == "list":
                self.presenter.on_show()
            else:
                self.show_error("Невідома команда")
