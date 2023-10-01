# Write your MySQL query statement below

# cte calculating rank using dense rank function
with cte as
(select *, dense_rank() over(order by salary desc) as r from Employee)

# handling the null case
select ifnull((select salary from cte where r = 2 limit 1), null) as SecondHighestSalary