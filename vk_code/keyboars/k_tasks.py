from vkbottle import Keyboard, KeyboardButtonColor, Callback

def get_task_type_keyboard():
    """Выбор типа задания"""
    keyboard = Keyboard(inline=True)
    keyboard.add(Callback("Задания 1-10", payload={"cmd": "task_1-10"}), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Callback("Готовые варианты", payload={"cmd": "redy_variant"}), color=KeyboardButtonColor.SECONDARY)
    return keyboard

def get_task_id_keyboard():
    """Выбор номера задания 1-10"""
    keyboard = Keyboard(inline=True)
    for i in range(1, 11):
        keyboard.add(Callback(str(i), payload={"cmd": "task_id", "id": i}), color=KeyboardButtonColor.PRIMARY)
        if i % 3 == 0:
            keyboard.row()
    return keyboard

def get_task_answer_keyboard(id_task, id, flag=0):
    """Клавиатура для ответа на задание"""
    keyboard = Keyboard(inline=True)
    if flag:
        keyboard.add(Callback("Показать ответ", payload={"cmd": "get_answer", "task_id": id_task, "id": id}), color=KeyboardButtonColor.POSITIVE)
        keyboard.row()
        keyboard.add(Callback("выбор заданий", payload={"cmd": "task_1-10"}), color=KeyboardButtonColor.SECONDARY)
        keyboard.add(Callback("=>", payload={"cmd": "task_id", "id": id_task}), color=KeyboardButtonColor.PRIMARY)
    return keyboard