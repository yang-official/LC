/* Find the sales people with average sales greater than 3 and selling at least two products */
-- SELECT
-- ranking

SELECT
    col,
    RANK() OVER (
        ORDER BY col
    ) myrank
FROM
    t;

SELECT
    col,
    RANK() OVER (
        ORDER BY col
    ) myrank
FROM
    t;

/* What is the total percentage of sales of a product compared to sales */
-- aggregate functions

/*Write an SQL query that makes recommendations using the pages that your friends liked.
Assume you have two tables: a two-column table of users and their friends,
and a two-column table of users and the pages they liked.
It should not recommend pages you already like*/
SELECT f.userid, l.pageid FROM friends f JOIN likes l ON l.userid = f.friendid
LEFT JOIN likes r ON (r.userid = f.userid AND r.pageid = l.pageid)
WHERE r.pageid IS NULL;

SELECT authors.author_name, SUM(books.sold_copies) AS sold_sum
FROM authors
JOIN books
ON books.book_name = authors.book_name
GROUP BY authors.author_name
ORDER BY sold_sum DESC
LIMIT 3;
