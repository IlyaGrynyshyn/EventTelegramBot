from aiogram import types
from keyboards.default import menu
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(text='📦 Про івент')
async def bot_help(message: types.Message):
    text = "Про івент"

    await message.answer(text, reply_markup=menu)
