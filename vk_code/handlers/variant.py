from vkbottle.bot import BotLabeler
from vkbottle import CallbackQuery

from keyboars.k_variant import get_variant_keyboard

variant_labeler = BotLabeler()

@variant_labeler.callback_query(payload={"cmd": "variant"})
async def process_variant_selection(callback: CallbackQuery):
    """Обработка выбора варианта"""
    print('make variant')
    await callback.answer("Вариант выбран!")

@variant_labeler.callback_query(payload={"cmd": "redy_variant"})
async def process_ready_variant(callback: CallbackQuery):
    """Показать готовые варианты"""
    user_id = callback.from_id
    await callback.ctx_api.messages.send(
        peer_id=user_id,
        message="Выберите вариант",
        keyboard=get_variant_keyboard()
    )
    await callback.answer()