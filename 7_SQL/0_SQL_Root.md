<h1 style='text-decoration:underline'>SQL</h1>

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
<h4>Database can have multiple tables</h4>
~~~sql
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