from vkbottle.bot import Message, BotLabeler
from vkbottle.dispatch.rules.base import Command

from database import Database
from keyboars.keyboars import get_main_menu

start_labeler = BotLabeler()
db = Database()

@start_labeler.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    user_id = message.from_id
    # Получаем информацию о пользователе через API
    user_info = await message.ctx_api.users.get(user_ids=[user_id])
    username = user_info[0].screen_name if user_info else None
    full_name = f"{user_info[0].first_name} {user_info[0].last_name}" if user_info else "Unknown"

    # Добавляем пользователя в базу данных
    db.add_user(user_id, username, full_name)

    welcome_text = f"""
👋 Привет, {full_name}!

🎯 Я — бот для подготовки к ОГЭ по информатике!

📚 Что я умею:
• Давать задания по всем темам ОГЭ
• Проверять твои ответы
• Показывать подробные решения
• Вести статистику твоих успехов
• Соревноваться с другими учениками

🚀 Начнем подготовку? Выбирай пункт меню ниже!
"""

    await message.answer(welcome_text, keyboard=get_main_menu())

@start_labeler.message(Command("help"))
async def cmd_help(message: Message):
    """Обработчик команды /help"""
    help_text = """
ℹ️ **Справка по использованию бота**

**Основные команды:**
/start - Начать работу с ботом
/help - Получить справку
/stats - Посмотреть статистику
/top - Топ-10 игроков

**Как работать с ботом:**
1. Нажми "🚀 Получить задание"
2. Выбери тему или получи случайное задание
3. Реши задачу и отправь ответ
4. Получи проверку и объяснение
5. Следи за своим прогрессом в статистике!

**Подсказки:**
• Используй кнопку "💡 Подсказка" если задача кажется сложной
• После решения смотри "📝 Решение" для лучшего понимания
• Регулярные занятия - ключ к успеху!
"""
    await message.answer(help_text)

@start_labeler.message(text="ℹ️ Помощь")
async def menu_help(message: Message):
    """Обработчик кнопки Помощь"""
    await cmd_help(message)