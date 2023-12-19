# # Write your MySQL query statement below
# select w1.id
# from Weather w1 join Weather w2 on datediff(w1.recordDate, w2.recordDate) = 1
# where w1.temperature > w2.temperature;

select w1.id
from Weather w1 join Weather w2 on to_days(w1.recordDate) - to_days(w2.recorddate) = 1
where w1.temperature > w2.temperature;