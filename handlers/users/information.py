from keyboards.default import menu
from loader import dp, db, bot
from aiogram import types


@dp.message_handler(text='ℹ Інформація')
async def enter_phone(message: types.Message):
    document = open('Договір публічної оферти.pdf', 'rb')
    await bot.send_document(chat_id=message.from_user.id, document=document)
    document.close()
