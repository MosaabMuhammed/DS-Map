# 3. Data Wrangling

<div style='width:1000px;margin:auto'>
<details><summary>Set the <b>Frequency</b> of date</summary>
<pre><code>df_example = df_example.asfreq(freq='1D')</code></pre>
</details>

<details><summary>Let <b>Matplotlib</b> understand dates</summary>
<pre><code>from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
</code></pre>
</details>

<details><summary><b>Augmented Dickey-Fuller (ADF) test </b>for detecting stationarity</summary>
<a href="./3_Data_Wragling/Chapter_2_Augmented_Dickey_Fuller_Test.html">notebook</a>
</details>

<details><summary><b>Ljung-Box test</b></summary>
A quick way to verify whether the first-order differencing has stationarized a time series is
to plot the ACF function and run the Ljung-Box test for the differenced series.
<a href="./3_Data_Wragling/Chapter_2_First_Order_Differencing.html">notebook</a>
</details>
</div>