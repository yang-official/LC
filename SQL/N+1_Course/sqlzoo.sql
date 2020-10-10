/*
SELECT
SUM and COUNT
JOIN
NULL
Self JOIN
*/

/*
SELECT (the basics)
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

/*
SELECT in SELECT (subqueries)
*/
-- Subqueries, SELECT within SELECT
SELECT name FROM world WHERE population > (SELECT population FROM world WHERE name='Russia');
SELECT name FROM world WHERE continent = 'Europe' AND gdp/population > (SELECT gdp/population FROM world WHERE name = 'United Kingdom');
SELECT name, continent FROM world WHERE continent IN (SELECT continent FROM world WHERE name in ('Argentina', 'Australia')) ORDER BY name;
SELECT name, population FROM world WHERE population > (SELECT population FROM world WHERE name = 'Canada') AND population < (SELECT population FROM world WHERE name = 'Poland');
SELECT name, CONCAT(ROUND(population / (SELECT population FROM world WHERE name = 'Germany') * 100),'%') FROM world WHERE continent = 'Europe';
-- using ALL
SELECT name FROM world WHERE gdp > ALL (SELECT gdp FROM world WHERE continent = 'Europe' AND gdp IS NOT NULL);
SELECT continent, name, area FROM world x WHERE area >= ALL (SELECT area FROM world y WHERE y.continent=x.continent AND area>0);
SELECT continent, name FROM world x WHERE name <= ALL (SELECT name FROM world y WHERE x.continent = y.continent);
SELECT name,continent,population FROM world x WHERE 25000000 >= ALL (SELECT population FROM world y WHERE x.continent=y.continent AND y.population>0);
SELECT name, continent FROM world x WHERE population > ALL (SELECT population*3 FROM world y WHERE y.continent = x.continent AND y.name != x.name);

/*
SUM and COUNT (aggregate functions)
*/
SELECT SUM(population) FROM world;
SELECT DISTINCT continent FROM world;
SELECT SUM(gdp) FROM world WHERE continent = 'Africa';
SELECT COUNT(name) FROM world WHERE area >= 1000000;
SELECT SUM(population) FROM world WHERE name IN ('Estonia','Latvia','Lithuania');
-- using GROUP BY and HAVING
SELECT continent, COUNT(name) FROM world GROUP BY continent;
SELECT continent, COUNT(name) FROM world WHERE population >= 10000000 GROUP BY continent;
SELECT continent FROM world GROUP BY continent HAVING SUM(population) >= 100000000;
-- MAX, AVG, DISTINCT, ORDER BY
SELECT COUNT(winner) FROM nobel;
SELECT DISTINCT subject FROM nobel;
SELECT COUNT(winner) FROM nobel WHERE subject = 'Physics';
SELECT subject, COUNT(winner) FROM nobel GROUP BY subject;
SELECT subject, MIN(yr) FROM nobel GROUP BY subject;
SELECT subject, COUNT(winner) FROM nobel WHERE yr = 2000 GROUP BY subject;
-- DISTINCT aggregates
SELECT subject, COUNT(DISTINCT winner) FROM nobel GROUP BY subject;
SELECT subject, COUNT(DISTINCT yr) FROM nobel GROUP BY subject;
-- HAVING
SELECT yr FROM nobel WHERE subject = 'Physics' GROUP BY yr HAVING COUNT(winner) = 3;
SELECT winner FROM nobel GROUP BY winner HAVING COUNT(winner) > 1;
SELECT winner FROM nobel GROUP BY winner HAVING COUNT(DISTINCT subject) > 1;
SELECT yr, subject FROM nobel WHERE yr >= 2000 GROUP BY yr, subject HAVING COUNT(winner) = 3;

/*
JOIN
*/
SELECT player, teamid, stadium, mdate FROM game JOIN goal ON (id=matchid) WHERE teamid = 'GER';
SELECT team1, team2, player FROM game JOIN goal ON id = matchid WHERE player LIKE 'Mario%';
SELECT player, teamid, coach, gtime FROM goal JOIN eteam on teamid=id WHERE gtime<=10;
SELECT mdate, eteam.teamname FROM game JOIN eteam ON team1 = eteam.id WHERE coach = 'Fernando Santos';
SELECT player FROM goal JOIN game ON matchid = id WHERE stadium = 'National Stadium, Warsaw';
SELECT DISTINCT player FROM game JOIN goal ON matchid = id WHERE (team1='GER' OR team2 = 'GER') AND teamid != 'GER';
SELECT teamname, COUNT(player) FROM eteam JOIN goal ON id=teamid GROUP BY teamname ORDER BY teamname;
SELECT stadium, COUNT(*) FROM game JOIN goal ON matchid = id GROUP BY stadium;
SELECT matchid, mdate, COUNT(*) FROM game JOIN goal ON matchid = id WHERE (team1 = 'POL' OR team2 = 'POL') GROUP BY matchid;
SELECT matchid, mdate, COUNT(*) FROM game JOIN goal ON matchid = id WHERE teamid = 'GER' GROUP BY matchid;
-- CASE WHEN
SELECT mdate, team1, SUM(CASE WHEN teamid = team1 THEN 1 ELSE 0 END) AS score1,
       team2, SUM(CASE WHEN teamid = team2 THEN 1 ELSE 0 END) AS score2
       FROM game LEFT JOIN goal ON (id = matchid) GROUP BY mdate,team1,team2 ORDER BY mdate, matchid, team1, team2;
-- more JOINs
SELECT id, title FROM movie WHERE yr = 1962;
SELECT yr FROM movie WHERE title = 'Citizen Kane';
SELECT id, title, yr FROM movie WHERE title LIKE '%Star Trek%' ORDER BY yr;
SELECT id FROM actor WHERE name = 'Glenn Close';
SELECT id FROM movie WHERE title = 'Casablanca';
SELECT name FROM actor JOIN casting on actor.id = casting.actorid WHERE movieid = (SELECT id FROM movie WHERE title = 'Casablanca');
SELECT name FROM actor join casting on id = actorid WHERE movieid = (SELECT id FROM movie WHERE title = 'Alien');
SELECT title FROM movie JOIN casting on movie.id = casting.movieid JOIN actor on actor.id = casting.actorid WHERE actor.name = 'Harrison Ford';
SELECT title FROM movie JOIN casting on movie.id = casting.movieid JOIN actor on actor.id = casting.actorid WHERE actor.name = 'Harrison Ford' AND ord != 1;
SELECT title, name FROM movie JOIN casting ON movie.id = casting.movieid JOIN actor ON actor.id = casting.actorid WHERE yr = 1962 AND ord = 1;
SELECT yr,COUNT(title) FROM movie JOIN casting ON movie.id=movieid JOIN actor ON actorid=actor.id WHERE name='Rock Hudson' GROUP BY yr HAVING COUNT(title) > 2;
SELECT title, name FROM movie JOIN casting ON movie.id = movieid JOIN actor ON actor.id = actorid WHERE movie.id IN (SELECT movie.id FROM movie JOIN casting ON movie.id = movieid JOIN actor ON actor.id = actorid WHERE name = 'Julie Andrews') AND ord = 1;
SELECT name FROM actor JOIN casting ON id = actorid WHERE ord = 1 GROUP BY name HAVING COUNT(*) >= 15 ORDER BY name;
SELECT title, COUNT(actorid) FROM movie JOIN casting on movie.id = movieid JOIN actor ON actor.id = actorid WHERE yr = 1978 GROUP BY title ORDER BY COUNT(actorid) DESC, title;
SELECT name FROM actor JOIN casting ON id = actorid WHERE name != 'Art Garfunkel' AND movieid in (SELECT movieid FROM actor JOIN casting ON actor.id = actorid WHERE name = 'Art Garfunkel');
--NULL, INNER JOIN, LEFT JOIN, RIGHT JOIN
SELECT name FROM teacher WHERE dept IS NULL;
SELECT teacher.name, dept.name FROM teacher INNER JOIN dept ON (teacher.dept=dept.id);
SELECT teacher.name, dept.name FROM teacher LEFT JOIN dept ON (teacher.dept=dept.id);
SELECT teacher.name, dept.name FROM teacher RIGHT JOIN dept ON (teacher.dept=dept.id);
SELECT name, COALESCE(mobile, '07986 444 2266') FROM teacher;
SELECT teacher.name, COALESCE(dept.name, 'None') FROM teacher LEFT JOIN dept ON teacher.dept = dept.id;
SELECT COUNT(name), COUNT(mobile) FROM teacher;
SELECT dept.name, COUNT(teacher.name) FROM teacher RIGHT JOIN dept ON teacher.dept = dept.id GROUP BY dept.name;
-- CASE WHEN condition1 THEN value1 WHEN condition2 THE value2 ELSE def_value END
SELECT name, CASE WHEN dept in (1, 2) THEN 'Sci' ELSE 'Art' END FROM teacher;
SELECT name, CASE WHEN dept in (1, 2) THEN 'Sci' WHEN dept = 3 THEN 'Art' ELSE 'None' END FROM teacher;
-- Self JOIN
SELECT count(id) FROM stops;
SELECT id FROM stops WHERE name = 'Craiglockhart';
SELECT id, name FROM stops JOIN route ON route.stop = stops.id WHERE num = '4' AND company = 'LRT';
SELECT company, num, COUNT(*) FROM route WHERE stop=149 OR stop=53 GROUP BY company, num HAVING COUNT(*) = 2;
SELECT a.company, a.num, a.stop, b.stop FROM route a JOIN route b ON (a.company=b.company AND a.num=b.num) WHERE a.stop=53 AND b.stop = (SELECT id FROM stops WHERE name = 'London Road');
SELECT a.company, a.num, stopa.name, stopb.name FROM route a JOIN route b ON (a.company=b.company AND a.num=b.num) JOIN stops stopa ON (a.stop=stopa.id) JOIN stops stopb ON (b.stop=stopb.id) WHERE stopa.name='Craiglockhart' AND stopb.name='London Road';
SELECT DISTINCT a.company, a.num FROM route a JOIN route b ON a.company=b.company AND a.num = b.num WHERE a.stop = 115 AND b.stop = 137;
SELECT a.company, a.num FROM route a JOIN route b on a.company=b.company AND a.num=b.num JOIN stops stopa ON stopa.id=a.stop JOIN stops stopb ON stopb.id=b.stop WHERE stopa.name='Craiglockhart' AND stopb.name='Tollcross';
SELECT DISTINCT stopb.name, a.company, a.num FROM route a JOIN route b on a.company=b.company AND a.num=b.num JOIN stops stopa ON stopa.id=a.stop JOIN stops stopb ON stopb.id=b.stop WHERE stopa.name='Craiglockhart';
SELECT a.num, a.company, stopb.name, c.num, c.company
FROM route a
JOIN route b ON a.company=b.company AND a.num = b.num
JOIN route c ON b.stop=c.stop
JOIN route d ON c.company=d.company AND c.num=d.num
JOIN stops stopa ON a.stop=stopa.id
JOIN stops stopb ON b.stop=stopb.id
JOIN stops stopc ON c.stop=stopc.id
JOIN stops stopd ON d.stop=stopd.id
WHERE stopa.name='Craiglockhart' AND stopd.name='Lochend';

-- Window functions
SELECT lastName, party, votes
  FROM ge
 WHERE constituency = 'S14000024' AND yr = 2017
ORDER BY votes DESC;

SELECT party, votes,
       RANK() OVER (ORDER BY votes DESC) as posn
  FROM ge
 WHERE constituency = 'S14000024' AND yr = 2017
ORDER BY party;

SELECT yr,party, votes,
      RANK() OVER (PARTITION BY yr ORDER BY votes DESC) as posn
  FROM ge
 WHERE constituency = 'S14000021'
ORDER BY party,yr;

SELECT constituency,party, votes, RANK() OVER (PARTITION BY constituency ORDER BY votes DESC) as posn
  FROM ge
 WHERE constituency BETWEEN 'S14000021' AND 'S14000026'
   AND yr  = 2017
ORDER BY posn, constituency;

SELECT constituency, party
  FROM (
    SELECT constituency,party,
      RANK() OVER (PARTITION BY constituency ORDER BY votes DESC)
        AS posn
      FROM ge
     WHERE constituency BETWEEN 'S14000021' AND 'S14000026'
       AND yr  = 2017
   ) AS ed
WHERE posn = 1;

SELECT party,COUNT(1)
  FROM (
    SELECT constituency,party,
      RANK() OVER (PARTITION BY constituency ORDER BY votes DESC)
        AS posn
      FROM ge
     WHERE constituency LIKE 'S%'
       AND yr  = 2017
   ) AS ed
WHERE posn = 1
GROUP BY party;

--Window LAG
SELECT name, DAY(whn), confirmed, deaths, recovered FROM covid
WHERE name = 'Spain' AND MONTH(whn) = 3 ORDER BY whn;

SELECT name, DAY(whn), confirmed, LAG(confirmed, 1) OVER (PARTITION BY name ORDER BY whn) AS dbf
FROM covid WHERE name = 'Italy' AND MONTH(whn) = 3 ORDER BY whn;

SELECT name, DAY(whn), confirmed - LAG(confirmed, 1) OVER (PARTITION BY name ORDER BY whn) AS new
FROM covid WHERE name = 'Italy' AND MONTH(whn) = 3 ORDER BY whn;

SELECT name, DATE_FORMAT(whn,'%Y-%m-%d'), confirmed - LAG(confirmed, 1) OVER (PARTITION BY name ORDER BY whn) AS 'new this week'
FROM covid WHERE name = 'Italy' AND WEEKDAY(whn) = 0 ORDER BY whn;

SELECT tw.name, DATE_FORMAT(tw.whn,'%Y-%m-%d'), tw.confirmed - lw.confirmed
FROM covid tw LEFT JOIN covid lw ON
  DATE_ADD(lw.whn, INTERVAL 1 WEEK) = tw.whn
  AND tw.name=lw.name
WHERE tw.name = 'Italy' AND WEEKDAY(tw.whn) = 0
ORDER BY tw.whn;

SELECT
   name,
   confirmed,
   RANK() OVER (ORDER BY confirmed DESC) rc,
   deaths,
   RANK() OVER (ORDER BY deaths DESC) rc
  FROM covid
WHERE whn = '2020-04-20'
ORDER BY confirmed DESC;

SELECT
   world.name,
   ROUND(100000*confirmed/population,0),
   RANK() OVER (ORDER BY confirmed/population) AS rank
  FROM covid JOIN world ON covid.name=world.name
WHERE whn = '2020-04-20' AND population > 10000000
ORDER BY population DESC;

SELECT name,DATE_FORMAT(whn,'%Y-%m-%d'), newCases AS peakNewCases
FROM (
  SELECT name,whn,newCases, RANK() OVER (PARTITION BY name ORDER BY newCases DESC) rnc
  FROM (
    SELECT name, whn,
      confirmed - LAG(confirmed, 1) OVER (PARTITION BY name ORDER BY whn) as newCases
    FROM covid
  ) AS x
) AS y
WHERE rnc = 1 AND newCases>1000 ORDER BY whn
