from keyboards.default import menu
from loader import dp, db, bot
from aiogram import types


@dp.message_handler(text='ℹ Інформація')
async def enter_phone(message: types.Message):
<<<<<<< HEAD
    document = open('dohovir_publichnoi_oferty.pdf', 'rb')
=======
    document = open('Договір публічної оферти.pdf', 'rb')
>>>>>>> 5ed3f464b3bc0625d44757cd36d0e3c948b72ff9
    await bot.send_document(chat_id=message.from_user.id, document=document)
    document.close()
