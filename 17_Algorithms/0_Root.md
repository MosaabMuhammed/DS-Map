<h1 style='color:darkcyan;text-decoration:underline'>Algorithms</h1>
<div style='width:1000px;margin:auto'>

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

</div>
































