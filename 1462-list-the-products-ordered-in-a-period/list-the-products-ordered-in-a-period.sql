# Write your MySQL query statement below
select p.product_name , sum(o.unit) as unit
from Products p inner join Orders o on p.product_id = o.product_id
where datediff('2020-02-29',o.order_date)<=28 and datediff('2020-02-29',o.order_date)>=0
group by p.product_name
having sum(o.unit) >=100 