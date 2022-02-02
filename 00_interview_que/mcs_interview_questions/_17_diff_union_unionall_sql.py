"""
17.difference between union and union all?

The only difference between Union and Union All is that Union extracts the rows that are
being specified in the query while Union All extracts all the rows including the duplicates
(repeated values) from both the queries.

#union operator:

Union operator in MySQL allows us to combine two or more results from multiple SELECT
queries into a single result set. It has a default feature to remove the duplicate rows
from the tables. This operator syntax always uses the column's name in the first SELECT
statement to be the column names of the output.

MySQL Union must follow these basic rules:

    1.The number and order of the columns should be the same in all queries.
    2.The corresponding columns position of each select query must have a compatible data type.
    3.The column name selected in the different SELECT queries must be in the same order.
    4.The column name of the first SELECT query will be the column names of the output.

#union all?

The UNION ALL operator combines two or more results from multiple SELECT queries and returns all
records into a single result set. It does not remove the duplicate rows from the output of the
SELECT statements.

#difference between union and union-all?


UNION

1.It combines the result set from multiple
tables and returns distinct records into
a single result set.

2.Following is the basic syntax of UNION operator:
SELECT column_list FROM table1
UNION
SELECT column_list FROM table2;

3.It has a default feature to eliminate the duplicate rows from the output.

4.Its performance is slow because it takes time to find and then remove duplicate records.

5.Most database users prefer to use this operator.

6.syntax:
SELECT column1, Column2 ...Column (N) FROM tableA
UNION
SELECT column1, Column2 ...Column (N) FROM tableB;

UNION ALL

1.It combines the result set from multiple tables and
returns all records into a single result set.

2.Following is the basic syntax of UNION ALL operator:
SELECT column_list FROM table1
UNION ALL
SELECT column_list FROM table2;

3.It has no feature to eliminate the duplicate rows from the output.

4.Its performance is fast because it does not eliminate the duplicate rows.

5.Most database users do not prefer to use this operator.

6. syntax:
SELECT column1, Column2 ...Column (N) FROM tableA
Union All
SELECT column1, Column2 ...Column (N) FROM tableB;

"""