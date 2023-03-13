from aiogram import types
from keyboards.default import menu
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(text='📦 Про івент')
async def bot_help(message: types.Message):
    text = """
    *The Power of Identity* - захід created by ALENA MAER, з метою занурити вас у світ ….
.
.
.
.
.

Agenda заходу буде такою:

-  Networking space  
- Панельна Дискусія з ученицями попередніх потоків Наставництва 
- Alena’s speech 
- Music/Photo/Beauty time 


✨З нетерпінням чекаємо зустріти саме тебе 29го квітня о 13:00 в KameLotHub✨
    """

    await message.answer(text, reply_markup=menu)
