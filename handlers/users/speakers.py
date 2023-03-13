from aiogram import types
from aiogram.types import CallbackQuery, InputFile
from keyboards.inline import speakers

from loader import dp, bot


@dp.message_handler(text='🧑 Спікери')
async def bot_help(message: types.Message):
    text = """
    Головний спікер та creator - 
ALENA MAER, яка і буде вести вас протягом усього заходу і ділитись найважливішими кроками в онлайн. 

А також протягом "Панельної Дискусії" ви познайомитесь із ученицями курсу SMM&PSYCHOLOGY. Якщо ти хочеш дізнатись більше про них - тицяй кнопки нижче🔥
    """
    await message.answer(text, reply_markup=speakers)


@dp.callback_query_handler(lambda c: c.data == 'Dana')
async def speaker_info(call: CallbackQuery):
    text = """
    Привіт👋 мене звати Дана і ось моя історія:

🔥Після курсу почала співпрацю з проєктами в США, Європі та Україні. Вже під час курсу мала проєкти в Празі. 

🪄Змогла розкрити себе зовсім з іншого боку, прийняти свої сильні сторони та забула про значення слова «тривожність». 

Нарешті почала працювати в кайф, та заробляти в легкості.🫧 Зрозуміла, що можна бути «не зручною», та можна дозволяти собі все, що захочеться, та просто жити життям своєї мрії.
    """

    photo = InputFile(path_or_bytesio='data/images/photo_2023-03-13_13-52-43.jpg', filename='Dana')
    await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=text)
    await call.answer(cache_time=30)
    # await call.message.answer(text)


@dp.callback_query_handler(lambda c: c.data == 'Liza')
async def speaker_info(call: CallbackQuery):
    text = """
    А ось власне історія Лізи 🪄

Я давно не наважувалась потрапити у сферу СММ, але тільки рік тому зробила перший крок для цього. 
Наставництво від Альони саме і стало тією рушійною силою мого стрімкого розвитку💥

Наразі я веду проєкт закордоном, та маю проєкти в Україні. Я вірю, та знаю що є можливості для росту, але я вже надзвичайно пишаюсь цими досягненнями❤️‍🔥. 

До Наставництва була надзвичайно закомплексована, але зараз відчуваю себе більш впевнено та сильною ✨
    """

    photo = InputFile(path_or_bytesio='data/images/photo_2023-03-13_13-55-34.jpg', filename='Liza')
    await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=text)
    await call.answer(cache_time=30)
    # await call.message.answer(text)
