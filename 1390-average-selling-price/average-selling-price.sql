# Write your MySQL query statement below
select p.product_id, coalesce(round(sum(p.price*u.units)/sum(u.units),2),0)  as average_price
from Prices p left outer join UnitsSold u on p.product_id=u.product_id and p.end_date>=u.purchase_date and p.start_date<=u.purchase_date
group by p.product_id  