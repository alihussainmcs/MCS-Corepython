1) display ename,job,sal,deptno,dname whose location is "CHICAGO"
select
e1.ename,e1.job,e1.sal,e1.deptno,d1.dname,d1.loc
from
emp e1,
dept d1
where e1.deptno = d1.deptno
AND d1.loc = 'CHICAGO'
2) display number of employees whose department is "ACCOUNTING" (write two queries using "Subquery" and "Joints")
select
count(*) num_of_employees,d1.dname
from
emp e1,
dept d1
where
e1.deptno = d1.deptno
AND d1.dname = 'ACCOUNTING'
GROUP BY d1.dname

3) display ename,job,sal,dname whose dname 5th character should be "S"
select
e1.ename,e1.job,e1.sal,e1.deptno,d1.dname,d1.loc
from
emp e1,
dept d1
where e1.deptno = d1.deptno
AND d1.dname LIKE '____S%'
4) display dname,loc whose dname doesnot contain employees
SELECT
 d1.dname,d1.loc
FROM
dept d1
WHERE
NOT EXISTS (SELECT empno from emp e1 where e1.deptno = d1.deptno)
5) display ename,job,sal,dname,loc whose sal greater than or equal to 3000
select
e1.ename,e1.job,e1.sal,e1.deptno,d1.dname,d1.loc
from
emp e1,
dept d1
where e1.deptno = d1.deptno
AND sal >=3000
6) display ename,job,sal whose sal is greater than avgerage sal of employees(Using Subquery)
select ename,job,sal from emp where sal >(select avg(sal) from emp)

7) display employee details AND dept details and apply deptno in Ascending order 
 and Job in descending order.And sal is greater than or equal to 2500
 select
e1.ename,e1.job,e1.sal,e1.deptno,d1.dname,d1.loc
from
emp e1,
dept d1
where e1.deptno = d1.deptno
AND e1.sal >=2500
ORDER BY deptno ASC,job DESC
 
 
8) display number of employees and job details.
(How many employees available in a specific job)

select count(*) num_of_employees,job
from
emp
group by job

9) display number of employees available in location "DALLAS"(Using EXISTS and IN operators)

select count(*) num_of_employees
from emp e1
where exists (select deptno from dept d1 where loc='DALLAS' and e1.deptno = d1.deptno)

select count(*) num_of_employees
from emp e1 where deptno in(select deptno from dept where loc='DALLAS')

10) display employee details whose salary between 2500 and 3000

SELECT ENAME,JOB,SAL,DEPTNO
FROM
EMP 
WHERE SAL BETWEEN 2500 and 3000

Today Topics:-
------------
->Important functions
->Constraints
->Review Assignment1 Queries

CONCAT:-
------
This function allows you to concatenate two strings together.

Syntax:-
-------
CONCAT( string1, string2 )

Example:-
-------
SELECT CONCAT('This is ','SQL') VAL;

Concat with ||:-

-------------
Syntax:-
------
string1 || string2 [ || string_n ]

SELECT 'This is String1'||' String2'||' String3' VAL;

COALESCE();
-----
Syntax:-
COALESCE(e1, e2)

The COALESCE() function accepts two arguments. 
If e1 evaluates to null, then COALESCE() function returns e2. 
If e1 evaluates to non-null, the COALESCE() function returns e1.

SELECT ENAME,JOB,SAL,COALESCE(COMM,0) COMM FROM EMP


12.CONSTRAINTS
==============
Constraints are the rules enforced on data columns on table.
These are used to prevent invalid data from being entered into the database.
This ensures the accuracy and reliability of the data in the database.

1.NOT NULL − Ensures that a column cannot have NULL value.

2.UNIQUE − Ensures that all values in a column are different.

3.PRIMARY Key − Uniquely identifies each row/record in a database table.

4.FOREIGN Key − Constrains data based on columns in other tables.

5.CHECK − It ensures that all values in a column satisfy certain conditions.

1.NOT NULL:-
===========
It will not allows to store null values.

Example:-
--------
CREATE TABLE employee(
   ID             integer PRIMARY KEY,
   NAME           TEXT    NOT NULL,
   ADDRESS        VARCHAR(500),
   SALARY         DECIMAL(12,2)
);

insert into employee(id,name) values(101,'Ram');
insert into employee(id) values(101);

2.UNIQUE
--------
It will not allows to store duplicate values.

drop table employee;

CREATE TABLE employee(
   ID             integer PRIMARY KEY,
   NAME           TEXT    NOT NULL,
   empno          integer UNIQUE,
   ADDRESS        VARCHAR(500),
   SALARY         DECIMAL(12,2)
);

insert into employee(id,name,empno) values(102,'Naveen',1001);
insert into employee(id,name,empno) values(103,'Depak',1001);
insert into employee(id,name,empno) values(103,'Depak',1002);

3.PRIMARY KEY:-
-------------
It will not allows to store null values and duplicate records.

drop table employee;

CREATE TABLE employee(
   ID             integer PRIMARY KEY,
   NAME           TEXT    ,
   empno          integer ,
   ADDRESS        VARCHAR(500),
   SALARY         DECIMAL(12,2)
);

insert into employee(id,name,empno) values(101,'Naveen',1001);
insert into employee(id,name,empno) values(101,'Praveen',1002);
insert into employee(id,name,empno) values(null,'Kiran',1003);

4.FOREIGN KEY:-
-------------
 A foreign key means that values in one table must also appear in another table.
 
 The referenced table is called the parent table while the table with the foreign key is called the child table.
 The foreign key in the child table will generally reference a primary key in the parent table.
 
 
select * from emp

select * from dept

CREATE TABLE dept_details
(deptno integer NOT NULL,
 dname varchar(20),
 loc VARCHAR(20),
 CONSTRAINT deptno_pk PRIMARY KEY(deptno)
 );
 
 insert into dept_details values(10,'ACCOUNTING','CHICAGO');
 
 select * from dept_details
 
 CREATE TABLE emp_details
(empno INTEGER NOT NULL,
ename VARCHAR(10),
job VARCHAR(10),
deptno integer NOT NULL,
sal decimal(12,2) NOT NULL,
constraint empno_pk PRIMARY KEY(empno),
constraint deptno_fk FOREIGN KEY(deptno)
REFERENCES dept_details(deptno)
);

INSERT INTO EMP_DETAILS(EMPNO,ENAME,SAL,DEPTNO) VALUES(1001,'Ram',3000.00,10);

INSERT INTO EMP_DETAILS(EMPNO,ENAME,SAL,DEPTNO) VALUES(1002,'Sam',5000.00,10);

ALTER TABLE emp_details
DROP constraint deptno_fk;

ALTER TABLE emp_details
ADD constraint deptno_fk FOREIGN KEY(deptno)
REFERENCES dept_details(deptno);

5.CHECK
-------
It allows you to specify a condition on each row in a table.

CREATE TABLE suppliers
(
  supplier_id integer,
  supplier_name varchar(50),
  CONSTRAINT check_supplier_name
  CHECK (supplier_name = upper(supplier_name))
);

insert into suppliers(supplier_id,supplier_name) values(200,'IBM');

insert into suppliers(supplier_id,supplier_name) values(200,'ibm');