from string import punctuation

from aiogram import F, types, Router

user_group_router = Router()

restricted_words = {'racoon','orange','banan'}

def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.__contains__(message.text.lower().split()):
        await message.delete()