Today Topic:
------------
-> DDL Commands
-> DML Commands
-> Create new table using exising table in db with same table structure
-> Select data using where Clause
-------------------------------------
 

DDL (Data definition language)
CREATE
DROP
ALTER

Example:- 

CREATE TABLE students_table(
student_id integer,
student_name varchar(100),
branch varchar(50)
);

DML (Data manupulation language)
INSERT
UPDATE
DELETE

INSERT INTO students_table VALUES(100101,'Ram','ECE');

INSERT INTO students_table VALUES(100102,'Ravi','EEE');

INSERT INTO students_table VALUES(100103,'Swaroop','CSE');

INSERT INTO students_table VALUES(100104,'Naveen','ECE');

SELECT student_id,student_name,branch FROM students_table;

UPDATE students_table SET branch = 'CSE' WHERE student_id = 100104;

UPDATE STUDENTS_TABLE SET BRANCH = 'CIVIL',student_id=100204 WHERE STUDENT_NAME ='Naveen';

SELECT student_id,student_name,branch FROM students_table;

DELETE FROM students_table where student_name = 'Ravi';

SELECT student_id,student_name,branch FROM students_table;

DROP TABLE students_table;

--How to create table using existing table available in database?

CREATE TABLE employee_copy AS SELECT * FROM emp;

SELECT * FROM employee_copy;

--How to remove or drop table from database?
DROP TABLE employee_copy;


CREATE TABLE employee_copy AS SELECT * FROM emp WHERE 1=1; --with records

DROP TABLE employee_copy;

--How to create the new table with same structure of exising table in db without records?
CREATE TABLE employee_copy AS SELECT * FROM emp WHERE 1=2; --without records

-------------------------------
--working on emp and dept tables:-
-------------------------------
--4.select data using where clause, group by, having and LIKE operator
-------------------------------
SELECT empno,ename,job,sal FROM emp;

--Display employee details of their job is "MANAGER"?
SELECT empno,ename,job,sal FROM emp WHERE job = 'MANAGER';
