/*
https://leetcode.com/problems/rank-scores/

Write a SQL query to rank scores. If there is a tie between two scores,
both should have the same ranking. Note that after a tie,
the next ranking number should be the next consecutive integer value.
In other words, there should be no "holes" between ranks.
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table,
your query should generate the following report (order by highest score):
+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
*/

/* MySQL */
SELECT S.Score, COUNT(S2.Score) AS Rank FROM Scores S,
(SELECT DISTINCT Score FROM Scores) S2
WHERE S.Score<=S2.Score
GROUP BY S.Id
ORDER BY S.Score DESC;

/* Using DENSE_RANK() in SQL Server and Oracle */
SELECT Score, DENSE_RANK() OVER (ORDER BY Score DESC) AS RANK FROM Scores;
