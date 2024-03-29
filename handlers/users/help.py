from aiogram import types
from keyboards.inline import help
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(4)
@dp.message_handler(text='❓ Допомога')
async def bot_help(message: types.Message):
    text = "Якшо у вас виникли питання щодо покупки квитка, пишіть нам в телеграм"
    await message.answer(text, reply_markup=help)
