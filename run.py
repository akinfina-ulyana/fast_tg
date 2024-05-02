import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
from app.database.models import async_main

import logging

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
