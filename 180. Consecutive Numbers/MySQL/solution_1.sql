# Write your MySQL query statement below

with cte as(
select *, lead(num, 1) over() as num_1, lead(num, 2) over() as num_2 from Logs)

select distinct num as ConsecutiveNums
from cte
where num = num_1 and num = num_2