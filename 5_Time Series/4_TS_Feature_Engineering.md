<h1 id="4featureengineeringts">4. Feature Engineering (TS)</h1>

<div style='width:1000px;margin:auto'>
<details><summary><b>Lags</b> & <b>Rolling Window</b> </summary>
<details><summary>Tutorials</summary>
<p>
First off what each features mathematically does:
<ul>
    <li><b>lag_7:</b> sales shifted 7 steps downwards for each group. The example above focuses on one group only as an example. That is why the first value appears on the 7th index.</li>
    <li><b>lag_28:</b> sales shifted 28 steps downwads. That is why the first value appears on the 28th index.</li>

    <li><b>rmean_7_7:</b> rolling mean sales of a window size of 7 over column lag_7. First value (0.2857) appears on the 13th index because means including nan are nan.</li>

    <li><b>rmean_7_28:</b> rolling mean sales of a window size of 7 over column lag_28. First value (0.357) appears on the 34th index because that is the first time the mean formula gets all 7 non-nan values.</li>
    <li><b>rmean_28_7:</b> rolling mean sales of a window size of 28 over column lag_7. First value (0.2857) appears on the 3th index because it is the first time the mean formula gets 28 non-nan values.</li>
    <li><b>rmean_28_28:</b> rolling mean sales of a window size of 28 over column lag_28. First value appears on 55th index because that is the first time the formula here all non-nan values.</li></ul>
<br>

<b>The intuition as far as I can understand is the following:</b><br>
<ul>
    <li>1. Captures the week-on-week similarity and that too of just the past week. In other words, people are likely to shop this monday similar to the last monday (except it is some special occassion).</li>
    <li>2. Captures the weekly similarity from a month-to-month perspective. Example: people in the 1st weekend of a month shop more so that weekend looks more similar to first weeks of other months than the previous weekend. (Though 28 is arguable here. A month is generally 30. Interesting would be a variable window depending on when the comparative week starts. Dealing with edge cases like week divided into 2 months will be tricky).</li><br>

<b>Since individual data points are prone to erratic spikes or troughs, mean provides a more "representative" picture.</b><br><br>

    <li>3. Captures the information regarding the sales of the whole previous week ending 7 days in the past i.e. if we are at day 14, then the average is of sales from days 1-7 NOT days 7-14. This provides the information about the whole week and not just a single day sale comparison like lag_7 to bring the lag_7 value into "better weekly context".</li>
    <li>4. Captures the information regarding the sales of the entire previous 4 weeks ending 7 days in the past i.e. if we are at day 35, then the average is sales from days 1-28.</li>

    <li>5. Captures the information regarding the sales of the whole week ending 4 weeks ago i.e. if we are on day 35, then the average is of sales from day 1-7. (Assuming for simplicity the month is 28 days), this provides the information of not just a month-to-month comparison of the same day (day 7 of month one vs day 7 of month two), but the entire week leading up to day 7. Again the idea I believe is to capture the whole week and not just a single day sale comparison like lag_28 to bring the lag_28 value into "better weekly context".</li>

    <li>6. Captures the information regarding the sales of the entire previous 4 weeks ending 4 weeks in the past i.e. if we are at day 56, then the average is of days 1-28. (Assuming for simplicity the month is 28 days), the idea again is to bring the point value of lag_28 into a better context (i.e. of day 28 when being compared to day 56) into a "better monthly context".</li></ul><br>

<b>How would you "talk" about these features?</b><br>
<ul>
    <li>Hey let's see how the sales were last friday compared to this friday?</li>
    <li>Hey let's see how the sales were first weekend of the last month compared to first weekend of this month?</li>
    <li>May be comparing last saturday to this saturday is too specific. Week-on-week same day trends are more likely to be similar if the prior week went similar too. It would make sense to not just have the last saturday but also the mean of the whole week leading upto that day to give the model the "hint" how normal the whole week was.</li></ul>
</details>

<details><summary>Code</summary><pre><code>lags = [7, 28]
lag_cols = [f"lag_{lag}" for lag in lags]
for lag, lag_col in zip(lags, lag_cols):
df[lag_col] = dt[['id', 'sales']].groupby("id")['sales'].shift(lag)

wins = [7, 28]
for win in wins:
for lag, lag_col in zip(lags, lag_cols):
    df[f"rmean_{lag}_{win}"] = dt[['id', lag_col]].groupby("id")[lag_col].transform(lambda x: x.rolling(win).mean()
</code></pre>
</details>
</p></details>

<details><summary><b>Resampling</b></summary>
<pre><code>#Resample and compute daily mean
daily = df['Chemical conc.'].resample('D')
daily_mean = daily.mean()
</code></pre>
</details>
<details><summary><b>Aggregation</b></summary>
<pre><code>#Calculate month wise statistics
monthly_stats = df.groupby(by='Month_Year')['Mean temparature'].aggregate([np.mean, np.median, np.std])
monthly_stats.reset_index(inplace=True)
monthly_stats.head(10)
</code></pre>
</details>
<details><summary><b>Rolling</b></summary>
<pre><code>#Now we will calculate weekly moving average on the original time series of mean daily temparature
weekly_moving_average = df['Mean temparature'].rolling(7).mean()

#Now we will calculate monthly moving average on the original time series of mean daily temparature
monthly_moving_average = df['Mean temparature'].rolling(30).mean()

#Let's caluclate the weekly and monthly avergaes with a stride of length 2
weekly_moving_average_2stride = df['Mean temparature'].rolling(7).mean()[::2]
monthly_moving_average_2stride = df['Mean temparature'].rolling(30).mean()[::2]
</code></pre>
</details>
</div>