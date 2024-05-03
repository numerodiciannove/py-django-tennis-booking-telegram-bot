from aiogram import Bot
from aiogram.types import Message
from telegream_bot.utils.db_utils import get_user_bookings


async def get_my_bookings(message: Message, bot: Bot):
    bookings = await get_user_bookings(message.from_user.id)
    if isinstance(bookings, str):
        await bot.send_message(
            message.from_user.id,
            bookings,
        )
    else:
        formatted_bookings = "\n".join(
            [f"{day}: {time} - {'🔁' if is_repetitive else ''}{event}" for day, time, event, is_repetitive in
             bookings])
        await bot.send_message(
            message.from_user.id,
            formatted_bookings,
        )
