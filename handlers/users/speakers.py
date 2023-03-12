from aiogram import types
from aiogram.types import CallbackQuery, InputFile
from keyboards.inline import speakers

from loader import dp, bot


@dp.message_handler(text='🧑 Спікери')
async def bot_help(message: types.Message):
    text = "Детальніше про спікерів:"
    await message.answer(text, reply_markup=speakers)


@dp.callback_query_handler(lambda c: c.data == 'Dana')
async def speaker_info(call: CallbackQuery):
    text = """Привіт, мене звати Дана, ось моя історія.\n
    Після курсу почала співпрацю з проєктами в США, Європі та Україні. Під час курсу мала проєкти в Празі. \n
    Змогла розкрити себе зовсім з іншого боку, прийняти свої сильні сторони та забула про значення слова «тривожність». \n
    Нарешті почала працювати в кайф, та заробляти в легкості. Зрозуміла, що можна бути «не зручною», можна дозволяти собі все, що захочеться, та просто жити життям своєї мрії.
    """

    photo = InputFile(path_or_bytesio='data/images/IMG_6998.JPG', filename='Dana')
    await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=text)
    await call.answer(cache_time=30)
    # await call.message.answer(text)


@dp.callback_query_handler(lambda c: c.data == 'Liza')
async def speaker_info(call: CallbackQuery):
    text = """Привіт, мене звати Ліза, ось моя історія.\n
    Після курсу почала співпрацю з проєктами в США, Європі та Україні. Під час курсу мала проєкти в Празі. \n
    Змогла розкрити себе зовсім з іншого боку, прийняти свої сильні сторони та забула про значення слова «тривожність». \n
    Нарешті почала працювати в кайф, та заробляти в легкості. Зрозуміла, що можна бути «не зручною», можна дозволяти собі все, що захочеться, та просто жити життям своєї мрії.
    """

    photo = InputFile(path_or_bytesio='data/images/photo_2023-03-12_22-33-27.jpg', filename='Liza')
    await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=text)
    await call.answer(cache_time=30)
    # await call.message.answer(text)
