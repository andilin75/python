-- Задание 1. Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.

select name as 'Имя', count(user_id) as 'Количество заказов' from users, orders where users.id = user_id group by name; 

-- Задание 2. Выведите список товаров products и разделов catalogs, который соответствует товару.

select name as 'Товары',
	(select name from catalogs where id = products.catalog_id) as 'Раздел'
from products;

-- Задание 3. Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
-- Поля from, to и label содержат английские названия городов, поле name — русское. 
-- Выведите список рейсов flights с русскими названиями городов.

select id, 
	(select name from cities where label = flights.from) as 'Откуда',
	(select name from cities where label = flights.to) as 'Куда'
from flights, cities group by id;