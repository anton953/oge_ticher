from vkbottle.bot import Message, BotLabeler
from vkbottle import CtxStorage, CallbackQuery
from vkbottle.dispatch.rules.base import PayloadRule

from task_manager import TaskManager
from keyboars.k_tasks import get_task_id_keyboard, get_task_answer_keyboard
from database import Database

import re
import html

tasks_labeler = BotLabeler()
db = Database()
task_manager = TaskManager()
ctx_storage = CtxStorage()

# Состояния пользователей (аналог FSM)
user_states = {}

class TaskStates:
    waiting_for_answer = "waiting_for_answer"
    waiting_for_confirmation = "waiting_for_confirmation"

@tasks_labeler.callback_query(payload={"cmd": "task_1-10"})
async def process_task_selection(callback: CallbackQuery):
    """Выбор заданий 1-10"""
    user_id = callback.from_id
    # Очищаем состояние
    if user_id in user_states:
        del user_states[user_id]
    
    await callback.ctx_api.messages.send(
        peer_id=user_id,
        message="Выберите тип задания",
        keyboard=get_task_id_keyboard()
    )
    await callback.answer()

async def send_task(task_id, message: Message, user_id: int):
    """Отправка задания"""
    print('make tasks')
    data = task_manager.get_random(task_id)
    id = data['id']
    condition = data['condition']
    answer = data['answer']

    # Очистка HTML тегов
    caption_text = re.sub(r'<br\s*/?>', '\n', condition, flags=re.IGNORECASE)
    caption_text = re.sub(r'<.*?>', '', caption_text)
    caption_text = f"Описание: {html.escape(caption_text)}"

    print(f'############# answer: {answer}')

    await message.answer(caption_text, keyboard=get_task_answer_keyboard(task_id, id, 1))

    # Сохраняем состояние
    user_states[user_id] = {
        "state": TaskStates.waiting_for_answer,
        "current_task": task_id,
        "correct_answer": answer,
        "attempts": 0
    }

@tasks_labeler.callback_query(payload={"cmd": "task_id"})
async def process_task_learning_selection(callback: CallbackQuery):
    """Выбор конкретного задания"""
    task_id = callback.payload.get("id")
    user_id = callback.from_id
    
    # Создаем фейковое сообщение для совместимости
    from vkbottle.bot import Message
    msg = Message(
        text="",
        peer_id=user_id,
        from_id=user_id,
        id=0,
        date=0
    )
    msg.ctx_api = callback.ctx_api
    
    await send_task(task_id, msg, user_id)
    await callback.answer()

@tasks_labeler.callback_query(payload={"cmd": "get_answer"})
async def process_get_answer(callback: CallbackQuery):
    """Показать ответ"""
    task_id = callback.payload.get("task_id")
    id = callback.payload.get("id")
    
    data = task_manager.get_by_id(task_id, id)
    answer = data['answer']
    
    user_id = callback.from_id
    await callback.ctx_api.messages.send(
        peer_id=user_id,
        message=f'✅Правильный ответ: {answer}'
    )
    await callback.answer()
    
    # Очищаем состояние
    if user_id in user_states:
        del user_states[user_id]

@tasks_labeler.message()
async def handle_answer(message: Message):
    """Обработка ответа пользователя"""
    user_id = message.from_id
    
    # Проверяем, есть ли состояние ожидания ответа
    if user_id not in user_states or user_states[user_id].get("state") != TaskStates.waiting_for_answer:
        return  # Не обрабатываем, если не ждем ответ
    
    user_answer = message.text.strip().lower()
    print(user_answer)
    
    # Получаем данные из состояния
    state_data = user_states[user_id]
    correct_answer = state_data.get('correct_answer')
    task_id = state_data.get('current_task')
    attempts = state_data.get('attempts', 0) + 1
    
    # Обновляем количество попыток
    user_states[user_id]['attempts'] = attempts
    
    # Проверяем ответ
    if user_answer == correct_answer.lower():
        # Правильный ответ
        await message.answer(
            "✅ **АБСОЛЮТНО ВЕРНО!**\n\n"
            f"Вы ответили с {attempts} попытки!"
        )
        # Очищаем состояние и отправляем новое задание
        del user_states[user_id]
        await send_task(task_id, message, user_id)
    else:
        # Неправильный ответ
        if attempts >= 3:
            # Сдаемся после 3 попыток
            await message.answer(
                f"❌ К сожалению, правильный ответ: **{correct_answer}**\n\n"
            )
            del user_states[user_id]
            await send_task(task_id, message, user_id)
        else:
            # Даем еще попытку
            await message.answer(
                f"❌ Неправильно. Попробуйте еще раз.\n"
                f"Осталось попыток: {3 - attempts}"
            )