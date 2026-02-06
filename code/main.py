import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.start import router as start_router
from handlers.tasks import router as tasks_router
from handlers.main_screen_func import router as main_screen_router

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    """Основная функция запуска бота"""
    
    # Инициализация бота
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    # Инициализация диспетчера
    dp = Dispatcher()
    
    # Подключение роутеров
    dp.include_router(start_router)
    dp.include_router(tasks_router)
    dp.include_router(main_screen_router)
    
    # Запуск polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) # type: ignore

if __name__ == "__main__":
    try:
        logger.info("Бот запускается...")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен")