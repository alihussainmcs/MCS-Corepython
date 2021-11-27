-> Character Functions

--7.4 Character Functions
--LENGTH --It returns the length of the string
Syntax:-
LENGTH( string1 )
---
SELECT LENGTH(' ')
Result: 1

LENGTH('postgreSQL')
Result: 10

LENGTH('postgreSQL ')
Result: 11
--------

SELECT
empno employee_number,
LENGTH(ename) emp_name_length,
ename,
LENGTH(job) job_name_length,
job,
sal salary,
deptno department_number,
LENGTH('testing string') test_length
FROM
emp;
--UPPER -- It converts to uppercase
SELECT
empno employee_number,
UPPER(ename) employee_name,
UPPER(job) job,
sal salary,
deptno department_number,
UPPER('testing string') test_upper
FROM
emp;

--LOWER --It converts to lower case
Syntax:-
LOWER( string1 )
---
LOWER('Testing LowerCase');
Result: 'testing lowercase'

LOWER('GEORGE BURNS 123   ');
Result: george burns 123 
---

SELECT
empno employee_number,
LOWER(ename) employee_name,
LOWER(job) job,
sal salary,
deptno department_number,
LOWER('TESTING STRING') test_lower
FROM
emp;


--TRIM --TRIM function removes all specified characters either from the beginning or the end of a string.
Syntax:-
TRIM( [ [ LEADING | TRAILING | BOTH ] trim_character FROM ] string1 )

--Parameters or Arguments
LEADING
--The function will remove trim_character from the front of string1.
TRAILING
--The function will remove trim_character from the end of string1.
BOTH
--The function will remove trim_character from the front and end of string1.
trim_character
--The character that will be removed from string1. If this parameter is omitted, the TRIM function will remove space characters from string1.
---Examples:-
SELECT TRIM('   tech   ')
Result: 'tech'

TRIM(' '  FROM  '   tech   ')
Result: 'tech'

TRIM(LEADING '0' FROM '000123')
Result: '123'

TRIM(TRAILING '1' FROM 'Tech1')
Result: 'Tech'

TRIM(BOTH '1' FROM '123Tech111')
Result: '23Tech'
---
SELECT
empno employee_number,
TRIM(ename) employee_name,
TRIM(job) job,
sal salary,
deptno department_number,
TRIM('1245' FROM '245321testing string ') trim_testing
FROM
emp;
--LTRIM -- LTRIM function removes all specified characters from the left-hand side of a string.
Syntax:-
LTRIM( string1 [, trim_string] )
---
LTRIM('   tech')
Result: 'tech'

LTRIM('   tech', ' ')
Result: 'tech'

LTRIM('000123', '0')
Result: '123'

LTRIM('123123Tech', '123')
Result: 'Tech'

LTRIM('123123Tech123', '123')
Result: 'Tech123'

LTRIM('xyxzyyyTech', 'xyz')
Result: 'Tech'

LTRIM('6372Tech', '0123456789')
Result: 'Tech'
---
SELECT
empno employee_number,
LTRIM(ename) employee_name,
LTRIM(job) job,
sal salary,
deptno department_number,
LTRIM('89888999testing string','89') ltrim_testing
FROM
emp;
--RTRIM -- RTRIM function removes all specified characters from the right-hand side of a string
Syntax:-
RTRIM( string1 [, trim_string ] )
---Examples:-
RTRIM('tech   ')
Result: 'tech'

RTRIM('tech   ', ' ')
Result: 'tech'

RTRIM('123000', '0')
Result: '123'

RTRIM('Tech123123', '123')
Result: 'Tech'

RTRIM('123Tech123', '123')
Result: '123Tech'

RTRIM('Techxyxzyyy', 'xyz')
Result: 'Tech'

RTRIM('Tech6372', '0123456789')
Result: 'Tech'
---
SELECT
empno employee_number,
RTRIM(ename) employee_name,
RTRIM(job) job,
sal salary,
deptno department_number,
RTRIM('testing string23332 ','23') rtrim_testing
FROM
emp;
--LPAD -- LPAD function pads the left-side of a string with a specific set of characters 
--syntax:-
LPAD( string1, padded_length [, pad_string] )

----Examples:-
SELECT LPAD('tech', 7);
Result: '   tech'

LPAD('tech', 8, '0');
Result: '0000tech'

LPAD('testing string', 14, 'z');
Result: 'testing string'

LPAD('testing string', 16, 'z');
Result: 'zztesting string'
----

Example:- 1
SELECT
empno employee_number,
LPAD(ename,15) emp_name_with_lpad,
job,
sal salary,
deptno department_number
FROM
emp;

Example:- 2
SELECT
empno employee_number,
LPAD(ename,15,'Y') emp_name_with_lpad,
job,
sal salary,
deptno department_number
FROM
emp;

Example:- 3
SELECT
empno employee_number,
LPAD(ename,15,'YA') emp_name_with_lpad,
job,
sal salary,
deptno department_number
FROM
emp;
--RPAD --RPAD function pads the right-side of a string with a specific set of characters
Syntax:-
RPAD( string1, padded_length [, pad_string] )
---Example:-
RPAD('tech', 7)
Result: 'tech   '

RPAD('tech', 8, '0')
Result: 'tech0000'

RPAD('testing string', 14, 'z')
Result: 'testing string'

RPAD('testing string', 16, 'z')
Result: 'testing stringzz'
---
Example:- 1
SELECT
empno employee_number,
RPAD(ename,15) emp_name_with_rpad,
job,
sal salary,
deptno department_number
FROM
emp;

Example:- 2
SELECT
empno employee_number,
RPAD(ename,15,'Y') emp_name_with_rpad,
job,
sal salary,
deptno department_number
FROM
emp;

Example:- 3
SELECT
empno employee_number,
RPAD(ename,15,'YA') emp_name_with_rpad,
job,
sal salary,
deptno department_number
FROM
emp;

SELECT LPAD(RPAD('testing string', 16, 'z'),20,'Y')

SELECT RTRIM(LTRIM('6372Tech98778888', '0123456789'),'0123456789')

SELECT RTRIM(LTRIM('         6372Tech98778888          '))


Today Topics:-
------------
-> Advanced Character functions
-> Operators
-> Joins

--SUBSTR --SUBSTR function allows you to extract a substring from a string.
Syntax:-
SUBSTR( string, start_position [, length ] )
string
	--The source string.
start_position
	--The starting position for extraction. The first position in the string is always 1.
length
	--Optional. It is the number of characters to extract. If this parameter is omitted, the SUBSTR function will return the entire string.
---Examples--
SELECT SUBSTR('This is a test', 6, 2)
Result: 'is'

SUBSTR('This is a test', 6)
Result: 'is a test'

SUBSTR('This is postgreSQL', 9, 10)
Result: 'postgreSQL'

--position --position function is used to find the location of a substring within a specified string.
Syntax:-
POSITION(search_string in main_string) 

search_string	--> The substring which is to be searched.
main_string	    --> The string in which the position of the substring will be detected.

--Example--
SELECT POSITION('SQL' IN 'postgreSQL');
	
---------------------
--8.Operators (Arithmetic, Comparison, Logical, Other Operators(IN, BETWEEN, EXISTS))
---------------------
1.Arithmetic Operators
2.Comparison Operators
3.Logical Operators

--8.1 Arithmetic Operators
-- + (Addition)
SELECT 100 + 2 val;

-- - (Subtraction)

SELECT 100 - 2 val;

-- * (Multiplication)

SELECT 100 * 2 val;

-- / (Division)

SELECT 100/2 val;

--8.2 Comparison Operators
-- < , <= , > , >= <> , =

SELECT empno,ename,job,sal FROM emp WHERE sal < 5000;
 
SELECT empno,ename,job,sal FROM emp WHERE sal <= 5000;

SELECT empno,ename,job,sal FROM emp WHERE sal > 3000;

SELECT empno,ename,job,sal FROM emp WHERE sal >= 3000;

SELECT empno,ename,job,sal FROM emp WHERE sal <> 3000;

		--OR
SELECT empno,ename,job,sal FROM emp WHERE sal != 3000;

SELECT empno,ename,job,sal FROM emp WHERE sal = 3000;

--8.3 Logical Operators
-- AND , OR , NOT

--AND --> To add condition

SELECT empno,ename,job,sal FROM emp WHERE sal = 3000 AND job='ANALYST';

--OR --> Either of condition should be true

SELECT empno,ename,job,sal FROM emp WHERE (sal = 3000 OR sal=5000);

SELECT empno,ename,job,sal FROM emp WHERE ename NOT IN('KING','SCOTT');

--IN --> To check multiple values

SELECT empno,ename,job,sal FROM emp WHERE ename IN('KING','SCOTT');

--BETWEEN --> To check range of values

SELECT * FROM emp WHERE sal BETWEEN 2900 AND 3100;

--================
--9.Joins
--================
1.INNER JOIN (or SIMPLE JOIN)
2.LEFT OUTER JOIN (or LEFT JOIN)
3.RIGHT OUTER JOIN (or RIGHT JOIN)
4.FULL OUTER JOIN (or FULL JOIN)

1.INNER JOIN (or SIMPLE JOIN)
--PostgreSQL INNER JOINS return all rows from multiple tables where the join condition is met.

Syntax:-
SELECT columns
FROM table1 
INNER JOIN table2
ON table1.column = table2.column;


Example:-
SELECT
e.empno,e.ename,e.job,d.dname,e.deptno
FROM
emp e
INNER JOIN dept d
ON e.deptno = d.deptno;

This PostgreSQL INNER JOIN example would return all rows from the emp and dept tables where there is a matching deptno value in both the emp and dept tables.

2.LEFT OUTER JOIN (or LEFT JOIN)

--This type of join returns all rows from the LEFT-hand table specified in the left side table and only those rows from the right side table where the joined fields are equal (join condition is met).
Syntax:-
SELECT columns
FROM table1
LEFT OUTER JOIN table2
ON table1.column = table2.column;


Example:-
SELECT
e.empno,e.ename,e.job,d.dname
FROM
dept d
LEFT OUTER JOIN emp e
ON e.deptno = d.deptno;

3.RIGHT OUTER JOIN (or RIGHT JOIN)
--This type of join returns all rows from the RIGHT-hand table specified in the left-side table and only those rows from right-side table where the joined fields are equal (join condition is met).

Syntax:-
SELECT columns
FROM table1
RIGHT OUTER JOIN table2
ON table1.column = table2.column;

Example:-
SELECT
e.empno,e.ename,e.job,d.dname
FROM
emp e
RIGHT OUTER JOIN dept d
ON e.deptno = d.deptno;

4.FULL OUTER JOIN (or FULL JOIN)

-- This type of join returns all rows from the LEFT-hand table and RIGHT-hand table with nulls in place where the join condition is not met.

Syntax:-
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;

Example:-
SELECT
e.empno,e.ename,e.job,d.dname
FROM
emp e
FULL OUTER JOIN dept d
ON e.deptno = d.deptno;

Self Join:-
==========
A self-join is a regular join that joins a table to itself. In practice, you typically use a self-join to query hierarchical data or to compare rows within the same table.

To form a self-join, you specify the same table twice with different table aliases.

SELECT
 e.ename employee,
 m.ename manager
FROM
emp e
INNER JOIN emp m
ON e.mgr = m.empno
