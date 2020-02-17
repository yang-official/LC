/*
177
https://leetcode.com/problems/nth-highest-salary/

Write a SQL query to get the nth highest salary
from the Employee table.
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table,
the nth highest salary where n = 2 is 200.
If there is no nth highest salary,
then the query should return null.
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
*/

/*
To generate a Test Table:
CREATE TABLE Employee (
  Id INT,
  Salary INT
);
INSERT INTO Employee (Id, Salary) VALUES
(1, 100),
(2, 200),
(3, 300),
(4, 200);
*/

SET N = N - 1;
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC 
LIMIT 1 OFFSET N

/*
SQL Server and Oracle can use RANK() and DENSE_RANK() Functions
DENSE_RANK() always returns consecutive integers for ties
RANK() always returns discrete ones
*/
BEGIN
SELECT DISTINCT Salary INTO result
FROM (
  SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) RANK FROM Employee
)
WHERE RANK = N;
EXCEPTION WHEN NO_DATA_FOUND THEN result := null;
END;
