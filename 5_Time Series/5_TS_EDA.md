# 4. Exploratory Data Analysis (EDA)

<div style="width:1000px;margin:auto">

<details><summary><b>Tips & Tricks</b></summary><p>

<details><summary><b>Heatmap</b> for <b>Daily</b> usage</summary><p>
<a href='./5_EDA/Heatmap_daily_time_series.html#Sales-Heatmap-Calendar'>How to use (Notebook)</a>
<h4>Code</h4>
```python
# ----------------------------------------------------------------------------
# Author:  Nicolas P. Rougier
# License: BSD
# ----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from datetime import datetime
from dateutil.relativedelta import relativedelta


def calmap(ax, year, data):
    ax.tick_params('x', length=0, labelsize="medium", which='major')
    ax.tick_params('y', length=0, labelsize="x-small", which='major')

    # Month borders
    xticks, labels = [], []
    start = datetime(year,1,1).weekday()
    for month in range(1,13):
        first = datetime(year, month, 1)
        last = first + relativedelta(months=1, days=-1)

        y0 = first.weekday()
        y1 = last.weekday()
        x0 = (int(first.strftime("%j"))+start-1)//7
        x1 = (int(last.strftime("%j"))+start-1)//7

        P = [ (x0,   y0), (x0,    7),  (x1,   7),
              (x1,   y1+1), (x1+1,  y1+1), (x1+1, 0),
              (x0+1,  0), (x0+1,  y0) ]
        xticks.append(x0 +(x1-x0+1)/2)
        labels.append(first.strftime("%b"))
        poly = Polygon(P, edgecolor="black", facecolor="None",
                       linewidth=1, zorder=20, clip_on=False)
        ax.add_artist(poly)
    
    ax.set_xticks(xticks)
    ax.set_xticklabels(labels)
    ax.set_yticks(0.5 + np.arange(7))
    ax.set_yticklabels(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    ax.set_title("{}".format(year), weight="semibold")
    
    # Clearing first and last day from the data
    valid = datetime(year, 1, 1).weekday()
    data[:valid,0] = np.nan
    valid = datetime(year, 12, 31).weekday()
    # data[:,x1+1:] = np.nan
    data[valid+1:,x1] = np.nan

    # Showing data
    ax.imshow(data, extent=[0,53,0,7], zorder=10, vmin=-1, vmax=1,
              cmap="RdYlBu_r", origin="lower", alpha=.75)
```
</p></details>

<details><summary><b>Upsampling</b></summary>
<p><b>Upsampling</b> Chaning the time from, for example, <b>minutes to seconds</b>. <br><b>Upsampling</b> helps us to visualize and analyze data in more detail, and these fine-grained observations are calculated using <b>interpolation</b>.<br>
<h5>Pitfalls:</h5>
<b>Upsampling</b> leads to <b>NaN</b> values. the methods used in <b>interpolation</b> are linear or cubic splines for imputing <b>NaN</b> values. This might not represent the original data, so the analysis & visualization might be misleading.</p>

```
# Aggregate dataframe by year since we have a yearly time-series dataframe.
walmart_store_count = walmart_stores.groupby("YEAR")[["storenum"]].agg("count").rename(columns={"storenum": "store_count"})
```

```
# Convert the frequecy to 2 days (Upsampling):
walmart_store_count_series = walmart_store_count_series.asfreq('2D')
# And this will generated NaNs, and we will fill it with interpolation.
```

```
# Imputing NaNs with interpolation.
walmart_store_count_series = walmart_store_count_series.interpolate(method="spline", order=2)

# Then plot it.
walmart_store_count_series.plot(style=":")
```
<img src="./imgs/upsampling.png">
</details>

<details><summary><b>Downsampling</b></summary>
<p><b>Downsampling</b> Chaning the time from, for example, <b>months to years</b>. <br><b>Downsampling</b> helps summarize and get a general sense of trends in data.<br>
<h5>Pitfalls:</h5>
<b>Downsampling</b> aggregates the observation over sample frequency, where we provide a frequency to function as an argument, so we might lose information.</p>

```
# After aggreation, we will smooth out the plot using downsampling with a frequency of BA(business year).
plt.figure(figsize=(12, 8))
plt.ylabel("Interpolated Values")
plt.plot(walmart_store_count_series)
walmart_store_count_series.resample('BA').mean().plot(style=':', title="Values Smoothen by Business Year Frequency") #BA stands for Business Year
```
<img src="./imgs/downsampling_1.png">

```
# Downsample with a frequency of BQ(business quarter) to observe higher granularity.
plt.figure(figsize=(12,8))
plt.ylabel("Interpolated Values")
walmart_store_count_series.plot(alpha=0.5, style='-')
walmart_store_count_series.resample('BQ').mean().plot(style=':', title="Values Smoothen by Business Quarter Frequency")#BQ stands for Business quarter
```
<img src="./imgs/downsampling_2.png">
</details>

</p></details>

<hr>

<details><summary><b>Time-Series Analysis Course</b></summary><p>

<details><summary><b>Time-Series with Pandas</b></summary><p>

<ul>
<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/00-Datetime-Index.html#Python-Datetime-Review"><b>1. Datetime Index</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/01-Time-Resampling.html#Import-the-data"><b>2. Making Datetime as index and parse it as datetime64</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/01-Time-Resampling.html#resample()"><b>3. Resample</b> (making aggregation over time)</a></p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/02-Time-Shifting.html#Time-Shifting"><b>4. Time Shifting</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/03-Rolling-and-Expanding.html#Rolling-and-Expanding"><b>5. Rolling &amp; Expanding</b></a></p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/04-Visualizing-Time-Series-Data.html#Visualizing-Time-Series-Data"><b>6. Visualizing Time-Series Data</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/06-Pandas-Time-Series-Exercises-SET-ONE-Solutions.html"><b>From month as number to String</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/04-Time-Series-with-Pandas/08-Time-Series-with-Pandas-Project-Exercise-SET-TWO-Solutions.html"><b>Extensive Time-Series EDA</b></a> 
</p></p></li>
</ul>
</p>
</details>

<details><summary><b>Statsmodel for Time-Series Analysis</b></summary> 
<p>

<ul>
<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/05-Time-Series-Analysis-with-Statsmodels/00-Introduction-to-Statsmodels.html"><b>1. Hodrick-Prescott filter</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/05-Time-Series-Analysis-with-Statsmodels/01-ETS-Decomposition.html"><b>2. ETS Decomposition</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/05-Time-Series-Analysis-with-Statsmodels/02-EWMA-Exponentially-Weighted-Moving-Average.html"><b>3. EWMA (Exponantially Weighted Moving Average)</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/05-Time-Series-Analysis-with-Statsmodels/03-Holt-Winters-Methods.html#Holt-Winters-Methods"><b>4. Holt-Winters Smoothing (Simple, Double, Triple)</b></a> </p></li>
</ul>
</p>
</details>

</p>
</details>

</div>