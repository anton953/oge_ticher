import sqlite3
import json
from datetime import datetime
from config import DB_NAME

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Создание таблиц в базе данных"""
        # Таблица пользователей
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                full_name TEXT,
                registered_date TEXT,
                last_active TEXT,
                level INTEGER DEFAULT 1,
                score INTEGER DEFAULT 0,
                correct_answers INTEGER DEFAULT 0,
                total_attempts INTEGER DEFAULT 0
            )
        ''')

        # Таблица прогресса по темам
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                topic TEXT,
                correct INTEGER DEFAULT 0,
                attempts INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')

        # Таблица решённых задач
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS solved_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                task_id INTEGER,
                solved_date TEXT,
                is_correct BOOLEAN,
                time_spent INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')

        self.conn.commit()

    def add_user(self, user_id, username, full_name):
        """Добавление нового пользователя"""
        try:
            self.cursor.execute('''
                INSERT OR IGNORE INTO users (user_id, username, full_name, registered_date, last_active)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, username, full_name, datetime.now().isoformat(), datetime.now().isoformat()))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False

    def update_user_activity(self, user_id):
        """Обновление времени последней активности"""
        self.cursor.execute('''
            UPDATE users SET last_active = ? WHERE user_id = ?
        ''', (datetime.now().isoformat(), user_id))
        self.conn.commit()

    def update_user_score(self, user_id, is_correct, points=10):
        """Обновление счёта пользователя"""
        if is_correct:
            self.cursor.execute('''
                UPDATE users 
                SET score = score + ?, 
                    correct_answers = correct_answers + 1,
                    total_attempts = total_attempts + 1
                WHERE user_id = ?
            ''', (points, user_id))
        else:
            self.cursor.execute('''
                UPDATE users 
                SET total_attempts = total_attempts + 1
                WHERE user_id = ?
            ''', (user_id,))
        self.conn.commit()

    def get_user_stats(self, user_id):
        """Получение статистики пользователя"""
        self.cursor.execute('''
            SELECT * FROM users WHERE user_id = ?
        ''', (user_id,))
        user = self.cursor.fetchone()
        
        if user:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, user))
        return None

    def close(self):
        """Закрытие соединения с базой данных"""
        self.conn.close()