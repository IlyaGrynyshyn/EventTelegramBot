from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from keyboards.default import menu
from loader import dp, db
from aiogram import types


# @dp.message_handler(state='registration_phone')
# async def get_phone(message: types.Message, state: FSMContext):
#     await message.answer('Пришли мені свій номер телефону')
#     await state.set_state('registration_phone')


# @dp.message_handler(state='registration_phone')
# async def enter_phone(message: types.Message, state: FSMContext):
#     phone = message.text
#     await message.answer('✉️ Пришли мені свою пошту')
#     await state.set_state('registration_email')


@dp.message_handler(content_types=['contact'], state='registration_phone')
async def contact(message, state: FSMContext):
    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        await message.answer('✉️ Пришли мені свою пошту', reply_markup=keyboard2)
        phonenumber = str(message.contact.phone_number)
        db.update_phone(phone=phonenumber, telegram_id=message.from_user.id)
        await state.set_state('registration_email')


@dp.message_handler(state='registration_email')
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    db.update_email(email=email, telegram_id=message.from_user.id)
    message_text = """
    Дякуємо 🤍
Ти вже зробив перший крок до змін, ми так пишаємось тобою!

Якщо хочеш отримати додаткові матеріали, ексклюзивну інформацію від Насті, долучайся до каналу інтенсиву:

https://t.me/+fVYobL82-5I1Mjky

В день інтенсиву за 5 хвилин до початку ми дамо тобі посилання на інтенсив, тому будь ласка, не полишай цей бот 🙌🏻

Запис інтенсиву буде, але радимо доєднатись онлайн, щоб мати змогу поставити Насті свої запитання та отримати можливість першим доєднатись до великого курсу за найнижчою ціною 💪🏻🔥
    """
    await message.answer(text=message_text, reply_markup=menu)
    await state.finish()
