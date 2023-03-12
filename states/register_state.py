from aiogram.dispatcher.filters.state import StatesGroup, State


class Registration(StatesGroup):
    PHONE = State()
    EMAIL = State()
