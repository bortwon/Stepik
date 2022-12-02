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
# ==========================================================
# 9.3
# ----------------------------------------------------------
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

# ---------------------------------------------------------------

