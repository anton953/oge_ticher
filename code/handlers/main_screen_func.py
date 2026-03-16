from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
# from tasks.task_manager import TaskManager
from keyboars.keyboars import *
from keyboars.k_learning import get_task_learning_type_keyboard

from database import Database

router = Router()
db = Database()
# task_manager = TaskManager()

class TaskStates(StatesGroup):
    waiting_for_answer = State()
    waiting_for_confirmation = State()

@router.message(F.text == "🚀 Получить задание")
async def get_task_menu(message: Message, state: FSMContext):
    await state.clear()   

    """Меню выбора типа задания"""
    text = """
    📚 <b>Выбери тип задания:</b>
    
    • <b>🎲 Случайное</b> - задача из любой темы
    • <b>🔢 Номера 1-5</b> - информация и её кодирование
    • <b>💻 Номера 6-11</b> - алгоритмы и программирование
    • <b>📊 Номера 12-18</b> - анализ данных и таблицы
    • <b>🧩 Задание 13-16</b> - исполнители и алгоритмы
    • <b>📈 Задание 17</b> - электронные таблицы
    
    Выбирай и начинай решать! 💪
    """
    await message.answer(text, parse_mode="HTML", reply_markup=get_task_type_keyboard())





@router.message(F.text == "📚 Oбучение")
async def learning(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Выберите тип задания", reply_markup=get_task_learning_type_keyboard())











