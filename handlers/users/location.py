from keyboards.default import menu
from loader import dp, db
from aiogram import types

from utils.misc import rate_limit

@rate_limit(4)
@dp.message_handler(text='📍 Локація')
async def enter_phone(message: types.Message):
    message_text = '🚩 "The Power of Identity" пройде в місті Ужгород, на вулиці вул. Крилова 10, 2-й поверх в KameLotHub Space'

    await message.answer(text=message_text, reply_markup=menu)
