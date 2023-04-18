import vk_api
from vk_api import audio
import requests
from time import time
import os

REQUEST_STATUS_CODE = 200
name_dir = 'audio'
path = name_dir 
login = '89991236084'  # Номер телефона
password = 'Stilov1488'  # Пароль
my_id = '____'  # Ваш id vk

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()  # Теперь можно обращаться к методам API как к обычным 
                                        # классам
vk_audio = audio.VkAudio(vk_session)  # Получаем доступ к audio

#https://github.com/imartemy1524/vk_audio