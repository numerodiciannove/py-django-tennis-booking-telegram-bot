from aiogram.utils.keyboard import InlineKeyboardBuilder
from asgiref.sync import sync_to_async
from booking.models import Booking


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
