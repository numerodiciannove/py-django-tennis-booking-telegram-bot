import asyncio
import logging
import os

import dotenv
from aiogram import Bot, Dispatcher, types, Router

dotenv.load_dotenv()

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

main_router = Router()
dp.include_router(main_router)


@main_router.message()
async def echo_message(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Wait a second..."
    )
    await message.answer(text=message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
