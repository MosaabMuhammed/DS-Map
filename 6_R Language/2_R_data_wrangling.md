# Data Wrangling [R]
<div style='width:1000px;margin:auto'>

<details><summary><b>DataTypes</b></summary>
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

# Load from existing R dataframes.
data(mtcars)

## Load from csv file
# we use stringsAsFactors=FALSE to treat strings as strings not factors
# Note: Factor means a categorical variable that has different flavors or levels.
statesInfo <- read.csv('stateData.csv', stringsAsFactors=FALSE)

## Load from tsv
df <- read.delim('pseudo_facebook.tsv')
df <- read.csv('pseudo_facebook.tsv', sep='\t')
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

<details><summary><b>summary</b> [.describe()]</summary>
<p>
~~~
# like df.descibe in python to show some descriptive statistics about the columns in the data frame.
summary(df)
~~~
</p>
</details>

<details><summary>How many <b>unique</b> values in <b>a Categorical (factor)</b> Variable</summary>
<p>
~~~
# like df.descibe in python to show some descriptive statistics about the columns in the data frame.
table(df$cat_col)

######### output ################ age
      18-24       25-34       35-44       45-54       55-64 65 or Above    Under 18 
      15802       11575        2257         502         140          60        2330 
~~~

<h4>2. Show only the levels of the categorical variable</h4>
~~~
levels(df$cat_col)

####### Output ##########

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

# Select by numbers of columns
head(statesInfo[, c(1, 2, 3)])

# Select a bunch of columns by number
head(df[, 1:5])  # select from first column to the fifth.
~~~
</p>
</details>

<details><summary><b>Select based on Condition</b></summary>
<p>
~~~
# 1. using "subset(dataframe, condition on columns)" 
stateSubset <- subset(df, state.region == 1)

# 2. using "df[Rows Condition, Columns Condition]
stateSubset <- df[df$state.region == 1, ]   # Select all columns for that condition

## Note: "state.region" is the name of the columns
~~~
</p>
</details>

<details><summary>Remove <b>Missing Values</b></summary>
<p>
~~~
# Extract missing data (in thise case, returns empty)
df_without_na <- na.omit(df)

# NOTE:
# In this case, you get an empty data frame, because every state has at least one missing value amongst the 153 fields. In contrast, if you ran the function with income_total, you’d just get the same data frame, because no values are missing for the first seven columns.
~~~
</p>
</details>

<details><summary><b>Merge</b> 2 dataframes together [.merge]</summary>
<p>
~~~
# Combine
income0813 <- merge(df1, df2, by="Id")
~~~
</p>
</details>


<details><summary><b>Save</b> dataframe as csv file [.to_csv]</summary>
<p>
~~~
# Save df in a csv file
write.table(income_total, "data/income-totals.csv",
    row.names=FALSE, sep=",")

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