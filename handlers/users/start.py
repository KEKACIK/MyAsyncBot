from aiogram.dispatcher.filters import Command
from aiogram import types

from loader import dp


@dp.message_handler(Command('start'))
async def start(message: types.Message):
    print(message.chat.id)
    await message.answer("Loh")

