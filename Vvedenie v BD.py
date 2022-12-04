# ====================================1.1 Термины и определения=========================================================

# Что такое кортеж в терминологии баз данных?
# строка в таблице, набор значений атрибутов


# Что не является характеристикой реляционных СУБД?
# простота представления любой предметной области в виде набора таблиц


# Где применяются базы данных?
# - В банковских системах
# - В веб-сервисах
# - В мобильных приложениях
# - В электронных библиотеках


# ----------------------------------------------------------------------------------------------------------------------
# База данных платежной системы `billing_simple` состоит из одной таблицы `billing` следующей структуры:
#
# CREATE TABLE IF NOT EXISTS `billing_simple`.`billing` (
#   `payer_email` VARCHAR(255) NULL,
#   `recipient_email` VARCHAR(255) NULL,
#   `sum` DECIMAL(18,2) NULL,
#   `currency` VARCHAR(3) NULL,
#   `billing_date` DATE NULL,
#   `comment` TEXT NULL)
# ENGINE = InnoDB;
# Задание
# Выведите поступления денег от пользователя с email 'vasya@mail.com'.
# В результат включите все столбцы таблицы и не меняйте порядка их вывода. Если, конечно, хотите успешно пройти
# проверку результата запроса )

use billing_simple;

SELECT * FROM billing
WHERE payer_email = 'vasya@mail.com';

# ----------------------------------------------------------------------------------------------------------------------

# Добавьте в таблицу одну запись о платеже со следующими значениями:
# email плательщика: 'pasha@mail.com'
# email получателя: 'katya@mail.com'
# сумма: 300.00
# валюта: 'EUR'
# дата операции: 14.02.2016
# комментарий: 'Valentines day present)'

INSERT INTO billing (
payer_email, recipient_email, sum, currency, billing_date, comment)
VALUES (
'pasha@mail.com',
'katya@mail.com',
300.00,
'EUR',
'2016-02-14',
'Valentines day present)');

# ----------------------------------------------------------------------------------------------------------------------

# Измените адрес плательщика на 'igor@mail.com' для всех записей таблицы, где адрес плательщика 'alex@mail.com'.

UPDATE billing SET payer_email='igor@mail.com'
	WHERE payer_email='alex@mail.com'

# ----------------------------------------------------------------------------------------------------------------------

# Удалите из таблицы записи, где адрес плательщика или адрес получателя установлен в неопределенное значение или
# пустую строку.

DELETE FROM billing
WHERE payer_email is NULL
OR recipient_email is null
OR payer_email = ''
OR recipient_email = '';

# ----------------------------------------------------------------------------------------------------------------------

# Узнать общую выручку по каждому товару

USE store_simple;

SELECT * from store;

SELECT sum(price * sold_num) as general, product_name from store
GROUP BY product_name
order by general DESC;


# Узнать общую выручку магазина (итог = 397709.00)

USE store_simple;

SELECT * from store;

SELECT sum(price * sold_num) as general from store
order by general DESC;


# Задание
# Выведите общее количество заказов компании.
USE project_simple;

select COUNT(1) from project;


# ЗАДАНИЕ
# База данных магазина `store_simple` состоит из одной таблицы `store` следующей структуры:
#
# CREATE TABLE IF NOT EXISTS `store_simple`.`store` (
#   `product_name` VARCHAR(255) NULL,
#   `category` VARCHAR(255) NULL,
#   `price` DECIMAL(18,2) NULL,
#   `sold_num` INT NULL)
# ENGINE = InnoDB;
#
# Задание
# Выведите количество товаров в каждой категории. Результат должен содержать два столбца:
# название категории,
# количество товаров в данной категории.

select category, Count(1) from store
GROUP BY category;

# Query result:
# +-------------------+----------+
# | category          | Count(1) |
# +-------------------+----------+
# | Snacks            | 13       |
# | Air Fresheners    | 17       |
# | Cakes             | 12       |
# | Juices            | 6        |
# | Tea & Coffee      | 16       |
# | Health & Medicine | 11       |
# | Bath Products     | 4        |
# | Water             | 11       |
# | Dental Care       | 3        |
# | Candy             | 7        |
# +-------------------+----------+
# Affected rows: 10


# TASK
# База данных магазина `store_simple` состоит из одной таблицы `store` следующей структуры:
#
# CREATE TABLE IF NOT EXISTS `store_simple`.`store` (
#   `product_name` VARCHAR(255) NULL,
#   `category` VARCHAR(255) NULL,
#   `price` DECIMAL(18,2) NULL,
#   `sold_num` INT NULL)
# ENGINE = InnoDB;
#
# Задание
# Выведите 5 категорий товаров, продажи которых принесли наибольшую выручку. Под выручкой понимается сумма произведений стоимости товара на количество проданных единиц. Результат должен содержать два столбца:
# название категории,
# выручка от продажи товаров в данной категории.

USE store_simple;

select category, sum(sold_num * price) as summa from store
GROUP BY category
ORDER BY summa desc
LIMIT 5;

# Query result:
# +----------------+----------+
# | category       | summa    |
# +----------------+----------+
# | Air Fresheners | 67816.00 |
# | Snacks         | 59991.00 |
# | Cakes          | 54172.00 |
# | Water          | 53860.00 |
# | Tea & Coffee   | 52868.00 |
# +----------------+----------+
# Affected rows: 5



# TASK
# База данных учета проектов `project_simple` состоит из одной таблицы `project` следующей структуры:
#
#
#
# CREATE TABLE IF NOT EXISTS `project_simple`.`project` (
#   `project_name` VARCHAR(255) NULL,
#   `client_name` VARCHAR(255) NULL,
#   `project_start` DATE NULL,
#   `project_finish` DATE NULL,
#   `budget` DECIMAL(18,2) NULL)
# ENGINE = InnoDB;
#
# Задание
# Выведите в качестве результата одного запроса общее количество заказов, сумму стоимостей (бюджетов) всех проектов,
# средний срок исполнения заказа в днях.
#
# NB! Для вычисления длительности проекта удобно использовать встроенную функцию datediff().

USE project_simple;

select
	COUNT(1) as 'Кол-во заказов',
	sum(budget) as 'Общая сумма, руб.',
	avg(datediff(project_finish, project_start)) as 'Среднее время выполнения'
from
	project;
where
	project_finish is not null
	and
	project_start is not null
# Query result:
# +----------------+---------------+--------------+
# | kol_vo_zakazov | general_price | Sredniy_srok |
# +----------------+---------------+--------------+
# | 100            | 50746251.00   | 171.9300     |
# +----------------+---------------+--------------+
# Affected rows: 1


