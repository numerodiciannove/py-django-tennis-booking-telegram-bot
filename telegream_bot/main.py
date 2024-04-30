import asyncio
import logging
import os

import dotenv
from aiogram import Bot, Dispatcher, types

dotenv.load_dotenv()

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
