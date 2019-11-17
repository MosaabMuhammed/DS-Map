<h1 style='text-decoration:underline'>SQL</h1>
<h2 style='width:440px;margin:auto'>Declarative Programming Language</h2><br>

<div style='width:1000px;margin:auto'>
<details><summary>1. Start <b>MySQL</b> in the <b>Command Line</b></summary><p>
~~~
mysql -u root -p

# Then write your password "root"
# -u: used to use the username
# root: the name of the user
# -p: means I'll give the password.
~~~
</p></details>

<details><summary>2. Create <b>Database</b></summary><p>
<h4>Database can have multiple tables</h4>
~~~sql
CREATE DATABASE name_of_database;

# Add semi-colon at the end to finish your command.
~~~
</p></details>

<details><summary>3. Use Specific <b>Database</b></summary><p>
~~~
USE name_of_db;

####### OUTPUT #########
Database Changed.
~~~
</p></details>

<details><summary>4. <b>Import/Source</b> Existing database into MySQL</summary><p>
~~~
# NOTE: you need to create an empty database first, the use it, then source the existing database.

SOURCE path/to/database.sql;
~~~
</p></details><br>

<details><summary>5. <b>Show All Available Tables</b> in Database</summary><p>
~~~
SHOW TABLES;

##### Output ####
+------------------+
| Tables_in_imdb   |
+------------------+
| actors           |
| directors        |
| directors_genres |
| movies           |
| movies_directors |
| movies_genres    |
| roles            |
+------------------+
7 rows in set (0.00 sec)

~~~
</p></details>

<details><summary>6. Show <b>Description & Columns</b> in a Table</summary><p>
~~~
DESCRIBE <table_name>;

##### Output ######
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| id         | int(11)      | NO   | PRI | 0       |       |
| first_name | varchar(100) | YES  | MUL | NULL    |       |
| last_name  | varchar(100) | YES  | MUL | NULL    |       |
| gender     | char(1)      | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+
4 rows in set (0.04 sec)

# Field: has the name of the column.
# Type: has the type of the values in that column.
# Null: means that column can have Null values.
# Key: whether it's Primary or MULtiple (means one value can occur many times)
# Default: means default value of no value is assigned.
# Extra:
~~~
</p></details><br>

<details><summary>7. <b>SELECT</b>: to see values of columns</summary><p>
```sql
# Show all row for all columns, since "*" means all columns
SELECT * FROM <table_name>;

# Select specific columns from table.
SELECT <col_name>, <col_name> FROM <table_name>; 

# The output is called "Result-set" and it's actually a table contains a set of rows with column names.
# NOTE: Always use specific columns to select because it will be much faster than collecting all the data.
#result-set: a set of rows that form the result of a query along with column-names and meta-data.
# SELECT will select the rows with the same order in the table.
```
</p></details>

<details><summary>8. <b>LIMIT/OFFSET</b>: to make selecting rows flexiable</summary><p>
~~~sql
# 1. Using Limit: will limit the number of rows to the number assigned in the command.
# In this example, select only the first 20 rows
SELECT <col_name>, <col_name> FROM <table_name> LIMIT 20

# 2. Using OFFSET: will make MySQL start selecting from row numbered that offset.
# In this example, select 20 rows starting from offset 20
SELECT <col_name>, <col_name> FROM <table_name> LIMIT 20 OFFSET 20
~~~
</p></details>

<details><summary>9. <b>ORDER BY:</b> to order the selected rows</summary><p>
~~~sql
# NOTE: the default ordering is Ascending (from low to high)
SELECT <col_name>, <col_name> FROM <table_name> ORDER BY <col_name> DESC/ASC LIMIT 5;

# Output
+---------------------+-----------+------+
| name                | rankscore | year |
+---------------------+-----------+------+
| Horse Shoeing       |      NULL | 1893 |
| Blacksmith Scene    |       6.8 | 1893 |
| Carnival Dance, The |      NULL | 1894 |
| Armand D'Ary        |      NULL | 1894 |
| Caicedo (with Pole) |      NULL | 1894 |
+---------------------+-----------+------+
5 rows in set (0.13 sec)

~~~
</p></details>

<details><summary>10. <b>DISTINCT</b>: to show unique values in a column</summary><p>
~~~
# Show Unique values in a column
SELECT DISTINCT <col_name> FROM <table_name>;

# Select Unique combination between multiple columns
SELECT DISTINCT <col_name>, <col_name> FROM <table_name>;
~~~
</p></details>

<details><summary>11. <b>WHERE</b>: to apply condition/filter on the selected data</summary><p>
~~~
# list all movies with rankscore>9
SELECT <col_name>, <col_name>, <col_name> FROM <table_name> WHERE <col_name> > 9 ;

# Condition's outputs: TRUE, FALSE, NULL

# Comparison Operators:
# =: equals
# <> or !=: Not Equals
#  <: Less than
# <=: Less than or equal
# >: Greater than
# >= : Greater than or equal

SELECT * FROM <table_name> WHERE <col_name> = 'Comedy';

SELECT * FROM <table_name> WHERE <col_name> <> 'Horror';

#### BIG NOTE #####
# NULL => doesnot-exist/unknown/missing

# "=" doesnot work with NULL, will give you an empty result-set.
# Instead we use "IS NULL" or "IS NOT NULL"
SELECT <col_name>,<col_name>,<col_name> FROM <table_name> WHERE <col_name> = NULL;


SELECT <col_name>,<col_name>,<col_name> FROM <table_name> WHERE <col_name> IS NULL LIMIT 20;

SELECT name,year,rankscore FROM <table_name> WHERE rankscore IS NOT NULL LIMIT 20;
~~~
</p></details>

<details><summary>12. <b>Logical Operators</b></summary><p>
<h4>1. Using AND:</h4>
~~~
SELECT name,year,rankscore FROM movies WHERE rankscore>9 AND year>2000;
~~~
<h4>2. Using OR:</h4>
~~~mysql
SELECT name,year,rankscore FROM movies WHERE rankscore>9 OR year>2007;
~~~
<h4>3. Using NOT:</h4>
~~~
SELECT name,year,rankscore FROM movies WHERE NOT year<=2000 LIMIT 20;
~~~
<h4>4. Using BETWEEN:</h4>
~~~
SELECT name,year,rankscore FROM movies WHERE year BETWEEN 1999 AND 2000;
#inclusive: year>=1999 and year<=2000
# Both 1999 and 2000 are included.
#### BIG NOTE: if the first number is larger than the second number, this command won't work.
~~~
<h4>5. Using IN:</h4>
~~~
SELECT director_id, genre FROM directors_genres WHERE genre IN ('Comedy','Horror');
# same as genre='Comedy' OR genre='Horror'
~~~
<h4>6. Using LIKE:</h4>
~~~
SELECT name,year,rankscore FROM movies WHERE name LIKE 'Tis%';
# % => wildcard character to imply zero or more characters


SELECT first_name, last_name FROM actors WHERE first_name LIKE '%es';
# first name ending in 'es'


SELECT first_name, last_name FROM actors WHERE first_name LIKE '%es%';
#first name contains 'es'


SELECT first_name, last_name FROM actors WHERE first_name LIKE 'Agn_s';
# '_' implies exactly one character.


# If we want to macth % or _, we should use the backslash as the escape character: \% and \_


SELECT first_name, last_name FROM actors WHERE first_name LIKE 'L%' AND first_name NOT LIKE 'Li%';
~~~
</p></details> 

<details><summary>13. <b>Aggregate Functions</b></summary><p>
<h4>1. COUNT</h4>
~~~
SELECT COUNT(*) FROM movies;

SELECT COUNT(*) FROM movies where year>2000;

SELECT COUNT(year) FROM movies;
~~~

<h4>2. MIN & MAX</h4>
~~~
SELECT MIN(year) FROM movies;


SELECT MAX(year) FROM movies;
~~~

<h4>3. SUM & AVG</h4>
~~~
SELECT SUM(price) FROM movies;


SELECT AVG(price) FROM movies;
~~~
</p></details>

<details><summary>14. <b>GROUP BY</b></summary><p>
~~~
# find number of movies released per year

SELECT year, COUNT(year) FROM movies GROUP BY year;

SELECT year, COUNT(year) FROM movies GROUP BY year ORDER BY year;

########## Using Aliases #######
SELECT year, COUNT(year) year_count FROM movies GROUP BY year ORDER BY year_count;
# year_count is an alias.

# often used with COUNT, MIN, MAX or SUM.
# if grouping columns contain NULL values, all null values are grouped together.
~~~
</p></details>

<details><summary>15. <b>HAVING</b></summary><p>
~~~
# Print years which have >1000 movies in our DB [Data Scientist for Analysis]

SELECT year, COUNT(year) year_count FROM movies GROUP BY year HAVING year_count>1000;
# specify a condition on groups using HAVING.


Order of execution:
1. GROUP BY to create groups
2. apply the AGGREGATE FUNCTION
3. Apply HAVING condition.


# often used along with GROUP BY. Not Mandatory.

SELECT name, year  FROM movies HAVING year>2000;
# HAVING without GROUP BY is same as WHERE



SELECT year, COUNT(year) year_count FROM movies WHERE rankscore>9 GROUP BY year HAVING year_count>20;

# HAVING vs WHERE
## WHERE is applied on individual rows while HAVING is applied on groups.
## HAVING is applied after grouping while WHERE is used before grouping.
~~~
</p></details>

<details><summary>16. <b>Keyword Order</b></summary><p>
<p><a href="https://dev.mysql.com/doc/refman/8.0/en/select.html"><b>Ref</b></a> </p>
~~~
SELECT
    [ALL | DISTINCT | DISTINCTROW ]
      [HIGH_PRIORITY]
      [STRAIGHT_JOIN]
      [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
      [SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
    select_expr [, select_expr ...]
    [FROM table_references
      [PARTITION partition_list]
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}, ... [WITH ROLLUP]]
    [HAVING where_condition]
    [WINDOW window_name AS (window_spec)
        [, window_name AS (window_spec)] ...]
    [ORDER BY {col_name | expr | position}
      [ASC | DESC], ... [WITH ROLLUP]]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    [INTO OUTFILE 'file_name'
        [CHARACTER SET charset_name]
        export_options
      | INTO DUMPFILE 'file_name'
      | INTO var_name [, var_name]]
    [FOR {UPDATE | SHARE} [OF tbl_name [, tbl_name] ...] [NOWAIT | SKIP LOCKED] 
      | LOCK IN SHARE MODE]]
~~~
</p></details>

<details><summary>17. <b>JOIN...ON</b>: combine data from multiple tables</summary><p>
<p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Web/www.w3schools.com/www.w3schools.com/sql/sql_join.html"><b>W3School on JOIN</b></a> </p>
<h4>1. Natural Join</h4> 
~~~
# natural join: a join where we have the same column-names across two tables.
#T1: C1, C2
#T2: C1, C3, C4

SELECT * FROM T1 JOIN T2;

SELECT * FROM T1 JOIN T2 USING (C1);

# returns C1,C2,C3,C4
# no need to use the keyword "ON"
~~~

<h4>2. Inner Join</h4>
~~~
# For each movie, print name and the genres
SELECT m.name, g.genre from movies m  JOIN movies_genres g ON m.id=g.movie_id LIMIT 20;

# table aliases: m and g
~~~

<h4>3. Left Outer Join</h4>
~~~
SELECT m.name, g.genre from movies m  LEFT JOIN movies_genres g ON m.id=g.movie_id LIMIT 20;

#LEFT JOIN or LEFT OUTER JOIN
#RIGHT JOIN or RIGHT OUTER JOIN
#FULL JOIN or FULL OUTER JOIN
#JOIN or INNER JOIN
~~~

<h4>4. Right Outer Join</h4>
~~~
SELECT m.name, g.genre from movies m  RIGHT JOIN movies_genres g ON m.id=g.movie_id LIMIT 20;

#LEFT JOIN or LEFT OUTER JOIN
#RIGHT JOIN or RIGHT OUTER JOIN
#FULL JOIN or FULL OUTER JOIN
#JOIN or INNER JOIN
~~~

<h4>5. Full Outer Join</h4>
~~~
SELECT m.name, g.genre from movies m  FULL JOIN movies_genres g ON m.id=g.movie_id LIMIT 20;

#LEFT JOIN or LEFT OUTER JOIN
#RIGHT JOIN or RIGHT OUTER JOIN
#FULL JOIN or FULL OUTER JOIN
#JOIN or INNER JOIN
~~~

<h4>6. K-ways Join</h4>
~~~
# NULL for missing counterpart rows.

# 3-way joins and k-way joins
SELECT a.first_name, a.last_name FROM actors a JOIN roles r ON a.id=r.actor_id JOIN movies m on m.id=r.movie_id AND m.name='Officer 444';

#Practical note about joins: Joins can be expensive computationally when we have large tables.
~~~
</p></details>

<details><summary>18. <b>Nested Queries</b></summary><p>
~~~
# Sub-Queries or Nested Queries or Inner Queries

# Examble:

# List all actors in the movie Schindler's List
#https://www.imdb.com/title/tt0108052/fullcredits/?ref_=tt_ov_st_sm


SELECT first_name, last_name from actors WHERE id IN 
	( SELECT actor_id from roles WHERE movie_id IN 
			(SELECT id FROM movies where name='Schindler's List)
	);



# Syntax:
SELECT column_name [, column_name ]
FROM   table1 [, table2 ]
WHERE  column_name OPERATOR
   (SELECT column_name [, column_name ]
   FROM table1 [, table2 ]
   [WHERE])

# first the inner query is executed and then the outer query is executed using the output values in the inner query


# IN, NOT IN, EXISTS, NOT EXISTS, ANY, ALL, Comparison operators

#EXISTS returns true if the subquery returns one or more records or NULL
# ANY operator returns TRUE if any of the subquery values meet the condition.
# ALL operator returns TRUE if all of the subquery values meet the condition.



SELECT * FROM movies where rankscore >= ALL (SELECT MAX(rankscore) from movies);
# get all movies whose rankscore is same as the maximum rankscore.

# e.g: rankscore <> ALL(...)
~~~
</p></details><br>

<details><summary>19. <b>Data Manipulation</b>: SELECT, INSERT, UPDATE, DELETE</summary><p>
<h4>2. INSERT</h4>
~~~
# Data Manupulation Language: SELECT, INSERT, UPDATE, DELETE

INSERT INTO movies(id, name, year, rankscore) VALUES (412321, 'Thor', 2011, 7);

INSERT INTO movies(id, name, year, rankscore) VALUES (412321, 'Thor', 2011, 7), (412322, 'Iron Man', 2008, 7.9), (412323, 'Iron Man 2', 2010, 7);


# INSERT FROM one table to annother using nnested sub query: https://en.wikipedia.org/wiki/Insert_(SQL)#Copying_rows_from_other_tables
~~~

<h4>3. UPDATE</h4>
~~~
UPDATE <TableName> SET col1=val1, col2=val2 WHERE condition

UPDATE movies SET rankscore=9 where id=412321;

# Update multiple rows also.
# Can be used along with Sub-queries.
~~~

<h4>4. DELETE</h4>
~~~
DELETE FROM movies WHERE id=412321;

# Remove all rows: TRUNCATE TABLE TableName; 
# Same as selete without a WHERE Clause.
~~~
</p></details>

<details><summary>20. <b>Data Definition Language:</b> to define/modify tables.</summary><p>
<ul>
<li><a href="https://www.journaldev.com/16774/sql-data-types"><b>DataTypes</b></a></li>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Web/www.w3schools.com/www.w3schools.com/sql/sql_constraints.html"><b>Constraints</b></a></li></ul>
~~~
CREATE TABLE language  ( id INT PRIMARY, lang VARCHAR(50) NOT NULL);


# NOT NULL - Ensures that a column cannot have a NULL value
# UNIQUE - Ensures that all values in a column are different
# PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
# FOREIGN KEY - Uniquely identifies a row/record in another table
# CHECK - Ensures that all values in a column satisfies a specific condition
# DEFAULT - Sets a default value for a column when no value is specified
# INDEX - Used to create and retrieve data from the database very quickly
~~~
</p></details>

<details><summary>21. <b>ALTER:</b> ADD, MODIFY, DROP columns in a table</summary><p>
~~~
# ALTER: ADD, MODIFY, DROP

ALTER TABLE language ADD country VARCHAR(50);

ALTER TABLE language MODIFY country VARCHAR(60);

ALTER TABLE langauge DROP country;
~~~
</p></details>

<details><summary>22. <b>DROP:</b> to drop tables</summary><p>
~~~
# Removes both the table and all of the data permanently.
DROP TABLE Tablename;

DROP TABLE TableName IF EXISTS;

#https://dev.mysql.com/doc/refman/8.0/en/drop-table.html

TRUNCATE TABLE TableName;

# as discussed earlier same as DELETE FROM TableName;
~~~
</p></details><br>

<details><summary>24. <b>Data Control Language</b> for DB Admins.
</summary><p>
~~~
https://en.wikipedia.org/wiki/Data_control_language
https://dev.mysql.com/doc/refman/8.0/en/grant.html
https://dev.mysql.com/doc/refman/8.0/en/revoke.html
~~~
</p></details>

</div>































