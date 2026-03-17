from vkbottle import Keyboard, KeyboardButtonColor, Callback

def get_variant_keyboard():
    """Выбор варианта (1-10)"""
    keyboard = Keyboard(inline=True)
    for i in range(1, 11):
        keyboard.add(Callback(str(i), payload={"cmd": "variant", "id": i}), color=KeyboardButtonColor.PRIMARY)
        if i % 3 == 0:
            keyboard.row()
    return keyboard