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

</div>