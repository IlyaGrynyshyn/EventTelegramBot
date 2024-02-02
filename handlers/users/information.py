from keyboards.default import menu
from loader import dp, db, bot
from aiogram import types

from utils.misc import rate_limit

@rate_limit(4)
@dp.message_handler(text='ℹ Інформація')
async def enter_phone(message: types.Message):
    document = open('dohovir_publichnoi_oferty.pdf', 'rb')
    await bot.send_document(chat_id=message.from_user.id, document=document)
    document.close()
