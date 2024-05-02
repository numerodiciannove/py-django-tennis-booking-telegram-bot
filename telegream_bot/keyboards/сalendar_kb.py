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

calendar_day_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗓Понеділок"),
            KeyboardButton(text="🗓Вівторок"),
            KeyboardButton(text="🗓Середа"),
        ],
        [
            KeyboardButton(text="🗓Четвер"),
            KeyboardButton(text="🗓П’ятниця"),
            KeyboardButton(text="🗓Субота")
        ],
        [
            KeyboardButton(text="🗓Неділя"),
        ],
        [
            KeyboardButton(text="✍️ Cтворити бронь")
        ],
        [
            KeyboardButton(text="🔙 Повернутись до меню")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)

add_day_calendar_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Понеділок"),
            KeyboardButton(text="Вівторок"),
            KeyboardButton(text="Середа"),
        ],
        [
            KeyboardButton(text="Четвер"),
            KeyboardButton(text="П’ятниця"),
            KeyboardButton(text="Субота")
        ],
        [
            KeyboardButton(text="Неділя"),
        ],
        [
            KeyboardButton(text="✍️ Cтворити бронь")
        ],
        [
            KeyboardButton(text="🔙 Повернутись до меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)


is_repetitive_calendar_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Одноразова")
        ],
        [
            KeyboardButton(text="Постійна")
        ],
        [
            KeyboardButton(text="🔙 Повернутись до меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)

events_calendar_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎾"),
            KeyboardButton(text="🎾👨‍👧‍👧"),
        ],
        [
            KeyboardButton(text="🎾👯"),
            KeyboardButton(text="🎾🏆")
        ],
        [
            KeyboardButton(text="🏐"),
            KeyboardButton(text="🏀")
        ],
        [
            KeyboardButton(text="🔙 Повернутись до меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Натисни на кнопку нижче. 💫"
)
