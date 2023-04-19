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

#https://github.com/imartemy1524/vk_audio