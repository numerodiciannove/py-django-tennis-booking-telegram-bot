from asgiref.sync import sync_to_async
from booking.models import Booking
from user.models import TelegramUser


@sync_to_async
def get_user_by_telegram_id(telegram_id):
    try:
        user = TelegramUser.objects.get(telegram_id=telegram_id)
        return user
    except TelegramUser.DoesNotExist:
        return None


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
