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
        ],
        [
            KeyboardButton(text='ℹ Інформація')
        ]
    ], resize_keyboard=True
)
