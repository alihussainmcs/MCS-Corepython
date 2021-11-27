Today Topics:-
-------------
-> ORDER BY Clause
-> DISTINCT keyword
-> Predefined functions
--------------------------

--------------------
---ORDER BY---------
--------------------
SELECT empno,ename,sal,job,deptno 
FROM
emp
ORDER BY deptno

SELECT empno,ename,sal,job,deptno 
FROM
emp
ORDER BY deptno ASC,ename ASC

---------
SELECT empno,ename,sal,job,deptno 
FROM
emp
ORDER BY deptno ASC,ename DESC

SELECT empno,ename,sal,job,deptno 
FROM
emp
ORDER BY 1

--------------------
-----DISTINCT-------
--------------------
--Display job from employee table with unique values
SELECT DISTINCT job from emp; --> Distinct takes more time to execute

SELECT job --> Group by should be use for better performance than DISTINCT
FROM
emp
GROUP BY job;


-------------------
-- 7.Predefined functions
-------------------
1.Aggregate Functions
2.Number Functions
3.Date Functions
4.Conversion Functions
5.Character Functions

--7.1 Aggregate Functions
--SUM --> To get total value

SELECT SUM(sal) total_sal
FROM
emp

--MAX --> To get maximum value
SELECT MAX(sal) max_sal
FROM
emp

--MIN --> To get minimum value
SELECT MIN(sal) min_sal
FROM
emp

--AVG --> To get average value
SELECT ROUND(AVG(sal),2) avg_sal
FROM
emp

--COUNT  --> To get number of records
SELECT COUNT(*) cnt --> * takes more time because it considers all columns
FROM
emp

SELECT COUNT(1) cnt --> consume less time to execute and it consider based on first column
FROM
emp

SELECT COUNT(empno) cnt 
FROM
emp

--7.2 Number Functions
----------------------
--ABS --It converts negative value to positive
Syntax:-
ABS( number )
---
SELECT ABS(-23);

ABS(-23)
Result: 23

ABS(-23.6)
Result: 23.6

ABS(-23.65)
Result: 23.65

ABS(23.65)
Result: 23.65

ABS(23.65 * -1)
Result: 23.65
---

SELECT empno,ename,job,sal, ABS(-45) val from emp;

SELECT empno,ename,job,sal, ABS(54) val from emp;

--ROUND --round to nearest integer
Syntax:-
ROUND( number [, decimal_places] )
---
SELECT ROUND(125.315)
Result: 125

ROUND(125.315, 0)
Result: 125

ROUND(125.315, 1)
Result: 125.3

ROUND(125.316, 2)
Result: 125.32

ROUND(125.315, 3)
Result: 125.315

ROUND(-125.315, 2)
Result: -125.32

SELECT ROUND(125.5658, 1);

SELECT ABS(ROUND(-125.685));
---

SELECT empno,ename,job,sal, ROUND(45.8934,2) val from emp; 

SELECT empno,ename,job,sal, ROUND(45.8994,2) val from emp; 

--TRUNC --truncated the value
Syntax:-
TRUNC( number [, decimal_places] )
---
SELECT TRUNC(125.815)
Result: 125

TRUNC(125.815, 0)
Result: 125

TRUNC(125.815, 1)
Result: 125.8

TRUNC(125.815, 2)
Result: 125.81

TRUNC(125.815, 3)
Result: 125.815
---
SELECT empno,ename,job,sal, TRUNC(45.8934) val from emp; 


--7.3 Date Functions
--------------------

SELECT empno,ename,job,sal, CURRENT_DATE today_date from emp; --current date

SELECT empno,ename,job,sal, CURRENT_TIME today_time from emp; --current time with time zone

SELECT empno,ename,job,sal, now() today_date_time from emp; --current timestamp with time zone

--========================
--7.4 Conversion Functions
--========================

--PostgreSQL TO_DATE Function: Convert String to Date
--Conversion Functions
Syntax:-
TO_DATE(text,format_mask);
--The TO_DATE() function accepts two string arguments.The first argument is string
--that you want to convert to date.the second one is the input format.
--Example:- (simply it converts string to date format)

SELECT TO_DATE('20210126','YYYYMMDD');

--postgreSQL TO_CHAR FUNCTION : Convert Date or number to String
Syntax:-
to_char( value, format_mask )

SELECT TO_CHAR(now(),'DD Month YYYY');

SELECT TO_CHAR(now(),'Day Month YYYY');

SELECT TO_CHAR(now(),'Dy Mon YYYY');

SELECT TO_CHAR(now(),'Dy Mon YYYY HH24:MI:SS');

SELECT TO_CHAR(now(),'Dy Mon YYYY HH12:MI:SS');

SELECT TO_CHAR(now(),'Dy Mon YYYY HH12:MI:SS am');

SELECT TO_CHAR(now(),'Dy Mon YYYY HH12:MI:SS am tz');

---- Number examples for to_char
SELECT to_char(1210, '9999.99');

SELECT to_char(1210.7, '9G999.99');

SELECT to_char(121, '9 9 9');

SELECT to_char(121, '00999');


SELECT empno,ename,job,sal, TO_CHAR(now(),'DD-MON') date_month from emp; --day and month

SELECT empno,ename,job,sal, TO_CHAR(now(),'DAY') today_day from emp; --day

SELECT empno,ename,job,sal, TO_CHAR(now(),'MONTH') this_month from emp; --month

SELECT empno,ename,job,sal, TO_CHAR(now(),'YYYY') this_year from emp; --year

SELECT empno,ename,job,sal, TO_CHAR(now(),'HH24:MI:SS') today_time from emp; --day



