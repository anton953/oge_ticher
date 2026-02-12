from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def get_task_id_keyboard():
    """Выбор типа задания"""
    builder = InlineKeyboardBuilder()
    for i in range(1, 11):
        builder.add(InlineKeyboardButton(text=f"{i}", callback_data=f"task_id_{i}"))
        
    """Выбор типа задания"""
    # builder.add(InlineKeyboardButton(text="16", callback_data="task_16"))
    builder.adjust(3)
    return builder.as_markup()


def get_task_learning_type_keyboard():
    """Выбор типа задания"""
    builder = InlineKeyboardBuilder()
    for i in range(1, 14):
        builder.add(InlineKeyboardButton(text=f"{i}", callback_data=f"learning_{i}"))
        
    """Выбор типа задания"""
    # builder.add(InlineKeyboardButton(text="16", callback_data="task_16"))
    builder.adjust(3)
    return builder.as_markup()
