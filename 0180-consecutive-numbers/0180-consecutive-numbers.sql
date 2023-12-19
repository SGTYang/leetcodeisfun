# Write your MySQL query statement below
# select distinct(l1.Num) as ConsecutiveNums
# from Logs l1, Logs l2, Logs l3
# where l1.Id = l2.Id - 1 and l2.Id = l3.Id - 1 and l1.Num = l2.Num and l2.Num = l3.Num;

select distinct(n1) as ConsecutiveNums
from (select num as n1, lead(num, 1) over(order by id) as n2, lag(num, 1) over(order by id) as n0 from Logs) res
where n1=n2 and n1=n0;