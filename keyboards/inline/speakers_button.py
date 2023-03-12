from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import type_of_visit_callback

speakers = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(
                                            text='Дана',
                                            callback_data="Dana"
                                        ),
                                        InlineKeyboardButton(
                                            text='Ліза',
                                            callback_data='Liza'
                                        )
                                    ]
                                ])
