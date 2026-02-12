from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from task_manager import TaskManager

from keyboars.k_tasks import *

from database import Database

from task_manager import TaskManager


import requests


router = Router()
db = Database()
task_manager = TaskManager()



class TaskStates(StatesGroup):
    waiting_for_answer = State()
    waiting_for_confirmation = State()


@router.callback_query(F.data.startswith("task_id_"))
async def process_task_learning_selection(callback: CallbackQuery):

    print('make tasks')
    task_id = int(callback.data.split("_")[2])
    data = task_manager.get_random(task_id)
    id = data['id']
    condition = data['condition']
    answer = data['answer']  
    
    

    if '<img src=' in condition:
        b = condition.find('\"')
        e = condition.rfind('\"')

        ur = condition[(b + 1):e]

        url = 'https://kpolyakov.spb.ru/cms/images/' + ur

        await callback.message.answer_photo(
            photo=url,
            caption="Фото из интернета"
        )
        # response = requests.get(url)

        # if response.status_code == 200:
        #     with open('buuf.jpg', 'wb') as f:
        #         f.write(response.content)
        #     print("Фото успешно скачано")
        # else:
        #     print("Не удалось скачать фото")
        
    
    await callback.message.answer(condition, reply_markup=get_task_id_keyboard())

    





@router.callback_query(F.data.startswith("task_1-10"))
async def process_task_selection(callback: CallbackQuery):
    await callback.message.answer("Выберите тип задания", reply_markup=get_task_id_keyboard())
    await callback.message.delete() # type: ignore
