# ==8. ML Models==

<details><summary>Holt-Winters Model</summary>
<p>
[**Fitting & Evaluating**](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udemy/[%20FreeCourseWeb.com%20]%20Udemy%20-%20Python%20for%20Time%20Series%20Data%20Analysis/01.%20Introduction/UDEMY_TSA_FINAL/06-General-Forecasting-Models/00-Introduction-to-Forecasting.html#Introduction-to-Forecasting)  

~~~python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

fitted_model = ExponentialSmoothing(train_data['Thousands of Passengers'],trend='mul',seasonal='mul',seasonal_periods=12).fit()
~~~
</p>
</details>
