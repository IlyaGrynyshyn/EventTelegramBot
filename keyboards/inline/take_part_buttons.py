from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import type_of_visit_callback

type_of_visit = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(
                                                 text='👋 Я прийду',
                                                 callback_data="will_come"
                                             ),
                                             InlineKeyboardButton(
                                                 text='👩‍💻 Я буду онлайн',
                                                 callback_data='will_online'
                                             )
                                         ]
                                     ])
