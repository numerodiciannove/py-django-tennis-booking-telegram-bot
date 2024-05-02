from aiogram import Bot
from aiogram.types import Message
from telegream_bot.keyboards.profile_kb import profile_kb
from telegream_bot.keyboards.сalendar_kb import calendar_day_kb


async def go_to_main_menu(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"Обери далі...",
        reply_markup=profile_kb
    )


async def show_calendar_days(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"Обери далі...",
        reply_markup=calendar_day_kb
    )
