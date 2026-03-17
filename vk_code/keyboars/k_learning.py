from vkbottle import Keyboard, KeyboardButtonColor, Callback

def get_task_id_keyboard():
    """Выбор номера задания"""
    keyboard = Keyboard(inline=True)
    for i in range(1, 11):
        keyboard.add(Callback(str(i), payload={"cmd": "task_id", "id": i}), color=KeyboardButtonColor.PRIMARY)
        if i % 3 == 0:
            keyboard.row()
    return keyboard

def get_task_learning_type_keyboard():
    """Выбор типа обучения (1-13)"""
    keyboard = Keyboard(inline=True)
    for i in range(1, 14):
        keyboard.add(Callback(str(i), payload={"cmd": "learning", "id": i}), color=KeyboardButtonColor.PRIMARY)
        if i % 3 == 0:
            keyboard.row()
    return keyboard