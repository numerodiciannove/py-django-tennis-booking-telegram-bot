from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Зареєструватись")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)
