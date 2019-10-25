# Starter

<div style='width:1000px;margin:auto'>

<details><summary><b>Basic DataTypes</b></summary><p>

<details><summary><b>1. Int</b></summary><p>
~~~
# you must add L at the end to tell R that your variables is integer or it will be double by default
x <- 2L

typeof(x)
# "integer"
class(x)
mode(x)

is.integer(x)  # TRUE
~~~
</p></details>

<details><summary><b>2. Double</b></summary><p>
~~~
x <- 5.3321

is.double(x)  # TRUE
~~~
</p></details>

<details><summary><b>3. Complex</b></summary><p>
~~~
z <- 2 + 4i

typeof(z)
# "complex"

is.complex(z) # True
~~~
</p></details>

<details><summary><b>4. Character</b></summary><p>
~~~
s <- "h"

typeof(s)
# "character"

is.character(x)  # TRUE
~~~
</p></details>

<details><summary><b>5. Logical</b></summary><p>
~~~
s <- T
s <- TRUE

s <- F
s <- FALSE

typeof(s)
# "logical"

is.logical(x)  # TRUE
~~~
</p></details>

</p></details>



<details><summary><b>New DataTypes</b></summary>
<p>
<p><a href="https://www.statmethods.net/input/datatypes.html">See the whole <b> Datatypes </b> from here</a> </p>

<details><summary><b>1. Vector</b> [Array in python]</summary>
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
              
udacious[-1] # will return a vector except the first value, unlike python.
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

<details><summary><b>2. Matrices</b></summary>
<p>
~~~
# All columns in a matrix must have the same mode(numeric, character, etc.) and the same length. The general format is

# mymatrix <- matrix(vector, nrow=r, ncol=c, byrow=FALSE,
#   dimnames=list(char_vector_rownames, char_vector_colnames))

# byrow=TRUE indicates that the matrix should be filled by rows. byrow=FALSE indicates that the matrix should be filled by columns (the default). dimnames provides optional labels for the columns and rows.\

# generates 5 x 4 numeric matrix
y<-matrix(1:20, nrow=5,ncol=4)

# another example
cells <- c(1,26,24,68)
rnames <- c("R1", "R2")
cnames <- c("C1", "C2")
mymatrix <- matrix(cells, nrow=2, ncol=2, byrow=TRUE,
  dimnames=list(rnames, cnames))
  
# Identify rows, columns or elements using subscripts.
x[,4] # 4th column of matrix
x[3,] # 3rd row of matrix
x[2:4,1:3] # rows 2,3,4 of columns 1,2,3


# Another way of creating matrices using rbind() & cbind()
# rbind()
r1 <- c('I', 'am', 'happy')
r2 <- c('What', 'a', 'day')
r3 <- c(1, 2, 3)

c <-rbind(r1, r2, r3)
c

# cbind
r <- cbind(r1, r2, r3)
r
~~~
</p>
</details>

<details><summary><b>3. Arrays</b></summary>
<p>
<blockquote>
  <p>Note: Arrays are similar to matrices but can have more than two dimensions. See help(array) for details. </p>
</blockquote>

</p>
</details>

<details><summary><b>4. DataFrames</b></summary>
<p>
<blockquote>
  <p>A data frame is more general than a matrix, in that different columns can have different modes (numeric, character, factor, etc.). This is similar to SAS and SPSS datasets.</p>
</blockquote>
~~~
d <- c(1,2,3,4)
e <- c("red", "white", "red", NA)
f <- c(TRUE,TRUE,TRUE,FALSE)
mydata <- data.frame(d,e,f)
names(mydata) <- c("ID","Color","Passed") # variable names
~~~
</p>
</details>

<details><summary><b>5. Lists</b> [dict in python]</summary>
<p>
<blockquote>
  <p>An ordered collection of objects (components). A list allows you to gather a variety of (possibly unrelated) objects under one name.</p>
</blockquote>
~~~
# example of a list with 4 components -
# a string, a numeric vector, a matrix, and a scaler
w <- list(name="Fred", mynumbers=a, mymatrix=y, age=5.3)

# example of a list containing two lists
v <- c(list1,list2)
~~~

<blockquote>
  <p>Identify elements of a list using the [[]] convention.</p>
</blockquote>
~~~
mylist[[2]] # 2nd component of the list
mylist[["mynumbers"]] # component named mynumbers in list
~~~

</p>
</details>

<details><summary><b>6. Factors</b> [cat variables]</summary>
<p>
<blockquote>
  <p>1. Tell R that a variable is nominal by making it a factor. The factor stores the nominal values as a vector of integers in the range [ 1... k ] (where k is the number of unique values in the nominal variable), and an internal vector of character strings (the original values) mapped to these integers.</p>
</blockquote>
~~~
# variable gender with 20 "male" entries and
# 30 "female" entries
gender <- c(rep("male",20), rep("female", 30))
gender <- factor(gender)
# stores gender as 20 1s and 30 2s and associates
# 1=female, 2=male internally (alphabetically)
# R now treats gender as a nominal variable
summary(gender)
~~~

<blockquote>
  <p>2. An ordered factor is used to represent an ordinal variable.</p>
</blockquote>
~~~
# variable rating coded as "large", "medium", "small'
rating <- ordered(rating, levels=c("small", "medium", "large")
# recodes rating to 1,2,3 and associates
# 1=large, 2=medium, 3=small internally
# R now treats rating as ordinal

# Alternative way
# T means True
rating <- factor(rating, levels=c("small", "medium", "large"), ordered=T)
~~~

</p>
</details>

</p>
</details>

<details><summary><b>Loops</b></summary><p>

<details><summary><b>1. While Loop</b></summary><p>
~~~
counter <- 1

while(counter < 10){
	print(counter)
	counter <- counter + 1
}
~~~
</p></details>

<details><summary><b>2. For Loop</b></summary><p>
~~~
for(i in 2:10) {
	print(paste('Hello R', i))
}
~~~
</p></details>

</p></details>

<details><summary><b>If/else Condition</b></summary><p>
~~~
rm(answer) # remove that variables
x <- rnorm(1) # choose random number from normal distribution

if(x > 1){
  answer <- 'Greater than 1'
  print(answer)
  
} else if(x >= -1){
  answer <- "between -1 and 1"
} else {
  answer <- 'Less than -1'
  print(answer)
}
~~~
</p></details>

<details><summary><b>Function</b></summary><p>
~~~
myfunc <- function() {
	# put your code here.	
}
~~~
</p></details>

<details><summary><b>General Functions</b></summary><p>

<details><summary><b>seq()</b>: Generate a sequence [range()]</summary><p>
~~~
# (start, stop, step)
seq(1, 15, 2)

# 1, 5, 9, 13
~~~
</p></details>

<details><summary><b>rep()</b>: repeat a value n times</summary><p>
~~~
# (value, n)
# repeat 3, 50 times
rep(3, 50)
~~~
</p></details>

</p></details>


<details><summary><b>Misc</b></summary>
<p>

<details><summary>Needs <b>Help</b></summary>
<p>
~~~
# Add '?' before any command to get some describtion
?names(mtcars)
~~~
</p>
</details>

<details><summary><b>Key Bindings</b></summary>
<p>
<ol>
<li><b>[Ctrl + Enter]</b>: Perform the current command, and move the cursor to the following command.</li>

<li><b>[Alt + Enter]</b>: Perform <i>only</i> the current command.</li>
</ol>
</p>
</details>

<details><summary>See or Change <b>Location</b></summary>
<p>
~~~
# see the working directory
getwd()

# change the working directory
setwd('link/to/path')
~~~
</p>
</details>

<details><summary>See files in the current directory</summary>
<p>
~~~
# see files in the current directory
list.files()
~~~
</p>
</details>

</p>
</details>

<details><summary><b>Rmd</b></summary>
<p>
<h4>markdown for R in Rstudio</h4>
<h4>Note:</h4> After you finish, press <b>knit</b>in Rstudio to convert Rmd to HTML.
~~~
# Example
Speed and Stopping Distances of Cars
========================================================

This is an R Markdown document or RMD. Markdown is a simple formatting syntax for authoring web pages (click the **Help** toolbar button for more details on using R Markdown).
<details><summary>Code</summary>
<p>
```{r}
?cars
str(cars)
```
</p>
</details>


```{r fig.height=10, fig.width=10}
plot(cars)
```
~~~
</p>
</details>

</div>