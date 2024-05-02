import logging

from aiogram import Bot
from aiogram.types import Message
from asgiref.sync import sync_to_async
from booking.models import Booking

from telegream_bot.keyboards.сalendar_kb import calendar_kb

logger = logging.getLogger(__name__)


async def open_calendar(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"Обери далі...",
        reply_markup=calendar_kb
    )


async def get_monday_calendar(message: Message, bot: Bot):
    try:
        day_info = await get_day_calendar("Понеділок")
        await send_day_info(message.from_user.id, day_info, bot)
    except Exception as e:
        await bot.send_message(
            message.from_user.id,
            f"Произошла ошибка: {str(e)}"
        )


async def get_tuesday_calendar(message: Message, bot: Bot):
    try:
        day_info = await get_day_calendar("Вівторок")
        await send_day_info(message.from_user.id, day_info, bot)
    except Exception as e:
        await bot.send_message(
            message.from_user.id,
            f"Произошла ошибка: {str(e)}"
        )


async def get_wednesday_calendar(message: Message, bot: Bot):
    try:
        day_info = await get_day_calendar("Середа")
        await send_day_info(message.from_user.id, day_info, bot)
    except Exception as e:
        await bot.send_message(
            message.from_user.id,
            f"Произошла ошибка: {str(e)}"
        )


async def get_thursday_calendar(message: Message, bot: Bot):
    try:
        day_info = await get_day_calendar("Четвер")
        await send_day_info(message.from_user.id, day_info, bot)
    except Exception as e:
        await bot.send_message(
            message.from_user.id,
            f"Произошла ошибка: {str(e)}"
        )


async def get_friday_calendar(message: Message, bot: Bot):
    try:
        day_info = await get_day_calendar("П’ятниця")
        await send_day_info(message.from_user.id, day_info, bot)
    except Exception as e:
        await bot.send_message(
            message.from_user.id,
            f"Произошла ошибка: {str(e)}"
        )


async def get_saturday_calendar(message: Message, bot: Bot):
    try:
        day_info = await get_day_calendar("Субота")
        await send_day_info(message.from_user.id, day_info, bot)
    except Exception as e:
        await bot.send_message(
            message.from_user.id,
            f"Произошла ошибка: {str(e)}"
        )


async def get_sunday_calendar(message: Message, bot: Bot):
    try:
        day_info = await get_day_calendar("Неділя")
        await send_day_info(message.from_user.id, day_info, bot)
    except Exception as e:
        await bot.send_message(
            message.from_user.id,
            f"Произошла ошибка: {str(e)}"
        )


# Show one day
async def get_day_calendar(day):
    try:
        day_info = {'day': f"🗓 <b>{day}</b>", 'bookings': []}
        for time, _ in Booking.TIME_SLOTS:
            bookings_info = await get_bookings_for_day_time_event(day, time)
            day_info['bookings'].append(
                {'time': time, 'bookings_info': bookings_info})
        return day_info
    except Exception as e:
        logger.error(f"Error getting calendar for day {day}: {str(e)}")
        return None


# Show all days
async def show_calendar_all(message: Message, bot: Bot):
    try:
        all_days = await get_all_calendar_days()
        for day_info in all_days:
            await send_day_info(message.from_user.id, day_info, bot)
    except Exception as e:
        await bot.send_message(
            message.from_user.id,
            f"Виникла помилка: {str(e)}"
        )


async def get_all_calendar_days():
    all_days = []
    for day, _ in Booking.DAY_OF_WEEK:
        day_info = {'day': f"🗓 <b>{day}</b>", 'bookings': []}
        for time, _ in Booking.TIME_SLOTS:
            bookings_info = await get_bookings_for_day_time_event(day, time)
            day_info['bookings'].append(
                {'time': time, 'bookings_info': bookings_info})
        all_days.append(day_info)
    return all_days


async def send_day_info(user_id, day_info, bot):
    try:
        day_message = f"{day_info['day']}\n \n"
        for booking_info in day_info['bookings']:
            time = booking_info['time']
            bookings_info = booking_info['bookings_info']
            if bookings_info:
                booked_by_str = ', '.join([info[0] for info in bookings_info])
                event_str = ', '.join([info[1] for info in bookings_info])
                is_repetitive_str = ', '.join([str(info[2]) for info in bookings_info])
                if is_repetitive_str:
                    is_repetitive_str = "🔁"
                else:
                    is_repetitive_str = ""
                booking_message = f"🔴 <b>{time}</b> {is_repetitive_str}{event_str}{booked_by_str}\n"
            else:
                booking_message = f"🟢 <b>{time}</b>: Вільно\n"
            day_message += booking_message
        await bot.send_message(user_id, day_message)
    except Exception as e:
        await bot.send_message(
            user_id,
            f"Виникла помилка: {str(e)}"
        )

@sync_to_async
def get_bookings_for_day_time_event(day, time):
    bookings = Booking.objects.filter(day=day, time=time).values_list(
        'user__telegram_username', 'event', 'is_repetitive'
    )
    return list(bookings)
