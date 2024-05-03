import asyncio
import logging
import os

from aiogram import Dispatcher, Bot, F
from dotenv import load_dotenv
from telegream_bot.handlers.add_booking import (
    start_booking,
    add_day,
    add_time,
    add_is_repetitive,
    add_event
)
from telegream_bot.handlers.cahnge_profile import change_profile
from telegream_bot.handlers.calendar import (
    open_calendar,
    show_calendar_all,
    get_monday_calendar,
    get_tuesday_calendar,
    get_wednesday_calendar,
    get_thursday_calendar,
    get_friday_calendar,
    get_saturday_calendar,
    get_sunday_calendar
)
from telegream_bot.handlers.chane_user import (
    start_change_name,
    set_new_name,
    set_new_phone, start_change_phone
)
from telegream_bot.handlers.delete_booking import start_bookings_for_delete
from telegream_bot.handlers.menu import go_to_main_menu, show_calendar_days
from telegream_bot.handlers.my_bookings import get_my_bookings
from telegream_bot.state.booking import BookingState
from telegream_bot.state.change_name import ChangeUserName
from telegream_bot.state.change_phone import ChangeUserPhone
from telegream_bot.state.register import RegisterState

from .handlers.start import get_start
from .utils.commands import set_commands
from aiogram.filters import Command
from .handlers.registration import (
    start_register,
    register_name,
    register_phone
)

load_dotenv()

ADMIN_ID = os.environ["ADMIN_ID"]
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()


# Send a message to admin when bot started
async def start_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text="Бот запущен!")


# Start message
dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands="start"))

# Register user
dp.message.register(start_register, F.text == "Зареєструватись")
dp.message.register(register_name, RegisterState.first_name)
dp.message.register(register_phone, RegisterState.phone_number)

# Menu
dp.message.register(go_to_main_menu, F.text == "🔙 Повернутись до меню")

# Calendar
dp.message.register(open_calendar, F.text == "🗓Календар")
dp.message.register(get_monday_calendar, F.text == "🗓Понеділок")
dp.message.register(get_tuesday_calendar, F.text == "🗓Вівторок")
dp.message.register(get_wednesday_calendar, F.text == "🗓Середа")
dp.message.register(get_thursday_calendar, F.text == "🗓Четвер")
dp.message.register(get_friday_calendar, F.text == "🗓П’ятниця")
dp.message.register(get_saturday_calendar, F.text == "🗓Субота")
dp.message.register(get_sunday_calendar, F.text == "🗓Неділя")
dp.message.register(show_calendar_all,
                    F.text == "🔎 Переглянути розклад на тиждень")
dp.message.register(show_calendar_days,
                    F.text == "🔎 Переглянути розклад по дням")

# Create booking
dp.message.register(start_booking, F.text == "✍️ Cтворити бронь")
dp.message.register(add_day, BookingState.day)
dp.callback_query.register(add_time, BookingState.time)
dp.message.register(add_is_repetitive, BookingState.is_repetitive)
dp.message.register(add_event, BookingState.event)

# Change user -Є profile keyboard
dp.message.register(change_profile, F.text == "😎Профіль")

# Change user name
dp.message.register(start_change_name, F.text == "Змінити ім'я")
dp.message.register(set_new_name, ChangeUserName.first_name)

# Change user phone
dp.message.register(start_change_phone, F.text == "Змінити номер телефону")
dp.message.register(set_new_phone, ChangeUserPhone.phone_number)

# Get user bookings
dp.message.register(get_my_bookings, F.text == "📝 Мої бронювання")

# Delete my bookings
dp.message.register(start_bookings_for_delete, F.text == "❌ Відминити бронь")


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
