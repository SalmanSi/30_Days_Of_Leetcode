# Write your MySQL query statement below
Delete from Person
where id not in (select minid from  (select min(id) as minid from Person group by email) as a)