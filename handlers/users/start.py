from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import registration_keybord, menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    message_text = """Привіт, друже! Чим я можу тобі допомогти?
    """
    if db.exist_user(telegram_id=message.from_user.id):
        await message.answer(message_text, reply_markup=menu)
    else:
        message_text = """Привіт, друже! Я твій провідник на івент SMM.
        Щоб зареєструватись, залиш будь ласка свої дані 👇🏻 
        """
        db.add_user(name=message.from_user.full_name, telegram_id=message.from_user.id)
        await message.answer(message_text)
        await message.answer(text='📱 Номер телефону', reply_markup=registration_keybord)
        await message.answer(text='⬇️⁣')
        await state.set_state('registration_phone')
        # await state.finish()
