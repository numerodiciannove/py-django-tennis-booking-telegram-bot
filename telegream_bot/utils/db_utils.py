from asgiref.sync import sync_to_async
from user.models import TelegramUser


@sync_to_async
def get_user_by_telegram_id(telegram_id):
    try:
        user = TelegramUser.objects.get(telegram_id=telegram_id)
        return user
    except TelegramUser.DoesNotExist:
        return None
