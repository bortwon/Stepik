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



# ===================== Бот "Угадай число" ==============================

# Игра для одного пользователя

from aiogram import Bot, Dispatcher
from aiogram.filters import Text, Command
from aiogram.types import Message
from config import config
import random


bot_token: str = config.bot_token.get_secret_value()

# Создаем объекты бота и диспетчера
bot: Bot = Bot(bot_token)
dp: Dispatcher = Dispatcher()

# Количество попыток, доступных пользователю в игре
attempts: int = 5

# Словарь, в котором будут храниться данные пользователя
user: dict = {'in_game': False,
        'secret_number': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}


# Функция возвращающая случайное целое число от 1 до 100
def get_random_number() -> int:
    return random.randint(1, 100)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def get_start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду /help')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def get_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {attempts} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


# Этот хэндлер будет срабатывать на команду "/stat"
@dp.message(Command(commands=['stat']))
async def get_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {user["total_games"]}\n'
                         f'Игр выиграно: {user["wins"]}')


# Этот хэндлер будет срабатывать на команду "/cancel"
@dp.message(Command(commands=['cancel']))
async def get_cancel_command(message: Message):
    if user['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом')
        user['in_game'] = False
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')


# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру
@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра',
                       'Играть', 'Хочу играть'], ignore_case=True))
async def get_positive_answer(message: Message):
    if not user['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
        user['in_game'] = True
        user['secret_number'] = get_random_number()
        user['attempts'] = attempts
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
@dp.message(Text(text=['Нет', 'Не', 'Не хочу', 'Не буду'], ignore_case=True))
async def get_negative_answer(message: Message):
    if not user['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')


# Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def get_numbers_answer(message: Message):
    if user['in_game']:
        if int(message.text) == user['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\n'
                                 'Может, сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
            user['wins'] += 1
        elif int(message.text) > user['secret_number']:
            await message.answer('Загаданное число меньше!')
            user['attempts'] -= 1
        elif int(message.text) < user['secret_number']:
            await message.answer('Загаданное число больше!')
            user['attempts'] -= 1

        if user['attempts'] == 0:
            await message.answer(f'К сожалению, у вас больше не осталось '
                                 f'попыток. Вы проиграли :(\n\nМое число '
                                 f'было {user["secret_number"]}\n\nДавайте '
                                 f'сыграем еще?')
            user['in_game'] = False
            user['total_games'] += 1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message()
async def get_other_answers(message: Message):
    if user['in_game']:
        await message.answer('Мы же сейчас с вами играем. '
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')


if __name__ == '__main__':
    dp.run_polling(bot)


# Какие есть проблемы у текущей реализации бота "Угадай число"?

# - Бот не сохраняет состояние пользователя в базе данных и если по каким-то причинам будет отключен - вся информация
# о пользователе потеряется
# - Токен! Очень нежелательно хранить секреты в исполняемом файле бота!
# - Бот не может корректно обрабатывать апдейты от нескольких пользователей
# - Нет обработки ошибок, которые могут возникнуть в процессе работы бота



# ------------------- Игра "Угадай число" для многих пользователей --------------------

# Сейчас наш бот, по сути, не делает особых различий между пользователями, и если одновременно попытаются играть
# несколько человек - возникнет хаос. У всех пользователей будет ОДНО на всех состояние, либо "Игра", либо "Не игра".
# На всех пользователей будет ОДНО и то же загаданное число. На всех пользователей будет ВСЕГО 5 попыток. В общем, все
# сломается.
#
# Для того, чтобы такого не происходило, нам как-то нужно развести пользователей друг от друга. И самое очевидное, что
# приходит на ум - сделать словарь словарей, где ключами будут ID пользователей, а значениями словари из первого
# примера бота "Угадай число". Если приходит новый пользователь, которого нет в словаре - он в словарь добавляется. А
# если пользователь уже взаимодействовал с ботом - бот сможет понять на каком этапе это взаимодействие находится.
#
# Давайте немного модифицируем код, чтобы сделать его более универсальным.
#
# Нам просто нужно, когда пользователь стартует бота, проверять знает ли бот этого пользователя. Если нет - в словарь
# users добавляется id пользователя в качестве ключа, а в качестве значения добавляется словарь вида:
#
# {'in_game': False,
#  'secret_number': None,
#  'attempts': None,
#  'total_games': 0,
#  'wins': 0}
# ID пользователя можно получить так message.from_user.id.
#
#
# Весь код многопользовательского бота "Угадай число":

from aiogram import Bot, Dispatcher
from aiogram.filters import Text, Command
from aiogram.types import Message
from config import config
import random


bot_token: str = config.bot_token.get_secret_value()

# Создаем объекты бота и диспетчера
bot: Bot = Bot(bot_token)
dp: Dispatcher = Dispatcher()

# Количество попыток, доступных пользователю в игре
attempts: int = 5

# Словарь, в котором будут храниться данные пользователя
user: dict = {'in_game': False,
        'secret_number': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}

users: dict = {}

# Функция возвращающая случайное целое число от 1 до 100
def get_random_number() -> int:
    return random.randint(1, 100)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def get_start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду /help')
    if message.from_user.id not in users:
        users[message.from_user.id] = user


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def get_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {attempts} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')


# Этот хэндлер будет срабатывать на команду "/stat"
@dp.message(Command(commands=['stat']))
async def get_stat_command(message: Message):
    await message.answer(f'Всего игр сыграно: {users[message.from_user.id]["total_games"]}\n'
                         f'Игр выиграно: {users[message.from_user.id]["wins"]}')


# Этот хэндлер будет срабатывать на команду "/cancel"
@dp.message(Command(commands=['cancel']))
async def get_cancel_command(message: Message):
    if user['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом')
        users[message.from_user.id]['in_game'] = False
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')


# Этот хэндлер будет срабатывать на согласие пользователя сыграть в игру
@dp.message(Text(text=['Да', 'Давай', 'Сыграем', 'Игра',
                       'Играть', 'Хочу играть'], ignore_case=True))
async def get_positive_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['secret_number'] = get_random_number()
        users[message.from_user.id]['attempts'] = attempts
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')


# Этот хэндлер будет срабатывать на отказ пользователя сыграть в игру
@dp.message(Text(text=['Нет', 'Не', 'Не хочу', 'Не буду'], ignore_case=True))
async def get_negative_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')


# Этот хэндлер будет срабатывать на отправку пользователем чисел от 1 до 100
@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def get_numbers_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\n'
                                 'Может, сыграем еще?')
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
        elif int(message.text) > users[message.from_user.id]['secret_number']:
            await message.answer('Загаданное число меньше!')
            users[message.from_user.id]['attempts'] -= 1
        elif int(message.text) < users[message.from_user.id]['secret_number']:
            await message.answer('Загаданное число больше!')
            users[message.from_user.id]['attempts'] -= 1

        if users[message.from_user.id]['attempts'] == 0:
            await message.answer(f'К сожалению, у вас больше не осталось '
                                 f'попыток. Вы проиграли :(\n\nМое число '
                                 f'было {users[message.from_user.id]["secret_number"]}\n\nДавайте '
                                 f'сыграем еще?')
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


# Этот хэндлер будет срабатывать на остальные любые сообщения
@dp.message()
async def get_other_answers(message: Message):
    if message.from_user.id not in users:
        users[message.from_user.id] = user
    if users[message.from_user.id]['in_game']:
        await message.answer('Мы же сейчас с вами играем. '
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')


if __name__ == '__main__':
    print(users)
    dp.run_polling(bot)


# ==========================================================================