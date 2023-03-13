from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from keyboards.default import menu
from keyboards.inline import type_of_visit
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
        await message.answer('✉️ Надішли мені свою пошту', reply_markup=keyboard2)
        phonenumber = str(message.contact.phone_number)
        db.update_phone(phone=phonenumber, telegram_id=message.from_user.id)
        await state.set_state('registration_email')


@dp.message_handler(state='registration_email')
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    db.update_email(email=email, telegram_id=message.from_user.id)
    message_text = """
    Дякуємо, що залишила свої дані.
А тепер обери варіант як ти плануєш відвідати наш захід🪄?
    """
    await message.answer(text=message_text, reply_markup=menu)
    await message.answer('🤔 Як ти плануєш відвідати захід?', reply_markup=type_of_visit)
    await state.finish()
