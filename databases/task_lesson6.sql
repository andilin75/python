

-- Задание 1. Проанализировать запросы, которые выполнялись на занятии, определить возможные корректировки и/или улучшения 
-- (JOIN пока не применять).

-- Считаем количество друзей пользователя id = 1 без использования union

use vk1;

select count(*) from 
(select initiator_user_id, target_user_id from friend_requests where (initiator_user_id = 1 or target_user_id =1)
and status = 'approved') as friends;


-- Задание 2. Пусть задан некоторый пользователь. 
-- Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.

-- Для пользователя id = 749:

use vk;

select count(from_profile_id) as count_message, from_profile_id from messages 
where to_profile_id = 749
and from_profile_id 
in (
select initiator_profile_id from friend_requests where target_profile_id = 749 and status = 'approved'
union
select target_profile_id from friend_requests where initiator_profile_id = 749 and status = 'approved'
)
group by from_profile_id order by count_message desc;


-- Задание 3. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей
 
select count(*) from 
(select id from profiles order by birthday desc limit 10) as youngest, 
profiles_likes where id = profile_id

-- Задание 4. Определить кто больше поставил лайков (всего) - мужчины или женщины?

select count(*) as total,
	(select gender from profiles where id = profiles_likes.initiator_profile_id) as gender
from profiles_likes group by gender;
	
-- Задание 5. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети

select id, concat(name, ' ',surname) as profile,
	(select count(*) from comments where profile_id = profiles.id) as comments,	
	(select count(*) from friend_requests where initiator_profile_id = profiles.id) as friend_requests,
	(select count(*) from friend_requests where target_profile_id = profiles.id and status in ('approved', 'declined')) as response,
	(select count(*) from messages where from_profile_id = profiles.id) as messages,
	(select count(*) from posts where profile_id = profiles.id) as posts,
	(select count(*) from profiles_likes where initiator_profile_id = profiles.id) as likes,
	(select (comments + friend_requests + response + messages + posts + likes)) as total,
	created_at
from profiles group by id order by total, created_at limit 10; 




