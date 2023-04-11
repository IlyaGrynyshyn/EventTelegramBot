from aiogram import types
from keyboards.default import menu
from loader import dp, db,bot


@dp.message_handler(text='gigi')
async def all_users(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Ім'я - Номер телефону - Відвідує - Сплачено")
    users = db.select_all_payed_user()
    for i in users:
        is_pay = i[6]
        type_visit = i[5]
        if type_visit == 'offline':
            visit = 'Офлайн'
        else:
            visit = 'Онлайн'
        if is_pay == 1:
            pay = 'Так'
        else:
            pay = 'Ні'
        message_text = f"{i[2]} - {i[3]} - {visit} - {pay}"
        await message.answer(text=message_text, reply_markup=menu)
