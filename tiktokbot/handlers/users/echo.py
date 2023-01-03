from aiogram import types
from time import sleep
from loader import bot, dp
from aiogram.dispatcher.filters import Text
from youtube import yt
# Echo bot

@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Downloading started...")





@dp.message_handler(Text(startswith='https://www.youtube.com/'))
async def test(message: types.Message):
    natija1 = yt(message.text)
    await message.answer_audio(natija1['video'])



