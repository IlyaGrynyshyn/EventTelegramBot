from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

help = InlineKeyboardMarkup(row_width=1,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardButton(
                                                 text='HELP',
                                                 callback_data="help",
                                                 url='https://t.me/kris_nd'
                                             ),
                                         ]
                                     ])
