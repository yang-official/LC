-- ORDER
/*
1.SELECT
2.FROM
3.JOIN (ON)
4.WHERE
5.GROUP BY
6.HAVING
7.ORDER BY
8.LIMIT
*/

-- Aggregates
SELECT COUNT(*) FROM table_name WHERE column1 = 'something';
SELECT AVG(column1) FROM table_name WHERE column2 > 1000;

-- GROUP BY
SELECT column1, COUNT(column2) FROM table_name GROUP BY column1;
SELECT column1, SUM(column2) FROM table_name GROUP BY column1;
SELECT column1, MIN(column2) FROM table_name GROUP BY column1;
SELECT column1, MAX(column2) FROM table_name GROUP BY column1;
-- Aliases
SELECT column1, COUNT(column2) AS number_of_values FROM table_name GROUP BY column1;

-- JOIN
SELECT * FROM table1 JOIN table2 ON table1.column1 = table2.column1;

-- HAVING: WHERE is executed before aggregates, so use HAVING to filter
SELECT column1, COUNT(column2) FROM table_name
GROUP BY column1
HAVING COUNT(column2) > 100;

-- Subqueries
SELECT COUNT(*) FROM (
  SELECT column1, COUNT(column2) AS inner_number_of_values
  FROM table_name GROUP BY column1
) AS inner_query
WHERE inner_number_of_values > 100;
