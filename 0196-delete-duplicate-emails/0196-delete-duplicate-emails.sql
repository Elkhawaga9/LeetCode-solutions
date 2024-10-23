# Write your MySQL query statement below
Delete p2
from Person p1 join Person p2
Where p1.Email = p2.Email AND
p1.Id < p2.Id
;
