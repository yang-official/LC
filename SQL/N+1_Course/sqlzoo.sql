/*
An SQL Course
SELECT basics
SUM and COUNT
JOIN
NULL
Self JOIN
*/

/*
name	continent	area 	population	gdp
Afghanistan	Asia	652230	25500100	20343000000
Albania	Europe	28748 	2831741 	12960000000
Algeria	Africa	2381741 	37100000 	188681000000
Andorra	Europe	468	78115 	3712000000
Angola	Africa	1246700 	20609294 	100990000000
*/

-- WHERE clause
SELECT population FROM world WHERE name = 'Germany';
-- IN clause
SELECT name, population FROM world WHERE name IN ('Sweden', 'Norway', 'Denmark');
-- BETWEEN clause
SELECT name, area FROM world WHERE area BETWEEN 200000 AND 250000;
-- LIKE for pattern matching
SELECT name FROM world WHERE name LIKE 'Y%'; -- start with Y
SELECT name FROM world WHERE name LIKE '%Y'; -- end with Y
SELECT name FROM world WHERE name LIKE '%x%'; -- contain the letter x
SELECT name FROM world WHERE name LIKE '%land'; -- end with land
SELECT name FROM world WHERE name LIKE 'C%ia'; -- start with C and end with ia
SELECT name FROM world WHERE name LIKE '%oo%'; -- has oo in name
SELECT name FROM world WHERE name LIKE '%a%a%a%'; -- has three or more a
SELECT name FROM world WHERE name LIKE '_t%'; --has t as second character
SELECT name FROM world WHERE name LIKE '%o__o%'; -- has two o separated by two others
SELECT name FROM world WHERE name LIKE '____'; -- exactly four characters
SELECT name FROM world WHERE name = capital; -- name is the capital
SELECT name FROM world WHERE capital = concat(name, ' City'); --capital is name plus city
SELECT capital, name FROM world WHERE capital LIKE concat('%',name,'%'); -- capital includes name
SELECT capital, name FROM world WHERE capital LIKE concat('%', name, '%') AND capital != name; -- find extensions only
SELECT name, replace(capital, name, '') FROM world WHERE capital LIKE concat('%', name, '%') AND capital != name; -- keep the extension only
-- Calculations and Logic
SELECT name, continent, population FROM world;
SELECT name FROM world WHERE population >= 200000000;
SELECT name, gdp/population AS 'per capita GDP' FROM world WHERE population >= 200000000; -- per capita
SELECT name, population/1000000 FROM world WHERE continent = 'South America'; -- in the millions
SELECT name, population FROM world WHERE name IN ('France', 'Germany', 'Italy');
SELECT name FROM world WHERE name LIKE '%United%';
SELECT name, population, area FROM world WHERE area > 3000000 OR population > 250000000; -- OR
SELECT name, population, area FROM world WHERE area > 3000000 XOR population > 250000000; -- XOR
SELECT name, population, area FROM world WHERE (area > 3000000 AND population <= 250000000) OR (area <= 3000000 AND population > 250000000); -- XOR
SELECT name, ROUND(population/1000000,2) AS 'population', ROUND(gdp/1000000000,2) AS 'GDP' FROM world WHERE continent = 'South America'; -- Rounding
SELECT name, ROUND(gdp/population, -3) AS 'per capita gdp' FROM world WHERE gdp > 1000000000000; -- Rounding
SELECT name, capital FROM world WHERE LENGTH(name) = LENGTH(capital); -- length function
SELECT name, capital FROM world WHERE LEFT(name,1) = LEFT(capital, 1) AND name <> capital; --left, not equals <>
SELECT name FROM world WHERE name LIKE '%a%' AND name LIKE '%e%' AND name LIKE '%i%' AND name LIKE '%o%' AND name like '%u%' AND name NOT LIKE '% %'; -- NOT LIKE
-- Practice
SELECT yr, subject, winner FROM nobel WHERE yr = 1950;
SELECT winner FROM nobel WHERE yr = 1962 AND subject = 'Literature';
SELECT yr, subject FROM nobel WHERE winner = 'Albert Einstein';
SELECT winner FROM nobel WHERE subject = 'Peace' AND yr >= 2000;
SELECT yr, subject, winner FROM nobel WHERE subject = 'Literature' AND yr >= 1980 AND yr <= 1989;
SELECT * FROM nobel WHERE winner IN ('Theodore Roosevelt','Woodrow Wilson','Jimmy Carter','Barack Obama');
SELECT winner FROM nobel WHERE winner LIKE 'John%';
SELECT * FROM nobel WHERE (subject = 'Physics' AND yr = 1980) OR (subject = 'Chemistry' AND yr = 1984);
SELECT * FROM nobel WHERE yr = 1980 AND subject NOT IN ('Chemistry', 'Medicine');
SELECT * FROM nobel WHERE (subject = 'Medicine' AND yr < 1910) OR (subject = 'Literature' AND yr >= 2004);
SELECT * FROM nobel WHERE winner = 'Eugene O\'neill'; -- escaping single quotes
SELECT winner, yr, subject FROM nobel WHERE winner LIKE 'Sir%' ORDER BY yr DESC, winner; -- ORDER BY
SELECT winner, subject FROM nobel WHERE yr = 1984 ORDER BY subject IN ('Physics','Chemistry'), subject, winner; -- numerical value of expressions
-- Subqueries, SELECT within SELECT
