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

 


@router.callback_query(F.data.startswith("learning_"))
async def process_task_learning_selection(callback: CallbackQuery):

    task_id = int(callback.data.split("_")[1]) # type: ignore
    photo = FSInputFile(f"photo/{task_id}.png")


    await callback.message.answer_photo(photo, caption=f'задание №{task_id}')
    await callback.message.delete()


