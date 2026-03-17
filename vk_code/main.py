import logging
from vkbottle import Bot, API
from vkbottle.framework.labeler import BotLabeler

from config import VK_TOKEN
from handlers.start import start_labeler
from handlers.tasks import tasks_labeler
from handlers.main_screen_func import main_screen_labeler
from handlers.learning import learning_labeler
from handlers.variant import variant_labeler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = Bot(token=VK_TOKEN)
api = API(token=VK_TOKEN)

# Создание главного лейблера
main_labeler = BotLabeler()

# Подключение всех лейблеров
bot.labeler.load(start_labeler)
bot.labeler.load(main_screen_labeler)
bot.labeler.load(learning_labeler)
bot.labeler.load(variant_labeler)
bot.labeler.load(tasks_labeler)

@bot.error_handler.register_error_handler
async def error_handler(event: Exception):
    logger.error(f"Произошла ошибка: {event}")

if __name__ == "__main__":
    logger.info("Бот запускается...")
    bot.run_forever()