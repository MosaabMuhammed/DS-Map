# Data Visualization

<div sytle='width:1000px;margin:auto'>

<details><summary>Install <b>ggplot2</b></summary><p>
~~~
install.packages('ggplot2')
library(ggplot2)
~~~
</p></details>

<details><summary>1. Explore <b>One</b> Variable</b></summary><p>

<details><summary><b>1. Histograms</b></summary><p>

<details><summary><b>1.1. using scale_x_continuous()</b></summary><p>
<h4>1. using qplot()</h4>
~~~
qplot(x=dob_day, data=df) +
  scale_x_continuous(breaks=1:31) +
  geom_histogram(binwidth = 1)
~~~

<h4>2. using ggplot()</h4>
~~~
ggplot(aes(x = dob_day), data = pf) +
  geom_histogram(binwidth = 1) +
  scale_x_continuous(breaks = 1:31)
~~~
</p></details>

<details><summary><b>1.2. using facet_wrap()</b></summary><p>
<blockquote>
we use it, to make interaction between 2 variables.
</blockquote>
~~~
qplot(x=dob_day, data=df) + 
	scale_x_continuous(breaks=1:31) + # scale x axis to that limit
	facet_wrap(~dob_month, ncol=3)
~~~
~~~
ggplot(data=df, aes(x=dob_day)) + 
  geom_histogram(binwidth = 1) +
  scale_x_continuous(breaks = 1:31) + 
  facet_wrap(~dob_month)
~~~
<p><img src="imgs/20191021-194824.png" alt="" /></p>
</p></details>

<details><summary><b>1.3. using xlim</b></summary><p>
~~~
# this
qplot(data=df, x=friend_count, xlim=c(0, 1000))

# or this
qplot(data=df, x=friend_count) + 
  scale_x_continuous(limits = c(1, 1000))
~~~

~~~
# Using ggplot
ggplot(aes(x = friend_count), data = pf) +
  geom_histogram() +
  scale_x_continuous(limits = c(0, 1000))
~~~
</p></details>

</p></details>

</p></details>

</div>