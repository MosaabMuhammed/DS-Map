# 1. Starter Code

<div style='width:1000px;margin:auto;'>


<li><a href="https://www.browserling.com/tools/line-length-sort"><b><span style='color:#333'>Reorder your imports based on length</span></b></a> </li>
<li><a href="./1_starter//21_debugging.html"><b><span style='color:#333'>Debugger</span></b></a> </li>


<details><summary> <b>Macros</b> </summary><p>
<ul>
<li><a href="./1_starter/Macros.html#Macros"><b><span style='color:#333'>How to build a macro</span></b></a> </li>
</ul>

<details><summary> <b>__basic</b> </summary><p>
~~~python
# Version 1.3
import numpy as np
import pandas as pd
import seaborn as sns
from tqdm import tqdm_notebook as tqdm
from termcolor import colored
import os
import gc
import sys

import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt

%matplotlib inline
%precision 4

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '{:.4f}'.format(x)) #Limiting floats output to 3 decimal points

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

plt.style.use('fivethirtyeight')
sns.set_style('white')

print('Basic libraries have been loaded!')
~~~
</p></details>

<details><summary> <b>__basic_funcs</b> </summary><p>
~~~python
from termcolor import colored
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

############### Show colored text #############


def bg(value, type='num', color='blue'):
    value = str('{:,}'.format(value)) if type == 'num' else str(value)
    return colored(' ' + value + ' ', color, attrs=['reverse', 'blink'])


############ Print the variable name ##############
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


def shape(*args):
    for df in args:
        print(f'~> {colored(var2str(df), attrs=["blink"]):{15}} has {bg(df.shape[0]):>{10}} rows, and {bg(df.shape[1]):>{10}} columns.')


############### Summary Table #####################
from scipy import stats

# Summary dataframe


def summary(df, sort_col=0):
    summary = pd.DataFrame({'dtypes': df.dtypes}).reset_index()
    summary.columns = ['Name', 'dtypes']
    summary['Missing'] = df.isnull().sum().values
    summary['M_Percent'] = round(100 * summary['Missing'] / df.shape[0], 2)
    summary['Uniques'] = df.nunique().values
    summary['First Value'] = df.loc[0].values
    summary['Second Value'] = df.loc[1].values
    summary['Third Value'] = df.loc[2].values

    for name in summary['Name'].value_counts().index:
        summary.loc[summary['Name'] == name, 'Entropy'] = round(stats.entropy(df[name].value_counts(normalize=True), base=2), 2)

    summary = summary.sort_values(by=[sort_col], ascending=False) if sort_col else summary

    # Print some smmaries.
    print(f'~> Dataframe has {bg(df.shape[0])} Rows, and {bg(df.shape[1])} Columns.')
    print(f'~> Dataframe has {bg(summary[summary["Missing"] > 0].shape[0], color="red")} Columns have [Missing] Values.')
    print('---' * 20)
    for type_name in np.unique(df.dtypes):
        print(f'~> There are {bg(df.select_dtypes(type_name).shape[1])}\t Columns that have [Type] = {bg(type_name, "s", "green")}')

    return summary.style.background_gradient(cmap='summer_r')


def reduce_mem_usage(df):
    start_mem = df.memory_usage().sum() / 1024**3
    print('~> Memory usage of dataframe is {:.3f} GB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.uint8).min and c_max < np.iinfo(np.uint8).max:
                    df[col] = df[col].astype(np.uint8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.uint16).min and c_max < np.iinfo(np.uint16).max:
                    df[col] = df[col].astype(np.uint16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.uint32).min and c_max < np.iinfo(np.uint32).max:
                    df[col] = df[col].astype(np.uint32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
                elif c_min > np.iinfo(np.uint64).min and c_max < np.iinfo(np.uint64).max:
                    df[col] = df[col].astype(np.uint64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        # Comment this if you have NaN value in this column.
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024 ** 3
    print('~> Memory usage after optimization is: {:.3f} GB'.format(end_mem))
    print('~> Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    print('---' * 20)
    return df


def show_annotation(dist, n=5, size=14, total=None):
    sizes = [] # Get highest value in y
    for p in dist.patches:
        height = p.get_height()
        sizes.append(height)

        dist.text(p.get_x()+p.get_width()/2.,          # At the center of each bar. (x-axis)
               height+n,                            # Set the (y-axis)
               '{:1.2f}%'.format(height*100/total) if total else '{}'.format(height), # Set the text to be written
               ha='center', fontsize=size) 
    dist.set_ylim(0, max(sizes) * 1.15); # set y limit based on highest heights


def dd(*args):
    print('--'*20)
    for x in args:
        varName = colored(var2str(x), attrs=['blink'])
        print(f"~> Type  of {varName}: {colored(type(x), 'green')}")
        print(f"~> Shape of {varName}: {colored(str(x.shape), 'blue')}")
        print('--'*20)
        
        
print(f'~> The following functions are defined successfully: {bg("bg", "s")}, {bg("shape", "s")}, {bg("var2str", "s")}, {bg("reduce_mem_usage", "s")}, {bg("summary", "s")}, {bg("show_annotation", "s")}, {bg("dd", "s")}')


~~~
</p></details>

</p></details>

<details><summary> <b>Make the header at the center</b> </summary>
<p>
~~~html
<p style="font-size:36px;text-align:center"> <b>Personalized cancer diagnosis</b> </p>
~~~
</p>
</details>

<details><summary> <b>Show Plots</b> in the <b>Terminal</b> </summary>
<p>
~~~python
%pylab
~~~
</p>
</details>

<details><summary> <b>Save the last output value</b> in a <b>Variable</b> </summary>
<p>
~~~python
np.random.choice(students, 21) # performing this will output something to the console

# Apply the following to save it to a variable
sample = _
~~~
</p>
</details>


<details><summary> <b>Shapes in python Comments</b> </summary>
<p>

<p><a href="https://textfac.es/"><b>More textfaces</b></a> </p>
~~~python

 ¯\_(ツ)_/¯		( ͡° ͜ʖ ͡°)

  ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿

 ʕ•ᴥ•ʔ			▄︻̷̿┻̿═━一

  ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)

 (▀̿Ĺ̯▀̿ ̿)    		(ง ͠° ͟ل͜ ͡°)ง

  ༼ つ ◕_◕ ༽つ		(づ｡◕‿‿◕｡)づ

	 ̿'̿'\̵͇̿̿\з=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ ̿ ̿

 (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)

 ┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴   		( ͡°╭͜ʖ╮͡° )		(ಥ﹏ಥ)

   (͡ ͡° ͜ つ ͡͡°)			(• ε •) 		(ง'̀-'́)ง	(ᵔᴥᵔ)
   
   [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]		(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧		(¬‿¬)
   
   (╯°□°)╯︵ ʞooqǝɔɐɟ		(づ￣ ³￣)づ
   
   (;´༎ຶД༎ຶ`)			༼ つ  ͡° ͜ʖ ͡° ༽つ
   
   (╯°□°）╯︵ ┻━┻		( ͡ᵔ ͜ʖ ͡ᵔ )		ヾ(⌐■_■)ノ♪
   
   （╯°□°）╯︵( .o.)		┬──┬ ノ( ゜-゜ノ)
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

<p><a href="./1_starter/a-data-science-framework-to-achieve-99-accuracy.html#3.1-Import-Libraries">Import Libraries</a></p>

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

<details><summary> <b>Profile Reporting</b> </summary>
<p>
```
import pandas_profiling as pp

pp.ProfileReport(train)
```
</p>
</details>

<details><summary> <b>Table of Content - Bootstrap way</b> </summary>
<p>
```
<div class="list-group" id="list-tab" role="tablist">
  <h3 class="list-group-item list-group-item-action active" data-toggle="list"  role="tab" aria-controls="home">Notebook Content!</h3>
  <a class="list-group-item list-group-item-action" data-toggle="list" href="#libraries" role="tab" aria-controls="profile">Import Libraries<span class="badge badge-primary badge-pill">1</span></a>
  <a class="list-group-item list-group-item-action" data-toggle="list" href="#load" role="tab" aria-controls="messages">Load Data<span class="badge badge-primary badge-pill">2</span></a>
  <a class="list-group-item list-group-item-action"  data-toggle="list" href="#visual" role="tab" aria-controls="settings">Visualization of data<span class="badge badge-primary badge-pill">3</span></a>
  <a class="list-group-item list-group-item-action" data-toggle="list" href="#word" role="tab" aria-controls="settings">WordCloud<span class="badge badge-primary badge-pill">4</span></a> 
  <a class="list-group-item list-group-item-action" data-toggle="list" href="#clean" role="tab" aria-controls="settings">Cleaning the text<span class="badge badge-primary badge-pill">5</span></a>
    <a class="list-group-item list-group-item-action" data-toggle="list" href="#split" role="tab" aria-controls="settings">Train and test Split<span class="badge badge-primary badge-pill">6</span></a>
    <a class="list-group-item list-group-item-action" data-toggle="list" href="#model" role="tab" aria-controls="settings"> Creating the Model<span class="badge badge-primary badge-pill">7</span></a>
    <a class="list-group-item list-group-item-action" data-toggle="list" href="#eval" role="tab" aria-controls="settings">Model Evaluation<span class="badge badge-primary badge-pill">8</span></a>
</div>
```
<h4>Then at each cell, do the following</h4>
```
# header one
<a id='libraries'></a>

# Header two
<a id='load'></a>

# and so on.

```
</p>
</details>

<details><summary> <b>List & Labels - Bootstrap way</b> </summary>
<p>
```
<ul style="list-style-type:square;">
  <li><span class="label label-default">id</span> a unique identifier for each tweet</li>
  <li><span class="label label-primary">text </span> the text of the tweet</li>
  <li><span class="label label-success">location</span>  the location the tweet was sent from (may be blank)</li>
    <li><span class="label label-danger">keyword</span>  a particular keyword from the tweet (may be blank)</li>
</ul>

```
</p>
</details>

</div>
