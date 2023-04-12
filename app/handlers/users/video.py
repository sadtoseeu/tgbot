from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
from states import Dowload

from pytube import YouTube

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

import os
import uuid
import shutil


def dowload_video(url, type='audio'):
    yt = YouTube(url)
    audio_id = uuid.uuid4().fields[-1]
    if type == 'audio':
        yt.streams.filter(only_audio=True).first().download("audio", f"{audio_id}.mp3")
        return f"{audio_id}.mp3"
    elif type == 'video':
        return f"{audio_id}.mp4"


@dp.message_handler(Command('audio'))
async def start_dow(message: types.Message):
    await message.answer(text=f"Пришлите ссылку на видео.")
    await Dowload.dowload.set()

@dp.message_handler(state=Dowload.dowload)
async def dowload(message: types.Message, state: FSMContext):

    title = dowload_video(message.text)
    audio = open(f'audio/{title}', 'rb')
    
    shutil.copyfile(f'audio/{title}', f'audio/1.mp3')
    audio = open(f'audio/1.mp3', 'rb')

    try:
        await bot.send_audio(message.chat.id, audio)
    except:
        await message.answer()

    for item in os.listdir("audio/"):
        if item.endswith(".mp3"):
            os.remove(os.path.join("audio/", item))

    await state.finish()