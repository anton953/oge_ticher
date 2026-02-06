import json
import random

class TaskManager:
    def __init__(self, json_path):
        """Загружает JSON-файл с заданиями"""
        with open(json_path, 'r', encoding='utf-8') as f:
            self.tasks = json.load(f)
        # Словарь для быстрого поиска по номеру
        self._by_id = {t['id']: t for t in self.tasks}
    
    def get_all(self):
        """Вернуть все задания (список)"""
        return self.tasks
    
    def get_by_id(self, task_id):
        """Найти задание по номеру (строка или число)"""
        return self._by_id.get(str(task_id))
    
    def get_answer(self, task_id):
        """Получить только ответ по номеру задания"""
        task = self.get_by_id(task_id)
        return task['answer'] if task else None

    def get_random(self):
        """Получить случайное задание"""
        return random.choice(self.tasks)
    
    def count(self):
        """Количество заданий"""
        return len(self.tasks)


if __name__ == '__main__':
    manager = TaskManager('tasks/task_1.json')

    # # Всего заданий
    # print(manager.count())  # 76

    # # Получить задание по ID
    # task = manager.get_by_id('8405')
    # print(task['condition'])  # текст условия
    # print(task['answer'])    # Dota

    # # Только ответ (быстро)
    # print(manager.get_answer(573))  # 104

    # Все задания
    # for task in manager.get_all():
    #     print(task['id'], task['answer'])


    # Случайное задание
    task = manager.get_random()
    print(task['id'])  # например: 8342
    print(task['condition'])        # полный текст условия
    print(task['answer'])          # например: 2

    # Для тестирования — 5 случайных вопросов
    for i in range(5):
        t = manager.get_random()
        print(f"{t['id']}: {t['answer']}")