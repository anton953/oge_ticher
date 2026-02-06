from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from database import Database
from keyboars import get_main_menu

router = Router()
db = Database()

@router.message(CommandStart())
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name
    
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
    
    await message.answer(welcome_text, reply_markup=get_main_menu())

@router.message(Command("help"))
async def cmd_help(message: Message):
    """Обработчик команды /help"""
    help_text = """
    ℹ️ <b>Справка по использованию бота</b>
    
    <b>Основные команды:</b>
    /start - Начать работу с ботом
    /help - Получить справку
    /stats - Посмотреть статистику
    /top - Топ-10 игроков
    
    <b>Как работать с ботом:</b>
    1. Нажми "📚 Получить задание"
    2. Выбери тему или получи случайное задание
    3. Реши задачу и отправь ответ
    4. Получи проверку и объяснение
    5. Следи за своим прогрессом в статистике!
    
    <b>Подсказки:</b>
    • Используй кнопку "💡 Подсказка" если задача кажется сложной
    • После решения смотри "📝 Решение" для лучшего понимания
    • Регулярные занятия - ключ к успеху!
    """
    await message.answer(help_text, parse_mode="HTML")

@router.message(F.text == "ℹ️ Помощь")
async def menu_help(message: Message):
    """Обработчик кнопки Помощь"""
    await cmd_help(message)
















@router.callback_query(F.data.startswith("hint_"))
async def get_hint(callback: CallbackQuery):
    """Получение подсказки"""
    await callback.answer()
    task_id = int(callback.data.split("_")[1])
    
    task = task_manager.get_task(task_id=task_id)
    if task and "hints" in task and task["hints"]:
        hint_text = f"💡 <b>Подсказка к заданию #{task_id}:</b>\n\n{task['hints'][0]}"
        await callback.message.answer(hint_text, parse_mode="HTML")
    else:
        await callback.message.answer("🤔 Подсказка для этого задания пока не готова.")

@router.callback_query(F.data.startswith("solution_"))
async def get_solution(callback: CallbackQuery):
    """Получение решения"""
    await callback.answer()
    task_id = int(callback.data.split("_")[1])
    
    task = task_manager.get_task(task_id=task_id)
    if task and "explanation" in task:
        solution_text = f"📝 <b>Решение задания #{task_id}:</b>\n\n{task['explanation']}"
        await callback.message.answer(solution_text, parse_mode="HTML")
    else:
        await callback.message.answer("📖 Решение для этого задания готовится.")

@router.callback_query(F.data == "next_task")
async def get_next_task(callback: CallbackQuery):
    """Следующее задание"""
    await callback.answer()
    await get_task_menu(callback.message)