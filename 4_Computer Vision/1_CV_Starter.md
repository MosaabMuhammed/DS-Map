# 1. Starter Code

- [**Reorder your imports based on length**](https://www.browserling.com/tools/line-length-sort) 

- [**Debugger**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Applied%20ML%20Course/0_Code/1_Python/21_debugging.html) 

<details><summary> **Make the header at the center** </summary>
<p>

~~~html
<p style="font-size:36px;text-align:center"> <b>Personalized cancer diagnosis</b> </p>
~~~

</p>
</details> 

<details><summary> **Colored** Text </summary>
<p>

~~~python
from termcolor import colored

# ****************SHOW COLORED text**********
def bg(value, type='num', color='blue'):
    value = str('{:,}'.format(value)) if type == 'num' else str(value)
    return colored(' '+value+' ', color, attrs=['reverse', 'blink'])
~~~

</p>
</details> 

<details><summary> **List of Libraries** </summary>
[Import Libraries](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_%20A%20Data%20Science%20Framework%20to%20achieve%2099%20Accuracy/a-data-science-framework-to-achieve-99-accuracy.html#3.1-Import-Libraries) 
<p style="margin: 0">

	import pandas as pd
	import numpy as np
	import matplotlib.pyplot as plt
	import seaborn as sns
	
	# Ignore warnings
	import warnings
	warnings.filterwarnings('ignore')
	
~~~python
import warnings
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn #ignore annoying warning (from sklearn and seaborn)
~~~
</p>
</details>

<details><summary> **Checking file exists or not** </summary>
<p style="margin: 0">

~~~python
# Checking if file exists or not.
if os.path.isfile('/kaggle/input/path_to_file.csv'):
    result = pd.read_csv(''/kaggle/input/path_to_file.csv')
else:
    result = pd.merge(data, text, on='ID', how='left')
    result.to_csv('text_data_combined.csv', index=False)
result.sample(5)
~~~
</p>
</details>

<details><summary> **Ploting Settings** </summary>
<p style="margin: 0">
~~~python
%matplotlib inline
%precision 2
# plt.style.use('ggplot')
sns.set_style('white')
plt.style.use('fivethirtyeight')
~~~
~~~python
pd.set_option('display.float_format', lambda x: '{:.3f}'.format(x)) #Limiting floats output to 3 decimal points
~~~

	
</p>
</details> 

<details><summary> **Color Printed Text** </summary>
[More Colors & Features](https://pypi.org/project/termcolor/) 
<p style="margin: 0">

	from termcolor import colored
	print(colored('value', 'color'))
	
</p>
</details> 

<details><summary> **Organized list of strings** </summary>
<p style="margin: 0">
~~~
print("Train Variant".ljust(15), train_variants_df.shape)
print("Train Text".ljust(15), train_text_df.shape)
print("Test Variant".ljust(15), test_variants_df.shape)
print("Test Text".ljust(15), test_text_df.shape)

######### Result ##########
# Train Variant   (3321, 4)
# Train Text      (3321, 2)
# Test Variant    (5668, 3)
# Test Text       (5668, 2)
~~~
</p>
</details>

<details><summary> **See All Variables details in notebook** </summary>
<p style="margin: 0">

	%whos
	
</p>
</details> 

<details><summary> **Compute the execution time of the cell** </summary>
<p style="margin: 0">

	%%time
	
</p>
</details> 

<details><summary> **Data Pretty Printer** </summary>
<p style="margin: 0">

	import pprint
	stuff = ['banana', 'apple', 'stuff1', 'stuff2']
	pprint.pprint(stuff)
	
</p>
</details> 


<details><summary> **Clean Up Memory** </summary>
<p style="margin: 0">
~~~python
# Clean up memory
gc.enable()
del model, train_features, valid_features
gc.collect()
~~~
</p>
</details> 

<details><summary> **Timmer** Function (Human Readable) </summary>
<p style="margin: 0">
~~~python
# Credit: https://www.kaggle.com/tilii7/hyperparameter-grid-search-with-xgboost
## Importing
from datetime import datetime

## Define the timer function
def timer(start_time=None):
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec = divmod(temp_sec, 60)
        print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))
        
### Call the function
# Here we go
start_time = timer(None) # timing starts from this point for "start_time" variable
random_search.fit(X, Y)
timer(start_time) # timing ends here for "start_time" variable
~~~
#### Result
~~~python
 Time taken: 0 hours 42 minutes and 17.04 seconds.
~~~
</p>
</details> 


