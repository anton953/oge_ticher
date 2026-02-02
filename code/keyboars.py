from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder





def get_main_menu():
    """Основное меню"""
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="🚀 Получить задание"))
    builder.add(KeyboardButton(text="📚 Oбучение"))
    builder.add(KeyboardButton(text="ℹ️ Помощь"))
    builder.add(KeyboardButton(text="📊 Моя статистика"))
    builder.add(KeyboardButton(text="📈 Топ игроков"))
    builder.add(KeyboardButton(text="⚙️ Настройки"))

    builder.adjust(2, 2, 2)
    return builder.as_markup(resize_keyboard=True)



def get_task_type_keyboard():
    """Выбор типа задания"""
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Задания 1-10", callback_data="task_1-10"))
    builder.add(InlineKeyboardButton(text="Готовые варианты", callback_data="redy_variant"))
    
    builder.adjust(1)
    return builder.as_markup()


def get_variant_keyboard():
    """Выбор типа задания"""
    builder = InlineKeyboardBuilder()
    for i in range(1, 11):
        builder.add(InlineKeyboardButton(text=f"{i}", callback_data=f"variant_{i}"))
        
    """Выбор типа задания"""
    # builder.add(InlineKeyboardButton(text="16", callback_data="task_16"))
    builder.adjust(3)
    return builder.as_markup()


def get_task_id_keyboard():
    """Выбор типа задания"""
    builder = InlineKeyboardBuilder()
    for i in range(1, 14):
        builder.add(InlineKeyboardButton(text=f"{i}", callback_data=f"task_id_{i}"))
        
    """Выбор типа задания"""
    # builder.add(InlineKeyboardButton(text="16", callback_data="task_16"))
    builder.adjust(3)
    return builder.as_markup()


def get_task_learning_type_keyboard():
    """Выбор типа задания"""
    builder = InlineKeyboardBuilder()
    for i in range(1, 14):
        builder.add(InlineKeyboardButton(text=f"{i}", callback_data=f"task_{i}"))
        
    """Выбор типа задания"""
    # builder.add(InlineKeyboardButton(text="16", callback_data="task_16"))
    builder.adjust(3)
    return builder.as_markup()







def get_answer_keyboard(task_id):
    """Клавиатура с вариантами ответа"""
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="✅ Проверить ответ", callback_data=f"check_{task_id}"))
    builder.add(InlineKeyboardButton(text="💡 Подсказка", callback_data=f"hint_{task_id}"))
    builder.add(InlineKeyboardButton(text="📝 Решение", callback_data=f"solution_{task_id}"))
    builder.add(InlineKeyboardButton(text="➡️ Следующее", callback_data="next_task"))
    builder.adjust(2, 2)
    return builder.as_markup()

def get_confirmation_keyboard():
    """Клавиатура подтверждения"""
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="✅ Да, правильно!", callback_data="confirm_correct"))
    builder.add(InlineKeyboardButton(text="❌ Нет, ошибка", callback_data="confirm_wrong"))
    return builder.as_markup()