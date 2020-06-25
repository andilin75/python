-- Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, 
-- числового id и строкового name.

drop database if exists example;
create database if not exists example;
use example;
drop table if exists users;
create table if not exists users (
	id serial primary key,
    name varchar (255) 
);

insert ignore into users values (default, 'Андрей');

select * from users;










