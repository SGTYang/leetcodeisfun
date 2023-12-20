# Write your MySQL query statement below
select v.visited_on, sum(c.amount) as amount, round(sum(c.amount)/7, 2) as average_amount
from Customer as c, (select distinct(visited_on) from Customer) as v
where datediff(v.visited_on, c.visited_on) >= 0 and datediff(v.visited_on, c.visited_on) <= 6
group by v.visited_on having count(distinct(c.visited_on)) = 7
order by v.visited_on asc