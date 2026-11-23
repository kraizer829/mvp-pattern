"""Точка входу: збирає Model, View і Presenter разом."""
from model import TaskModel
from presenter import TaskPresenter
from view import ConsoleTaskView


def main() -> None:
    view = ConsoleTaskView()
    TaskPresenter(TaskModel(), view)
    view.run()


if __name__ == "__main__":
    main()
