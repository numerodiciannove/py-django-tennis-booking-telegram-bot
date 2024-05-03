from aiogram import Bot
from aiogram.types import Message
from telegream_bot.keyboards.profile_kb import profile_kb


async def get_help(message: Message, bot: Bot):
        help_text = (
            f"Привіт!,👋 {message.from_user.full_name}!\n"
            f"Мене звати 'PO 🎾 TENNIS BOT'.\n\n"
            f"Я бот який допомогає робити бронювання "
            f"спорт локації в 'ЖК Паркові Озера' міста Київ. \n\n"
            f"В мене є декілька особливостей з позначками:\n\n"
            f"🎾💪: Персональне тренування\n"
            f"🎾👶👧🏻🧒🏾: Тенісна група для дітей\n"
            f"🎾🧍‍♂️🧍‍♀️🧍: Тенісна група для дорослих\n"
            f"🎾🏆: Тенісний турнір\n"
            f"🏐: Волейбол\n"
            f"🏀: Баскетбол\n\n"
            f"Основний чат бота: @Nikitarista\n"
            f"Monobank: 5375 4115 0688 6717\n\n"
            f"Якшо є бажання залишити донат розробнику @numerodiciannove для покращеня бота:\n"
            f"Monobank: 4441 1144 5035 4715\n\n"
            f"Також всі технічні питання до @numerodiciannove (якщо шахраї i когось треба забанити)."

        )
        await bot.send_message(
            message.from_user.id, help_text, reply_markup=profile_kb
        )
