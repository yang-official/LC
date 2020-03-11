/*
https://leetcode.com/problems/consecutive-numbers/

Write a SQL query to find all numbers that appear at least three times consecutively.
+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+

For example, given the above Logs table,
1 is the only number that appears consecutively for at least three times.
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
*/

SELECT
  DISTINCT a.Num AS ConsecutiveNums
FROM
  Logs AS a,
  Logs AS b,
  Logs AS c
WHERE
  a.Num = b.Num
  AND b.Num = c.Num
  AND a.Id = b.Id + 1
  AND b.Id = c.Id + 1;

/*
Create table Logs(
    Id INT,
    Num INT
);
Insert into Logs (Id, Num) Values
(1,1),
(2,1),
(3,1),
(4,2),
(5,1),
(6,2),
(7,2);
*/
