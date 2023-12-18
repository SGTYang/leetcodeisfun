# Write your MySQL query statement below
# select s.user_id, Round(avg(case when c.action="confirmed" then 1 else 0 end), 2) as confirmation_rate
# from Signups as s left join Confirmations as c on s.user_id = c.user_id
# group by s.user_id

select s.user_id, case when c.action is NULL then 0 else round((sum(c.action="confirmed")/count(c.action)), 2) end as confirmation_rate
from Signups as s left join Confirmations as c on s.user_id = c.user_id
group by s.user_id;