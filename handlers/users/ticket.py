from aiogram import types
from keyboards.default import menu
from loader import dp, db
from utils.misc import rate_limit



@dp.message_handler(text='🎫 Мій квиток')
@rate_limit(4)
async def take_part(message: types.Message):
    global number, name, phone, visit, is_pay, message_text
    ticket = await db.select_ticket(message.from_user.id)
    if ticket:
        number = ticket[0]
        name = ticket[2]
        phone = ticket[3]
        email = ticket[4]
        type_visit = ticket[5]
        is_pay = ticket[6]
        if type_visit == 'offline':
            visit = 'Офлайн'
        else:
            visit = 'Онлайн'
        if is_pay == 1:
            pay = 'Так'
        else:
            pay = 'Ні'
        message_text = f"""Квиток #{number}\n\n📌 Ім'я учасника: {name}\n\n📞 Номер телефону: {phone}\n\n🧠 Формат участі: {visit}\n\n💸 Оплата: {pay}\n\n❤️‍🔥 Приєднатись до закритого коммьюніті можна вже тут: https://t.me/+LP5wYwzkN9xmYzM6 """
    else:
        message_text = '❗️ У вас поки що немає квитка, щоб купити його натисність на кнопку "Взяти участь"'
    await message.answer(text=message_text, reply_markup=menu)

