from aiogram import Bot
from aiogram.types import Message
from asgiref.sync import sync_to_async
from booking.models import Booking
from user.models import TelegramUser


async def get_my_bookings(message: Message, bot: Bot):
    bookings = await get_user_bookings(message.from_user.id)
    if isinstance(bookings, str):
        await bot.send_message(
            message.from_user.id,
            bookings,
        )
    else:
        formatted_bookings = "\n".join(
            [f"{day}: {time} - {event}" for day, time, event, is_repetitive in
             bookings])
        await bot.send_message(
            message.from_user.id,
            formatted_bookings,
        )


@sync_to_async
def get_user_bookings(user_telegram_id: int):
    user = TelegramUser.objects.get(telegram_id=user_telegram_id)
    bookings = Booking.objects.filter(user=user).values_list("day",
                                                             "time",
                                                             "event",
                                                             "is_repetitive"
                                                             )
    if not bookings:
        return "Ще нема записів."
    return list(bookings)
