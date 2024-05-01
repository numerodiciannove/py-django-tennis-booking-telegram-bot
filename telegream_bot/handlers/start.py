from aiogram import Bot
from aiogram.types import Message
from telegream_bot.keyboards.profile_kb import profile_kb
from telegream_bot.keyboards.register_kb import register_keyboard
from telegream_bot.utils.db_utils import get_user_by_telegram_id


async def get_start(message: Message, bot: Bot):
    user = await get_user_by_telegram_id(message.from_user.id)

    if not user:
        hello_text = (
            f"Привіт!,👋 {message.from_user.full_name}!\n"
            f"Мене звати 'PO 🎾 TENNIS BOT'.\n\n"
            f"Я бот який допомогає робити бронювання "
            f"тенісного корту за датою та часом. У майбутньому я зможу допомогати "
            f"тобі у пошуку напарників по сусідству. \n\n"
            f"Для бронювання (якщо ти ще не зареєстрований) з початку треба пройти швидку реєстрацію. \n\n"
            f"Для продовження натисни 'Зареєструватись' 💫"
        )
        await bot.send_message(
            message.from_user.id, hello_text, reply_markup=register_keyboard
        )
    else:
        await bot.send_message(
            message.from_user.id,
            f"Привіт, {user.first_name}👋!",
            reply_markup=profile_kb
        )
