# Угадайка чисел
# Описание проекта: программа генерирует случайное число в диапазоне от 11 до 100100 и просит пользователя угадать
# это число.

# Если догадка пользователя больше случайного числа, то программа должна
# вывести сообщение 'Слишком много, попробуйте еще раз'.

# Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.

# Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
#
# Составляющие проекта:
#
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл while;
# Бесконечный цикл;
# Операторы break, continue;
# Работа с модулем random для генерации случайных чисел.

import random

random_num = random.randint(1, 100)


def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


def quess_number():
    print('Добро пожаловать в числовую угадайку')
    counter = 0
    while True:
        user_num = input()
        if is_valid(num=user_num):
            user_num = int(user_num)
            if user_num < random_num:
                print('Слишком мало, попробуйте еще раз')
                counter += 1
            elif user_num > random_num:
                print('Слишком много, попробуйте еще раз')
                counter += 1
            else:
                print('Вы угадали, поздравляем!')
                counter += 1
                print('Количество проделанных попыток:', counter)
                return 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            counter += 1








# ШАР СУДЬБЫ

from random import *


def ball_of_destiny():

    answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено',
               'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы',
               'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да',
               'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да',
               'Сконцентрируйся и спроси опять', 'Весьма сомнительно']


    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

    name_user = input('Как Вас зовут?:\n')

    print('Приветствую тебя,', name_user)

    while True:
        input('Ты пришел ко мне с вопросом, ибо будущее твое туманно. Задай же вопрос и получишь ответ:\n')
        print(choice(answers))

        while True:
            result = input('Хотите еще узнать о Вашем загадочном будущем?\nВведите: Да или Нет\n')
            if result.lower() == 'да':
                break
            elif result.lower() == 'нет':
                print('Возвращайся в мой отдел по раскрытию загадок судьбы. Я всегда буду рад видеть тебя,', name_user)
                break
            elif result.lower() != 'да' or result.lower() != 'нет':
                print('Определись уже наконец, ведь каждая секунда '
                      'промедления отдаляет тебя от постижения истинности бытия!\n')
        if result.lower() == 'нет':
            break


# ball_of_destiny()




# ГЕНЕРАТОР ПАРОЛЕЙ

def gener_password():

    digits = '23456789'
    lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
    punctuation = '#$%&*+-=?@^_.'
    similar = 'il1Lo0O'

    while True:
        chars = ''
        res = ''
        qua_passw = int(input('Введите количество паролей, которые нужно сгенерировать:\n'))
        length_passw = int(input('Введите желаемую длину пароля(-ей):\n'))
        while True:
            want_digits = input('Включать ли цифры в пароль?\nВведите Да или Нет:\n')
            if want_digits.lower() == 'да':
                chars += digits
                break
            elif want_digits.lower() == 'нет':
                break
            else:
                print('Я Вас не понимаю. ВВЕДИТЕ ДА ИЛИ НЕТ!')
        while True:
            want_lower_letters = input('Включать ли строчные буквы в пароль?\nВведите Да или Нет:\n')
            if want_lower_letters.lower() == 'да':
                chars += lowercase_letters
                break
            elif want_lower_letters.lower() == 'нет':
                break
            else:
                print('Я Вас не понимаю. ВВЕДИТЕ ДА ИЛИ НЕТ!')
        while True:
            want_upper_letters = input('Включать ли прописные буквы в пароль?\nВведите Да или Нет:\n')
            if want_upper_letters.lower() == 'да':
                chars += uppercase_letters
                break
            elif want_upper_letters.lower() == 'нет':
                break
            else:
                print('Я Вас не понимаю. ВВЕДИТЕ ДА ИЛИ НЕТ!')
        while True:
            want_symbols = input('Включать ли специальные символы в пароль?\nВведите Да или Нет:\n')
            if want_symbols.lower() == 'да':
                chars += punctuation
                break
            elif want_symbols.lower() == 'нет':
                break
            else:
                print('Я Вас не понимаю. ВВЕДИТЕ ДА ИЛИ НЕТ!')
        while True:
            want_similar = input('Включать ли неоднозначные символы в пароль?\nВведите Да или Нет:\n')
            if want_similar.lower() == 'да':
                chars += similar
                break
            elif want_similar.lower() == 'нет':
                break
            else:
                print('Я Вас не понимаю. ВВЕДИТЕ ДА ИЛИ НЕТ!')

        for i in range(qua_passw):
            res = ''
            for j in range(length_passw):
                res += choice(chars)
            print(res)

        while True:
            finish_check = input('Хотите ли Вы подобрать новые пароли?\nВведите Да или Нет:\n')
            if finish_check.lower() == 'да':
                break
            elif finish_check.lower() == 'нет':
                print('Ваш аккаунт теперь в безопасности!')
                break
            elif finish_check.lower() != 'да' and finish_check.lower() != 'нет':
                print('Я Вас не понимаю. ВВЕДИТЕ ДА ИЛИ НЕТ!')
                continue
        if finish_check.lower() == 'нет':
            break


# gener_password()




# ШИФР ЦЕЗАРЯ
import time
import random

what_purpose = input('Что нужно сделать: шифровать или дешифровать?\n').lower()
while what_purpose != 'шифровать' and what_purpose != 'дешифровать':
    what_purpose = input('Вы не ввели цель задачи! Выберите: шифровать или дешифровать.\n')

what_lang = input('Какой нужен язык: русский или английский?\n').lower()
while what_lang != 'русский' and what_lang != 'английский':
    what_lang = input('Вы не ввели язык! Выберите: русский или английский.\n')

what_step = input('Какой нужен шаг?\n')
while what_step.isdigit() != True:
    what_step = input('Ввод неверный! Введите число:\n')

what_text = input('Введите необходимый текст:\n')
while what_text.isspace() == True:
    what_text = input('Ввод неверный! Введите текст:\n')


def cezar(purpose, lang, step, text):

    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    if purpose == 'шифровать':
        res = ''
        if lang == 'русский':
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i].islower():
                        res += lower_rus_alphabet[(lower_rus_alphabet.index(text[i]) + int(step)) % len(lower_rus_alphabet)]
                    else:
                        res += upper_rus_alphabet[(upper_rus_alphabet.index(text[i]) + int(step)) % len(upper_rus_alphabet)]
                else:
                    res += text[i]
        elif lang == 'английский':
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i].islower():
                        res += lower_eng_alphabet[(lower_eng_alphabet.index(text[i]) + int(step)) % len(lower_eng_alphabet)]
                    else:
                        res += upper_eng_alphabet[(upper_eng_alphabet.index(text[i]) + int(step)) % len(upper_eng_alphabet)]
                else:
                    res += text[i]
        print('Пусть все тайное станет явным... AVA\nЗашифрованный текст:', res)
    elif purpose == 'дешифровать':
        res = ''
        if lang == 'русский':
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i].islower():
                        res += lower_rus_alphabet[(lower_rus_alphabet.index(text[i]) - int(step)) % len(lower_rus_alphabet)]
                    else:
                        res += upper_rus_alphabet[(upper_rus_alphabet.index(text[i]) - int(step)) % len(upper_rus_alphabet)]
                else:
                    res += text[i]
        elif lang == 'английский':
            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i].islower():
                        res += lower_eng_alphabet[(lower_eng_alphabet.index(text[i]) - int(step)) % len(lower_eng_alphabet)]
                    else:
                        res += upper_eng_alphabet[(upper_eng_alphabet.index(text[i]) - int(step)) % len(upper_eng_alphabet)]
                else:
                    res += text[i]
        print('Пусть все тайное станет явным... AVA\nДешифрованный текст:', res)
    print('Прощай....AVA')


cezar(purpose=what_purpose, lang=what_lang, step=what_step, text=what_text)




# СИСТЕМЫ СЧИСЛЕНИЯ

# Из 2-ной в 10
n = str(111111)
n = n[::-1]
res = 0
for i in range(len(n)):
    res += int(n[i]) * 2 ** int(i)

# print(res)


# Из 16 в 10:
n = '1AF2'
n = n[::-1]
res = 0

for i in range(len(n)):
    if n[i] == 'A':
        res += 10 * 16 ** i
    elif n[i] == 'F':
        res += 15 * 16 ** i
    else:
        res += int(n[i]) * 16 ** i

# print(res)

# или
# print(int(n, 16))



# В саду 88n фруктовых деревьев, из них 32n яблони, 22n груши, 16n слив и 17n вишен. В какой системе
# счисления посчитаны деревья?
#
# Примечание. Переведите числа из nn-ой системы счисления в десятичную и составьте уравнение.

for n in range(8, 16):
    if 8 * n + 8 == (3 * n + 2) + (2 * n + 2) + (n + 6) + (n + 7):
        print(n)



# Переведите десятичное число 1000 в шестнадцатеричную систему счисления.
print(hex(1000).split('x')[-1])


# Переведите десятичное число 513 в двоичную систему счисления.
print(bin(513))



# Курс Сергея Балакирева Добрый Добрый Пайтон
# ======================================================================================================================
# 9.3
# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 4. На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# True

# ввод строки (переменную s не менять)
s = input()
s_lst = [x.split('=') for x in s.split()]

# здесь продолжайте программу
tp = tuple({key: value for key, value in s_lst}.items())

# ----------------------------------------------------------------------------------------------------------------------

# Подвиг 5. (Для учебных целей). Вводится строка. Необходимо в ней заменить кириллические символы на
# соответствующие латинские обозначения (без учета регистра букв), а все остальные символы - на символ дефиса (-).
# Для этого в программе определен словарь (см. листинг). Используя его, запишите функцию map, которая бы выдавала
# преобразованные фрагменты для входной строки. На основе этой функции сформируйте строку, состоящую из
# преобразованных фрагментов (фрагменты в строке должны идти друг за другом без пробелов). Отобразите
# результат на экране.
#
# Sample Input:
# Привет Питон

# Sample Output:
# privet-piton

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу
s = input()

print(''.join(map(lambda x: t[x] if x in t.keys() else '-', s.lower())))

# ----------------------------------------------------------------------------------------------------------------------

# Подвиг 6. Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map,
# которая бы возвращала названия городов только длиной более 5 символов. Вместо остальных названий - строку
# с дефисом ("-"). Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.
#
# Sample Input:
# Москва Уфа Вологда Тула Владивосток Хабаровск

# Sample Output:
# Москва - Вологда - Владивосток Хабаровск

print(' '.join(map(lambda x: x if len(x) > 5 else '-', input().split())))

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================
# 9.4 Функция filter
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------

# Подвиг 1. Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию filter, которая бы
# возвращала только названия длиной более 5 символов. Извлеките первые три полученных значения с помощью функции next
# и отобразите их на экране в одну строчку через пробел. (Полагается, что минимум три значения имеются).
#
# Sample Input:
# Тула Ульяновск Хабаровск Владивосток Омск Уфа

# Sample Output:
# Ульяновск Хабаровск Владивосток

res = filter(lambda x: len(x) > 5, input().split())

for i in range(3):
    print(next(res), end=' ')

# ----------------------------------------------------------------------------------------------------------------------

# Подвиг 2. Вводится список предметов в виде списка:
#
# название_1: вес_1
# ...
# название_N: вес_N
#
# С помощью функции map, необходимо сначала преобразовать этот список строк в кортеж, элементами которого также
# являются кортежи:
#
# (('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))
#
# А, затем, отфильтровать (исключить) все предметы с весом менее 500, используя функцию filter. Вывести на экран
# список оставшихся предметов (только их названия) в одну строчку через пробел.
#
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
#
# Sample Input:
# зонт=1000
# палатка=10000
# спички=22
# котелок=543

# Sample Output:
# зонт палатка котелок

lst_in = ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']
lst_in = [x.split('=') for x in lst_in]
res = tuple({key: val for key, val in lst_in}.items())
res = list(filter(lambda x: int(x[1]) >= 500, res))

print(*[x[0] for x in res], sep=' ')

# ----------------------------------------------------------------------------------------------------------------------

# Подвиг 3. Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
#
# Sample Input:
# 8 11 0 -23 140 1

# Sample Output:
# 11 -23

print(*list(map(int, filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))))

# ----------------------------------------------------------------------------------------------------------------------

# Подвиг 4. Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей коллекции.
# Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел, записанных через
# пробел. Необходимо выделить значения, присутствующие в обоих списках и оставить среди них только четные. Результат
# вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.
#
# При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.
#
# Sample Input:
# 1 5 2 7 10 25 50 100
# 5 2 3 7 10 25 55

# Sample Output:
# 2 10

s, g= set(map(int, input().split())), set(map(int, input().split()))

print(*sorted(list(filter(lambda x: x % 2 == 0, list(s & g)))))

# ----------------------------------------------------------------------------------------------------------------------

# Подвиг 5. Вводится список email-адресов в одну строчку через пробел. Среди них нужно оставить только корректно
# записанные адреса. Будем полагать, что к таким относятся те, что используют латинские буквы, цифры и символ
# подчеркивания. А также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же,
# могут быть и другие символы).
#
# Результат отобразить в виде строки email-адресов, записанных через пробел.
#
# Sample Input:
# abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com

# Sample Output:
# abc@it.ru biba123@list.ru sc_lib@list.ru

import string
def check(mail):
    chars = string.ascii_lowercase + string.digits + '@._'
    check_dogs = mail.split('@')
    if mail.index('@') > mail.index('.'):
        return False
    if len(check_dogs) != 2:
        return False
    for char in mail:
        if char not in chars:
            return False
    else:
        return True

l = input().split()
print(*list(filter(lambda x: check(x), l)))

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================
# 9.5 Функция zip
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 1. Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой.
# При реализации программы используйте функции zip и map. Выведите на экран первые три значения, используя функцию
# next. Значения выводятся в строчку через пробел. (Полагается, что три выходных значения всегда будут присутствовать).
#
# Sample Input:
# -7 8 11 -1 3
# 1 2 3 4 5 6 7 8 9 10

# Sample Output:
# -7 16 33

res = map(lambda x: int(x[0]) * int(x[1]), zip(input().split(), input().split()))

for i in range(3):
    print(next(res), end=' ')

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 2. Вводится неравномерная таблица целых чисел. С помощью функции zip выровнить эту таблицу, приведя ее
# к прямоугольному виду, отбросив выходящие элементы. Вывести результат на экран в виде такой же таблицы чисел.
#
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
#
# Sample Input:
# 1 2 3 4 5 6
# 3 4 5 6
# 7 8 9
# 9 7 5 3 2

# Sample Output:
# 1 2 3
# 3 4 5
# 7 8 9
# 9 7 5

lst_in = [list(map(int, input().split())) for i in range(4)]
res = list(zip(*zip(*lst_in)))
for i in res:
    print(*i, sep=' ')

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 3. Вводится таблица целых чисел. Необходимо сначала эту таблицу представить двумерным списком чисел, а затем,
# с помощью функции zip выполнить транспонирование этой таблицы (то есть, строки заменить на соответствующие столбцы).
# Результат вывести на экран в виде таблицы чисел (числа в строках следуют через пробел).
#
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
#
# Sample Input:
# 1 2 3 4
# 5 6 7 8
# 9 8 7 6

# Sample Output:
# 1 5 9
# 2 6 8
# 3 7 7
# 4 8 6

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
lst_in = [list(map(int, x.split())) for x in lst_in]
res = [list(row) for row in zip(*lst_in)]
for row in res:
    print(*row)

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 4. Вводится строка из слов, записанных через пробел. Необходимо на их основе составить прямоугольную таблицу
# из трех столбцов и N строк (число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить.
# Реализовать эту программу с использованием функции zip. Результат отобразить на экране в виде прямоугольной
# таблицы из слов, записанных через пробел (в каждой строчке).
#
# Sample Input:
# Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь

# Sample Output:
# Москва Уфа Тула
# Самара Омск Воронеж
# Владивосток Лондон Калининград

x = iter(input().split())
for i in list(zip(x, x, x)):
    print(*i)

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 5. Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:
#
# (символ, порядковый индекс)
#
# Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее. То есть, число пар
# может быть 10 и менее. Используя функцию zip сформируйте указанные кортежи и сохраните в список с именем lst.
#
# Программа ничего не должна отображать на экране, только формировать список из кортежей.
#
# Sample Input:
# Python дай мне силы пройти этот курс до конца!

# Sample Output:
# True

# считывание строки в переменную s (эту переменную в программе не менять)
s = input()
# здесь продолжайте программу
lst = list(zip(s, range(10)))

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================
# 9.6. Сортировка с помощью sort и sorted
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 2. На вход поступает список целых чисел, записанных в одну строчку через пробел. Преобразуйте сначала
# эту строку в список из целых чисел, а затем список в кортеж из целых чисел. То есть, в программе будет две разные
# коллекции: список и кортеж. Отсортируйте по возрастанию значений эти коллекции методом sort, если это возможно, а
# иначе - примените функцию sorted.
#
# На экран ничего выводить не нужно, только сформировать две отсортированные коллекции: lst (список) - результат
# сортировки списка; tp_lst (кортеж) - результат сортировки кортежа.
#
# P. S. На результаты сортировок обязательно должны ссылаться переменные с именами lst и tp_lst!
#
# Sample Input:
# -2 -1 8 11 4 5

# Sample Output:
# True

s = input()
lst = list(map(int, s.split()))
lst.sort()
tp_lst = tuple(lst)

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 3.
# На вход функции с именем get_sort поступает словарь, например, такой:
#
# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
#
# Необходимо отсортировать словарь d по убыванию ключей(лексикографическая сортировка строк) и возвратить список из
# соответствующих значений ключей словаря.Например, для указанного словаря d, результатом должен быть список:
#
# ['дерево', 'лошадь', 'собака', 'кот', 'книга']
#
# Сигнатура функции get_sort должна быть следующей:
#
# def get_sort(d): ...
#
# В программе только определить функцию, вызывать ее не нужно и что - либо выводить на экран тоже не нужно.
#
# P.S.Подсказка: список в функции get_sort лучше всего формировать с помощью генератора списков.
#
# Sample Input:

# Sample Output:
# True

def get_sort(d):
    return [i[1] for i in sorted(d.items(), reverse=True)]

d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
print(get_sort(d))

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 4. На вход программы поступает список целых чисел, записанных в одну строчку через пробел.
# Необходимо выбрать из них четыре наибольших уникальных значения. Результат вывести на экран в порядке
# их убывания в одну строчку через пробел.
#
# Sample Input:
# 10 5 4 -3 2 0 5 10 3

# Sample Output:
# 10 5 4 3

s = set(map(int, input().split()))
print(*sorted(s, reverse=True)[:4])

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 5. На вход программы поступают два списка целых чисел (каждый в отдельной строке), записанных в одну строчку
# через пробел. Длины списков могут быть разными. Необходимо первый список отсортировать по возрастанию, а
# второй - по убыванию. Полученные пары из обоих списков сложить друг с другом и получить новый список чисел.
# Результат вывести на экран в виде строки чисел через пробел.
#
# P. S. Подсказка: не забываем про функцию zip.
#
# Sample Input:
# 7 6 4 2 6 7 9 10 4
# -4 5 10 4 5 65

# Sample Output:
# 67 14 9 11 10 3

l1 = list(map(int, input().split()))
l1.sort()
l2 = list(map(int, input().split()))
l2.sort(reverse=True)
print(*list(map(lambda x: x[0] + x[1], zip(l1, l2))))

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 6. На вход программы поступает список товаров в формате:
#
# название_1:цена_1
# ...
# название_N:цена_N
#
# Необходимо преобразовать этот список в словарь, ключами которого выступают цены (целые числа), а
# значениями - соответствующие названия товаров. Необходимо написать функцию, которая бы принимала на
# входе словарь и возвращала список из наименований трех наиболее дешевых товаров.
# Вызовите эту функцию и отобразите на экране полученный список в порядке возрастания цены в одну строчку через пробел.
#
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
#
# Sample Input:
# смартфон:120000
# яблоко:2
# сумка:560
# брюки:2500
# линейка:10
# бумага:500

# Sample Output:
# яблоко линейка бумага
def f(l):
    res = [i.split(':') for i in l]
    d = {int(val): key for key, val in res}
    return [x[1] for x in sorted(d.items())][:3]

l = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
print(*f(l))

# ----------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================
# 9.7 Аргумент key для сортировки по ключу
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 1. На вход программы поступает список наименований рек, записанных в одну строчку через пробел.
# Необходимо отсортировать этот список в порядке убывания длин названий. Результат вывести в одну строчку через пробел.
#
# Sample Input:
# Лена Енисей Волга Дон

# Sample Output:
# Енисей Волга Лена Дон

s = input().split()
print(*sorted(s, key=len, reverse=True))

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 2. На вход программы поступает строка в формате:
#
# предмет_1=вес_1
# ...
# предмет_N=вес_N
#
# Веса предметов заданы целыми числами. Необходимо на основе этих данных сформировать словарь и, затем, на основе
# этого словаря сформировать список предметов по убыванию их веса. (В списке должны находиться только наименования
# предметов без их весов).
#
# Отобразить полученный результат в виде строки с названиями через пробел.
#
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
#
# Sample Input:
# ножницы=100
# котелок=500
# спички=20
# зажигалка=40
# зеркальце=50

# Sample Output:
# котелок ножницы зеркальце зажигалка спички

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
d = {key: int(val) for key, val in [i.split('=') for i in lst_in]}
print(*sorted(d, key=lambda x: d[x], reverse=True))

# ----------------------------------------------------------------------------------------------------------------------
# Подвиг 3. Известно, что порядок нот, следующий: до, ре, ми, фа, соль, ля, си. На вход программы поступает строка
# с набором этих нот, записанных через пробел. Необходимо сформировать список из входной строки с
# нотами, отсортированными указанным образом. Результат вывести в виде строки из нот, записанными через пробел.
#
# Sample Input:
# до фа соль до ре фа ля си

# Sample Output:
# до до ре фа фа соль ля си

l = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
print(*sorted(input().split(), key=lambda x: l.index(x)))

# ----------------------------------------------------------------------------------------------------------------------
# Значимый подвиг 4. Имеется таблица с данными, представленная в формате:
#
# Номер;Имя;Оценка;Зачет
# 1;Иванов;3;Да
# 2;Петров;2;Нет
# ...
# N;Балакирев;4;Да
#
# Эти данные необходимо представить в виде двумерного (вложенного) кортежа. Все числа должны быть представлены
# как целые числа. Затем, отсортировать данные так, чтобы столбцы шли в порядке:
#
# Имя;Зачет;Оценка;Номер
#
# Реализовать эту операцию с помощью сортировки. Результат должен быть представлен также в виде двумерного кортежа
# и присвоен переменной с именем t_sorted.
#
# Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.
#
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
#
# Sample Input:
# Номер;Имя;Оценка;Зачет
# 1;Портос;5;Да
# 2;Арамис;3;Да
# 3;Атос;4;Да
# 4;д'Артаньян;2;Нет
# 5;Балакирев;1;Нет

# Sample Output:
# True

import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
lst_in = list(map(str.strip, sys.stdin.readlines()))
persons = []

for index, person in enumerate(lst_in):
    number, name, mark, credit = person.split(';')
    if index == 0:
        person_data = (name, credit, mark, number)
    else:
        person_data = (name, credit, int(mark), int(number))
    persons.append(person_data)


t_sorted = tuple(persons)

# ----------------------------------------------------------------------------------------------------------------------
