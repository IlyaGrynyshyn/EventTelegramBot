from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import menu
from loader import dp, db


@dp.me@dp.message_handler(text='🎫 Мій квиток')
async def take_part(message: types.Message):
    global number, name, phone, visit, is_pay, message_text
    ticket = db.select_ticket(message.from_user.id)
    print(ticket)
    if ticket:
        number = ticket[0]
        name = ticket[2]
        phone = ticket[3]
        email = ticket[4]
        type_visit = ticket[5]
        is_pay = ticket[6]
        if type_visit == 'offline':
            visit = '�лайн'
        else:
            visit = 'Онлайн'
        if is_pay == 1:
            pay = 'Так'
        else:
            pay = 'Ні'
        message_text = f"""Квиток #{number}\n📌 Ім'я учасника: {name}\n📞 Номер телефону: {phone}\n🧠 Формат участі: {visit}\n💸 Оплата: {pay}\n❤️‍🔥 Приєднатись до закритого коммьюніті можна вже тут: https://t.me/+LP5wYwzkN9xmYzM6
        """
    else:
        message_text = '❗️ У вас поки що немає квитка, щоб купити його натисність на кнопку "Взяти участь"'
    await message.answer(text=message_text, reply_markup=menu)

