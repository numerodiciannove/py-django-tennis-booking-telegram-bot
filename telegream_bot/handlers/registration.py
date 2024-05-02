import logging

from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from telegream_bot.keyboards.profile_kb import profile_kb
from telegream_bot.state.register import RegisterState
from asgiref.sync import sync_to_async
from telegream_bot.utils.db_utils import get_user_by_telegram_id
from user.models import TelegramUser

logger = logging.getLogger(__name__)


async def start_register(message: Message, state: FSMContext, bot: Bot):
    user = await get_user_by_telegram_id(message.from_user.id)
    if user:
        await bot.send_message(
            message.from_user.id,
            f"Ааа все! 🤓 \n\n{user.first_name} - @{user.telegram_username} вже зареєстрован!",
            reply_markup=profile_kb
        )
    else:
        await bot.send_message(message.from_user.id, "Давай почнемо💫")
        await bot.send_message(message.from_user.id, "Як тебе звати?")
        await state.set_state(RegisterState.first_name)


async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"Рад знайомству😌, {message.text}!"
    )
    await bot.send_message(
        message.from_user.id,
        f"Зараз треба вказати свій номер телефону. щоб бути на зв'язку. \n\n"
        f"📞Вкажіть свій номер у форматі: 0951112233\n"
    )
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.phone_number)


async def register_phone(message: Message, state: FSMContext, bot: Bot):
    if len(message.text) == 10:
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get("regname")
        reg_phone = reg_data.get("regphone")
        msg = f"Все добре!👌\n\n Ти вказав: \n {reg_name} - {reg_phone}"
        await bot.send_message(
            message.from_user.id, msg, reply_markup=profile_kb
        )

        await create_user(
            first_name=reg_name,
            phone_number=reg_phone,
            telegram_id=message.from_user.id,
            telegram_username=f"@{message.from_user.username}"
        )
        await state.clear()
    else:
        await bot.send_message(
            message.from_user.id,
            "Вказан не вірний номер телефону."
        )


@sync_to_async
def create_user(first_name, phone_number, telegram_id, telegram_username):
    TelegramUser.objects.create(
        first_name=first_name,
        phone_number=phone_number,
        telegram_id=telegram_id,
        telegram_username=telegram_username
    )
