# Write your MySQL query statement below
select s.product_id, s.year as first_year, s.quantity, s.price
from Sales as s left join Product as p on s.product_id = p.product_id
where (s.product_id, s.year) in (select product_id, min(year) from Sales group by product_id);