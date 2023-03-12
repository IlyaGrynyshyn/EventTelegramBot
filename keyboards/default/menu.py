from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤝 Взяти участь"),
            KeyboardButton(text='📍 Локація')
        ],
        [
            KeyboardButton(text='🧑 Спікери'),
            KeyboardButton(text='🎫 Мій квиток')
        ],
        [
            KeyboardButton(text='❓ Допомога'),
            KeyboardButton(text='📦 Про івент')
        ]
    ], resize_keyboard=True
)
