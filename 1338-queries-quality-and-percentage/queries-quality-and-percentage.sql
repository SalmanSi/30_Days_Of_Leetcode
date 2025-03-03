# Write your MySQL query statement below
select query_name,round(sum(rating/position)/count(rating),2) as quality, round((select count(*) from Queries where query_name=q1.query_name and rating<3)*100/count(rating),2) as poor_query_percentage
from Queries q1
group by query_name
