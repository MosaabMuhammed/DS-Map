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

</p></details>

<hr>

<details><summary><b>Time-Series Analysis Course</b></summary>
<p>

<details><summary><b>Time-Series with Pandas</b></summary>
<p>

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