# 3. Data Wrangling

<div style='width:1000px;margin:auto'>
<details><summary>Set the <b>Frequency</b> of date</summary>
```python
df_example = df_example.asfreq(freq='1D')
```
</details>

<details><summary>Let <b>Matplotlib</b> understand dates</summary>
```python
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
```
</details>
</div>