from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ustoz_shogird = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="Sherik kerak"),
            KeyboardButton(text="Ish joyi kerak")
        ],
        [
            KeyboardButton(text="Hodim kerak"),
            KeyboardButton(text="Ustoz kerak")
        ],
        [
            KeyboardButton(text="Shogird kerak")
        ]
    ],
    resize_keyboard=True
)

finish = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ]
    ],
    resize_keyboard=True
)