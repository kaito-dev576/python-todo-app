import json
from task import Task


def save_tasks(tasks):
    with open("todo.json", "w", encoding="utf-8") as file:
        json.dump(
            [task.to_dict() for task in tasks],
            file,
            ensure_ascii=False,
            indent=4
        )


def load_tasks():
    try:
        with open("todo.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            tasks = [Task.from_dict(task) for task in data]
    except FileNotFoundError:
        tasks = []

    return tasks