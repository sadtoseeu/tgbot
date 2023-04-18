import vk_api
from vk_api import audio
import requests
from time import time
import os


from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


REQUEST_STATUS_CODE = 200
name_dir = 'audio'
path = name_dir 
login = '89991236084'  # Номер телефона
password = 'Stilov1488'  # Пароль
my_id = '____'  # Ваш id vk



@dp.message_handler(Command('vk'))
async def start_dow(message: types.Message):
    await message.answer(text=f"Название.")
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
    
    


vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()  # Теперь можно обращаться к методам API как к обычным 
                                        # классам
vk_audio = audio.VkAudio(vk_session)  # Получаем доступ к audio

#https://github.com/imartemy1524/vk_audio