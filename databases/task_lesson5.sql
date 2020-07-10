-- Практическое задание по теме «Операторы, фильтрация, сортировка и ограничение»

-- Задание 1. Пусть в таблице users поля created_at и updated_at оказались незаполненными. 
-- Заполните их текущими датой и временем.

update users 
set
	created_at = CURRENT_TIMESTAMP
where created_at is null;

update users 
set
	updated_at = CURRENT_TIMESTAMP
where updated_at is null;

-- Задание 2. Таблица users была неудачно спроектирована. 
-- Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате 20.10.2017 8:10. 
-- Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.

ALTER TABLE users MODIFY COLUMN created_at DATETIME NULL;
ALTER TABLE users MODIFY COLUMN updated_at DATETIME NULL;

-- Задание 3. В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, 
-- если товар закончился и выше нуля, если на складе имеются запасы. 
-- Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. 
-- Однако нулевые запасы должны выводиться в конце, после всех 

select * from storehouses_products  order by value=0 asc, value asc;

-- Практическое задание теме «Агрегация данных»

-- Задание 1. Подсчитайте средний возраст пользователей в таблице users.

select sum((TO_DAYS(NOW()) - TO_DAYS(birthday_at))/365.25) / count(*)  from users;

-- Задание 2. Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
-- Следует учесть, что необходимы дни недели текущего года, а не года рождения.

SELECT count(day_week) 
  FROM
    (SELECT 
    	dayname(concat(year(curdate()),'-',date_format(birthday_at, '%m-%d'))) as day_week from users) 
  as birthday_count group by day_week;

-- Подсчитать получилось, но вывести еще и названия дней недели одним выражением без создания дпополнительной таблицы - нет.










