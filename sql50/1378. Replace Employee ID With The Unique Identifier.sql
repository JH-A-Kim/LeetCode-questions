# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees as e1 LEFT JOIN EmployeeUNI as e2 ON e1.id=e2.id; 