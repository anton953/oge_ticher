from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from tasks.task_manager import TaskManager
from keyboars import *
from database import Database

router = Router()
db = Database()
task_manager = TaskManager()

class TaskStates(StatesGroup):
    waiting_for_answer = State()
    waiting_for_confirmation = State()

@router.message(F.text == "🚀 Получить задание")
async def get_task_menu(message: Message):
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
async def learning(message: Message):
    await message.answer("Выберите тип задания", reply_markup=get_task_learning_type_keyboard())


@router.callback_query(F.data.startswith("task_id_"))
async def process_task_learning_selection(callback: CallbackQuery):

    print('make tasks')

 
@router.callback_query(F.data.startswith("variant_"))
async def process_task_learning_selection(callback: CallbackQuery):

    print('make variant')

@router.callback_query(F.data.startswith("task_1-10"))
async def process_task_selection(callback: CallbackQuery):
    await callback.message.answer("Выберите тип задания", reply_markup=get_task_id_keyboard())
    await callback.message.delete() # type: ignore


@router.callback_query(F.data.startswith("redy_variant"))
async def process_task_selection(callback: CallbackQuery):
    await callback.message.answer("Выберите вариант", reply_markup=get_variant_keyboard())
    await callback.message.delete() # type: ignore
    pass



@router.callback_query(F.data.startswith("task_"))
async def process_task_learning_selection(callback: CallbackQuery):

    task_id = int(callback.data.split("_")[1]) # type: ignore
    photo = FSInputFile(f"photo/{task_id}.png")


    await callback.message.answer_photo(photo, caption=f'задание №{task_id}')
    await callback.message.delete()









    

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