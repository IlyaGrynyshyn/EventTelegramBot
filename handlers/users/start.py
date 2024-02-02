from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu
from loader import dp, db
from utils.misc import rate_limit


@dp.message_handler(CommandStart())
@rate_limit(4)
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    message_text = """
    Привіт, прекрасна💌
Я твій провідник на захід *The Power of Identity*. 
    """
    if await db.exist_user(telegram_id=message.from_user.id):
        await message.answer(message_text, reply_markup=menu)
    else:
        message_text = """
        Привіт, прекрасна💌
Я твій провідник на захід 
*The Power of Identity*, що пройде 29го квітня, у м. Ужгород 🫧
Щоб зареєструватись, залиш будь ласка свої дані 👇🏻
        """
        await db.add_user(name=message.from_user.full_name, telegram_id=message.from_user.id)
        await message.answer(message_text)
        await message.answer(text='📱 Напиши мені свій номер телефону.')
        await message.answer(text='⬇️⁣')
        await state.set_state('registration_phone')
