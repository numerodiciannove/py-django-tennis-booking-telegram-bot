from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from telegream_bot.keyboards.create_kb import usr_time_slots_for_delete_kb
from telegream_bot.utils.db_utils import get_user_bookings


async def start_bookings_for_delete(
        message: Message,
        bot: Bot,
):
    await bot.send_message(
        message.from_user.id,
        f"Обери що відминити:",
        reply_markup=await usr_time_slots_for_delete_kb(message.from_user.id)
    )
