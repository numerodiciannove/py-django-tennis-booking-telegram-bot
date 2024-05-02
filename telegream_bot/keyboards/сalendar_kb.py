from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

calendar_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔎 Переглянути розклад на тиждень"),
            KeyboardButton(text="🔎 Переглянути розклад по дням")
        ],
        [
            KeyboardButton(text="✍️ Cтворити бронь")
        ],
        [
            KeyboardButton(text="📝 Мої бронювання"),
            KeyboardButton(text="❌ Відминити бронь")
        ],
        [
            KeyboardButton(text="🔙 Повернутись до меню")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)
