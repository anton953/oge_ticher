from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from task_manager import TaskManager

from keyboars.k_tasks import *

from database import Database

from task_manager import TaskManager


import re
from aiogram import html


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
            # caption=clean_caption
        )
        # response = requests.get(url)

        # if response.status_code == 200:
        #     with open('buuf.jpg', 'wb') as f:
        #         f.write(response.content)
        #     print("Фото успешно скачано")
        # else:
        #     print("Не удалось скачать фото")
        
    # caption_text = "Евпсихий решил серьезно заняться изучением языков программирования. Он записал одну и ту же программу на разных языках.\n\nПрограмма:\n```python\ns = int(input())\nt = int(input())\nA = int(input())\nif (s < A) and (t > 5) and (s > 5) and (t < A):\n    print(\"YES\")\nelse:\n    print(\"NO\")\n```\n\nБыло проведено 9 запусков программы, при которых в качестве значений переменных s и t вводились следующие пары чисел:\n(1, 2); (12, 3); (3, 12); (11, 12); (-13, -12); (-13, 12); (-14, 11); (10, 10); (10, 6)\n\nСколько существует целых значений параметра А, при котором для указанных входных данных программа напечатает «YES» 2 раза?"
    # caption_text = re.sub(r'<br\s*/?>', '\n', caption_text, flags=re.IGNORECASE)
    caption_text = re.sub(r'<.*?>', '', condition)
    caption_text = f"Описание: {html.quote(caption_text)}"

    
    await callback.message.answer(caption_text, reply_markup=get_task_answer_keyboard(task_id, id, 1))

    

@router.callback_query(F.data.startswith("get_answer_"))
async def process_task_selection(callback: CallbackQuery):
    task_id = int(callback.data.split("_")[2])
    id = int(callback.data.split("_")[3])


    data = task_manager.get_by_id(task_id, id)
    answer = data['answer']  



    await callback.message.answer(f'Правельный ответ: {answer}', 0)
    # await callback.message.delete() # type: ignore





@router.callback_query(F.data.startswith("task_1-10"))
async def process_task_selection(callback: CallbackQuery):
    await callback.message.answer("Выберите тип задания", reply_markup=get_task_id_keyboard())
    await callback.message.delete() # type: ignore


