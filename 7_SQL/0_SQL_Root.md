<h1 style='text-decoration:underline'>SQL</h1>

<h2 style='width:500px;margin:auto'>Declarative Programming Language</h2>

<p><br></p>

<div style='width:1000px;margin:auto'>

<a href="1_SQL_Interview_Questions.html" style="font-weight:bold;font-size:17px">SQL Interview Questions</a>
<hr>
<details><summary>Start <b>MySQL</b> in the <b>Command Line</b></summary><p><pre><code>mysql -u root -p

# Then write your password "root"
# -u: used to use the username
# root: the name of the user
# -p: means I'll give the password.
</code></pre>
</p></details>

<details><summary>Create <b>Database</b></summary><p>
<h4>Database can have multiple tables</h4><pre><code class="sql language-sql">CREATE DATABASE name_of_database;

# Add semi-colon at the end to finish your command.
</code></pre>
</p></details>

<details><summary><b>Show All Available Databases</b> in Database</summary><p><pre><code>SHOW DATABASES;
</code></pre>
</p></details>

<details><summary>Use Specific <b>Database</b></summary><p><pre><code>USE name_of_db;

####### OUTPUT #########
Database Changed.
</code></pre>
</p></details>

<details><summary>Create <b>Table</b></summary><p>
<pre><code class="sql language-sql">CREATE TABLE student ( 
    student_id INT PRIMARY KEY, 
    name VARCHAR(20), 
    major VARCHAR(20)
);

# OR
CREATE TABLE student ( 
    student_id INT, 
    name VARCHAR(20), 
    major VARCHAR(20),
    PRIMARY KEY(student)
);

# Add semi-colon at the end to finish your command.
</code></pre>
</p></details>

<details><summary><b>Import/Source</b> Existing database into MySQL</summary><p><pre><code># NOTE: you need to create an empty database first, the use it, then source the existing database.

SOURCE path/to/database.sql;
</code></pre>
</p></details><br>

<details><summary><b>Show All Available Tables</b> in Database</summary><p><pre><code>SHOW TABLES;

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
</code></pre>
</p></details>

<details><summary>Show <b>Description & Columns</b> in a Table</summary><p><pre><code>DESCRIBE &lt;table_name&gt;;

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
</code></pre>
</p></details><br>

<details><summary>7. <b>SELECT</b>: to see values of columns</summary><p><pre><code class="sql language-sql"># Show all row for all columns, since "*" means all columns
SELECT * FROM &lt;table_name&gt;;

# Select specific columns from table.
SELECT &lt;col_name&gt;, &lt;col_name&gt; FROM &lt;table_name&gt;; 

# The output is called "Result-set" and it's actually a table contains a set of rows with column names.
# NOTE: Always use specific columns to select because it will be much faster than collecting all the data.
#result-set: a set of rows that form the result of a query along with column-names and meta-data.
# SELECT will select the rows with the same order in the table.
</code></pre>
</p></details>

<details><summary><b>LIMIT/OFFSET</b>: to make selecting rows flexiable</summary><p><pre><code class="sql language-sql"># 1. Using Limit: will limit the number of rows to the number assigned in the command.
# In this example, select only the first 20 rows
SELECT &lt;col_name&gt;, &lt;col_name&gt; FROM &lt;table_name&gt; LIMIT 20

# 2. Using OFFSET: will make MySQL start selecting from row numbered that offset.
# In this example, select 20 rows starting from offset 20
SELECT &lt;col_name&gt;, &lt;col_name&gt; FROM &lt;table_name&gt; LIMIT 20 OFFSET 20
</code></pre>
</p></details>

<details><summary><b>AS</b></summary><p><pre><code class="sql language-sql">SELECT first_name AS forename, last_name AS surname FROM employee;

+----------+----------+
| forename | surname  |
+----------+----------+
| David    | Wallace  |
| Jan      | Levinson |
| Michael  | Scott    |
| Angela   | Martin   |
| Kelly    | Kapoor   |
| Stanley  | Hudson   |
| Josh     | Porter   |
| Andy     | Bernard  |
| Jim      | Halpert  |
+----------+----------+

</code></pre>
</p></details>

<details><summary><b>ORDER BY:</b> to order the selected rows</summary><p><pre><code class="sql language-sql"># NOTE: the default ordering is Ascending (from low to high)
SELECT &lt;col_name&gt;, &lt;col_name&gt; FROM &lt;table_name&gt; ORDER BY &lt;col_name&gt; DESC/ASC LIMIT 5;

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
</code></pre>
</p></details>

<details><summary><b>WildCards</b></summary><p><pre><code class="sql language-sql">-- % = any # characters, _ = one character

-- Find any client's who are an LLC
SELECT *
FROM client
WHERE client_name LIKE '%LLC';

-- Find any branch suppliers who are in the label business
SELECT *
FROM branch_supplier
WHERE supplier_name LIKE '% Label%';

-- Find any employee born on the 10th day of the month
SELECT *
FROM employee
WHERE birth_day LIKE '_____10%';

-- Find any clients who are schools
SELECT *
FROM client
WHERE client_name LIKE '%Highschool%';
</code></pre>
</p></details>

<details><summary><b>Unions</b></summary><p><pre><code class="sql language-sql">-- Find a list of employee and branch names
SELECT employee.first_name AS Employee_Branch_Names
FROM employee
UNION
SELECT branch.branch_name
FROM branch;

-- Find a list of all clients & branch suppliers' names
SELECT client.client_name AS Non-Employee_Entities, client.branch_id AS Branch_ID
FROM client
UNION
SELECT branch_supplier.supplier_name, branch_supplier.branch_id
FROM branch_supplier;

</code></pre>
</p></details>


<details><summary><b>DISTINCT</b>: to show unique values in a column</summary><p><pre><code># Show Unique values in a column
SELECT DISTINCT &lt;col_name&gt; FROM &lt;table_name&gt;;

# Select Unique combination between multiple columns
SELECT DISTINCT &lt;col_name&gt;, &lt;col_name&gt; FROM &lt;table_name&gt;;
</code></pre>
</p></details>

<details><summary><b>WHERE</b>: to apply condition/filter on the selected data</summary><p><pre><code># list all movies with rankscore&gt;9
SELECT &lt;col_name&gt;, &lt;col_name&gt;, &lt;col_name&gt; FROM &lt;table_name&gt; WHERE &lt;col_name&gt; &gt; 9 ;

# Condition's outputs: TRUE, FALSE, NULL

# Comparison Operators:
# =: equals
# &lt;&gt; or !=: Not Equals
#  &lt;: Less than
# &lt;=: Less than or equal
# &gt;: Greater than
# &gt;= : Greater than or equal

SELECT * FROM &lt;table_name&gt; WHERE &lt;col_name&gt; = 'Comedy';

SELECT * FROM &lt;table_name&gt; WHERE &lt;col_name&gt; &lt;&gt; 'Horror';

#### BIG NOTE #####
# NULL =&gt; doesnot-exist/unknown/missing

# "=" doesnot work with NULL, will give you an empty result-set.
# Instead we use "IS NULL" or "IS NOT NULL"
SELECT &lt;col_name&gt;,&lt;col_name&gt;,&lt;col_name&gt; FROM &lt;table_name&gt; WHERE &lt;col_name&gt; = NULL;


SELECT &lt;col_name&gt;,&lt;col_name&gt;,&lt;col_name&gt; FROM &lt;table_name&gt; WHERE &lt;col_name&gt; IS NULL LIMIT 20;

SELECT name,year,rankscore FROM &lt;table_name&gt; WHERE rankscore IS NOT NULL LIMIT 20;
</code></pre>
</p></details>

<details><summary><b>Logical Operators</b></summary><p>
<h4>1. Using AND:</h4><pre><code>SELECT name,year,rankscore FROM movies WHERE rankscore&gt;9 AND year&gt;2000;
</code></pre>
<h4>2. Using OR:</h4><pre><code class="mysql language-mysql">SELECT name,year,rankscore FROM movies WHERE rankscore&gt;9 OR year&gt;2007;
</code></pre>
<h4>3. Using NOT:</h4><pre><code>SELECT name,year,rankscore FROM movies WHERE NOT year&lt;=2000 LIMIT 20;
</code></pre>
<h4>4. Using BETWEEN:</h4><pre><code>SELECT name,year,rankscore FROM movies WHERE year BETWEEN 1999 AND 2000;
#inclusive: year&gt;=1999 and year&lt;=2000
# Both 1999 and 2000 are included.
#### BIG NOTE: if the first number is larger than the second number, this command won't work.
</code></pre>
<h4>5. Using IN:</h4><pre><code>SELECT director_id, genre FROM directors_genres WHERE genre IN ('Comedy','Horror');
# same as genre='Comedy' OR genre='Horror'
</code></pre>
<h4>6. Using LIKE:</h4><pre><code>SELECT name,year,rankscore FROM movies WHERE name LIKE 'Tis%';
# % =&gt; wildcard character to imply zero or more characters


SELECT first_name, last_name FROM actors WHERE first_name LIKE '%es';
# first name ending in 'es'


SELECT first_name, last_name FROM actors WHERE first_name LIKE '%es%';
#first name contains 'es'


SELECT first_name, last_name FROM actors WHERE first_name LIKE 'Agn_s';
# '_' implies exactly one character.


# If we want to macth % or _, we should use the backslash as the escape character: \% and \_


SELECT first_name, last_name FROM actors WHERE first_name LIKE 'L%' AND first_name NOT LIKE 'Li%';
</code></pre>
</p></details> 

<details><summary>13. <b>Aggregate Functions</b></summary><p>
<h4>1. COUNT</h4><pre><code>SELECT COUNT(*) FROM movies;

SELECT COUNT(*) FROM movies where year&gt;2000;

SELECT COUNT(year) FROM movies;
</code></pre>

<h4>2. MIN & MAX</h4><pre><code>SELECT MIN(year) FROM movies;


SELECT MAX(year) FROM movies;
</code></pre>

<h4>3. SUM & AVG</h4><pre><code>SELECT SUM(price) FROM movies;


SELECT AVG(price) FROM movies;
</code></pre>
</p></details>

<details><summary>14. <b>GROUP BY</b></summary><p><pre><code># find number of movies released per year

SELECT year, COUNT(year) FROM movies GROUP BY year;

SELECT year, COUNT(year) FROM movies GROUP BY year ORDER BY year;

########## Using Aliases #######
SELECT year, COUNT(year) year_count FROM movies GROUP BY year ORDER BY year_count;
# year_count is an alias.

# often used with COUNT, MIN, MAX or SUM.
# if grouping columns contain NULL values, all null values are grouped together.
</code></pre>
</p></details>

<details><summary>15. <b>HAVING</b></summary><p><pre><code># Print years which have &gt;1000 movies in our DB [Data Scientist for Analysis]

SELECT year, COUNT(year) year_count FROM movies GROUP BY year HAVING year_count&gt;1000;
# specify a condition on groups using HAVING.


Order of execution:
1. GROUP BY to create groups
2. apply the AGGREGATE FUNCTION
3. Apply HAVING condition.


# often used along with GROUP BY. Not Mandatory.

SELECT name, year  FROM movies HAVING year&gt;2000;
# HAVING without GROUP BY is same as WHERE



SELECT year, COUNT(year) year_count FROM movies WHERE rankscore&gt;9 GROUP BY year HAVING year_count&gt;20;

# HAVING vs WHERE
## WHERE is applied on individual rows while HAVING is applied on groups.
## HAVING is applied after grouping while WHERE is used before grouping.
</code></pre>
</p></details>

<details><summary>16. <b>Keyword Order</b></summary><p>
<p><a href="https://dev.mysql.com/doc/refman/8.0/en/select.html"><b>Ref</b></a> </p><pre><code>SELECT
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
</code></pre>
</p></details>

<details><summary>17. <b>JOIN...ON</b>: combine data from multiple tables</summary><p>
<p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Web/www.w3schools.com/www.w3schools.com/sql/sql_join.html"><b>W3School on JOIN</b></a> </p>
<h4>1. Natural Join</h4> <pre><code># natural join: a join where we have the same column-names across two tables.
#T1: C1, C2
#T2: C1, C3, C4

SELECT * FROM T1 JOIN T2;

SELECT * FROM T1 JOIN T2 USING (C1);

# returns C1,C2,C3,C4
# no need to use the keyword "ON"
</code></pre>

<h4>2. Inner Join</h4><pre><code># For each movie, print name and the genres
SELECT m.name, g.genre from movies m  JOIN movies_genres g ON m.id=g.movie_id LIMIT 20;

# table aliases: m and g
</code></pre>

<h4>3. Left Outer Join</h4><pre><code>SELECT m.name, g.genre from movies m  LEFT JOIN movies_genres g ON m.id=g.movie_id LIMIT 20;

#LEFT JOIN or LEFT OUTER JOIN
#RIGHT JOIN or RIGHT OUTER JOIN
#FULL JOIN or FULL OUTER JOIN
#JOIN or INNER JOIN
</code></pre>

<h4>4. Right Outer Join</h4><pre><code>SELECT m.name, g.genre from movies m  RIGHT JOIN movies_genres g ON m.id=g.movie_id LIMIT 20;

#LEFT JOIN or LEFT OUTER JOIN
#RIGHT JOIN or RIGHT OUTER JOIN
#FULL JOIN or FULL OUTER JOIN
#JOIN or INNER JOIN
</code></pre>

<h4>5. Full Outer Join</h4><pre><code>SELECT m.name, g.genre from movies m  FULL JOIN movies_genres g ON m.id=g.movie_id LIMIT 20;

#LEFT JOIN or LEFT OUTER JOIN
#RIGHT JOIN or RIGHT OUTER JOIN
#FULL JOIN or FULL OUTER JOIN
#JOIN or INNER JOIN
</code></pre>

<h4>6. K-ways Join</h4><pre><code># NULL for missing counterpart rows.

# 3-way joins and k-way joins
SELECT a.first_name, a.last_name FROM actors a JOIN roles r ON a.id=r.actor_id JOIN movies m on m.id=r.movie_id AND m.name='Officer 444';

#Practical note about joins: Joins can be expensive computationally when we have large tables.
</code></pre>
</p></details>

<details><summary>18. <b>Nested Queries</b></summary><p><pre><code># Sub-Queries or Nested Queries or Inner Queries

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



SELECT * FROM movies where rankscore &gt;= ALL (SELECT MAX(rankscore) from movies);
# get all movies whose rankscore is same as the maximum rankscore.

# e.g: rankscore &lt;&gt; ALL(...)
</code></pre>
</p></details><br>

<details><summary>19. <b>Data Manipulation</b>: SELECT, INSERT, UPDATE, DELETE</summary><p>
<h4>2. INSERT</h4><pre><code># Data Manupulation Language: SELECT, INSERT, UPDATE, DELETE

INSERT INTO movies(id, name, year, rankscore) VALUES (412321, 'Thor', 2011, 7);

INSERT INTO movies(id, name, year, rankscore) VALUES (412321, 'Thor', 2011, 7), (412322, 'Iron Man', 2008, 7.9), (412323, 'Iron Man 2', 2010, 7);


# INSERT FROM one table to annother using nnested sub query: https://en.wikipedia.org/wiki/Insert_(SQL)#Copying_rows_from_other_tables
</code></pre>

<h4>3. UPDATE</h4><pre><code>UPDATE &lt;TableName&gt; SET col1=val1, col2=val2 WHERE condition

UPDATE movies SET rankscore=9 where id=412321;

# Update multiple rows also.
# Can be used along with Sub-queries.
</code></pre>

<h4>4. DELETE</h4><pre><code>DELETE FROM movies WHERE id=412321;

# Remove all rows: TRUNCATE TABLE TableName; 
# Same as selete without a WHERE Clause.
</code></pre>
</p></details>

<details><summary>20. <b>Data Definition Language:</b> to define/modify tables.</summary><p>
<ul>
<li><a href="https://www.journaldev.com/16774/sql-data-types"><b>DataTypes</b></a></li>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Web/www.w3schools.com/www.w3schools.com/sql/sql_constraints.html"><b>Constraints</b></a></li></ul><pre><code>CREATE TABLE language  ( id INT PRIMARY, lang VARCHAR(50) NOT NULL);


# NOT NULL - Ensures that a column cannot have a NULL value
# UNIQUE - Ensures that all values in a column are different
# PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
# FOREIGN KEY - Uniquely identifies a row/record in another table
# CHECK - Ensures that all values in a column satisfies a specific condition
# DEFAULT - Sets a default value for a column when no value is specified
# INDEX - Used to create and retrieve data from the database very quickly
</code></pre>
</p></details>

<details><summary><b>ALTER:</b> ADD, MODIFY, DROP columns in a table</summary><p><pre><code># ALTER: ADD, MODIFY, DROP

ALTER TABLE language ADD country VARCHAR(50);

ALTER TABLE language MODIFY country VARCHAR(60);

ALTER TABLE langauge DROP country;
</code></pre>
</p></details>

<details><summary><b>Add Foriegn key</b></summary><p><pre><code># Create foreign key where the referenced table is already created.
CREATE TABLE branch ( branch_id INT PRIMARY KEY, branch_name VARCHAR(40), mgr_id INT, mgr_start_date DATE, FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL);

# Create foreign key before creating the referenced table.
# super_id is foriegn key to the same table.
# branch_id is foriegn key to 'branch' table.
create table employee ( emp_id INT PRIMARY KEY, first_name VARCHAR(20), last_name VARCHAR(20), birth_date DATE, sex VARCHAR(1), salary INT, super_id INT, branch_id INT);

ALTER TABLE employee ADD FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL;
</code></pre>
</p></details>

<details><summary><b>DROP:</b> to drop tables</summary><p><pre><code># Removes both the table and all of the data permanently.
DROP TABLE Tablename;

DROP TABLE TableName IF EXISTS;

#https://dev.mysql.com/doc/refman/8.0/en/drop-table.html

TRUNCATE TABLE TableName;

# as discussed earlier same as DELETE FROM TableName;
</code></pre>
</p></details><br>

<details><summary>24. <b>Data Control Language</b> for DB Admins.
</summary><p><pre><code>https://en.wikipedia.org/wiki/Data_control_language
https://dev.mysql.com/doc/refman/8.0/en/grant.html
https://dev.mysql.com/doc/refman/8.0/en/revoke.html
</code></pre>
</p></details>

</div>