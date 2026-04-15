from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter



user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi, I'm virtual helper!")

@user_private_router.message(or_f(Command('menu'), (F.text.lower() == "menu")))
async def menu_cmd(message: types.Message):
    await message.answer("Here is menu: ")

@user_private_router.message((F.text.lower() == "about us"))
@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.answer("About us: ")

@user_private_router.message((F.text.lower() == 'payment'))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer("Here is payment options: ")

@user_private_router.message((F.text.lower().contains('shippi')) | (F.text.lower() == 'shipping options'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    await message.answer("Here is shipping options: ")
