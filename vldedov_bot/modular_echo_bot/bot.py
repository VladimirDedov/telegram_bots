import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

#Функция конфигурирования и запуска бота
async def main()-> None:
    config: Config = load_config() # Загружаем конфиг в переменную config
    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    #запускаем polling
    await dp.start_polling(bot)

#main асинхронная, мы не можем ее просто вызвать, как привыкли это
# делать с синхронными функциями, но зато мы можем запустить цикл событий
if __name__ == '__main__':
    asyncio.run(main())#Запуск цикла событий