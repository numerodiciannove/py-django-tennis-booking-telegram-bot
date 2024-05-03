from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from telegream_bot.keyboards.chane_profile import change_user_data_profile_kb


async def change_profile(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, "Давай змінемо💫")

    await bot.send_message(
        message.from_user.id,
        f"Обери далі...",
        reply_markup=change_user_data_profile_kb,
    )
