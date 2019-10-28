# Data Wrangling [R]
<div style='width:1000px;margin:auto'>

<details><summary><b>DataFrame</b></summary><p>

<details><summary><b>Load DataFrame</b></summary><p>
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

# TO open a window and choose a csv file by a mouse.
df <- read.csv(file.choose())

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
colnames(df)

# Print the name of the rows
row.names(mtcars)
rownames(df)

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
[1] "female" "male"  
~~~
</p>
</details>

<details><summary><b>By</b> statistic [.groupby in Python]</summary><p>
~~~
# (numeric variable, cat variable, statistic)
by(df$friend_count, df$gender, summary)

##### Output #####
df$gender: female
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
      0      37      96     242     244    4923 
------------------------------------------------------------------- 
df$gender: male
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
      0      27      74     165     182    4917 
~~~
</p></details>

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
</p></details>
</p></details>

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


<details><summary>Condition statistic for column using <b>group_by() & summarise()</b></summary><p>
~~~
# 1. First Trial
install.packages('dplyr')
library(dplyr)

age_groups <- group_by(df, age)
df.fc_by_age <- summarise(age_groups,
                          friend_count_mean = mean(friend_count),
                          friend_count_median = median(friend_count),
                          n = n())
df.fc_by_age <- arrange(df.fc_by_age, age)

head(df.fc_by_age)

#### Output ####
    age friend_count_mean friend_count_median     n
  <int>             <dbl>               <dbl> <int>
1    13              165.                 74    484
2    14              251.                132   1925
3    15              348.                161   2618
4    16              352.                172.  3086
5    17              350.                156   3283
6    18              331.                162   5196
~~~

~~~
# Second Trial
df.fc_by_age <- df %>%
  group_by(age) %>%
  summarise(friend_count_mean = mean(friend_count),
            friend_count_median = median(friend_count),
            n = n()) %>%
  arrange(age)
~~~
</p></details>

<details><summary>Find <b>Correlation</b></summary><p>
~~~
# you can choose between pearson or spearman and kendall.
cor.test(df$age, df$friend_count, method='pearson')

# Correlation with subset of the data
with(subset(df, age<=70), cor.test(age, friend_count, method='pearson'))
~~~
</p></details>


<details><summary>Add & Print  <b>2 Strings</b> together</summary><p>
~~~
name <- "mosaab"
paste('Hello', name)
~~~
</p></details>

</div>