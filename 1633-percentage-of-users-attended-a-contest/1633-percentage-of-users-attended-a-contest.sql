# Write your MySQL query statement below
select r.contest_id, round(count(u.user_id) / (select count(user_id) from Users) * 100, 2) as percentage
from Register as r
    left join Users as u
    on r.user_id = u.user_id
group by r.contest_id
order by percentage desc, r.contest_id asc