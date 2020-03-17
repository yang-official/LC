/*
https://leetcode.com/problems/rising-temperature/

Given a Weather table, write a SQL query to find all dates' Ids
with higher temperature compared to its previous (yesterday's) dates.
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
For example, return the following Ids for the above Weather table:
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
*/

Select W1.Id
From Weather W1 JOIN Weather W2
ON to_days(W1.RecordDate) = to_days(W2.RecordDate) + 1
Where W1.Temperature > W2.Temperature;
