from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from asgiref.sync import sync_to_async
from booking.models import Booking
from telegream_bot.keyboards.create_kb import usr_time_slots_for_delete_kb
from telegream_bot.keyboards.сalendar_kb import calendar_kb
from user.models import TelegramUser


async def start_bookings_for_delete(
        message: Message,
        bot: Bot,
):
    await bot.send_message(
        message.from_user.id,
        f"Обери що відминити:",
        reply_markup=await usr_time_slots_for_delete_kb(message.from_user.id)
    )


async def delete_booking(call: CallbackQuery, state: FSMContext):
    data = call.data.split("_")
    if len(data) == 4:
        day, time_slot, event, is_repetitive = data
        await delete_booking_from_db(call.from_user.id, day, time_slot)
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer(
            "Час був видалений.",
            reply_markup=calendar_kb
        )
    else:
        await call.message.edit_reply_markup(reply_markup=None)
        await call.message.answer("Неправильний формат даних.")


@sync_to_async
def delete_booking_from_db(user_id: int, day: str, time_slot: str):
    user = TelegramUser.objects.get(telegram_id=user_id)
    booking = Booking.objects.get(user=user, day=day, time=time_slot)
    booking.delete()
