# R Language

<div style='width:1000px;margin:auto'>

<details><summary><b>Tutorials</b></summary>
<p>

<details><summary><b>Vector [Array]</b></summary>
<p>

<details><summary>Vector of <b>Strings</b></summary>
<p>
~~~
# A 'vector' is one of the data types in R. Vectors must contain
# the same type of data, that is the entries must all be of the
# same type: character (most programmers call these strings),
# logical (TRUE or FALSE), or numeric.

udacious <- c("Chris Saden", "Lauren Castellano",
              "Sarah Spikes","Dean Eckles",
              "Andy Brown", "Moira Burke",
              "Kunal Chawla")
~~~

</p>
</details>

<details><summary>Vector of <b>Numbers</b></summary>
<p>
~~~
# R start indexing from 1.
# the output will contain 1 and 10 and all the numbers in between.

numbers <- c(1:10)

numbers

numbers <- c(numbers, 11:20)

numbers
~~~

</p>
</details>

<details><summary><b>Built-in Functions</b> For Vectors</summary>
<p>

<details><summary><b>Get length of characters </b></summary>
<p>
~~~
mystery = nchar(udacious)
mystery

########### output #########
[1] 11 17 12 11 10 11 12  6
~~~
</p>
</details>

<details><summary><b>Element Selection</b></summary>
<p>
~~~
udacious[mystery == 11]


########### output #########
[1] "Chris Saden" "Dean Eckles" "Moira Burke"
~~~
</p>
</details>


</p>
</details>

</p>
</details>



<details><summary><b>DataFrame</b></summary>
<p>

<details><summary><b>Load DataFrame</b></summary>
<p>
~~~
# You should see mtcars appear in the 'Environment' tab with
# <Promise> listed next to it. 

# The object (mtcars) appears as a 'Promise' object in the
# workspace until we run some code that uses the object.

# R has stored the mtcars data into a spreadsheet-like object
# called a data frame. Run the next command to see what variables
# are in the data set and to fully load the data set as an
# object in R. You should see <Promise> disappear when you
# run the next line of code.

data(mtcars)
~~~
</p>
</details>


<details><summary>Print <b>Column names</b> and <b>Row names</b></summary>
<p>
~~~
# Print out all the data frame
mtcars

# Print the name of the columns
names(mtcars)

# Print the name of the rows
row.names(mtcars)

# Run this code to change the row names of the cars to numbers.
row.names(mtcars) <- c(1:32)
~~~
</p>
</details>

<details><summary>Print <b>Structure</b> of <b>DataFrame</b> [.info]</summary>
<p>
~~~
# str = structure
str(mtcars)

########## output ##########
'data.frame':	32 obs. of  11 variables:
 $ mpg : num  21 21 22.8 21.4 18.7 18.1 14.3 24.4 22.8 19.2 ...
 $ cyl : num  6 6 4 6 8 6 8 4 4 6 ...
 $ disp: num  160 160 108 258 360 ...
 $ hp  : num  110 110 93 110 175 105 245 62 95 123 ...
 $ drat: num  3.9 3.9 3.85 3.08 3.15 2.76 3.21 3.69 3.92 3.92 ...
 $ wt  : num  2.62 2.88 2.32 3.21 3.44 ...
 $ qsec: num  16.5 17 18.6 19.4 17 ...
 $ vs  : num  0 0 1 1 0 1 0 1 1 1 ...
 $ am  : num  1 1 1 0 0 0 0 0 0 0 ...
 $ gear: num  4 4 4 3 3 3 3 4 4 4 ...
 $ carb: num  4 4 1 1 2 1 4 2 2 4 ...
~~~
</p>
</details>

<details><summary>Print <b>Shape</b> of <b>DataFrame</b> [.shape]</summary>
<p>
~~~
# print out the dimensions
dim(mtcars)

########## output ##########
[1] 32 11		# 32 rows, 11 columns
~~~
</p>
</details>

<details><summary><b>Head</b> & <b>Tail</b> [.head(), .tail()]</summary>
<p>
~~~
# It's tedious to relabel our data frame with the right car names
# so let's reload the data set and print out the first ten rows.

data(mtcars)
head(mtcars, 10)

# The head() function prints out the first six rows of a data frame
# by default. Run the code below to see.
head(mtcars)

# I think you'll know what this does.
tail(mtcars, 3)
~~~
</p>
</details>

<details><summary><b>Select specific Column</b></summary>
<p>
~~~
# 12. Let's examine our car data more closely. We can access an
# an individual variable (or column) from the data frame using
# the '$' sign. Run the code below to print out the variable
# miles per gallon. This is the mpg column in the data frame.

mtcars$mpg

# Print out any two other variables to the console.
mtcars$cyl
mtcars$drat
~~~
</p>
</details>

</p>
</details>

<details><summary><b>Statistics</b></summary>
<p>
~~~
# This is a vector containing the mpg (miles per gallon) of
# the 32 cars. Run this next line of code to get the average mpg for
# for all the cars. What is it?
mean(mtcars$mpg)
~~~
</p>
</details>

<details><summary>Needs <b>Help</b></summary>
<p>
~~~
# Add '?' before any command to get some describtion
?names(mtcars)
~~~
</p>
</details>

</p>
</details>

</div>