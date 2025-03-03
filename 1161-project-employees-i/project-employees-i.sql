# Write your MySQL query statement below
select p.project_id , Round(avg(e.experience_years),2) as average_years
from Project p inner join Employee E on p.employee_id=e.employee_id 
group by p.project_id