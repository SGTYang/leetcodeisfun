# # Write your MySQL query statement below
select w2.id
from Weather as w1 join Weather as w2
where w1.temperature < w2.temperature and datediff(w2.recordDate, w1.recordDate) = 1