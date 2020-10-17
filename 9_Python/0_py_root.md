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
</div>