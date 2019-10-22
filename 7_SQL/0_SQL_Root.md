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
</p></details>

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
</p></details>

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

<details><summary>2. Create <b>Database</b></summary><p>
<h4>Database can have multiple tables</h4>
~~~sql
CREATE DATABASE name_of_database;

# Add semi-colon at the end to finish your command.
~~~
</p></details>

<details><summary>2. Create <b>Database</b></summary><p>
<h4>Database can have multiple tables</h4>
~~~sql
CREATE DATABASE name_of_database;

# Add semi-colon at the end to finish your command.
~~~
</p></details>

<details><summary>2. Create <b>Database</b></summary><p>
<h4>Database can have multiple tables</h4>
~~~sql
CREATE DATABASE name_of_database;

# Add semi-colon at the end to finish your command.
~~~
</p></details>

</div>