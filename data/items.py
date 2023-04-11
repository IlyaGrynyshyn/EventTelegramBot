from utils.misc.item import Item
from aiogram.types import LabeledPrice

item1 = Item(
    title="Вхідний квиток на конференцію",
    currency="UAH",
    description='Вхідний квиток на відвідування конференції "The Power of Identity"',
    prices=[
        LabeledPrice(
            label='Вхідний квиток',
            amount=1100_00
        )
    ], start_parameter='create_invoice_will_come',
    need_phone_number=True,

)
# item2 = Item(
#     title="Вхідний квиток на --- ",
#     currency="UAH",
#     description='Вхідний квиток на ----',
#     prices=[
#         LabeledPrice(
#             label='Вхідний квиток',
#             amount=700_00
#         )
#     ], start_parameter='create_invoice_will_come',
#     need_phone_number=True,
#
# )
