# Write your MySQL query statement below

select distinct Max(salary) as SecondHighestSalary from Employee
where salary < (select Max(salary) from Employee);
