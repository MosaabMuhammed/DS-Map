<h1 style='text-decoration:underline'>SQL</h1>

<details><summary>1. Start <b>MySQL</b> in the <b>Command Line</b></summary><p>
~~~
mysql -u root -p

# Then write your password "root"
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

<details><summary>1. Start <b>SQL</b> in the <b>Command Line</b></summary><p>
~~~
mysql -u root -p

# Then write your password "root"
~~~
</p></details>