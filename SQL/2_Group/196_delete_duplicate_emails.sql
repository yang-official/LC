/*
https://leetcode.com/problems/delete-duplicate-emails/

Write a SQL query to delete all duplicate email entries in a table named Person,
keeping only unique emails based on its smallest Id.
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query,
the above Person table should have the following rows:
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Note:
Your output is the whole Person table after executing your sql. Use delete statement.
*/

/* retain the unique emails*/
SELECT MIN(Id) AS minId, Email FROM Person GROUP BY Email;
/* delete the emails which don't appear in the unique emails*/
DELETE FROM Person
WHERE Id NOT IN (
  SELECT minId FROM (
    SELECT MIN(Id) AS MinId, Email FROM Person GROUP BY Email
  ) AS tmp
);
