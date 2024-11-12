# Write your MySQL query statement below

SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT distinct MAX(Salary) FROM Employee);
