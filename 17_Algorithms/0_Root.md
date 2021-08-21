<h1 style='color:darkcyan;text-decoration:underline'>Algorithms</h1>
<div style='width:1000px;margin:auto'>

<details><summary><b>Search</b></summary>
<details><summary><b>Binary Search</b></summary>
The list must be sorted before using Binary Search.<br>
<details><summary>Iterative</summary>
<pre><code>
# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
	while l <= r:
		mid = l + (r - l) // 2;		
		# Check if x is present at mid
		if arr[mid] == x:
			return mid

		# If x is greater, ignore left half
		elif arr[mid] < x:
			l = mid + 1

		# If x is smaller, ignore right half
		else:
			r = mid - 1
	
	# If we reach here, then the element
	# was not present
	return -1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")
</code></pre>
</details>
<details><summary>Recursive</summary>
<pre><code># Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):
	# Check base case
	if r >= l:
		mid = l + (r - l) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid
		
		# If element is smaller than mid, then it
		# can only be present in left subarray
		elif arr[mid] > x:
			return binarySearch(arr, l, mid-1, x)

		# Else the element can only be present
		# in right subarray
		else:
			return binarySearch(arr, mid + 1, r, x)
	else:
		# Element is not present in the array
		return -1

# Driver Code
arr = [ 2, 3, 4, 10, 40 ]
x = 10
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print ("Element is present at index % d" % result)
else:
	print ("Element is not present in array")
</code></pre>
</details>
</details>
<br>

</details>

<details><summary><b>Sort</b></summary>
<details><summary><b>Bubble Sort</b></summary>
<pre><code>def bubbleSort(arr):
n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
  
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
  
bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i]), 
</code></pre>
</details>

<details><summary><b>Insertion Sort</b></summary>
<pre><code># Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])</code></pre>
</details>

<details><summary><b>Merge Sort</b></summary>
<pre><code>def mergeSort(arr):
    if len(arr) > 1:
         # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1</code></pre>
            
<pre><code>from collections import deque

def MergeSort(arr):
    if len(arr) == 1: return deque(arr)
    a = MergeSort(arr[:len(arr)//2])
    b = MergeSort(arr[len(arr)//2:])
    
    res = deque()
    while a and b:
        if a[0] <= b[0]:
            res.append(a.popleft())
        else:
            res.append(b.popleft())
    res += a
    res += b
    return res
</code></pre>
</details>

<details><summary><b>Quick Sort</b></summary>
<pre><code># Python program for implementation of Quicksort Sort
  
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
  
# Function to do Quick sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
</code></pre>
</details>

<details><summary><b>Topological Sorting</b></summary>
<pre><code># Python program to print topological sorting of a DAG
from collections import defaultdict
 
# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order
 
 
# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
 
print ("Following is a Topological Sort of the given graph")
 
# Function Call
g.topologicalSort()
</code></pre>
</details>

</details>

<details><summary><b>Graph</b></summary>
<details><summary><b>Depth-First Search</b></summary>
<details><summary>Recursive</summary>
<pre><code>from collections import defaultdict

class Graph:
    def __init__(self):
            self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (Starting from vertex 2)")
g.DFS(2)
</code></pre>
</details>
<details><summary>Iterative [Stack]</summary>
<pre><code># This class represents a directed graph using adjacency
# list representation
class Graph:
    def __init__(self,V): # Constructor
        self.V = V        # No. of vertices
        self.adj  = [[] for i in range(V)]  # adjacency lists
 
    def addEdge(self,v, w):     # to add an edge to graph
        self.adj[v].append(w)    # Add w to v’s list.
        
    # prints all not yet visited vertices reachable from s
    def DFS(self,s):            # prints all vertices in DFS manner from a given source.
                                # Initially mark all verices as not visited
        visited = [False for i in range(self.V)]
 
        # Create a stack for DFS
        stack = []
 
        # Push the current source node.
        stack.append(s)
 
        while (len(stack)):
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()
 
            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if (not visited[s]):
                print(s,end=' ')
                visited[s] = True
 
            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)
 
 
 
# Driver program to test methods of graph class
 
g = Graph(5); # Total 5 vertices in graph
g.addEdge(1, 0);
g.addEdge(0, 2);
g.addEdge(2, 1);
g.addEdge(0, 3);
g.addEdge(1, 4);
 
print("Following is Depth First Traversal")
g.DFS(0)
</code></pre>
</details>
</details>

<details><summary><b>Beadth-First Search</b></summary>
<pre><code>from collections import defaultdict
class Graph
    # Constructor
    def __init__(self)
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)
</code></pre>
</details>

<details><summary><b>Strongly Connected Components (SCC) - Kosaraju's algorithm</b></summary>
<pre><code># Kosaraju's algorithm to find strongly connected components in Python

from collections import defaultdict
class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()
</code></pre>
</details>
</details>

<details><summary><b>String</b></summary>
<details><summary><b>Largest Common Substring b/w 2 strings</b></summary>
<h3>Dynamic Programming</h3>
<pre><code>def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
    return lengths[len(a)][len(b)]

</code></pre>
</details>
</details>

</div>
































