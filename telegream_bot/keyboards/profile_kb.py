from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profile_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="😎Профіль")],
        [KeyboardButton(text="🎾Календар")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)
