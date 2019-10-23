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

<details><summary>10. <b>DISTINCT</b>: to show unique values in a column</summary><p>
~~~
# Show Unique values in a column
SELECT DISTINCT <col_name> FROM <table_name>;

# Select Unique combination between multiple columns
SELECT DISTINCT <col_name>, <col_name> FROM <table_name>;
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

</div>