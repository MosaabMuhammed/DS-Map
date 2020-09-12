# 3. Data Wrangling

<div style='width:1000px;margin:auto'>

<details><summary><b>Python</b></summary><p>

<details><summary><b>Sorting</b></summary><p>
<details><summary>Sort Dictionary easily by <b>keys</b> or <b>values</b></summary><p>
```
sorting = {1: 23, 2: 24, 4: 51, 10: 1, "cool": 20}

# to sort by values, put it first.
values, keys = zip(*sorted(zip(sorting.values(), sorting.keys())))
values, keys

# OUTPUT
((1, 20, 23, 24, 51), (10, 'cool', 1, 2, 4))
```
```
word_counts = {"a": 12, "b":23, "c": 1, "d":2}

# Sort by keys from small to large.
new_dict = sorted(word_counts, key=lambda val: val[0], reverse=False)
# [('a', 12), ('b', 23), ('c', 1), ('d', 2)]


# Sort by values from small to large.
new_dict = sorted(word_counts, key=lambda val: val[1], reverse=False)
# [('c', 1), ('d', 2), ('a', 12), ('b', 23)]
```
</p></details>

<details><summary>Sort <b>Lists</b></summary><p>
```
x = [4, 1, 2, 3]
y = sorted(x)  # x is unchanged.
x.sort()            # x is changed and sorted.

# Sort the list by absolute values from largest to smallest.
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
```
</p></details>
</p></details>



<details><summary> From <b>list of lists</b> to <b>list of items</b></summary><p>
```
list_of_lists = [[1, 2, 3, 4], [5, 6, 76], [123, 12, 123, 123,124123,123,123]]
list_elements = sum(terms, [])
```
</p></details>

<details><summary> <b>See Files in Current Directory</b> </summary><p>
```
import os
print(os.listdir("../input"))
```
</p></details>

<details><summary> <b>Difference</b> & <b>Intersection</b> & <b>Combination</b> b/w lists</summary><p>
```
a = [1, 2, 3, 4, 5]
b = [4, 5, 5, 6, 5, 6]

### 1. Existing in (a) but NOT in (b)
# Returns a set.
set(a).difference(b) # {1, 2, 3}
set(a) - set(b)          # {1, 2, 3}
# Returns array
np.setdiff1d(a, b)     # array([1, 2, 3])

### 2. Intersection b/w (a) and (b)
# Returns a set.
set(a).intersection(b)     # {4, 5}

# Returns an array.
np.intersect1d(a, b)       # array([4, 5])

### 3. All of them together.
a + b           
```
</p></details>
<details><summary> <b>Partial Function</b> [python 3] </summary><p>
```
from functools import partial 

# A normal function 
def add(a, b, c): 
    return 100 * a + 10 * b + c 
  
# A partial function with b = 1 and c = 2 
add_part = partial(add, c = 2, b = 1) 
  
# Calling partial function 
print(add_part(3)) 
```
</p></details>
<details><summary> <b>f-Literal</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/NLP%20with%20Python%20-%20Udemy/00-Python-Text-Basics/00-Working-with-Text-Files.html#Formatted-String-Literals-(f-strings)">Formatted String Literal</a> </p>
</p></details>


</p></details><hr>

<details><summary><b>Numpy</b> </summary><p>

<details><summary><b>Concatenate [c_]</b> in Numpy </summary><p>
```
# Example 1.
np.c_[[1, 2, 3], [5, 6, 7]]
# array([[1, 4],
#	       [2, 5],
#    	       [3, 6]])

# Example 2.
np.c_[[[1, 2, 3]], 0, 1, [[4, 5, 6]]]
# array([[1, 2, 3, 0, 1, 4, 5, 6]])
```
</p></details>
<details><summary>Add <b>new dimension</b> to vector/matrix [np.array] </summary><p>
```
#### Trick number #1:
# Add a second dimension
# This is like x[:, np.newaxis] == x[:, None]
x[np.newaxis].shape, x[None].shape

#### Trick number #2:
# Add a new dimension at last.
# This is much better/safe approch
x[..., None].shape, x[..., np.newaxis].shape


#### Trick number #3:
# First parameter is the array/tensor
# Second parameter is the position where you want to add.
# ex:  BEFORE: x.shape --> (4,)
#        AFTER:    x.shape --> (1, 4)
np.expand_dims(x, 0)
```
</p></details>

</p></details><hr>

<details><summary><b>DataFrame</b></summary><p>

<details><summary><b>Better Visualization for Sparse Matrix/Dataframe</b></summary><p>
```
# By simpling replacing 0 with ''
df[df==0] = 0
df
```
</p></details>

<details><summary>From <b>Normal Dataframe</b> to <b> Similarity Matrix</b></summary><p>

<h4>1. Create graph dataframe</h4>
```
col_index = "person"
col_value = "docs"

index1, index2, n_values = [], [], []
index_value = df.groupby(col_index)[col_value].apply(pd.Series.unique).to_dict()

for p1, p2 in itertools.permutations(np.unique(df[col_index].values), 2):
    index1.append(p1)
    index2.append(p2)
    n_values.append(len(set(index_value[p1]).intersection(index_value[p2])))

# Create a dataframe has columns ["index1", "index2", "common_values_b/w_them"]
index_df = pd.DataFrame({'index1': index1, 'index2': index2, 'n_values': n_values})
```

<h4>2. Create the Similarity Matrix</h4>
```
index_df = pd.pivot(index_df, index='index1', columns='index2', values='n_values')
```

<h4>3. Visualize it with Heatmap (if possible)</h4>
```
plt.figure(figsize=(10, 8))
sns.heatmap(person_df, cmap='viridis')
plt.title("People Correlation", size=30, y=1.05)
plt.xticks(size=16)
plt.yticks(size=16);
```
</p></details>

<details><summary>From <b>One-Hot Encoding</b> to <b> Unpiovt Table</b></summary><p>
<h4>1. Convert array of labels in a raw to One-Hot Encoding</h4>
```
df  = df_eng
col = "MoreSamples"

from sklearn.preprocessing import MultiLabelBinarizer

binarizer = MultiLabelBinarizer()
samples = binarizer.fit_transform(df[col].values)
```

<h4>2. Create the One-Hot encoding dataframe</h4>
```
samples_df = pd.DataFrame(samples, columns=binarizer.classes_)
df = pd.concat([df.reset_index(), samples_df.reset_index()], axis=1).drop(["index", col], axis=1)
```

<h4>3. Unpivot the One-Hot encoding dataframe</h4>
```
# Change "DisplayName" to your columns to be used as index.
df = pd.melt(df, id_vars=["DisplayName"])
df = df_eng[(df.value == 1)]
df.drop("value", axis=1, inplace=True)
```
</p></details>

<details><summary>Show <b>Thousands comma seperator</b> in dataframe </summary><p>
```
df = pd.read_csv("file.csv", thousands=",")
```
</p></details>

<details><summary> <b>Change value of cell in dataframe</b> </summary><p>
```
# using .at
news_df.at[idx, 'word'] = operations[operation_idx](random_row.word)
```
</p></details>
<details><summary> Rename<b> Repeated</b> columns </summary>
```python
cols = []
col_name = "Grill"
count = 1
for column in X.columns:
    if column == col_name:
        cols.append(f'{col_name}_{count}')
        count+=1
        continue
    cols.append(column)
X.columns = cols
```
</details>
<details><summary> <b>Display</b> Multiple dataframes</summary><p>
```
import IPython

def display(*dfs, head=True):
    for df in dfs:
        IPython.display.display(df.head() if head else df)
```
</p></details>
<details><summary> <b>Chain</b> of <b>Functions [pipe()]</b></summary><p>
```python
# using pipe, we can chain functions on dataframe or series.
prices = pd.read_csv(f"{INPUT_DIR}/sell_prices.csv").pipe(reduce_mem_usage)
```
</p></details>
<details><summary> Create <b>DataFrame for Testing</b> </summary><p>
```
# Import pandas
import pandas as pd

# Create the testing dataframe.
test_df = pd.util.testing.makeMixedDataFrame()
test_df = pd.util.testing.makeDataFrame()
test_df = pd.util.testing.makeMissingDataframe()
test_df = pd.util.testing.makeTimeDataFrame()
test_df = pd.util.testing.makePeriodFrame()
```
</p></details>
<details><summary> <b>Relationship Table</b> b/w <b> 2 categorical features</b></summary><p>
```
table = pd.crosstab(df.label, df.flow_id, normalize='columns'); table
```
</p></details>
<details><summary> Return columns have <b>NaNs or Infinite</b> values</summary><p>
```
def return_cols_have_inf(df):
    return [col for col in df if np.isfinite(df[col]).sum() != df.shape[0]]

def return_cols_have_nan(df):
    return [col for col in df if np.isnan(df[col]).sum()]
```
</p></details>
<details><summary><b>A series of arrays</b> to <b>DataFrame</b> </summary><p>
~~~python
X_train = X_train.apply(pd.Series)
~~~
</p></details>
<details><summary> <b>Progress Bar</b> for <b>Pandas Operations</b> </summary><p>
~~~python
from tqdm import tqdm
tqdm.pandas()

temp = tweet.text.progress_apply(len)
~~~
</p></details>
<details><summary> <b>Select All Columns EXCEPT specific columns</b> </summary>
<p>
~~~python
# Option 1
df.loc[:, df.columns != 'b']

# Option 2
df.drop('b', axis=1)

# Option 3
df[df.columns.difference(['b'])]

# Option 4
df.loc[:, ~df.columns.isin(['col1', 'col2'])]

# Option 5
df[map(lambda x :x not in ['b'], list(df.columns))]
~~~
</p></details>

<details><summary> <b>Save & Remove label at the same time</b> </summary><p>
```
label = iris.pop('species')
```
</p></details>
<details><summary> <b>Add Prefix or Suffix to all columns name</b> </summary><p>
~~~python
# Add Prefix
df.add_prefix('X_')

# Add Suffix
df.add_suffix('_Y')
~~~
</p></details>
<details><summary> <b>Create Rare Category</b> </summary><p>
~~~python
# See the value counts for each category
genre.value_counts()

# Select the top n categories
top_four = genre.value_counts().nlargest(4).index
top_four

# Add Rare category
genre_updated = genre.where(genre.isin(top_four), other='Rare')

# See the changes
genre_updated.value_counts()
~~~
</p></details>
<details><summary> <b>Select Multiple Slices of Columns from a DataFrame</b> </summary><p>
~~~python
# DataFrame
df = pd.DataFrame(np.random.rand(3, 11), columns=list('ABCDEFGHIJk'))

# Option 1
pd.concat([df.loc[:, 'A', 'C'], df.loc[:, 'F'], df.loc[:, 'J':'K']], axis='columns')

# Option 2
df[list(df.columns[0:3]) + list(df.columns[5]) + list(df.columns[9:11])]

# Option 3
df.iloc[:, np.r_[0:3, 5, 9:11]]

~~~
</p></details>
<details><summary> <b>Remove Duplicated cat/num features</b> </summary><p>
~~~python
train_enc = pd.DataFrame(index=train_reduced.index)

for col in tqdm_notebook(traintest.columns):
    train_enc[col] = train_reduced[col].factorize()[0]
~~~

~~~python
dup_cols = {}

for i, c1 in enumerate(tqdm_notebook(train_enc.columns)):
    for c2 in train_enc.columns[i+1:]:
        if c2 not in dup_cols and np.all(train_enc[c1] == train_enc[c2]):
            dup_cols[c2] = c1
~~~

<h4> Drop them </h4>
~~~python
traintest.drop(dup_cols.keys(), axis=1, inplace=True)
~~~
</p></details>
<details><summary>See If which features have <b>Differencet Distrubtion</b> in <b>traing</b> and <b>test</b> datasets <b>(KS Test)</b> </summary>
<p>

<p><a href="https://www.kaggle.com/alexpengxiao/preprocessing-model-averaging-by-xgb-lgb-1-39"><b>Credits</b></a> </p>
~~~python
from scipy.stats import ks_2samp
THRESHOLD_P_VALUE = 0.01 #need tuned
THRESHOLD_STATISTIC = 0.3 #need tuned
diff_cols = []
for col in train.columns:
    statistic, pvalue = ks_2samp(train[col].values, test[col].values)
    if pvalue <= THRESHOLD_P_VALUE and np.abs(statistic) > THRESHOLD_STATISTIC:
        diff_cols.append(col)
for col in diff_cols:
    if col in train.columns:
        train.drop(col, axis=1, inplace=True)
        test.drop(col, axis=1, inplace=True)
train.shape
~~~
</p></details>
<details><summary> Read <b>specific</b> # rows <b>(if data is large)</b> </summary><p>
~~~python
features_sample = pd.read_csv('../input/home-credit-default-risk-feature-tools/feature_matrix.csv', nrows = 20000)
~~~
</p></details>
<details><summary> Show <b>a specific number of columns in (df.head())</b> </summary><p>
~~~python
pd.options.display.max_columns = 1700
~~~
</p></details>
<details><summary> <b>De-Ananomitizing</b> </summary><p>
[<b>Example</b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&%20Visualization.html#Importing,-Importing,-Importing:) 
</p></details>
<details><summary> Show <b># of Unique Values</b> for each <b>Column</b> </summary><p>
~~~python
# Number of unique classes in each object column
app_train.select_dtypes('object').apply(pd.Series.nunique, axis = 0)

#### Result #####
NAME_CONTRACT_TYPE             2
CODE_GENDER                    3
FLAG_OWN_CAR                   2
FLAG_OWN_REALTY                2
NAME_TYPE_SUITE                7
NAME_INCOME_TYPE               8
NAME_EDUCATION_TYPE            5
NAME_FAMILY_STATUS             6
~~~
</p></details>
<details><summary> Rename <b>Columns Name</b> </summary><p>
```
rename = {'Column Name 1':'New Name 1', 
	'Column Name 2': 'New Name 2'}
data.rename(index=str, columns=rename, inplace=True)
```
</p></details>
<details><summary> Show a <b>Beautiful</b> Statistical Result </summary>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/1_Titanic%20Survival/EDA%20To%20Prediction(DieTanic).html#Embarked--%3E-Categorical-Value">See the <b>Result</b></a> <br>
<a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html">See the <b>Doc</b></a> </p>
<p>
```
data.groupby(['Fare_Range'])['Survived'].mean().to_frame().style.background_gradient(cmap='summer_r')

data['Age_band'].value_counts().to_frame().style.background_gradient(cmap='summer')#checking the number of passenegers in each band

pd.crosstab(data.Parch,data.Pclass).style.background_gradient(cmap='summer_r')
```
</p></details>
<details><summary> <b>Word Cloud</b></summary>
<p style="margin: 0">
~~~python
from wordcloud import WordCloud, STOPWORDS

# textn_w is your list of words.
wc = WordCloud(width=1440, height=1080, background_color='black',
               max_words=len(textn_w), stopwords=set(STOPWORDS)
wc.generate(textn_w)
print(bg('Word Cloud for non_duplicate Questions Pairs:', 'str', 'green'))
plt.figure(figsize=(20, 15))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off');
~~~

<h4> 2. Generate from Dictionary (tag, number of occurances)</h4>
[<b>Notebook</b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Applied%20ML%20Course/0_Code/0_Case%20Studies/4_Stackoverflow%20Tag%20Predictor/1_Course%20Code/SO_Tag_Predictor.html) 
~~~python
# Lets first convert the 'result' dictionary to 'list of tuples'
tup = dict(result.items())
#Initializing WordCloud using frequencies of tags.
wordcloud = WordCloud(    background_color='black',
                          width=1600,
                          height=800,
                          stopwords=set(STOPWORDS),
                    ).generate_from_frequencies(tup)

fig = plt.figure(figsize=(30,20))
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
fig.savefig("tag.png")
plt.show()
~~~
</p>
</details>
<details><summary>From <b>String</b> to <b>Date</b></summary>
<p style="margin: 0">
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/8_First%20Capstone%20Project/911%20Calls%20Data%20Capstone%20Project-Mosaab.html#From-String-to-Datetime">See <b>Code</b> in notebook</a> </p>
~~~python
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
~~~
</p>
</details>


<details><summary>Convert a Column to Type (<b>Int</b>)</summary>
<p style="margin: 0">
[See <b>Code</b> in Kaggle](https://www.kaggle.com/jemseow/machine-learning-to-predict-app-ratings) 
~~~python
# convert reviews to numeric
df['Reviews'] = df['Reviews'].astype(int)
~~~
</p>
</details>

<details><summary><b>Align Training & Testing data with same columns</b></summary>
<p>
[see <b>results</b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/3_Home%20Credit%20Loans/1_Start%20Here:%20A%20Gentle%20Introduction.html#Aligning-Training-and-Testing-Data) 
~~~python
train_labels = app_train['TARGET']

# Align the training and testing data, keep only columns present in both dataframes
app_train, app_test = app_train.align(app_test, join = 'inner', axis = 1)

# Add the target back in
app_train['TARGET'] = train_labels

print('Training Features shape: ', app_train.shape)
print('Testing Features shape: ', app_test.shape)
~~~
</p>
</details>


<details><summary>Show <b>Top Correlated Features</b> with <b>TARGET</b></summary>
<p>
~~~python
# Function to calculate correlations with the target for a dataframe
def target_corrs(df, target):

    # List of correlations
    corrs = []

    # Iterate through the columns 
    for col in df.columns:
        print(col)
        # Skip the target column
        if col != target:
            # Calculate correlation with the target
            corr = df[target].corr(df[col])

            # Append the list as a tuple
            corrs.append((col, corr))
            
    # Sort by absolute magnitude of correlations
    corrs = sorted(corrs, key = lambda x: abs(x[1]), reverse = True)
    
    return corrs
~~~
</p></details>
<details><summary><b>Add a record to a DataFrame</b></summary><p>
```
df = train.append(test, ignore_index=True)
```
</p></details>
<details><summary>From <b>groupby()</b> to <b>DataFrame</b></summary><p>
```
# Aggregate #passengers by month.
# you can pass multiple columns in the 2 brackets.
# Must be 2 brackets to result in dataframe, if 1 bracket, it will end in series if and only if 1 column is there.
df_per_month = df.groupby('month')[['#Passengers']].sum().reset_index()
df_per_month
```
</p></details>

</p></details><hr>

<details><summary><b>Misc</b></summary><p>

<details><summary> Upload <b> files</b> into colab </summary>
```python
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
```
</details>
<details><summary> <b>Sparse Matrix</b> </summary><p>
<p><a href="./3_data_wrangling/3-logreg-nb-imdb.html#5.-Sparse-Matrix-Representation">FastAI tutorials on Sparse Matrix</a> </p>
</p></details>

<details><summary><b>Settings for Plotting</b> </summary><p>
```
import matplotlib.pyplot as plt

def set_plot_sizes(sml, med, big):
    plt.rc('font', size=sml)          # controls default text sizes
    plt.rc('axes', titlesize=sml)     # fontsize of the axes title
    plt.rc('axes', labelsize=med)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=sml)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=sml)    # fontsize of the tick labels
    plt.rc('legend', fontsize=sml)    # legend fontsize
    plt.rc('figure', titlesize=big)  # fontsize of the figure title
    
# Usage
set_plot_sizes(12, 14, 16)
```
</p></details>
<details><summary> <b>[Profiling]</b> See which command takes the most in a function </summary><p>
```
# Let's run it in RandomForest.
m = RandomForestRegressor(n_jobs=-1)
%prun m.fit(X, y)

# After that you can notice that the following command takes the most time in running m.fit()
# So we make once and use it multiple times.
%time X = np.array(X, dtype=np.float32)
```
</p></details>
<details><summary>Save List using <b>Pickle</b> and <b>joblib</b></summary><p>
<h4>1. Save list</h4>
~~~python
# Pickle
# Save the onehot columns to later use.
with open('onehot_cols.pkl', 'wb') as f:
    pickle.dump(onehot_cols, f)
    
# Joblib
from sklearn.externals import joblib

joblib.dump(my_model, "my_model.pkl")
~~~

<h4>2. Read List</h4>
~~~python
# Pickle
with open('onehot_cols.pkl', 'rb') as f:
	myList = pickle.load(f)
	
# Joblib
from sklearn.externals import joblib

my_model_loaded = joblib.load("my_model.pkl")
~~~

<h4>3. Read or Save (Compact Version) (best)</h4>
~~~python
# See if frequency encoded colums is there or not.
if os.path.isfile('./freq_cols.pkl'):
    with open('freq_cols.pkl', 'rb') as f: 
        freq_cols = pickle.load(f)
else:
    # Select only the dummy variables.
    freq_cols = [col for col in train.columns if col.startswith('freq')]
    
    # Save the onehot columns to later use.
    with open('freq_cols.pkl', 'wb') as f:
        pickle.dump(freq_cols, f)
~~~
</p></details>
<details><summary><b>Download & Extract tgz file</b> with Python</summary><p>
```
import os, tarfile
from six.moves import urllib

# Constants.
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH  = os.path.join("datasets", "housing")
HOUSING_URL   = os.path.join(DOWNLOAD_ROOT, HOUSING_PATH, "housing.tgz")

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
```
</p></details>


</p></details>
 </div>


