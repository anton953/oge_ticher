from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from tasks.task_manager import TaskManager
from keyboars import *
from database import Database

from task_manager import TaskManager

router = Router()
db = Database()
task_manager = TaskManager()



class TaskStates(StatesGroup):
    waiting_for_answer = State()
    waiting_for_confirmation = State()

 
@router.callback_query(F.data.startswith("variant_"))
async def process_task_learning_selection(callback: CallbackQuery):

    print('make variant')



@router.callback_query(F.data.startswith("redy_variant"))
async def process_task_selection(callback: CallbackQuery):
    await callback.message.answer("Выберите вариант", reply_markup=get_variant_keyboard())
    await callback.message.delete() # type: ignore
    pass
