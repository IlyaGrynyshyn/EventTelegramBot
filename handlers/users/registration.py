from aiogram.dispatcher import FSMContext
from keyboards.default import menu
from keyboards.inline import type_of_visit
from loader import dp, db
from aiogram import types
import re


@dp.message_handler(state='registration_phone')
async def contact(message, state: FSMContext):
    if re.match(r'^\+380\d{9}$', str(message.text)):
        await message.answer('✉️ Надішли мені свою пошту')
        # phonenumber = str(message.contact.phone_number)
        await db.update_phone(phone=str(message.text), telegram_id=message.from_user.id)
        await state.set_state('registration_email')
    else:
        await message.answer('❗️Будь ласка, введіть свій номер телефону у форматі +380XXXXXXXXX')


@dp.message_handler(state='registration_email')
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        await db.update_email(email=email, telegram_id=message.from_user.id)
        message_text = """
        Дякуємо, що залишила свої дані.
    А тепер обери варіант як ти плануєш відвідати наш захід🪄?
        """
        await message.answer(text=message_text, reply_markup=menu)
        await message.answer('🤔 Як ти плануєш відвідати захід?', reply_markup=type_of_visit)
        await state.finish()
    else:
        await message.answer('❗️Будь ласка, введіть свій email в форматі example@ex.com')

