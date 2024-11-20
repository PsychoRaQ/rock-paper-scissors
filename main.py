import asyncio
from aiogram import Bot, Dispatcher
from config_data import config
from handlers import other_handlers, user_handlers



async def main() -> None:
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(user_handlers.router, other_handlers.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())