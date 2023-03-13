from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, LabeledPrice
from data import config
from keyboards.default import menu
from keyboards.inline import type_of_visit
from loader import dp, db, bot
from data.items import item1
from states.will_online_state import Will_Online


@dp.message_handler(text='🤝 Взяти участь')
async def take_part(message: types.Message):
    await message.answer('🤔 Як ти плануєш відвідати захід?', reply_markup=type_of_visit)


@dp.callback_query_handler(lambda c: c.data == 'will_come')
async def will_come(call: CallbackQuery):
    db.update_type_visit('offline', call.from_user.id)
    await call.message.answer(
        f'''
        Бути офлайн - це твій найкращий внесок у свій розвиток, потрапити в інфополе таких же яскравих дівчат, отримати безцінний досвід і нарешті ближче познайомитись з розвитком в соц мережах. 

Твій вхідний квиток коштуватиме 777 гривень🪄

💳 Оплатити ти можеш натиснувши нижче на кнопку оплати
        ''', reply_markup=menu
    )
    await call.answer(cache_time=30)
    await bot.send_invoice(call.from_user.id,
                           **item1.generate_invoice(), payload='123')


@dp.callback_query_handler(lambda c: c.data == 'will_online')
async def will_online(call: CallbackQuery):
    await call.answer(cache_time=30)
    db.update_type_visit('online', call.from_user.id)
    await call.message.answer(
       f"""
       Ми раді твоїй участі, навіть якщо не зможемо побачити та обійняти тебе, але будемо знати, шо ти присутня на заході ОНЛАЙН🔥

Ми пам’ятаємо, що всі наші можливості стаються завдяки ЗСУ, саме тому ціну за такий онлайн формат обираєте ви.
Після заходу ми передамо донати на ЗСУ та відзвітуємо❣️

Напиши мені суму внеску ✨
       """, reply_markup=types.ReplyKeyboardRemove())
    await Will_Online.Q1.set()


@dp.message_handler(state=Will_Online.Q1)
async def get_amount(message: types.Message, state: FSMContext):
    try:
        amount = int(message.text)
        formating = int(str(amount) + "00")
        if amount < 49:
            await message.answer('Мінімальна сума 50 грн')
        else:
            await state.update_data(amount=amount)
            await bot.send_invoice(message.from_user.id,
                                   title='Квиток онлайн "The Power of Identity"',
                                   currency="UAH",
                                   description='Вхідний квиток на онлайн доступ заходу "The Power of Identity"',
                                   prices=[
                                       LabeledPrice(
                                           label='Вхідний квиток',
                                           amount=formating
                                       )
                                   ], start_parameter='create_invoice_will_come',
                                   need_phone_number=True,
                                   provider_token=config.PROVIDER_TOKEN,
                                   payload='11223')
            await state.finish()
    except ValueError:
        await message.answer('Ви ввели некоректну суму. ')


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)
    db.update_is_pay(query.from_user.id)
    message_text = """
    Оплата пройшла успішно❤️‍🔥

🤗 Ми раді, що ти приєднаєшся до нашого заходу.

Тепер твій квиток 🎟️ буде доступний у розділі *Мій квиток*

🪄Приєднуйся до нашого телеграм каналу та слідкуй за усіма новинами: https://t.me/+LP5wYwzkN9xmYzM6
    """
    await bot.send_message(chat_id=query.from_user.id, text=message_text, reply_markup=menu)
