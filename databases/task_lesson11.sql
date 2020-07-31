-- Практическое задание по теме “Оптимизация запросов”
-- Задание 1. Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, 
-- catalogs и products в таблицу logs помещается время и дата создания записи, название таблицы, идентификатор первичного ключа 
-- и содержимое поля name.

use shop;
drop table if exists `logs`;
CREATE TABLE if not exists `logs` (
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `table_name` varchar(255) not null,
  `table_id` int not NULL,
  `name` varchar(255) not null
) ENGINE=ARCHIVE;

delimiter //
create trigger user_insert after insert on users
for each row begin 
	insert into `logs` select new.created_at, 'users', new.id, new.name from users limit 1;
end //

create trigger catalog_insert after insert on catalogs
for each row begin
	declare created_at datetime DEFAULT CURRENT_TIMESTAMP;
	insert into `logs` select created_at, 'catalogs', new.id, new.name from catalogs limit 1;
end // 

create trigger product_insert after insert on products
for each row begin
	insert into `logs` select new.created_at, 'products', new.id, new.name from products limit 1;
end // 
delimiter ;

-- Практическое задание по теме “NoSQL”
-- Задание1. В базе данных Redis подберите коллекцию для подсчета посещений с определенных IP-адресов.

127.0.0.1:6379> sadd 10.35.108.151 '2020-07-30 09:43:24' '2020-07-30 08:43:58'
(integer) 2
127.0.0.1:6379> smembers 10.35.108.151
1) "2020-07-30 09:43:24"
2) "2020-07-30 08:43:58"
127.0.0.1:6379> scard 10.35.108.151
(integer) 2

-- Задание 2. При помощи базы данных Redis решите задачу поиска имени пользователя по электронному адресу и наоборот, 
-- поиск электронного адреса пользователя по его имени.

-- электронные адреса храним в формате имя_пользователя:электронный_адрес
127.0.0.1:6379> sadd email andrey:aand@.ru tanya:tat@.com vova:vv@.net
(integer) 3
-- ищем пользователя по электронному адресу tat@.com
127.0.0.1:6379> sscan email 0 match *:tat@.com
1) "0"
2) 1) "tanya:tat@.com"
-- ищем электронный адрес пользователя vova
127.0.0.1:6379> sscan email 0 match vova:*
1) "0"
2) 1) "vova:vv@.net""

-- Задание 3. Организуйте хранение категорий и товарных позиций учебной базы данных shop в СУБД MongoDB.

> use shop
switched to db shop


> db.shop.insertMany ([
... {
... "name" : "Intel Core i3-8100",
... "description" : "Процессор для настольных персональных компьютеров, основанных на платформе Intel.",
... "price" : 7890.00,
... "catalog_id" : "Процессоры",
... "created_at" : "2020-07-28 16:59:12",
... "updated_at" : "2020-07-28 16:59:12"
... },
... {
... "name" : "Intel Core i5-7400",
... "description" : "Процессор для настольных персональных компьютеров, основанных на платформе Intel.",
... "price" : 12700.00,
... "catalog_id" : "Процессоры",
... "created_at" : "2020-07-28 16:59:12",
... "updated_at" : "2020-07-28 16:59:12"
... },
... {
... "name" : "AMD FX-8320E",
... "description" : "Процессор для настольных персональных компьютеров, основанных на платформе AMD.",
... "price" : 4780.00,
... "catalog_id" : "Процессоры",
... "created_at" : "2020-07-28 16:59:12",
... "updated_at" : "2020-07-28 16:59:12"
... },
... {
... "name" : "AMD FX-8320",
... "description" : "Процессор для настольных персональных компьютеров, основанных на платформе AMD.",
... "price" : 7120.00,
... "catalog_id" : "Процессоры",
... "created_at" : "2020-07-28 16:59:12",
... "updated_at" : "2020-07-28 16:59:12"
... },
... {
... "name" : "ASUS ROG MAXIMUS X HERO",
... "description" : "Материнская плата ASUS ROG MAXIMUS X HERO, Z370, Socket 1151-V2, DDR4, ATX",
... "price" : 19310.00,
... "catalog_id" : "Материнские платы",
... "created_at" : "2020-07-28 16:59:12",
... "updated_at" : "2020-07-28 16:59:12"
... },
... {
... "name" : "Gigabyte H310M S2H",
... "description" : "Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX",
... "price" : 4790.00,
... "catalog_id" : "Материнские платы",
... "created_at" : "2020-07-28 16:59:12",
... "updated_at" : "2020-07-28 16:59:12"
... },
... {
... "name" : "MSI B250M GAMING PRO",
... "description" : "Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX",
... "price" : 5060.00,
... "catalog_id" : "Материнские платы",
... "created_at" : "2020-07-28 16:59:12",
... "updated_at" : "2020-07-28 16:59:12"
... }
... ])
{
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("5f23dd2c021e2aa0f48403b0"),
                ObjectId("5f23dd2c021e2aa0f48403b1"),
                ObjectId("5f23dd2c021e2aa0f48403b2"),
                ObjectId("5f23dd2c021e2aa0f48403b3"),
                ObjectId("5f23dd2c021e2aa0f48403b4"),
                ObjectId("5f23dd2c021e2aa0f48403b5"),
                ObjectId("5f23dd2c021e2aa0f48403b6")
        ]
}


> db.shop.insertMany ((catalogs = [
... {
... "name" : "Процессоры"
... },
... {
... "name" : "Материнские платы"
... },
... {
... "name" : "Видеокарты"
... },
... {
... "name" : "Жесткие диски"
... },
... {
... "name" : "Оперативная память"
... }
... ]))
{
        "acknowledged" : true,
        "insertedIds" : [
                ObjectId("5f23dfde021e2aa0f48403b7"),
                ObjectId("5f23dfde021e2aa0f48403b8"),
                ObjectId("5f23dfde021e2aa0f48403b9"),
                ObjectId("5f23dfde021e2aa0f48403ba"),
                ObjectId("5f23dfde021e2aa0f48403bb")
        ]
}
> db.shop.find().pretty()
{
        "_id" : ObjectId("5f23dd2c021e2aa0f48403b0"),
        "name" : "Intel Core i3-8100",
        "description" : "Процессор для настольных персональных компьютеров, основанных на платформе Intel.",
        "price" : 7890,
        "catalog_id" : "Процессоры",
        "created_at" : "2020-07-28 16:59:12",
        "updated_at" : "2020-07-28 16:59:12"
}
{
        "_id" : ObjectId("5f23dd2c021e2aa0f48403b1"),
        "name" : "Intel Core i5-7400",
        "description" : "Процессор для настольных персональных компьютеров, основанных на платформе Intel.",
        "price" : 12700,
        "catalog_id" : "Процессоры",
        "created_at" : "2020-07-28 16:59:12",
        "updated_at" : "2020-07-28 16:59:12"
}
{
        "_id" : ObjectId("5f23dd2c021e2aa0f48403b2"),
        "name" : "AMD FX-8320E",
        "description" : "Процессор для настольных персональных компьютеров, основанных на платформе AMD.",
        "price" : 4780,
        "catalog_id" : "Процессоры",
        "created_at" : "2020-07-28 16:59:12",
        "updated_at" : "2020-07-28 16:59:12"
}
{
        "_id" : ObjectId("5f23dd2c021e2aa0f48403b3"),
        "name" : "AMD FX-8320",
        "description" : "Процессор для настольных персональных компьютеров, основанных на платформе AMD.",
        "price" : 7120,
        "catalog_id" : "Процессоры",
        "created_at" : "2020-07-28 16:59:12",
        "updated_at" : "2020-07-28 16:59:12"
}
{
        "_id" : ObjectId("5f23dd2c021e2aa0f48403b4"),
        "name" : "ASUS ROG MAXIMUS X HERO",
        "description" : "Материнская плата ASUS ROG MAXIMUS X HERO, Z370, Socket 1151-V2, DDR4, ATX",
        "price" : 19310,
        "catalog_id" : "Материнские платы",
        "created_at" : "2020-07-28 16:59:12",
        "updated_at" : "2020-07-28 16:59:12"
}
{
        "_id" : ObjectId("5f23dd2c021e2aa0f48403b5"),
        "name" : "Gigabyte H310M S2H",
        "description" : "Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX",
        "price" : 4790,
        "catalog_id" : "Материнские платы",
        "created_at" : "2020-07-28 16:59:12",
        "updated_at" : "2020-07-28 16:59:12"
}
{
        "_id" : ObjectId("5f23dd2c021e2aa0f48403b6"),
        "name" : "MSI B250M GAMING PRO",
        "description" : "Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX",
        "price" : 5060,
        "catalog_id" : "Материнские платы",
        "created_at" : "2020-07-28 16:59:12",
        "updated_at" : "2020-07-28 16:59:12"
}
{ "_id" : ObjectId("5f23dfde021e2aa0f48403b7"), "name" : "Процессоры" }
{
        "_id" : ObjectId("5f23dfde021e2aa0f48403b8"),
        "name" : "Материнские платы"
}
{ "_id" : ObjectId("5f23dfde021e2aa0f48403b9"), "name" : "Видеокарты" }
{ "_id" : ObjectId("5f23dfde021e2aa0f48403ba"), "name" : "Жесткие диски" }
{
        "_id" : ObjectId("5f23dfde021e2aa0f48403bb"),
        "name" : "Оперативная память"
}



