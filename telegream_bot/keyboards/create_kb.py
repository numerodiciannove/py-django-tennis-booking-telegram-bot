from aiogram.utils.keyboard import InlineKeyboardBuilder
from asgiref.sync import sync_to_async
from booking.models import Booking
from user.models import TelegramUser


@sync_to_async
def time_slots_kb(day):
    all_time_slots = [time[0] for time in Booking.TIME_SLOTS]
    booked_time_slots = Booking.objects.filter(day=day).values_list("time",
                                                                    flat=True)
    available_time_slots = [
        time_slot for time_slot in all_time_slots
        if time_slot not in booked_time_slots
    ]
    kb = InlineKeyboardBuilder()
    for time_slot in available_time_slots:
        kb.button(text=f"{time_slot}", callback_data=f"{time_slot}")
        kb.adjust(1)
    return kb.as_markup()


@sync_to_async
def usr_time_slots_for_delete_kb(telegram_user_id):
    user = TelegramUser.objects.get(telegram_id=telegram_user_id)
    user_booked_time_slots = Booking.objects.filter(user=user).values_list('day', 'time')

    kb = InlineKeyboardBuilder()

    for day, time_slot in user_booked_time_slots:
        kb.button(text=f"{day}: {time_slot}", callback_data=f"{day}_{time_slot}")
        kb.adjust(1)
    return kb.as_markup()
