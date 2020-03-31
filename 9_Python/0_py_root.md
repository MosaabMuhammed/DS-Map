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

<details><summary><b>Looping over a range of numbers</b></summary>
```
for i in range(6):
	print(i)
```
</details></li>

<details><summary><b>Looping over a collection</b></summary>
```
colors = ["green", "red", "blue", "black"]

for color in colors:
	print(color)
```
</details>

<details><summary><b>Looping Backwards</b></summary>
```
colors = ["green", "red", "blue", "black"]

# Ugly
for i in range(len(colors)-1, -1, -1):
	print(colors[i])
	
# Pythonic
for color in reversed(colors):
	print(color)
```
</details>

<details><summary><b>Looping over a collection and indices</b></summary>
```
colors = ["green", "red", "blue", "black"]

# Ugly
for i in range(len(colors)):
	print(i, colors[i])
	
# Pythonic
for i, color in enumerate(colors):
	print(i, color)
```
</details>

<details><summary><b>Looping over 2 collections</b></summary>
```
colors = ["green", "red", "blue", "black"]
names = ["raymond", "rachel", "matthew"]

# Ugly
n = min(len(names), len(colors))
for i in range(n):
	print(names[i], '-->', colors[i])

	
# Pythonic
for name, color in zip(names, colors):
	print(name, "-->", color)
```
</details>

<details><summary><b>Looping in sorted order</b></summary>
<p><b>NOTE</b><ul>
<li><b>sorted():</b>new_list = sorted(list)</li>
<li><b>sort():</b> list.sort()  ""in-place""</li></p>
```
colors = ["green", "red", "blue", "black"]

# Pythonic
# Asceding
for color in sorted(colors):
	print(color)
	
# Decsending
for color in sorted(colors, reverse=True):
	print(color)
```
</details>

<details><summary><b>Custom Sort Order</b></summary>
```
colors = ["green", "red", "blue", "black"]
	
# Pythonic
print(sorted(colors, key=len))
```
</details>

<details><summary><b>Distinguishing multiple exit points in loops</b>[for-else]</summary>
```
colors = ["green", "red", "blue", "black"]

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
```
</details><br>

<details><summary><b>Looping Over dictionary Keys</b></summary>
```
d = {'mathew': 'blue', 'rachel': 'green', 'raymond': 'red'}

#Ugly
for k in d:
     print(k)

# Pythonic
for k in d.keys():
     print(k)
     
# Another Pythonic one
d = {k: d[k] for k in d}
```
</details>

<details><summary><b>Looping Over dictionary Keys nad Values</b></summary>
```
d = {'mathew': 'blue', 'rachel': 'green', 'raymond': 'red'}

#Ugly
for k in d:
     print(k, "-->", d[k])

# Pythonic
for k, v in d.items():
     print(k, v)
```
</details>

<details><summary><b>Construct a dictionary from pairs</b></summary>
```
names = ['raymond', 'rachel', 'meatthew']
colors = ['red', 'blue', 'black']

d = dict(zip(names, colors))
```
</details>

<details><summary><b>Counting with dictionaries</b></summary>
```
colors = ['red', 'red', 'green', 'blue', 'blue', 'green', 'red', 'blue']

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
```
</details>

<details><summary><b>Grouping with dictionaries</b></summary>
```
names = ['mosaab', 'cool', 'hany', 'shady', 'muhamed', 'raymond']

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
```
</details>
</ul></details>

</div>