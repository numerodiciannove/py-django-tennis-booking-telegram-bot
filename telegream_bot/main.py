import asyncio
import logging

from aiogram import Dispatcher, Bot, F
from dotenv import load_dotenv
from telegream_bot.state.register import RegisterState

from .handlers.start import get_start
from .utils.commands import set_commands
from aiogram.filters import Command
from .handlers.registration import start_register, register_name, register_phone
import os

load_dotenv()

ADMIN_ID = os.environ["ADMIN_ID"]
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Send message to admin when bot started
async def start_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Бот запущен!")


# Start message
dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands="start"))


# Register handler registration
dp.message.register(start_register, F.text=="Зареєструватись")
dp.message.register(register_name, RegisterState.first_name)
dp.message.register(register_phone, RegisterState.phone_number)


async def main():
    # Menu commands
    await set_commands(bot)

    logging.basicConfig(level=logging.INFO)
    try:
        await dp.start_polling(bot, skip_update=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
