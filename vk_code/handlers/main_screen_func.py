from vkbottle.bot import Message, BotLabeler
from vkbottle import CtxStorage

from keyboars.keyboars import get_task_type_keyboard
from keyboars.k_learning import get_task_learning_type_keyboard

main_screen_labeler = BotLabeler()
db = Database()  # Предполагается импорт из start.py или отдельно
ctx_storage = CtxStorage()

@main_screen_labeler.message(text="🚀 Получить задание")
async def get_task_menu(message: Message):
    """Меню выбора типа задания"""
    text = """
📚 **Выбери тип задания:**

• **🎲 Случайное** - задача из любой темы
• **🔢 Номера 1-5** - информация и её кодирование
• **💻 Номера 6-11** - алгоритмы и программирование
• **📊 Номера 12-18** - анализ данных и таблицы
• **🧩 Задание 13-16** - исполнители и алгоритмы
• **📈 Задание 17** - электронные таблицы

Выбирай и начинай решать! 💪
"""
    await message.answer(text, keyboard=get_task_type_keyboard())

@main_screen_labeler.message(text="📚 Обучение")
async def learning(message: Message):
    """Обучение"""
    await message.answer("Выберите тип задания", keyboard=get_task_learning_type_keyboard())