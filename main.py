# my_bot/main.py
import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import other_handlers, user_handlers
from config_date.config import Config, load_config
from keyboards.set_menu import set_main_menu

# Загрузка переменных из .env файла
config: Config = load_config()

#Инициализируем Логер
logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    # Получаем токен из переменных среды
    bot = Bot(
        token=config.tg_bot.token)
    await set_main_menu(bot)

    dp = Dispatcher()

    # Подключаем роутер
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)


    # Запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

