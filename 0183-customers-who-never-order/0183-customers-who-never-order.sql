# Write your MySQL query statement below
SELECT name as Customers
from Customers 
where id not in (
    Select customerId
    from Orders
)

;
