# Определения:


# API - Application Programming Interface (программный интерфейс приложения) - набор правил взаимодействия с каким-либо
# сервисом с помощью программных запросов. По сути, это описание как можно обратиться к сервису и какие ответы от него
# получить, без необходимости разбираться как именно сервис работает "под капотом". В контексте написания
# телеграм-ботов, имеется в виду Telegram Bot API.


# Callback - "обратный вызов" - это функция, которая передается в диспетчер, чтобы быть вызванной при наступлении
# соответствующих условий. То есть, если апдейт прошел соответствующий фильтр - вызывается callback-функция.


# Callback Query - апдейт, который приходит боту, если пользователь нажал на инлайн-кнопку.


# Deep-link - "глубокая ссылка" - ссылка вида https://t.me/my_bot?start=some_data, по которой пользователь может
# перейти в чат с телеграм-ботом. В чате, после перехода по ссылке, появится кнопка START, при нажатии на которую
# бот получит не только команду /start, но и данные some_data. Бывает полезно, если нужно отследить откуда пришел
# пользователь или для реферальной программы.


# Deploy - "развертывание" - запуск бота на удаленном сервере для бесперебойной работы.


# Dispatcher - "диспетчер" - специальный объект aiogram, который занимается получением апдейтов от
# серверов Telegram, распаковывает их и передает в соответствующие хэндлеры (обработчики).


# Filter - "фильтр" - шаблон, которому должен соответствовать апдейт или его часть, чтобы сработал отвечающий за
# него хэндлер. То есть когда боту приходит апдейт, диспетчер пытается последовательно пропустить его через
# фильтры и, как только объект проходит первый фильтр - срабатывает хэндлер, настроенный на обработку
# апдейта, прошедшего этот фильтр.


# FSM (Finite State Machine) - "машина состояний" - конечный автомат, который позволяет хранить состояние пользователя
# бота, чтобы в зависимости от этого состояния и действий пользователя, переводить пользователя в другие состояния.


# Handler - "обработчик" - функция, которая обрабатывает апдейт. В идеале, одна функция на каждый тип апдейтов с
# одинаковым или близким содержимым. Делать большую функцию, где проверять свойства апдейтов с
# помощью if...else - это, чаще всего, плохая практика.


# Inline-кнопка - "инлайн-кнопка" - кнопка, которая прикрепляется к отправляемому сообщению и может быть отправлена
# только как часть этого сообщения, в отличие от "обычных" кнопок, которые заменяют стандартную пользовательскую
# клавиатуру и не прикреплены к какому-либо сообщению бота.


# Inline-режим (inline-mode) - "инлайн-режим" - режим взаимодействия пользователя с ботом через поле ввода
# сообщения, без прямой отправки сообщения боту. Пользователь вводит в любом чате "@имя_бота," а затем запрос. Бот
# сразу получает апдейты, не дожидаясь пока пользователь полностью введет сообщение.


# Long polling - "долгий опрос" - способ взаимодействия бота с сервером Telegram, путем постоянного опроса сервера
# на предмет наличия апдейтов, но с таймаутом до разрыва соединения. То есть, бот ждет ответа от сервера какое-то
# время, не разрывая соединения. Если за это время апдейтов нет - сервер сообщает, что апдейтов нет и разрывает
# соединение. Боту нужно снова посылать запрос. А если апдейты есть, то сервер их боту отправляет сразу, не дожидаясь
# окончания соединения.


# Middleware - "промежуточное программное обеспечение" - специальная программа, которая является прослойкой между
# другими программами, передавая информацию от одной к другой. В контексте aiogram - это код, который предназначен
# что-то сделать с апдейтами до того, как они попадут в хэндлеры.


# Polling - "опрос" - способ получения апдейтов ботом от серверов Telegram, путем постоянного опроса этих серверов
# на наличие обновлений. В отличие от лонг поллинга, сервер отвечает сразу, независимо от того, есть апдейты или нет.
# Если они есть - сервер пересылает их боту, а если нет - отвечает, что апдейтов нет.


# Throttling - "удушение" - ограничение количества запросов пользователям. Если от пользователя приходит слишком много
# бессмысленных апдейтов, которые нагружают систему, имеет смысл не передавать их обработчикам, а просто отсекать.


# Token - "токен" - специальный ключ-идентификатор бота, по которому сервера Telegram идентифицируют бота. Имея этот
# ключ, можно управлять ботом, даже не являясь его владельцем, поэтому токен нужно хранить в защищенном месте
# и никому, без особой необходимости, не передавать. Владелец бота (именно как специального аккаунта в Telegram) может
# в любой момент перевыпустить токен.


# Update - "апдейт" - сообщение от сервера Telegram, которое получает бот. Но не только текстовое сообщение, которое
# пользователь отправил в чат, а вообще любое событие, поддерживаемое Telegram Bot API. Полный список возможных
# апдейтов можно посмотреть в документации.


# Username - в рамках Telegram - это уникальное имя бота или пользователя, с помощью которого можно получить доступ
# к чату с ним (например, @my_bot, @kmsint внутри приложения Telegram и https://t.me/my_bot, https://t.me/kmsint из
# внешних источников).


# Webhook - способ доставки апдейтов боту, при котором не бот постоянно опрашивает серверы Telegram на наличие новых
# сообщений (апдейтов), а сервер Telegram пересылает все новые апдейты на специальный URL-адрес, когда эти апдейты есть.


# /setname - позволяет менять название бота (не username, который уникален в рамках всего Telegram, а именно имя,
# которое отображается).


# /setdescription - команда, позволяющая настроить описание бота, которое увидит пользователь, когда впервые найдет
# бота в поиске или перейдет к нему по ссылке. То есть перед запуском бота.


# Какими командами в чате с BotFather можно вызвать список команд для создания и управления телеграм-ботами?
# - /start
# /help


# /setabouttext - эта команда добавляет или изменяет описание в профиле бота.


# /setuserpic - команда для того, чтобы у бота в профиле появилась картинка (аватар, юзерпик).


# /setcommands - служит для создания списка команд. У вашего бота появится такая-же синяя кнопка Menu, как на
# скриншоте у BotFather, при нажатии на которую будет открываться список команд. Если отправить вместо списка команд
# команду /empty - список команд либо останется пустым, либо станет пустым (если в нем уже были ваши команды).


# /deletebot - служит для удаления ваших ботов, которые больше не нужны. После ввода этой команды и выбора
# бота, которого требуется удалить, Телеграм еще раз спросит подтверждаете ли вы это действие и, если вы реально
# уверены, что пора избавиться от ненужного бота, вам надо будет ввести фразу-подтверждение, после чего бот будет
# окончательно удален.


# /token - команда, позволяющая получить токен для вашего бота. Если вы его, вдруг забыли или потеряли. При этом
# BotFather отправит вам старый токен, а не создаст новый, в отличие от команды /revoke, которая позволяет отозвать
# старый токен и сгенерировать новый.


# /revoke - команда, позволяющая отозвать текущий токен вашего бота и сгенерировать новый. Новый токен может
# понадобиться, если старый, по какой-то причине, скомпрометирован. Часто бывает, что при хранении кода бота,
# например, на гитхабе, по неопытности, пользователи отправляют туда и конфигурационный файл с токеном. И если
# проект при этом не приватный - токен становится виден всем и кто-нибудь может перехватить управление вашим ботом.
# До того момента, пока вы не отзовете старый токен, сгенерировав новый.


# /setinline - команда, включающая inline-режим для бота.


# Inline-режим позволяет использовать бота, как помощника для поиска информации, в каком чате вы бы не находились.
# То есть, допустим, вы общаетесь с кем-то и вспомнили, что смотрели какой-нибудь классный видос на ютубе и захотели
# им поделиться. Конечно, вы можете открыть ютуб, в поиске найти нужное видео, скопировать ссылку, вернуться к чату и
# отправить эту ссылку собеседнику. Но можно сделать и по-другому. Просто, находясь в чате с нужным собеседником
# набираете "@vid предположительное название видео" и появляется сразу список возможных видео, которые вы можете
# отправить в чат. Иногда бывает очень удобно! Вы можете настроить и своего бота так, чтобы он помогал вам искать
# информацию, не выходя из телеграм.
#
# После отправки команды /setinline нужно будет еще отправить placeholder - подсказку, которая будет появляться во
# время взаимодействия с ботом в инлайн-режиме.


# Чтобы лучше разобраться как работают боты в inline-режиме - попробуйте поиграться, например, с этими:
#
# @vid – поиск видео
# @gif – поиск GIF
# @wiki – поиск статей в Википедии
# @pic – поиск изображений от Яндекс
# @bold – форматирование текста


# Некоторые боты могут в инлайн-режиме запрашивать у пользователей их геопозицию, чтобы, например, порекомендовать
# какое-нибудь место по-близости, или выдать задание для квеста на местности, или найти рядом других пользователей
# бота и т.д. То есть, каждый раз набирая "@имя_бота" в любом чате, бот будет спрашивать разрешение на отправку
# геопозиции, а потом подгружать результаты, от нее зависящие. Чтобы добавить такой функционал - необходимо отправить
# команду Отцу ботов - /setinlinegeo. При этом инлайн-режим уже должен быть у бота включен.


# /setinlinefeedback - команда, которая позволяет включить сбор статистики, то есть бот будет получать апдейты о
# выбранных результатах пользователями в инлайн-режиме работы бота. Для высоконагруженных ботов с большим количеством
# пользователей имеет смысл получать один апдейт на каждые 10, 100 или 1000, для чего и служат соответствующие
# настройки (1/10, 1/100 и 1/1000)


# /setjoingroups - команда для настройки разрешения приглашать бота в группы. Если у бота статус "ENABLED" - бота
# можно приглашать в группы как участника, а если "DISABLED" - нельзя, то есть при попытке добавить бота в группу вы
# получите такое сообщение:

# Включается и выключается так же просто, как и в случае других настроек.


# /setprivacy - команда для настройки того, все ли сообщения будет бот видеть в группах. Если статус "ENABLED" - бот
# будет "видеть" только адресованные ему сообщения:
#
# которые начинаются как команды, т.е. с символа "/",
# c прямым упоминанием юзернейма бота,
# ответы на сообщения бота, ответы на ответы и так далее.
# А если статус приватного режима "DISABLED" - бот "видит" все сообщения, которые участники отправляют в группу. Под
# термином "видит" здесь понимается то, что Telegram Bot API будет присылать их боту в виде апдейтов.
#
# При этом, если бот является админом группы - он видит все сообщения пользователей, независимо от настройки /setprivacy.
#
# И еще один небольшой нюанс - при работе бота через Telegram Bot API, он не будет видеть сообщения других ботов, то
# есть не сможет с ними никак взаимодействовать. Если по каким-то причинам это ограничение будет вам мешать реализовать
# задуманный функционал - придется настраивать взаимодействие бота с серверами Telegram не через Telegram Bot API, а
# через Telegram API. В одном из следующих модулей мы кратко разберем какие есть ограничения у Telegram Bot API и как
# их можно попытаться обойти.


# Здесь флаг -m говорит интерпретатору запустить инструмент создания виртуального окружения venv как исполняемый
# модуль, а второй venv - название папки, в которую будет установлено виртуальное окружение. Оно может быть любым
# другим, но обычно принято называть его либо venv, либо env, от английского - virtual environment или просто
# environment.


# Для Windows (PowerShell):
# venv\Scripts\activate

# Выход из виртуального окружения - команда:
# deactivate


# И есть ещё забавная игра про гит: https://learngitbranching.js.org/


# git config --global user.name "Mikhail Kryzhanovskiy"
# и
# git config --global user.email "kms101@yandex.ru"


# Поэтому, на текущий момент у нас есть только один файл для отслеживания - это main.py. Давайте добавим его в индекс.
# Для этого выполним команду:
# git add main.py


# Также есть подсказка, что если какой-либо файл нужно удалить из индекса - можно выполнить команду:
#
# git rm --cached <файл>


# Но мы пока ничего удалять не будем, а наоборот, закоммитим текущее состояние файла командой:
#
# git commit -m "Это наш первый коммит в проекте"


# Примечание 2. Если закоммитить надо не весь индекс, а только некоторые файлы, например, чтобы разбить выполненную
# работу на несколько разных коммитов, можно выполнить команду:
#
# git commit -m <файл_1> <файл_2> <файл_3> "Комментарий к коммиту"


# Для этого сначала нужно на компьютере создать папку с репозиториями, в которую будет клонирован удаленный
# репозиторий. А если такая папка у вас уже есть - нужно в нее перейти.
#
# cd <путь_к_папке>
# И, находясь в этой папке, набирайте команду:
#
# git clone <ссылка_на_репозиторий>



# Доступ к GitHub по SSH ==========================================

# А теперь, чтобы GitHub мог нас аутентифицировать по SSH, нам и надо создать пару ключей. Делается это так.
# Открываем терминал и выполняем команду:
#
# ssh-keygen
# Получим сообщение вида:
#
# Generating public/private rsa key pair.
# Enter file in which to save the key (/Users/mikhail/.ssh/id_rsa):
# То есть нам предлагается ввести название файла, в котором будет храниться пара ключей. По умолчанию, предлагается
# название id_rsa - согласимся с предложением, нажав Enter. Будет создана директория .ssh, а также предложено ввести
# дополнительно passphrase для дополнительной защиты самой пары ключей.


# Была сгенерирована пара ключей. Закрытый хранится в файле id_rsa, а открытый в файле id_rsa.pub. Теперь нужно
# открытый ключ разместить в нашем аккаунте на GitHub. Чтобы увидеть и получить возможность скопировать открытый ключ в буфер обмена, нужно сначала перейти в директорию с парой ключей (у меня это /Users/mikhail/.ssh/, а у вас смотрите, что написано в терминале после фразы Your public key has been saved in) :
#
# cd /Users/mikhail/.ssh/
# Находясь в папке с ключами, надо выполнить команду:
#
# cat id_rsa.pub
# Откроется содержимое файла с открытым ключом, которое нужно скопировать в буфер обмена.
#
# Примечание. В принципе, можно и не переходить в папку с ключами, чтобы скопировать содержимое файла. Можно
# просто, находясь в любом месте файловой системы, выполнить команду:
#
# cat <путь_к_файлу_с_публичным_ключом>


# В Windows вместо команды cat можно использовать type

# ==========================================================


# ========== Аннотация типов ==================

# def say_something(number: int, word: str) -> str:
#     word = word.capitalize()
#     return word * number


# Синтаксис аннотаций для переменных следующий:
#
# <имя_переменной>: <тип_переменной> = <значение_переменной>
# Или без значения переменной:
#
# <имя_переменной>: <тип_переменной>

# Примеры:
#
# first_var  : int        = 5
# second_var : str        = 'second_var'
# third_var  : list       = []
# fourth_var : float
# fifth_var  : dict
# sixth_var  : tuple[int] = (1, 2)


# Синтаксис аннотаций для функций (методов):
#
# def <имя_функции>(<arg_1>: <тип>, <arg_2>: <тип> = <значение>) -> <тип_результата>:
#     <тело функции>
# Примеры:
#
# def get_something_1(arg_1: int, arg_2: str = '', arg_3: list[int]) -> str:
#     pass
#
#
# def get_something_2(arg_1: tuple[int, bool]) -> None:
#     pass


# ========= Аннотация типов ===========


# Выберите корректно аннотированные переменные:

var_1: int
var_3: tuple = (1, False, 'Hello')



# Выберите корректно аннотированную функцию:

def get_string(string: str, times: int, sep: str='') -> str:
    return sep.join([string] * times)


# Пример 1. Функция some_function принимает либо целое, либо вещественное число, а возвращает None.

def some_function(number: int | float) -> None:
    pass

# Пример 2. Функция another_some_function принимает либо целое, либо вещественное, либо комплексное число со значением
# по умолчанию, равным 0. Возращает None.

def another_some_function(number: int | float | complex = 0) -> None:
    pass

# Коллекции, типа, list, dict, tuple, set и т.п., также в квадратных скобках позволяют указывать типы, входящих в
# них объектов.

# Пример 3.

# lst_1: list[int]                # Все элементы списка lst_1 типа int
# tpl_2: tuple[bool]              # Все элементы кортежа tpl_2 типа bool
# tpl_3: tuple[int, bool, float]  # Кортеж tpl_3 состоит из трех элементов
#                                 # Первый типа int, второй типа bool, а третий типа float
# set_4: set[int | float]         # Элементы множества set_4 либо int, либо float типов

# Пример 4. Функция get_tuple принимает список, в котором могут быть вещественные числа и/или булевы значения, а
# возвращает кортеж целых чисел.

def get_tuple(lst: list[float | bool]) -> tuple[int]:
    return tuple(int(num) for num in lst)

# Пример 5. Функция do_something принимает словарь, ключами в котором являются целые числа, а значениями либо
# строки, либо булевы значения. Возвращает None.

def do_something(arg: dict[int, str | bool]) -> None:
    pass



# =========== Типы из модуля typing =========

# Помимо стандартных встроенных типов, для аннотаций можно использовать типы из модуля typing. Там много всего - можно
# подробно изучить в документации к модулю. Разберем некоторые интересные:
#
# Any
# Optional
# Union
# Literal
# Тип Any (использовать, по-возможности, никогда :) )
# Бывает так, что указать тип не представляется возможным, потому что точно неизвестно какие данные придут. Тогда
# используют тип Any из модуля typing.
#
from typing import Any


def func(arg: Any) -> None:
    pass


# Тип Optional
# Данный тип подразумевает, что данные могут быть либо какого-то конкретного типа, либо None.
#
# from typing import Optional
#
#
# var_1: Optional[int]


# Тип Union
# Как понятно из названия типа - это объединение разных типов. По сути - это другой способ записать, что переменная
# может быть либо одного, либо другого типа, как мы это делали с помощью символа |.
#
# Код:
#
# from typing import Union
#
#
# var_1: Union[int, float]
# var_2: Union[list, tuple, set]
# эквивалентен коду:
#
# var_1: int | float
# var_2: list | tuple | set


# Тип Literal
# Используется тогда, когда ожидаются очень конкретные значения (Literal - от английского "literally", то
# есть "буквально"). Например, в качестве ключей словаря могут быть только строки 'name', 'second_name' и 'username'.
# Тогда можно записать:
#
# from typing import Literal
#
#
# user : dict[Literal['name'] | Literal['second_name'] | Literal['username'], str]
# Во-первых, IDE сможет подсказать какие ключи в таком словаре доступны, а во-вторых, анализатор кода будет ругаться,
# если мы попробуем в такой словарь поместить какой-то другой ключ.



# ===================== Классы и датаклассы ==============


# Это до датакласса:
def get_user_info(user: User) -> str:
    return f'Возраст пользователя {user.name} - {user.age}, ' \
           f'а email - {user.email}'


user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
print(get_user_info(user_1))


# Это после датакласса

from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str


# Давайте приведу пример из разработки телеграм-ботов, чтобы немного заземлить теорию. Вот так, например, можно
# оформить класс Config, в экземпляре которого будут храниться конфигурационные данные для наших с вами ботов и
# данные для подключения к базе данных, которые мы будем получать сначала из переменных окружения:
#
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    db_host: str       # URL-адрес базы данных
    db_user: str       # Username пользователя базы данных
    db_password: str   # Пароль к базе данных
    database: str      # Название базы данных


@dataclass
class TgBot:
    token: str             # Токен для доступа к телеграм-боту
    admin_ids: list[int]   # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig

# Если создать экземпляр класса Config:
#
config = Config(tg_bot=TgBot(token=BOT_TOKEN,
                             admin_ids=ADMIN_IDS),
                db=DatabaseConfig(db_host=DB_HOST,
                                  db_user=DB_USER,
                                  db_password=DB_PASSWORD,
                                  database=DATABASE))

# То, например, получить токен бота можно, будет так:
#
token = config.tg_bot.token

# А пароль к базе данных так:
#
db_passw = config.db.db_password

# ===============================



# ================ __annotations__ =====================

# Пример. Функция get_string, получающая на вход строку и число, а возвращающаяя строку.

def get_string(string: str, number: int) -> str:
    return string * number

# Если обратиться к атрибуту __annotations__ функции get_string:

print(get_string.__annotations__)

# увидим следующий словарь:

# {'string': <class 'str'>, 'number': <class 'int'>, 'return': <class 'str'>}


# =================== ВЫВОДЫ ===================

# Итак, давайте резюмируем.
#
# Зачем вообще нужна аннотация типов?
#
# Выявление ошибок еще на этапе написания кода. С помощью IDE и статических анализаторов кода. А чем раньше выявлена
# ошибка, тем, в общем случае, дешевле ее исправить.
# Улучшение читаемости кода за счет явного указания, что ожидает и что возвращает функция или класс.
# Упрощение разработки в IDE за счет подсказок и автодополнения. В частности, в aiogram большое количество
# классов, которые являются отображением методов Telegram Bot API, и довольно удобно не лезть в документацию, а
# прямо внутри хэндлера, при его написаниии, получать мини-справку по доступному функционалу.
# Важная особенность 1:
#
# Интерпретатор никак не проверяет аннотации типов. То есть код, при котором в функцию будет передан не тот тип
# данных, что указан в аннотации, может отработать и без ошибок.
#
# Важная особенность 2:
#
# Переменные также можно аннотировать, причем необязательно присваивать им значения. Но надо иметь в виду, что
# присваивать значения переменным в программе нужно до их первого использования, иначе интерпретатор выкинет
# исключение NameError.
#
# Для аннотаций типов используются:
#
# Встроенные типы данных языка (int, float, str, list, dict, tuple...)
# Объекты из модуля typing (List, Dict, NamedTuple, Union, Optional, Any, NoReturn...)
# Пользовательские классы
# Классы из сторонних модулей
# Датаклассы из модуля dataclasses
# Примечание. Аннотации типов хранятся в атрибуте __annotations__ объектов.


# =====================================


# ============= API =============

# API (Application Programming Interface) - "программный интерфейс приложения" - описание правил, по которым одна
# компьютерная программа может взаимодействовать с другой.



# ============= Telegram Bot API =================

# Если попытаться уложить принцип взаимодействия с Telegram Bot API в одну фразу - получится что-то
# типа, "все взаимодействие происходит по одной схеме - отправка запросов на получение апдейтов с сервера Telegram и
# отправка запросов серверу на те или иные действия". Апдейты - это любые, доступные пользователю бота, действия, в
# рамках "общения" пользователя с ботом:
#
# Старт бота
# Отправка текстового сообщения
# Отправка стикера
# Нажатие на инлайн-кнопку
# Отправка аудиосообщения
# Отправка команды
# Нажатие на обычную кнопку
# Запросы к боту в инлайн-режиме
# ...


# Чтобы взаимодействовать со своими ботами через Telegram Bot API - нужно посылать запросы по следующей форме:
#
# https://api.telegram.org/bot<token>/METHOD_NAME
# Вместо <token> нужно вставить токен вашего бота, а вместо METHOD_NAME - имя метода, доступного в API. После
# METHOD_NAME еще можно после вопросительного знака ? посылать параметры в виде key1=value1&key2=value2. Таких пар
# ключ=значение может быть столько, сколько требуется.
#
# Чтобы, например, получить информацию по одному из моих ботов - я могу отправить прямо в адресной строке браузера
# GET-запрос вида:
#
# https://api.telegram.org/bot5424991242:AAGwomxQz1p46bRi_2m3V7kvJlt5RjK9xr0/getMe
# И, соответственно, получу ответ в формате JSON:
#
# {"ok":true,"result":{"id":5424991242,"is_bot":true,"first_name":"New_name","username":"VeryVeryVerySmart_bot",
# "can_join_groups":true,"can_read_all_group_messages":false,"supports_inline_queries":true}}



# =============== Polling ===================

# По сути, на одном из предыдущих шагов, когда мы с вами писали программу, которая опрашивает сервер Telegram на
# наличие апдейтов для бота, мы реализовали polling, то есть постоянный опрос сервера. Его суть в том, что идет
# обращение к серверу, сервер что-то отвечает и сразу закрывает соединение. При этом не важно, есть апдейты или нет.


# Вот так может выглядеть polling со стороны клиента, то есть нашего бота:
#
import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = ''
offset: int = -2
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')

# Вот так это выглядит в терминале:
#
# Время между запросами к Telegram Bot API: 3.149364948272705
# Время между запросами к Telegram Bot API: 3.1524858474731445
# Время между запросами к Telegram Bot API: 3.1554458141326904
# Был апдейт
# Время между запросами к Telegram Bot API: 3.1923599243164062
# Время между запросами к Telegram Bot API: 3.145864963531494
# Время между запросами к Telegram Bot API: 3.137209892272949
# Время между запросами к Telegram Bot API: 3.1353447437286377
# Был апдейт
# Время между запросами к Telegram Bot API: 3.152209997177124
# Время между запросами к Telegram Bot API: 3.1605660915374756
# Время между запросами к Telegram Bot API: 3.150103807449341



# ============ LONG POLLING =================


# Чтобы снизить нагрузку от большого количества частых запросов, Телеграм-сервера могут работать в режиме лонг
# поллинга. Long polling - это polling "с ожиданием апдейтов", то есть происходит соединение с сервером на определенное
# время (timeout). Если апдейты есть - сервер их отправляет и закрывает соединение, а если нет - то соединение остается
# открытым в течение этого времени. Если апдейты за это время появляются - сервер их отправляет и сразу закрывает
# соединение, а если не появляются, то соединение закрывается по истечении времени таймаута. Затем процесс обращения к
# серверу повторяется.
#
# Посмотрим на метод getUpdates Telegram Bot API:


# Нас интересует параметр timeout. Если мы передадим его в запросе к серверу отличным от нуля положительным целым
# числом, то будет работать схема лонг поллинга, описанная выше.
#
# Вот так может выглядеть long polling со стороны клиента (не забудьте вместо токена моего бота вставить токен
# вашего бота):
#
import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = ''
offset: int = -2
timeout: int = 60
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()

    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')


# Обратите внимание, что, не смотря на то, что мы для параметра timeout указали значение 60 - соединение закрывается
# где-то за 50 секунд. Видимо, это максимально возможное значение параметра timeout, прописанное в настройках серверов
# Telegram. Соответственно, больше этого значения делать timeout смысла не имеет, хотя и работать все равно все будет
# корректно.
#
# В продакшне, если вы используете polling, а не webhook - обязательно нужно использовать long polling, то есть
# передавать запрос на апдейты с параметром timeout отличным от нуля положительным целым числом. Polling, или в
# терминологии Telegram Bot API - short polling - когда timeout равен нулю, рекомендуется использовать только в
# тестовых целях.


# -------- Асинхронный long polling ------------

# В предыдущих примерах мы использовали синхронное программирование, то есть когда выполнялся запрос к серверу, мы
# зависали в этой точке и ничего другого не происходило. Мы что-то могли делать только в промежутке между
# запросами - либо когда приходил апдейт, либо когда заканчивалось время соединения timeout. Достаточно бездарная
# трата временных ресурсов, потому что никто нам не мешает что-то делать в то время, когда ожидаются ответы от сервера.
# Асинхронное программирование позволяет нам распараллелить процессы получения апдейтов и их обработки. Пусть себе одна
# сущность ожидает апдейты, а какая-нибудь другая в это время будет делать что-то другое.


# ===================================


# ========= ЭХО-БОТ =================

# Из aiogram.filters импортируем класс Command, чтобы фильтровать апдейты по наличию в них команд, то есть
# сочетаний символов, начинающихся со знака "/".

# Из aiogram.types импортируем класс Message. Апдейты этого типа мы будем ловить эхо-ботом.


# # Чтобы отправить текстовове сообщение в тот же чат используется упрощенная запись вида
# # await message.answer('Какой-то текст')


# Но если вы захотите отправить сообщение в какой-то другой чат (иногда, например, вы отправляете боту какое-то
# сообщение и хотите, чтобы он отправил его в канал или группу, или отдельным контактам, то есть не в тот же самый
# чат, куда вы прислали сообщение боту), тогда запись будет выглядеть так:
#
# await bot.send_message(chat_id='ID или название чата', text='Какой-то текст')
# Строго говоря, и в тот же самый чат можно ответить этим способом, вот так:
#
# await bot.send_message(message.chat.id, message.text)


# Откуда хэндлеры узнают про bot, который экземпляр класса Bot, если мы его туда не передавали? В нашем случае, когда
# весь код бота в одном файле, bot просто находится в глобальной области видимости, поэтому виден внутри хэндлеров.
# Но вообще, объект bot нужно передавать в хэндлеры в качестве параметра. И когда мы будем разносить логику работы
# бота по разным файлам - вы увидите, что в некоторых случаях мы будем напрямую указывать в хэндлерах дополнительный
# параметр bot класса Bot.


# Считается хорошим тоном умение бота реагировать на команду /help, чтобы пользователь мог получить подсказку по
# функционалу бота. Часто команды /start и /help объединяют и обрабатывают одним хэндлером, перечисляя их в декораторе
# списком @dp.message(Command(commands=['start', 'help'])). Но мы так делать не будем. На команду /start пусть бот
# реагирует приветствием, а на команду /help пусть скажет, что пользователь может получить от бота.
#
# # Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# # кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)


# -------- Регистрация хэндлеров в диспетчере -----------
# В примере с эхо-ботом мы регистрировали наши обработчики с помощью декораторов, но в aiogram есть и другой способ их
# регистрации. Можно напрямую вызвать соответствующий метод у диспетчера. Рассмотрим на примере того же самого эхо-бота.

# Регистрируем хэндлеры
# dp.message.register(process_start_command, Command(commands=["start"]))
# dp.message.register(process_help_command, Command(commands=['help']))
# dp.message.register(send_echo)


# Только текстовые? На самом деле нет. В него попадают любые апдейты, которые не попали в другие
# хэндлеры, зарегистрированные ранее. Но когда мы в хэндлере пытаемся отправить ответ в чат методом reply - этот метод
# подразумевает, что у апдейта есть поле text, а такое поле есть далеко не у всех апдейтов, поэтому при отправке в чат
# боту фото или стикера, или видео и т.п. - в терминал будет приходить ошибка. Далее мы посмотрим сначала как
# реагировать на каждый тип контента по-отдельности, а потом напишем полноценного Эхо-бота, который будет реагировать
# эхом вообще на любые отправляемые ему сообщения.



# --------------- Эхо-бот для фото ---------------------
# Чтобы наш эхо-бот мог срабатывать на отправку фото, добавим в его код некоторые импорты и такой хэндлер:
#
# from aiogram.types import ContentType
# from aiogram import F
#
# # ...
#
# # Этот хэндлер будет срабатывать на отправку боту фото
# async def send_photo_echo(message: Message):
#     print(message)
#     await message.reply_photo(message.photo[0].file_id)
#
# # ...
# И зарегистрируем его в диспетчере
#
# dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)



# -------Разница между message.reply и message.answer ------------------

# Наверное, вы итак догадались, но на всякий случай разберем и это. message.answer отправляет в чат сообщение, а
# message.reply отправляет ответ на сообщение. На скриншоте пример.


# У aiogram есть готовый метод, который отправит в чат копию сообщения, не зависимо от типа контента. Ну, почти.
# Все-таки есть типы апдейтов, которые не поддерживаются данным методом, но их немного. Метод называется send_copy.
# Сейчас мы с вами немного перепишем Эхо-бота с использованием этого метода.



# ==================== Апдейты ======================

# Апдейт (Update) - это любое событие, которое Telegram сохраняет для бота, которое затем можно получить по запросу и
# как-то обработать. То есть при взаимодействии с ботом, почти на любые действия пользователя, сохраняются апдейты
# на серверах Telegram. Пользователь отправил боту сообщение - апдейт, пользователь нажал на инлайн-кнопку - апдейт,
# пользователь отправил боту стикер - тоже апдейт.


# Как можно заметить, информации внутри объекта типа Message намного больше, чем в сыром JSON от Телеграм, но в
# основном, значения всех атрибутов None. Дело в том, что класс Message - универсальный класс, через который можно
# работать с разными апдейтами, поэтому у него там много полей. Если пользователь отправит боту фото - атрибуты будут
# заполнены немного иначе.
#
# Соответственно, обращаясь к атрибутам объектов - можно получать всю необходимую информацию об апдейтах. Этим мы
# будем очень часто пользоваться при написании ботов.
#
# Иногда апдейт удобно анализировать в JSON-формате. Для этого у объекта типа Message как раз есть метод json(). То
# есть, если вызвать этот метод - можно посмотреть на объект в виде json.



# Методу json, который есть у объекта типа Message можно передать некоторые дополнительные параметры. Например:
#
# indent: int  - задает отступы для JSON.
# exclude_none: bool  - если True, пропускает всё равное None.
# И тогда, например, команда print(message.json(indent=4, exclude_none=True)) выведет прямо в терминал объект типа
# Message с командой /start вот в таком, удобном для анализа, виде:
#
# {
#     "message_id": 6201,
#     "date": 1675449934,
#     "chat": {
#         "id": 173901673,
#         "type": "private",
#         "username": "kmsint",
#         "first_name": "Mikhail",
#         "last_name": "Kryzhanovskiy"
#     },
#     "from_user": {
#         "id": 173901673,
#         "is_bot": false,
#         "first_name": "Mikhail",
#         "last_name": "Kryzhanovskiy",
#         "username": "kmsint",
#         "language_code": "ru"
#     },
#     "text": "/start",
#     "entities": [
#         {
#             "type": "bot_command",
#             "offset": 0,
#             "length": 6
#         }
#     ]
# }


# Так, например, если мы хотим, чтобы хэндлер срабатывал именно на голосовое сообщение - надо об этом прямо попросить
# через указание типа контента в фильтре.
#
from aiogram import F
from aiogram.types import Message
#
# # ...
#
# # Навешиваем декоратор с указанием в качестве фильтра типа контента
@dp.message(F.voice)
async def process_sent_voice(message: Message):
    # Выводим апдейт в терминал
    print(message)
    # Отправляем сообщение в чат, откуда пришло голосовое
    await message.answer(text='Вы прислали голосовое сообщение!')



# Бывает так, что мы не знаем какого типа апдейт к нам должен прийти, но мы все равно хотим его поймать хэндлером и
# посмотреть как он выглядит. Тогда в качестве фильтра можно ничего не указывать.
#
# # ...
#
# # Навешиваем декоратор без фильтров, чтобы ловить любой тип апдейтов
# @dp.message()
# async def process_any_update(message: Message):
#     # Выводим апдейт в терминал
#     print(message)
#     # Отправляем сообщение в чат, откуда пришел апдейт
#     await message.answer(text='Вы что-то прислали')
# Примечание. Существует еще один способ ловить и анализировать апдейты с помощью aiogram. Даже не доводя их до
# хэндлеров. С помощью так называемого middleware. Но подробно об этом мы будем говорить в соответствующем разделе.