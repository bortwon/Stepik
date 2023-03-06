# =======================================================
# Общая информация о курсе
# =======================================================

# -------------------------------------------------------
# 1.4. Глоссарий
# -------------------------------------------------------

# -------------------------------------------------------
# Сопоставьте термины и их значения:

# Handler - Функция-обработчик
# FSM - Машина состояний
# API - Программный интерфейс приложения
# Throttling - Ограничение пропускной способности
# Deploy - Развертывание
# Middleware - Промежуточное ПО
# Polling - Опрос сервера



# =======================================================
# Общие сведения о телеграмм-ботах
# =======================================================

# -------------------------------------------------------

# ЦИКЛ ВЗАИМОДЕЙСТВИЯ

# Есть две основные технологии, которыми бот может получать то, что ему предназначено от сервера. Long polling и
# Webhook. Суть лонг поллинга состоит в том, чтобы постоянно опрашивать сервер на наличие обновлений (апдейтов),
# предназначенных боту, типа, "Есть, там, чего для меня?". А webhook - это когда сам сервер "стучится" к боту и
# говорит: "Тебе что-то пришло!", когда для бота что-то приходит. Сейчас не будем заострять на этих технологиях
# внимание, о них будет подробно далее в курсе. Long polling используется, в основном, на этапе разработки и
# тестирования бота, часто на компьютере самого разработчика, а webhook, когда бот уже запущен в продакшн.


# Сопоставьте названия команд с функционалом, который они активируют:
# Сопоставьте значения из двух списков

# /setabouttext - Изменение информации о боте в его профиле
# /setinline - Включение инлайн-режима для бота
# /setprivacy - Изменение режима видимости сообщений ботом в группах
# /setdescription - Изменение описания бота, которое пользователь видит перед стартом бота
# /revoke - Перевыпуск токена бота
# /setjoingroups - Разрешение или запрет добавлять бота в группы


# Выберите стандартный путь для отслеживаемого гитом файла.

# - Работаем с файлом - добавляем файл в индекс - коммитим изменения


# ======= API =========

# Как расшифровывается аббревиатура API в контексте данного курса?
# - Application Programming Interface



# Работа с API с помощью библиотеки requests

# Я не буду сейчас подробно останавливаться на функциях и методах библиотеки requests, просто покажу, как можно
# получать информацию с помощью GET-запросов. Давайте выясним где прямо сейчас находится Международная Космическая
# Станция.

import requests


api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)    # При другом коде ответа выводим этот код

# Если все получилось, то вы должны увидеть в терминале сообщение вида:

# {"message": "success", "iss_position": {"longitude": "7.6753", "latitude": "50.2226"}, "timestamp": 1668894374}
 # "longitude" и "latitude" - это, соответственно, долгота и широта текущего положения МКС.

# Код ответа 200 говорит об успешном выполнении запроса, соответственно, можно посмотреть, что содержится в
# атрибуте text переменной response.


# Получение точных координат

import requests
from pprint import pprint

api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
else:
    pprint(response.status_code)

print(data['iss_position']['longitude'])
print(data['iss_position']['latitude'])


# -----------------------

# Сделайте запрос к API http://numbersapi.com/ для числа 43 и скопируйте в текстовое поле полный ответ от сервиса.
# Примечание. Ответ не должен содержать в себе дополнительных символов (пробелов, переносов строки и т.п.) он должен
# быть ровно таким, каким его прислал сервис.

# - 43 is the maximum number of cars participating in a NASCAR race in the Cup Series or Nationwide Series.


# ============= Telegram Bot API =================

# Принцип взаимодействия мы с вами разобрали. С библиотекой requests немного познакомились. Давайте напишем простенькую
# программу, которая будет проверять наличие апдейтов на серверах телеграм от пользователей нашего бота, и на каждый
# апдейт будет отправлять в чат пользователю фразу: "Ура! Классный апдейт!". Вроде, и бессмысленно, а схема работы
# уложится в голове лучше :) Можете, кстати, другую фразу написать, если вам эта не по душе :)

import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '5424991242:AAGwomxQz1p46bRi_2m3V7kvJlt5RjK9xr0'
TEXT: str = 'Ура! Классный апдейт!'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1


# MAX_COUNTER - это количество итераций цикла, в котором мы получаем апдейты от сервера. Можете сделать любым, с
# каким захотите поэкспериментировать.



# Сформируйте и вставьте в поле ниже GET-запрос к Telegram Bot API, который отправит пользователю текстовое
# сообщение "AMAZING!"
# Уточнение. Вместо токена бота напишите <token>, вместо номера chat_id - <chat_id>
#
# Примечание. Ответ должен быть без кавычек, пробелов, переводов строки.

# https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=AMAZING!



# Укажите правильно сформированные GET-запросы к Telegram Bot API

# - https://api.telegram.org/bot<token>/getUpdates?offset=-1
# - https://api.telegram.org/bot<token>/getMe




# ========= LONG POLLING ===============

# Выберите значения параметра timeout, с которыми сервер Telegram будет работать в режиме long polling
# Пояснение. Запустите код из предыдущего шага с разными значениями параметра timeout, чтобы увидеть какие значения
# как работают.

#  100
#  10
#  20.63


# ================== ЭХО-БОТ ==============================

# Начнем с самого простого - напишем бота, который будет на наши сообщения отвечать нашими же сообщениями и на его
# примере рассмотрим самый простой шаблон.

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import Sticker
from aiogram import F
from config import config

bot_token: str = config.bot_token.get_secret_value()

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


@dp.message(F.photo)
async def process_send_photo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


@dp.message()
async def process_send_sticker(message: Message):
    await message.reply_sticker(message.sticker.file_id)


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)



# Расположите инструкции в правильном порядке, чтобы получился рабочий шаблон простейшего эхо-бота

# - Импортируем Bot, Dispatcher, фильтры и типы апдейтов
# - Сохраняем токен бота в переменную
# - Инициализируем объект бота
# - Инициализируем объект диспетчера
# - Создаем хэндлеры, реагирующие на команды
# - Создаем хэндлер, реагирующий на любые текстовые сообщения
# - Запускаем polling


# Регистрация хэндлеров

# dp.message.register(process_start_command, Command(commands=["start"]))
# dp.message.register(process_help_command, Command(commands=['help']))
# dp.message.register(send_echo)


# Полноценный эхо-бот

# У aiogram есть готовый метод, который отправит в чат копию сообщения, не зависимо от типа контента. Ну, почти.
# Все-таки есть типы апдейтов, которые не поддерживаются данным методом, но их немного. Метод называется send_copy.
# Сейчас мы с вами немного перепишем Эхо-бота с использованием этого метода.

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import config

bot_token: str = config.bot_token.get_secret_value()

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Данный тип апдейтов не поддерживается '
                                 'методом send_copy')


if __name__ == '__main__':
    dp.run_polling(bot)