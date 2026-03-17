from vkbottle import Keyboard, KeyboardButtonColor, Text, Callback

def get_main_menu():
    """Основное меню (Reply клавиатура)"""
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.add(Text("🚀 Получить задание"), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("📚 Обучение"), color=KeyboardButtonColor.SECONDARY)
    keyboard.row()
    keyboard.add(Text("ℹ️ Помощь"), color=KeyboardButtonColor.SECONDARY)
    keyboard.add(Text("📊 Моя статистика"), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("📈 Топ игроков"), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("⚙️ Настройки"), color=KeyboardButtonColor.NEGATIVE)
    return keyboard

def get_task_type_keyboard():
    """Выбор типа задания (Inline клавиатура)"""
    keyboard = Keyboard(inline=True)
    keyboard.add(Callback("Задания 1-10", payload={"cmd": "task_1-10"}), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Callback("Готовые варианты", payload={"cmd": "redy_variant"}), color=KeyboardButtonColor.SECONDARY)
    return keyboard

def get_answer_keyboard(task_id):
    """Клавиатура с вариантами ответа"""
    keyboard = Keyboard(inline=True)
    keyboard.add(Callback("✅ Проверить ответ", payload={"cmd": "check", "task_id": task_id}), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Callback("💡 Подсказка", payload={"cmd": "hint", "task_id": task_id}), color=KeyboardButtonColor.SECONDARY)
    keyboard.row()
    keyboard.add(Callback("📝 Решение", payload={"cmd": "solution", "task_id": task_id}), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Callback("➡️ Следующее", payload={"cmd": "next_task"}), color=KeyboardButtonColor.SECONDARY)
    return keyboard

def get_confirmation_keyboard():
    """Клавиатура подтверждения"""
    keyboard = Keyboard(inline=True)
    keyboard.add(Callback("✅ Да, правильно!", payload={"cmd": "confirm_correct"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Callback("❌ Нет, ошибка", payload={"cmd": "confirm_wrong"}), color=KeyboardButtonColor.NEGATIVE)
    return keyboard