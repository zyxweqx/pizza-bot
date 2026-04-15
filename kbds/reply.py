from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu"),
            KeyboardButton(text="About us"),
        ],
        [
            KeyboardButton(text="Shipping options"),
            KeyboardButton(text="Payment options"),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='What are you interesting in?'
)
del_kbd = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()

start_kb2.add(
KeyboardButton(text="Menu"),
    KeyboardButton(text="About shop"),
    KeyboardButton(text="Shipping options"),
    KeyboardButton(text="Payment options"),
)
start_kb2.adjust(2,2)

start_kb3 = ReplyKeyboardBuilder()

start_kb3.attach(start_kb2)
start_kb3.row(
    KeyboardButton(text="Review"),
)

test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Make a survey", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Send a mobile phone ☎️", request_contact=True),
            KeyboardButton(text="Send a location 🗺", request_location=True),
        ],
    ],
    resize_keyboard=True,
)


