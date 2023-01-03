import os
from aiogram import types
from time import sleep
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from tiktok import tk
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
from pytube import YouTube
from loader import *
from youtube import yt
from instagram import it
from facebook import fb

@dp.message_handler(Text(startswith='https://vt.tiktok.com/'))
async def test(message: types.Message):
    natija = tk(message.text)
    if await message.answer("Downloading started..."):
        sleep(3)
        await message.answer_audio(natija['video'])

@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def test(message: types.Message):
    natija = tk(message.text)
    if await message.answer("Downloading started..."):
        sleep(3)
        await message.answer_audio(natija['video'])

@dp.message_handler(Text(startswith='https://vm.tiktok.com/'))
async def test(message: types.Message):
    natija = tk(message.text)
    if await message.answer("Downloading started..."):
        sleep(3)
        await message.answer_audio(natija['video'])

@dp.message_handler(Text(startswith='https://www.youtube.com/'))
async def test(message: types.Message):
    link = message.text
    from io import BytesIO
    buffer = BytesIO()
    url = YouTube(link)
    audio = url.streams.get_audio_only()
    audio.stream_to_buffer(buffer=buffer)
    buffer.seek(0)
    filename = url.title
    natija1 = yt(message.text)
    if await message.answer("Downloading started..."):
        sleep(3)
        await message.answer_audio(natija1['video'])
        await message.answer("Wait, audio file is also downloading")
        await message.answer_audio(audio=buffer, caption=filename,)

@dp.message_handler(Text(startswith='https://youtu.be/'))
async def test(message: types.Message):
    link = message.text
    from io import BytesIO
    buffer = BytesIO()
    url = YouTube(link)
    audio = url.streams.get_audio_only()
    audio.stream_to_buffer(buffer=buffer)
    buffer.seek(0)
    filename = url.title
    natija1 = yt(message.text)
    if await message.answer("Downloading started..."):
        sleep(3)
        await message.answer_audio(natija1['video'])
        await message.answer("Wait, audio file is also downloading")
        await message.answer_audio(audio=buffer, caption=filename,)

@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def test(message: types.Message):
    natija2 = it(message.text)
    if await message.answer("Downloading started..."):
        sleep(3)
        await message.answer_audio(natija2['smth'])

@dp.message_handler(Text(startswith='https://www.facebook.com/'))
async def test(message: types.Message):
    natija3 = fb(message.text)
    if await message.answer("Downloading started..."):
        sleep(3)
        await message.answer_audio(natija3['videofb'])



@dp.callback_query_handler(Text(startswith='🎼'))
async def test2(call: CallbackQuery):
    await call.answer(cache_time=60)
    data = call.data[1:]
    await call.message.answer_audio(data)







