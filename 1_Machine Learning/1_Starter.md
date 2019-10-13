# 1. Starter Code

<div style='width:1000px;margin:auto;'>

<ul>
<li><a href="https://www.browserling.com/tools/line-length-sort"><b><span style='color:#333'>Reorder your imports based on length</span></b></a> </li>
</ul>

<ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Applied%20ML%20Course/0_Code/1_Python/21_debugging.html"><b><span style='color:#333'>Debugger</span></b></a> </li>
</ul>

<ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/How%20to%20win%20a%20Data%20Science%20Competition/Macros.html#Macros"><b><span style='color:#333'>Macros</span></b></a> </li>
</ul> 

<details><summary> <b>Make the header at the center</b> </summary>
<p>
~~~html
<p style="font-size:36px;text-align:center"> <b>Personalized cancer diagnosis</b> </p>
~~~
</p>
</details>

<details><summary> <b>Shapes in python Comments</b> </summary>
<p>
~~~python
# had to drop a pythonic line ¯\_(ツ)_/¯
~~~
</p>
</details>

<details><summary>Show<b> Table</b> using <b>Qgrid</b></summary>
<p>
~~~python
import qgrid
ggrid_widget = qgrid.show_grid(train, show_toolbar=True, grid_options={'forceFitColumns': False,
                                                                       'defaultColumnWidth': 100})
ggrid_widget
~~~
~~~python
## from qgrid_widget to dataframe aftering apply filters from qgrid (Awesome tool)
ggrid_widget.get_changed_df()
~~~
</p>
</details>

<details><summary><b>Pretty Print all cell outputs</b></summary>
<p>
<h4 style='color:#5462FF'>This means that, while normally you’d only get one output printed</h4>
~~~python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
~~~

<h4 style='color:#5462FF'>To go back.</h4>
~~~python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "last_expr"
~~~
</p>
</details>


<details><summary> <b>Colored</b> Text </summary>
<p>
~~~python
from termcolor import colored

# --------------SHOW COLORED text---------------
def bg(value, type='num', color='blue'):
    value = str('{:,}'.format(value)) if type == 'num' else str(value)
    return colored(' '+value+' ', color, attrs=['reverse', 'blink'])
~~~
</p>
</details> 

<details><summary> <b>Print the Name of the variable</b> </summary>
<p>
~~~python
# Credits: https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string
import inspect

def var2str(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
            	return names[0]
            	
 #### Use this
def shape(*args):
    max_len = 0
    for df in args:
        max_len = max(len(var2str(df)), max_len)
    for df in args:
        print(f'~> [{var2str(df).ljust(max_len)}] has {bg(df.shape[0])} rows, and {bg(df.shape[1])} columns.')
~~~

</p>
</details> 

<details><summary> <b>List of Libraries</b> </summary>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_%20A%20Data%20Science%20Framework%20to%20achieve%2099%20Accuracy/a-data-science-framework-to-achieve-99-accuracy.html#3.1-Import-Libraries">Import Libraries</a></p>

<p style="margin: 0">
~~~python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')
~~~
~~~python
import warnings
def ignore_warn(*args, **kwargs):
    pass
warnings.warn = ignore_warn #ignore annoying warning (from sklearn and seaborn)
~~~
</p>
</details>

<details><summary> <b>Checking file exists or not</b> </summary>
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

<details><summary> <b>Ploting Settings</b> </summary>
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

<details><summary> <b>Color Printed Text</b> </summary>
<p><a href="https://pypi.org/project/termcolor/">More Colors &amp; Features</a> </p>
<p style="margin: 0">
~~~python
from termcolor import colored
print(colored('value', 'color'))
~~~
</p>
</details> 

<details><summary> <b>Organized list of strings</b> </summary>
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

<details><summary> <b>See All Variables details in notebook</b> </summary>
<p style="margin: 0">
~~~python
%whos
~~~
</p>
</details> 

<details><summary> <b>Compute the execution time of the cell</b> </summary>
<p style="margin: 0">
~~~python
%%time
~~~
</p>
</details> 

<details><summary> <b>Data Pretty Printer</b> </summary>
<p style="margin: 0">
~~~python
import pprint
stuff = ['banana', 'apple', 'stuff1', 'stuff2']
pprint.pprint(stuff)
~~~
</p>
</details> 


<details><summary> <b>Clean Up Memory</b> </summary>
<p style="margin: 0">
~~~python
# Clean up memory
gc.enable()
del model, train_features, valid_features
gc.collect()
~~~
</p>
</details> 

<details><summary> <b>Timmer</b> Function (Human Readable) </summary>
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
<h4>Result</h4>
~~~python
 Time taken: 0 hours 42 minutes and 17.04 seconds.
~~~
</p>
</details> 

</div>
