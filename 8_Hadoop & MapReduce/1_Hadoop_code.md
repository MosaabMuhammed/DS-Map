<h1 style='text-decoration:underline'>Hadoop Code</h1>


<div style='width:1000px;margin:auto'>

<details><summary><b>To Run Hadoop</b></summary><p>
~~~
ssh localhost
ssh 0.0.0.0
source /usr/local/hadoop-working/hadoop-evn

start-dfs.sh
start-yarn.sh
jps
~~~
</p></details>

<details><summary><b>See files in current directory</b></summary><p>
~~~
hadoop fs -ls / 
~~~
</p></details>

<details><summary><b>Add a file to HDFS</b></summary><p>
~~~
# Add file.txt to /
hadoop fs -put file.txt /
~~~
</p></details>

<details><summary><b>head & tail</b></summary><p>
~~~
hadoop fs -tail /file.txt
~~~
</p></details>

</div>































