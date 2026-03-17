from vkbottle.bot import Message, BotLabeler
from vkbottle import PhotoMessageUploader

from keyboars.k_learning import get_task_learning_type_keyboard

learning_labeler = BotLabeler()

@learning_labeler.callback_query(payload={"cmd": "learning"})
async def process_task_learning_selection(callback):
    """Обработка выбора обучения"""
    task_id = callback.payload.get("id")
    user_id = callback.from_id
    
    # Загружаем фото
    photo_uploader = PhotoMessageUploader(callback.ctx_api)
    photo = await photo_uploader.upload(f"photo/{task_id}.png")
    
    await callback.ctx_api.messages.send(
        peer_id=user_id,
        attachment=photo,
        message=f'задание №{task_id}'
    )
    await callback.answer("Фото отправлено!")