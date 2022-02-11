<h1>Python</h1>

<div style='width:1000px;margin:auto'>

<details><summary><b>OOP</b></summary><ul>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Class-Variables:'>Class Variables</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Class-Methods-and-Static-Methods:'>Class Methods & Static Methods</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Inheritance:'>Inheritance</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Multiple-Inhertance:'>Multiple Inheritance</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Magic/Dunder-Methods:'>Magic/Dunder Methods</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Property-Decorator:'>@property Decorator</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Encapsulation:'>Encapsulation</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Importing-Modules:'>Importing Modules</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Python-Composition:'>Composition</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Python-Aggregation:'>Aggregation</a></li>
<li><a style='color:#333;font-weight:bold' href='OOP.html#Abstract-Class:'>Abstract Class</a></li>
</ul></details>

<hr>

<details><summary><b>Tips & Tricks</b></summary><ul>

<details><summary><b>Looping over a range of numbers</b></summary><pre><code>for i in range(6):
    print(i)
</code></pre>
</details></li>

<details><summary><b>Looping over a collection</b></summary><pre><code>colors = ["green", "red", "blue", "black"]

for color in colors:
    print(color)
</code></pre>
</details>

<details><summary><b>Looping Backwards</b></summary><pre><code>colors = ["green", "red", "blue", "black"]

# Ugly
for i in range(len(colors)-1, -1, -1):
    print(colors[i])

# Pythonic
for color in reversed(colors):
    print(color)
</code></pre>
</details>

<details><summary><b>Looping over a collection and indices</b></summary><pre><code>colors = ["green", "red", "blue", "black"]

# Ugly
for i in range(len(colors)):
    print(i, colors[i])

# Pythonic
for i, color in enumerate(colors):
    print(i, color)
</code></pre>
</details>

<details><summary><b>Looping over 2 collections</b></summary><pre><code>colors = ["green", "red", "blue", "black"]
names = ["raymond", "rachel", "matthew"]

# Ugly
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '--&gt;', colors[i])


# Pythonic
for name, color in zip(names, colors):
    print(name, "--&gt;", color)
</code></pre>
</details>

<details><summary><b>Looping in sorted order</b></summary>
<p><b>NOTE</b><ul>
<li><b>sorted():</b>new_list = sorted(list)</li>
<li><b>sort():</b> list.sort()  ""in-place""</li></p><pre><code>colors = ["green", "red", "blue", "black"]

# Pythonic
# Asceding
for color in sorted(colors):
    print(color)

# Decsending
for color in sorted(colors, reverse=True):
    print(color)
</code></pre>
</details>

<details><summary><b>Custom Sort Order</b></summary><pre><code>colors = ["green", "red", "blue", "black"]

# Pythonic
print(sorted(colors, key=len))
</code></pre>
</details>

<details><summary><b>Distinguishing multiple exit points in loops</b>[for-else]</summary><pre><code>colors = ["green", "red", "blue", "black"]

# Ugly
def find(seq, target):
     found = False
     for i, value in enumerate(seq):
             if value == trgt:
                     found = True
                     break
     if not found:
             return -1
     return i

# Pythonic
def find(seq, target):
    for i, value in enumerate(seq):
        if value == trgt:
            break

    else:
        return -1
    return i
</code></pre>
</details><br>

<details><summary><b>Looping Over dictionary Keys</b></summary><pre><code>d = {'mathew': 'blue', 'rachel': 'green', 'raymond': 'red'}

#Ugly
for k in d:
     print(k)

# Pythonic
for k in d.keys():
     print(k)

# Another Pythonic one
d = {k: d[k] for k in d}
</code></pre>
</details>

<details><summary><b>Looping Over dictionary Keys nad Values</b></summary><pre><code>d = {'mathew': 'blue', 'rachel': 'green', 'raymond': 'red'}

#Ugly
for k in d:
     print(k, "--&gt;", d[k])

# Pythonic
for k, v in d.items():
     print(k, v)
</code></pre>
</details>

<details><summary><b>Construct a dictionary from pairs</b></summary><pre><code>names = ['raymond', 'rachel', 'meatthew']
colors = ['red', 'blue', 'black']

d = dict(zip(names, colors))
</code></pre>
</details>

<details><summary><b>Counting with dictionaries</b></summary><pre><code>colors = ['red', 'red', 'green', 'blue', 'blue', 'green', 'red', 'blue']

# Basic
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

# Intermediate
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

# Pythonic
from collections import defaultdict

d = deafultdict(int)
for color in colors:
    d[color] += 1
</code></pre>
</details>

<details><summary><b>Grouping with dictionaries</b></summary><pre><code>names = ['mosaab', 'cool', 'hany', 'shady', 'muhamed', 'raymond']

# Basic
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

# Intermediate
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

# Pythonic
from collections import defaultdict

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
</code></pre>
</details>

<details><summary><b>Linking dictionaries</b></summary><pre><code>d1 = {'mosaab': 'blue', 'hany': 'black', 'sally': 'purple'}
d2 = {'shaker': 'yellow', 'hoda': 'brown'}

# Basic
totalDict = dict()
totalDict.update(d1)
totalDict.update(d2)

# Pythonic
totalDict = ChainMap(d1, d2)
</code></pre>
</details><br>


<details><summary><b>Improving Clarity</b></summary><pre><code># 1. Clarify function calls with keyword arguments. (It might slow you some milliseconds, but it's worth it).
# Ugly
twitter_search('@obama', False, 20, True)

# Pythonic 
twitter_search('@obama', retweets=False, numtweets=20, popular=True)
</code></pre>
</details>

<details><summary><b>Name Tuple</b></summary><pre><code># 2. Clarify multiple return values with named tuples.
# Ugly
doctest.testmode()
# (0, 4)

# Pythonic
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'], verbose=True)
p = Point(x=10, y=20)
p
# Point(x=10, y=20)
print(p.x, p.y)
# 10 20
</code></pre>
</details>

<details><summary><b>Unpacking Sequences</b></summary><pre><code>p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

# Ugly
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

# Pythonic
fname, lname, age, email = p
</code></pre>
</details>
<details><summary><b>Updating Sequences</b>[deque]</summary><pre><code>names = ['raymond', 'rachel', 'matthew', 'roger', 'betty']

# Ugly
del names[0]
names.pop(0)
names.insert(0, 'mark')

# Pythonic
from collections import deque

names = deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie'])

# Much faster
de names[0]
names.popleft()
names.appendleft('mark')
</code></pre>
</details>
</ul></details>

<details><summary><b>Logging</b></summary><ul>
<details><summary><b>Important Notes</b></summary><ul>
<li>Default Basic Logging level is <b>Warning</b></li>
<li><b>DEBUG</b>: Detailed information, typically of interest only when diagnosing problems.</li>
<li><b>INFO</b>: Confirmation that things are working as expected.</li>
<li><b>WARNING</b>: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.</li>
<li><b>ERROR</b>: Due to a more serious problem, the software has not been able to perform some function.</li>
<li><b>CRITICAL</b>: A serious error, indicating that the program itself may be unable to continue running.</li>
</ul></details>


<details><summary><b>Print Logging</b> by its level</summary>
<pre><code>import logging

num_1 = 20
num_2 = 10

# Print: Display console output for ordinary usage of a command line script or program
print()

# Info &amp; Debug: Report events that occur during normal operation of a program (e.g. for status monitoring or fault investigation)
logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
# output: DEBUG:root:{your message}

# warning/warn: Issue a warning regarding a particular runtime event
# logging.warning() if there is nothing the client application can do about the situation, but the event should still be noted
logging.warning('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# warnings.warn() in library code if the issue is avoidable and the client application should be modified to eliminate the warning
logging.warn('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# Report suppression of an error without raising an exception (e.g. error handler in a long-running server process)
logging.error('Div: {} / {} = {}'.format(num_1, num_2, div_result))
logging.exception('Div: {} / {} = {}'.format(num_1, num_2, div_result))
logging.critical('Div: {} / {} = {}'.format(num_1, num_2, div_result))
</code></pre>
</details>

<details><summary><b>Set Basic Level/FORMATTER/File</b></summary>
<a href="https://docs.python.org/3/library/logging.html#logrecord-attributes">Check different formatters</a>
<pre><code>import logging
# Working with the root logger.
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
                    
# if file exists, it will append the new logs.
# If file is defined, nothing will be printed, everything will be in the file.
</code></pre>
</details>
<details><summary><b>Set Specifi Logger</b></summary>
<pre><code>import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
</pre></code>
</details>

</ul></details>

<details><summary><b>Threading</b></summary>
Threading is related to I/O bound, like downloading images from the internet, reading/writing files.
<h4>Old way</h4>
<pre><code>import threading, time

start = time.perf_counter()

def do_something(sec):
    print(f"sleeping for {sec} sec")
    time.sleep(sec)
    return "done sleeping"

 threads = []
 for _ in range(10):
     t = threading.Thread(target=do_something, args=[1.5])
     t.start()
     threads.append(t)

 for thread in threads:
     thread.join()


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds.")
</pre></code>

<h4>Better way</h4>
<pre><code>import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

     for result in results:
         print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
</pre></code>
</details>

<details><summary><b>Multi-Processing</b></summary>
Multi-Processing is related to CPU bound, like using only one CPU to the computation and not using the other CPUs.
<h4>Old way</h4>
<pre><code>import multiprocess, time

start = time.perf_counter()

def do_something(sec):
    print(f"sleeping for {sec} sec")
    time.sleep(sec)
    return "done sleeping"

 threads = []
 for _ in range(10):
     t = multiprocess.Process(target=do_something, args=[1.5])
     t.start()
     threads.append(t)

 for thread in threads:
     thread.join()


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds.")
</pre></code>

<h4>Better way</h4>
<pre><code>import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

     for result in results:
         print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
</pre></code>
</details>

<details><summary><b>Sorting</b></summary>
<details><summary>Sort Dictionary easily by <b>keys</b> or <b>values</b></summary><p><pre><code>sorting = {1: 23, 2: 24, 4: 51, 10: 1, "cool": 20}

# to sort by values, put it first.
values, keys = zip(*sorted(zip(sorting.values(), sorting.keys())))
values, keys

# OUTPUT
((1, 20, 23, 24, 51), (10, 'cool', 1, 2, 4))
</code></pre><pre><code>word_counts = {"a": 12, "b":23, "c": 1, "d":2}

# Sort by keys from small to large.
new_dict = dict(sorted(word_counts.items(), key=lambda val: val[0], reverse=False)
# [('a', 12), ('b', 23), ('c', 1), ('d', 2)]


# Sort by values from small to large.
new_dict = dict(sorted(word_counts.items(), key=lambda val: val[1], reverse=False)
# [('c', 1), ('d', 2), ('a', 12), ('b', 23)]
</code></pre>
</p></details>

<details><summary>Sort <b>Lists</b></summary><p><pre><code>x = [4, 1, 2, 3]
y = sorted(x)  # x is unchanged.
x.sort()            # x is changed and sorted.

# Sort the list by absolute values from largest to smallest.
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
</code></pre>
</p></details>

<details><summary><b>Custom Comparator (sorting)</b></summary>
You have to check at least a.score versus b.score, and in the case of a tie, a.name versus b.name.<br> For an ascending sort, return -1, 0, 1 for a < b, a = b and a > b. <br>For descending, return 1, 0, -1 for a < b, a = b and a > b.
<pre><code>from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name  = name
        self.score = score
        
    def __repr__(self):
        return f"Player(name={self.name}, score={self.score})"
    # Sort descendingly by score, if equal sort by name
    def comparator(a, b):
        if a.score == b.score:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            else:
                return 0
        else:
            return b.score - a.score

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
</code></pre>
</details>

<details><summary><b>bisect(), bisect_right()</b></summary>
This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the right most position where element has to be inserted is returned. <br>This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.
<pre><code># O(log(n)) -> Bisect method works on the concept of binary search
# importing "bisect" for bisection operations
import bisect
  
# initializing list
li = [1, 3, 4, 4, 4, 6, 7]
  
# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print ("The rightmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect(li, 4))
  
# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print ("The rightmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect_right(li, 4, 0, 4))
#### The rightmost index to insert, so list remains sorted is  : 5
#### The rightmost index to insert, so list remains sorted is  : 4
</code></pre>
</details>

<details><summary><b>bisect_left()</b></summary>
This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. <br>If the element is already present in the list, the left most position where element has to be inserted is returned. <br>This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.
<pre><code># O(log(n)) -> Bisect method works on the concept of binary search
# Python code to demonstrate the working of
# bisect(), bisect_left() and bisect_right()
  
# importing "bisect" for bisection operations
import bisect
  
# initializing list
li = [1, 3, 4, 4, 4, 6, 7]
  
# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print ("The leftmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect_left(li, 4))
### The leftmost index to insert, so list remains sorted is  : 2
</code></pre>
</details>

<details><summary><b>insort(), insort_right()</b></summary>
 This function returns the sorted list after inserting number in appropriate position, if the element is already present in the list, the element is inserted at the rightmost possible position. <br>This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.
<pre><code># O(n) -> Inserting an element in sorted array requires traversal
import bisect
  
# initializing list
li1 = [1, 3, 4, 4, 4, 6, 7]
  
# initializing list
li3 = [1, 3, 4, 4, 4, 6, 7]
  
# using insort() to insert 5 at appropriate position
# inserts at 6th position
bisect.insort(li1, 5)
  
print ("The list after inserting new element using insort() is : ")
for i in range(0, 7):
    print(li1[i], end=" ")
  
print("\r")
# using insort_right() to insert 5 at appropriate position
# inserts at 5th position
bisect.insort_right(li3, 5, 0, 4)
  
print ("The list after inserting new element using insort_right() is : ")
for i in range(0, 7):
    print(li3[i], end=" ")
    
 """
 The list after inserting new element using insort() is : 
1 3 4 4 4 5 6 
The list after inserting new element using insort_right() is : 
1 3 4 4 5 4 6 
"""
</code></pre>
</details>

<details><summary><b>insort_left()</b></summary>
 This function returns the sorted list after inserting number in appropriate position, if the element is already present in the list, the element is inserted at the leftmost possible position. <br>This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.
<pre><code># O(n) -> Inserting an element in sorted array requires traversal
# importing "bisect" for bisection operations
import bisect

# initializing list
li2 = [1, 3, 4, 4, 4, 6, 7]
  
# using insort_left() to insert 5 at appropriate position
# inserts at 6th position
bisect.insort_left(li2, 5)

### The list after inserting new element using insort_left() is : 
## 1 3 4 4 4 5 6 
</code></pre>
</details><br>
</details>

<details><summary><b>String</b></summary>
<details><summary> <b>f-Literal</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/NLP%20with%20Python%20-%20Udemy/00-Python-Text-Basics/00-Working-with-Text-Files.html#Formatted-String-Literals-(f-strings)">Formatted String Literal</a> </p>
</p></details>

<details><summary><b>Check if char islower(), isupper(), isdigit(), islapha()</b></summary><p>
<pre><code>txt = "cooL"
txt[0].islower() # True
txt[0].isupper() # False
txt[0].isdigit() # False
txt[0].isalpha() # True
</code></pre>
</p></details>

<details><summary><b>str.index()</b>: Get index of substring</summary><p>
<pre><code> 'coolcool'[0]
#'c'
s = 'coolcool'
s.index('c')
#0
s.index('c', 1)
#4
s.index('c', 1, 2)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: substring not found
s.index('c', 1, 5)
#4
</code></pre>
</p></details>

<details><summary><b>Remove/Replace char/s</b></summary><p>
<pre><code># Remove a char from a string.
txt = 'abc12321cba'
txt.replace('a', '')
txt.translate({ord('a'): None})

# Remove multiple characters.
s = 'abc12321cba'
print(s.translate({ord(i): None for i in 'abc'}))
# 12321

## Remove specified number of times
s = 'abababab'
print(s.replace('a', 'A', 2))
# AbAbabab
</code></pre>
</p></details>

<details><summary><b>ord() / chr()</b>: get unicode index</summary><p>
<pre><code># ord() function takes string argument of a single Unicode character 
# and return its integer Unicode code point value.
print(ord('a')) # 97

print(chr(97)) # 'a'
</code></pre>
</p></details>

<br></details>


<details><summary><b>Random</b></summary><p><pre><code>import random
random.seed(42)

# random.random() produces numbers uniformly between 0 and 1 it's the random function we'll use most often
four_uniform_randoms = [random.random() for _ in range(4)]
#[0.8444218515250481,
# 0.7579544029403025,
# 0.420571580830845,
# 0.25891675029296335]

# Take random between range of numbers.
random.randrange(10) # choose randomly from [0, ..., 9]
random.randrange(3, 6) # choose randomly from [3, 4, 5]

# Shuffle given list.
lst= range(10)
random.shuffle(lst)
print(lst)
# [2, 5, 1, 8, ...]

# Pick random element from a list.
myPick = random.choice(['Alice', "bob", "charlie"])

# Pick a sublist of elements without duplication.
lottery_nums = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
# [16, 36, 10, 6, 25, 9]

# Pick a sublist of elements WITH duplication.
sublst = [random.choice(range(10)) for _ in range(4)]
# [9, 3, 3, 2]
</code></pre>
</p></details>

<details><summary> <b>Regex</b></summary><p><pre><code>import re

re.match("a", "cat") # --&gt; cat doesn't start with a
re.search("a", "cat") # --&gt; cat has an "a" in it.
re.split("[ab]", "carbs") # --&gt; split on a or b to ["c", "r", "s"]
re.sub("[0-9]", "-", "R2D2") # --&gt; replace digits with dashes.
</code></pre>
</p></details>

<details><summary><b>List</b></summary><p>
<details><summary> From <b>list of lists</b> to <b>list of items</b></summary><p><pre><code>list_of_lists = [[1, 2, 3, 4], [5, 6, 76], [123, 12, 123, 123,124123,123,123]]
list_elements = sum(terms, [])
</code></pre>
</p></details>
<details><summary> <b>Difference</b> & <b>Intersection</b> & <b>Combination</b> b/w lists</summary><p><pre><code>a = [1, 2, 3, 4, 5]
b = [4, 5, 5, 6, 5, 6]

### 1. Existing in (a) but NOT in (b)
# Returns a set.
set(a).difference(b) # {1, 2, 3}
set(a) - set(b)          # {1, 2, 3}
# Returns array
np.setdiff1d(a, b)     # array([1, 2, 3])

### 2. Intersection b/w (a) and (b)
# Returns a set.
set(a).intersection(b)     # {4, 5}

# Returns an array.
np.intersect1d(a, b)       # array([4, 5])

### 3. All of them together.
a + b           
</code></pre>
</p></details>

</p></details>

<details><summary><b>File</b></summary><p>
<details><summary> <b>See Files in Current Directory</b> </summary><p><pre><code>import os
print(os.listdir("../input"))
</code></pre>
</p></details>
</p></details>

<details><summary> <b>Difference</b> & <b>Intersection</b> b/w Counter()</summary><p><pre><code>from collections import Counter

cnt1, cnt2 = Counter("cool"), Counter("not cool")

# Union
cnt1 + cnt2

# Difference
cnt1.subtract(cnt2)
# NOTE: cnt1 will be overwritten.
</code></pre>
</p></details>

<details><summary> <b>Partial Function</b> [python 3] </summary><p><pre><code>from functools import partial 

# A normal function 
def add(a, b, c): 
    return 100 * a + 10 * b + c 

# A partial function with b = 1 and c = 2 
add_part = partial(add, c = 2, b = 1) 

# Calling partial function 
print(add_part(3)) 
</code></pre>
</p></details>

</p></details><hr>

</ul></details>
</div>