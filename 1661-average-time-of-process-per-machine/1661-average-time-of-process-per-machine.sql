# Write your MySQL query statement below
# SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp), 3) as processing_time
# FROM Activity a1, Activity a2
# WHERE a1.machine_id = a2.machine_id 
# AND a1.process_id = a2.process_id 
# AND a1.activity_type = "start" 
# AND a2.activity_type = "end"
# GROUP BY 1;

select a2.machine_id, round(avg(a2.timestamp - a1.timestamp), 3) as processing_time
from Activity as a1, Activity as a2
where a1.process_id = a2.process_id
and a1.machine_id = a2.machine_id
and a1.activity_type = "start"
and a2.activity_type = 'end'
group by a2.machine_id;