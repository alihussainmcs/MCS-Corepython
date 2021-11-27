Today Topic:-
------------
-> select data using where clause, group by, having and LIKE operator
-> Wildcard Characters 
	percent(%) wildcard
	underscore(_) wildcard
-> CASE Statement
-> Alias_name usage
-------------------------------
SELECT empno,ename,job,sal FROM emp;

--Display employee details of their job is "MANAGER"?
SELECT empno,ename,job,sal FROM emp WHERE job = 'MANAGER';

select empno,ename,job,mgr,sal from emp where UPPER(job)=UPPER('manager');

--Display employee details of their salary is greater than or equal to 3000?
SELECT empno,ename,job,sal FROM emp WHERE sal >=3000; 

--Display total salary of all employees
SELECT SUM(sal) total_sal FROM emp;

--Display total salary and job of all employees based on the job?
SELECT SUM(sal) total_sal,job FROM emp GROUP BY job;

--Display total salary and job of all employees based on the job and total salary is greater than or equal to 5000?
SELECT SUM(sal) total_sal,job FROM emp GROUP BY job HAVING SUM(sal) >=5000;

SELECT SUM(sal),job FROM emp GROUP BY job HAVING SUM(sal) <=5000;

select sum(sal) from emp where job='SALESMAN'



--Display employee details of their employee name stars with "J"
SELECT empno,ename,job,sal FROM emp WHERE ename LIKE 'J%'; --Using LIKE operator

--Display employee details of their employee name either starts with "J" or starts with "C"
SELECT empno,ename,job,sal FROM emp WHERE (ename like 'J%' OR ename like 'C%')

--Display employee details of their employee name starts with "J" letter and job is "MANAGER"
SELECT empno,ename,job,sal FROM emp WHERE ename like 'J%' AND JOB ='MANAGER'

--Display employee details of their employee name stars with letter "C"
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE 'C%'; --starts with C

--Display employee details of their employee name ends with letter "S"
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE '%S'; --end with S

--Display employee details of their employee name contains letters "LA"
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE '%LA%'; --contains LA

--Display employee details of their employee name doesnot contains letters "LA"
--Using NOT LIKE
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename NOT LIKE '%LA%'; --not contains LA


(Using underscore(_)).It represents single character
----------------------------------------------------

Requirement:-
--display employee details and employee name second character should be letter "I".
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE '_I%'; 

--from the last second character should be letter "E"
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE '%E_'; 

--third character should be letter "N"
SELECT 
empno,ename,job,sal,deptno
FROM
emp WHERE ename LIKE '__N%'; 




-----------------
--Structure of SQL Query--
-----------------
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY

CASE Statement:-
---------------
--Syntax:-

SELECT
CASE 
 WHEN column_name1 = Value1 THEN
 val1
 WHEN column_name1 = Value2 THEN
 Val2
 ELSE
 Val3
END column_n
FROM
table_name;

SELECT empno,ename,job,sal,deptno from emp;

SELECT
 CASE 
  WHEN sal <= 2500 THEN
  sal + 1000
  WHEN sal > 2500 AND sal <= 3000 THEN
  sal + 600
  ELSE
  sal + 400
 END sal_increment,empno,ename,job,sal,deptno
 FROM emp;
  
  
  select 
 CASE WHEN deptno='10' THEN
 'ACCOUNTING'
 WHEN DEPTNO='20' THEN
 'RESEARCH'
 WHEN DEPTNO='30' THEN
 'SALES'
 WHEN DEPTNO='40' THEN
 'OPERATIONS'
 END deparment_name,employee_tab.*
 FROM 
 emp employee_tab
 
 select
 CASE 
 WHEN job='MANAGER' then
 ename||' is '||job
 WHEN job='PRESIDENT' then
 ename||' is '||job||'  whose is having sal '||sal
 WHEN job='ANALYST' then
 ename||' is '||job||' whose department is'||deptno
 WHEN job='SALESMAN' then
 ename||' is '||job||'and whose joining date is '||hiredate
 WHEN job='CLERK' then
 ename||' is '||job||'and whose empno is '||empno
 END employee_name
 FROM emp
 --------------
 --Aliases (temporary name)
 --------------
 --Syntax
 SELECT column_name AS alias_name
FROM table_name;

--AS keyword is optional

SELECT column_name alias_name
FROM table_name;

Example:-

SELECT
empno employee_number,
ename employee_name,
job,
sal salary,
deptno department_number
FROM
emp;

SELECT
empno "Employee Number",
ename employee_name,
job,
sal salary,
deptno department_number
FROM
emp;

--table alias name
SELECT
e.empno employee_number,
e.ename employee_name,
e.job,
sal salary,
deptno department_number
FROM
emp e;

--with multiple table using alias name
SELECT
e.empno employee_number,
e.ename employee_name,
e.job,
sal salary,
d.deptno department_number,
d.dname
FROM
emp e,
dept d
WHERE
e.deptno = d.deptno;