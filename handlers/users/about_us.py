from aiogram import types
from keyboards.default import menu
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(4)
@dp.message_handler(text='📦 Про івент')
async def bot_help(message: types.Message):
    text = """
    *The Power of Identity* - захід створений by ALENA MAER, з метою занурити вас у світ проявленості, масштабності, сучасного, нестардартного SMM, та яскравого блогінгу. 
Ми прагнемо поділитись про можливості які дають соц мережі, та як за допомогою контенту проявляти себе різною. 

Вже 29го квітня ми поговоримо про:

✅ SMM нового покоління

✅ як онлайн допомагає змінитись внутрішньо, вирости 

✅ як рости в роботі онлайн, та до якого етапу ти можеш дійти 

Протягом заходу у вас буде можливість познайомитись із однодумцями на Networking space, та стати свідком Панельної Дискусії з ученицями попередніх потоків Наставництва SMM&PSYCHOLOGY, протягом якої випускниці поділяться своїм досвідом роботи в он-лайні та яких результатів вони вже досягли. 

Звучить вогонь, правда?❤️‍🔥

✨саме тому нетерпінням чекаємо побачити саме тебе на нашому заході 29го квітня о 13:00 в KameLotHub✨
    """

    await message.answer(text, reply_markup=menu)
