# Write your MySQL query statement below

#as rank is a function we doing alias in single quote
select score, dense_rank() over(order by score desc) as 'rank'
from Scores
order by score desc