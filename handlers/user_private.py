from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_marked_section, Bold, as_list

from filters.chat_types import ChatTypeFilter

from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi, I'm virtual helper!",
                         reply_markup=reply.start_kb3.as_markup(
                            resize_keyboard=True,
                            input_field_placeholder = 'What are you interested in?'))

@user_private_router.message(or_f(Command('menu'), (F.text.lower() == "menu")))
async def menu_cmd(message: types.Message):
    await message.answer("Here is menu: ")

@user_private_router.message((F.text.lower() == "about shop"))
@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("About us: ")

@user_private_router.message(or_f(Command('payment'), (F.text.lower().contains('payment'))))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):

    text = as_marked_section(
            Bold("Payment options:"),
            "By card in bot",
            "Cash",
            "In shop",
            marker="✅"
        )
    await message.answer(text.as_html())

@user_private_router.message((F.text.lower().contains('shippi')) | (F.text.lower() == 'shipping options'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):

    text = as_list(
        as_marked_section(
            Bold("Shipping options/order:"),
            "Courier",
            "I'll run over and pick it up now",
            "I'll eat at your place ",
            marker="✅ "
        ),
        as_marked_section(
            Bold("Forbidden:"),
            "Email",
            "Pigeons",
            marker="❌ "
        ),
        sep='\n---------------------\n'

    )
    await message.answer(text.as_html())

@user_private_router.message(F.contact)
async def get_contact_cmd(message: types.Message):
    await message.answer("Here is contact info: ")
    await message.answer(str(message.contact))

@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer("Here is location info: ")
    await message.answer(str(message.location))
