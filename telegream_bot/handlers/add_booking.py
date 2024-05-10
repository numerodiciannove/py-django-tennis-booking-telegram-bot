from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from asgiref.sync import sync_to_async
from booking.models import Booking
from telegream_bot.keyboards.profile_kb import profile_kb
from telegream_bot.keyboards.сalendar_kb import (
    add_day_calendar_kb,
    is_repetitive_calendar_kb,
    events_calendar_kb,
)
from telegream_bot.keyboards.create_kb import time_slots_kb
from telegream_bot.state.booking import BookingState
from user.models import TelegramUser


async def start_booking(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id,
                           "Давай почнемо💫.\n⚠️Вибирай відповідь тільки нажаттям на кнопки!⚠️")

    await bot.send_message(
        message.from_user.id,
        f"Обери день, натисни кнопку нижче...",
        reply_markup=add_day_calendar_kb,
    )

    await state.set_state(BookingState.day)


async def add_day(message: Message, state: FSMContext, bot: Bot):
    day_choices = [day[0] for day in Booking.DAY_OF_WEEK]

    if message.text not in day_choices:
        await state.clear()
        await bot.send_message(
            message.from_user.id,
            f"Меню....",
            reply_markup=profile_kb,
        )
        return

    await bot.send_message(
        message.from_user.id,
        f"Обери вільний час, натисни кнопку нижче...",
        reply_markup=await time_slots_kb(message.text),
    )
    await state.update_data(regday=message.text)
    await state.set_state(BookingState.time)


async def add_time(
        call: CallbackQuery,
        state: FSMContext,
):
    await call.message.answer(
        f"Добре, це постійна бронь, чи одноразова? \n\n Обери нижче:",
        reply_markup=is_repetitive_calendar_kb
    )
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.update_data(regtime=call.data)
    await state.set_state(BookingState.is_repetitive)


async def add_is_repetitive(message: Message, state: FSMContext, bot: Bot):
    repetitive_choices = ["Одноразова", "Постійна"]

    if message.text not in repetitive_choices:
        await state.clear()
        await bot.send_message(
            message.from_user.id,
            f"Меню...",
            reply_markup=profile_kb,
        )
        return

    await state.update_data(regisrepetetive=message.text)

    await bot.send_message(
        message.from_user.id,
        f"Обери подію: \n\n"
        f"🎾: Гра в теніс\n"
        f"🎾💪: Персональне тренування\n"
        f"🎾👶: Тенісна група для дітей\n"
        f"🎾👨‍👦‍👦️: Тенісна група для дорослих\n"
        f"🎾🏆: Тенісний турнір\n"
        f"🏐: Волейбол\n\n"
        f"Натисни кнопку нижче...",
        reply_markup=events_calendar_kb,
    )

    await state.set_state(BookingState.event)


async def add_event(message: Message, state: FSMContext, bot: Bot):
    event_choices = [event[0] for event in Booking.EVENTS]

    if message.text not in event_choices:
        await state.clear()
        await bot.send_message(
            message.from_user.id,
            f"Меню....",
            reply_markup=profile_kb,
        )
        return

    await state.update_data(reg_event=message.text)

    reg_data = await state.get_data()
    reg_day = reg_data.get("regday")
    reg_time = reg_data.get("regtime")
    reg_is_repetitive = reg_data.get("regisrepetetive")
    reg_event = reg_data.get("reg_event")

    await create_booking(
        user_telegram_id=message.from_user.id,
        day=reg_day,
        time=reg_time,
        is_repetitive=reg_is_repetitive,
        event=reg_event
    )

    booking_text = (
        f"🔴 Нова бронь!\n\n"
        f"Створив: @{message.from_user.username}\n"
        f"День: {reg_day}\n"
        f"Час: {reg_time}\n"
        f"{reg_is_repetitive}\n"
        f"Івент: {reg_event}"
    )

    await bot.send_message(
        chat_id=888888,
        text=booking_text
    )

    await state.clear()

    await bot.send_message(
        message.from_user.id,
        "Все добре! 🤓 Записав тебе ✍️",
        reply_markup=profile_kb,
    )


@sync_to_async
def create_booking(user_telegram_id, day, time, is_repetitive, event):
    user = TelegramUser.objects.get(telegram_id=user_telegram_id)

    if is_repetitive == "Постійна":
        is_repetitive = True
    else:
        is_repetitive = False

    if user.is_allowed:
        Booking.objects.create(
            user=user,
            day=day,
            time=time,
            is_repetitive=is_repetitive,
            event=event
        )
