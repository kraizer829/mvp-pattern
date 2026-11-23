"""Тести Presenter'а з фейковим View — головна перевага MVP:
логіку можна перевірити без реального інтерфейсу.

Запуск: python -m unittest test_presenter.py
"""
import unittest

from model import TaskModel
from presenter import TaskPresenter
from view import TaskView


class FakeView(TaskView):
    def __init__(self):
        self.tasks, self.messages, self.errors = [], [], []

    def show_tasks(self, lines):
        self.tasks = lines

    def show_message(self, text):
        self.messages.append(text)

    def show_error(self, text):
        self.errors.append(text)


class TaskPresenterTest(unittest.TestCase):
    def setUp(self):
        self.view = FakeView()
        self.presenter = TaskPresenter(TaskModel(), self.view)

    def test_add_task_updates_view(self):
        self.presenter.on_add("Вивчити MVP")
        self.assertEqual(self.view.tasks, ["1. [ ] Вивчити MVP"])

    def test_empty_title_shows_error(self):
        self.presenter.on_add("   ")
        self.assertEqual(len(self.view.errors), 1)
        self.assertEqual(self.view.tasks, [])

    def test_complete_task(self):
        self.presenter.on_add("Здати лабу")
        self.presenter.on_complete("1")
        self.assertEqual(self.view.tasks, ["1. [x] Здати лабу"])

    def test_remove_task(self):
        self.presenter.on_add("A")
        self.presenter.on_add("B")
        self.presenter.on_remove("1")
        self.assertEqual(self.view.tasks, ["2. [ ] B"])

    def test_bad_id_shows_error(self):
        self.presenter.on_complete("abc")
        self.presenter.on_complete("42")
        self.assertEqual(len(self.view.errors), 2)


if __name__ == "__main__":
    unittest.main()
