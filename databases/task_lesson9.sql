-- Практическое задание по теме “Транзакции, переменные, представления”

-- Задание 1 В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
-- Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.

start transaction;
insert into sample.users (name, birthday_at)
select name, birthday_at from shop.users where id = 1;
commit;

-- Задание 2. Создайте представление, которое выводит название name товарной позиции из таблицы products 
-- и соответствующее название каталога name из таблицы catalogs.

create view tbl (name_products, name_catalogs)
as 
select name,
  (select name from catalogs where id = catalog_id) as name_catalogs 
from products;


-- Практическое задание по теме “Хранимые процедуры и функции, триггеры"

-- Задание 1. Создайте хранимую функцию hello(), которая будет возвращать приветствие, 
-- в зависимости от текущего времени суток. С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", 
-- с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".

drop function if exists hello;
create function hello()
returns varchar(255) deterministic 
begin
	if (current_time() between '06:00:00' and '11:59:59') then
	return 'Доброе утро';
	end if;
    if (current_time() between '12:00:00' and '17:59:59') then
	return 'Добрый день';
	end if;
	if (current_time() between '18:00:00' and '23:59:59') then
	return 'Добрый вечер';
	end if;
	if (current_time() between '00:00:00' and '05:59:59') then
	return 'Доброй ночи';
	end if;
end;

-- Задание 2. В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
-- Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
-- Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
-- При попытке присвоить полям NULL-значение необходимо отменить операцию.

create trigger products_insert before insert on products
for each row begin 
  if new.name is null and new.description is null then
	signal sqlstate '45000' set MESSAGE_TEXT = 'Значения полей name и description не могут быть неопределенными одновременно';
  end if;
end 

create trigger products_update before update on products
for each row begin 
  if new.name is null and new.description is null then
	signal sqlstate '45000' set MESSAGE_TEXT = 'Значения полей name и description не могут быть неопределенными одновременно';
  end if;
end 









