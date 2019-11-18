<h1 style='text-decoration:underline'>Hadoop & MapReduce Code</h1>


<div style='width:1000px;margin:auto'>
<p><a href="https://docs.google.com/document/d/1MZ_rNxJhR4HCU1qJ2-w7xlk2MTHVqa9lnl_uj-zRkzk/pub" style="font-weight:bold">Transfer Files back and forth to the VM</a> </p>
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

<details><summary><b>Get a file From HDFS</b></summary><p>
~~~
# Get file.txt to /
hadoop fs -get file.txt /
~~~
</p></details>


<details><summary><b>head & tail</b></summary><p>
~~~
hadoop fs -tail /file.txt
~~~
</p></details>

<details><summary><b>Rename file</b></summary><p>
~~~
hadoop fs -mv file.txt newname.txt
~~~
</p></details>

<details><summary><b>Delete file</b></summary><p>
~~~
hadoop fs -rm file.txt
~~~
</p></details>

<details><summary><b>Create Folder</b></summary><p>
~~~
hadoop fs -mkdir myfolder
~~~
</p></details>

<hr>
<details><summary><b>Mapper() [Python]</b></summary><p>
<h4>Hadoop Streaming allows you to write your code for mapper and reducer in any language. The default is Java</h4>
~~~
# Your task is to make sure that this mapper code does not fail on corrupt data lines,
# but instead just ignores them and continues working
import sys

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        # This is the place you need to do some defensive programming
        # what if there are not exactly 6 fields in that line?
        # YOUR CODE HERE
        if len(data) == 6:
            date, time, store, item, cost, payment = data
        else:
            continue
        # this next line is called 'multiple assignment' in Python
        # this is not really necessary, we could access the data
        # with data[2] and data[5], but we do this for conveniency
        # and to make the code easier to read
        # date, time, store, item, cost, payment = data
        
        # Now print out the data that will be passed to the reducer
        print "{0}\t{1}".format(store, cost)
        
test_text = """2013-10-09\t13:22\tMiami\tBoots\t99.95\tVisa
2013-10-09\t13:22\tNew York\tDVD\t9.50\tMasterCard
2013-10-09 13:22:59 I/O Error
^d8x28orz28zoijzu1z1zp1OHH3du3ixwcz114<f
1\t2\t3"""

# This function allows you to test the mapper with the provided test string
def main():
	import StringIO
	sys.stdin = StringIO.StringIO(test_text)
	mapper()
	sys.stdin = sys.__stdin__
~~~
</p></details>

<details><summary><b>Reducer() [Python]</b></summary><p>
<h4>Hadoop Streaming allows you to write your code for mapper and reducer in any language. The default is Java</h4>
~~~
import sys

salesTotal = 0
oldKey      = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
		
	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
		print(oldKey, "\t", salesTotal)
		oldKey = thisKey
		salesTotal = 0
		
		oldKey = thisKey
		salesTotal += float(thisSale)
		
if oldKey != None:
	print(oldKey, "\t", salesTotal)
~~~
</p></details>

<details><summary><b>Test Mapper() & Reducer</b></summary><p>
<p><a href="https://www.youtube.com/watch?v=MYo8EZwDRUA">Video</a> </p>
</p></details>

</div>































