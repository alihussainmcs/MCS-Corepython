CREATE TABLE student1(
student1_name varchar(25),
student1_id varchar(25),
student1_mobile varchar(25),
student1_marks integer,
student1_fathername varchar(25),
student1_place varchar(25)
);

INSERT INTO student1 VALUES('mahindra','124g1a0131','9652265878',450,'ramu','anantapur');
INSERT INTO student1 VALUES('kishore','124g1a0132','7965326415',562, 'shyam','anantapur');
SELECT * FROM student1;

INSERT INTO student1 VALUES('kishore','124g1a0132','9658456465',632,'hari','anantapur');
INSERT INTO student1 VALUES('krishna','124g1a0133','7896541231',785,'varma','anantapur');
INSERT INTO student1 VALUES('vinay','124g1a0134','9656878456',564,'kiran','anantapur');
SELECT * FROM student1;

DELETE FROM student1 WHERE student1_marks = 632;
DELETE FROM student1 WHERE student1_name = 'kishor';
DELETE FROM student1 WHERE student1_fathername = 'kiran';
SELECT * FROM student1;


ALTER TABLE student1 ADD COLUMN student1_email  varchar(50);
select student1_email from student1;


UPDATE student1 SET student1_email='mahi@gmail.com' WHERE student1_name = 'mahindra';
select * from student1;
UPDATE student1 SET student1_email = 'ki1234@gmail.com' WHERE student1_name='kishore';
UPDATE student1 SET student1_email = 'krishnam@gmail.com' WHERE student1_id = '124g1a0133';
UPDATE student1 SET student1_email = 'vinay456@gmail.com' WHERE student1_marks = 564;
select student1_email FROM student1;

CREATE TABLE student1_copy AS SELECT * FROM student1 WHERE 1 = 1;
SELECT * from student1_copy;

DROP TABLE student1_copy;

SELECT * from student1_copy;
-- SQL Error [42P01]: ERROR: relation "student1_copy" does not exist
-- Position: 15







