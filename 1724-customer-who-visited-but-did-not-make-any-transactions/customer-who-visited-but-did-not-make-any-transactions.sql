# Write your MySQL query statement below
select customer_id,count(*) as count_no_trans from Visits

where visit_id not in (
select distinct v.visit_id
from Visits as v
JOIN Transactions as t on v.visit_id=t.visit_id)
group by customer_id
