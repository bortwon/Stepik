# =============== 1. Обработка web-страниц ====================

# ------------ 1.1 Скачивание web-страниц ---------------------

# ---------- Task 1 ---------------------
# Мы сохранили страницу с википедии про языки программирования и сохранили по
# адресу https://stepik.org/media/attachments/lesson/209717/1.html
#
# Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или C++ (ответ
# должен быть одной из этих двух строк).


from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
text = str(html)
py = int(html.count('Python'))
c = int(html.count('C++'))
if py > c:
    print('Python')
else:
    print('C++')


# -------------------------------------------


# ----------------- 1.2 Обработка html как текста --------------------

# ------------ Task 1 -------------------
# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python. В этой
# статье есть теги code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки, содержащиеся
# между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в алфавитном
# порядке, разделяя пробелами.
#
# Например, если исходный текст страницы выглядел бы так:
#
# <code>a</code>
# <a>bracadabr</a>
# <code>c</code>
# <code>b</code>
# <code>b</code>
# <code>c</code>

# то в ответ надо было бы ввести строку "b c".


from collections import Counter
from re import findall
from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
text = str(html)
regex = '<code>(.*?)</code>'
l = sorted(findall(regex, text))
l = Counter(l).most_common()
res = list(filter(lambda x: x[1] == l[0][1], l))
res = list(map(lambda x: x[0], res))
print(' '.join(res))

# ---------------------------------------