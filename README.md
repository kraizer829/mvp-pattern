# Шаблон MVP (Model–View–Presenter) на Python

Консольний застосунок «Список задач», реалізований за шаблоном MVP.

| Компонент | Файл | Відповідальність |
|---|---|---|
| Model | [model.py](model.py) | Дані та бізнес-логіка (додати, виконати, видалити задачу) |
| View | [view.py](view.py) | Інтерфейс `TaskView` і консольна реалізація: лише показ і введення |
| Presenter | [presenter.py](presenter.py) | Отримує дії від View, змінює Model, форматує дані й оновлює View |
| Збірка | [main.py](main.py) | Створює Model, View, Presenter і запускає застосунок |
| Тести | [test_presenter.py](test_presenter.py) | Перевірка Presenter'а з фейковим View |

## Як це працює

1. Користувач вводить команду у View (`add Купити хліб`).
2. View не обробляє її сам, а викликає `presenter.on_add(...)`.
3. Presenter змінює Model і викликає `view.show_tasks(...)` з уже відформатованими рядками.

View і Model одне про одного не знають — їх зв'язує лише Presenter.
Presenter залежить від абстрактного `TaskView`, тому View можна замінити
(наприклад, на GUI або фейковий View у тестах) без зміни логіки.

## Запуск

```
python main.py
python -m unittest test_presenter.py
```

Python 3.10+.
