from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton

change_user_data_profile_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Змінити ім'я")],
        [KeyboardButton(text="Змінити номер телефону")],
        [KeyboardButton(text="🔙 Повернутись до меню")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)
