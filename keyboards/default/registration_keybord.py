from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registration_keybord = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Share contact', request_contact=True)]
    ],
    resize_keyboard=True
)
