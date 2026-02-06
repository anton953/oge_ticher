import json
import random
from typing import Dict, List, Optional
from pathlib import Path

class TaskManager:
    def __init__(self, tasks_file: str = 'data/tasks.json'):
        self.tasks_file = tasks_file
        self.tasks = self.load_tasks()
        
    def load_tasks(self) -> Dict:
        """Загрузка заданий из файла"""
        try:
            with open(self.tasks_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Примерная структура задач для начала работы
            return {
                "tasks": {
                    "1-5": [
                        {
                            "id": 1,
                            "question": "Сколько бит информации содержит сообщение размером 16 Кбайт?",
                            "options": ["131072", "16384", "128", "1024"],
                            "correct": 0,
                            "explanation": "16 Кбайт = 16 * 1024 байт = 16384 байт = 16384 * 8 бит = 131072 бит",
                            "hints": ["1 Кбайт = 1024 байт", "1 байт = 8 бит"],
                            "difficulty": 1
                        }
                    ],
                    "6-11": [],
                    "12-18": [],
                    "13-16": [
                        {
                            "id": 101,
                            "question": "Исполнитель Вычислитель имеет две команды: 1. прибавь 2, 2. умножь на 3. Первая из них увеличивает число на экране на 2, вторая умножает его на 3. Запишите порядок команд для получения из числа 2 числа 28.",
                            "options": ["11212", "12121", "21112", "12211"],
                            "correct": 0,
                            "explanation": "Решение: 2 → +2=4 → *3=12 → +2=14 → *3=42 → +2=44 (неверно). Попробуем другой путь...",
                            "hints": ["Попробуйте действовать с конца", "28 должно делиться на 3 или быть на 2 меньше числа, делящегося на 3"],
                            "difficulty": 3
                        }
                    ],
                    "17": []
                }
            }
    
    def get_task(self, category: str = "random", task_id: Optional[int] = None) -> Optional[Dict]:
        """Получение задания по категории или ID"""
        if task_id:
            for cat, tasks in self.tasks["tasks"].items():
                for task in tasks:
                    if task["id"] == task_id:
                        return task
            return None
        
        if category == "random":
            # Собираем все задачи
            all_tasks = []
            for cat_tasks in self.tasks["tasks"].values():
                all_tasks.extend(cat_tasks)
            if all_tasks:
                return random.choice(all_tasks)
            return None
        
        if category in self.tasks["tasks"]:
            if self.tasks["tasks"][category]:
                return random.choice(self.tasks["tasks"][category])
        
        return None
    
    def check_answer(self, task_id: int, user_answer: str) -> bool:
        """Проверка ответа пользователя"""
        task = self.get_task(task_id=task_id)
        if not task:
            return False
        
        # Для задач с вариантами ответа
        if "options" in task:
            try:
                # Если ответ - индекс варианта
                if user_answer.isdigit():
                    answer_index = int(user_answer) - 1
                    return answer_index == task["correct"]
                # Если ответ - текст варианта
                elif user_answer in task["options"]:
                    return task["options"].index(user_answer) == task["correct"]
            except (ValueError, IndexError):
                pass
        
        # Для задач с текстовым ответом
        return user_answer.strip().lower() == str(task.get("answer", "")).strip().lower()