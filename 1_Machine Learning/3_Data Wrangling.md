# 3. Data Wrangling

<div style='width:1000px;margin:auto'>
<details><summary> <b>See Files in Current Directory</b> </summary><p>
```
import os
print(os.listdir("../input"))
```
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
</p>
</details>

<details><summary> <b>f-Literal</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/NLP%20with%20Python%20-%20Udemy/00-Python-Text-Basics/00-Working-with-Text-Files.html#Formatted-String-Literals-(f-strings)">Formatted String Literal</a> </p>
</p></details>

<details><summary> <b>Save & Remove label at the same time</b> </summary>
<p>
~~~python
label = iris.pop('species')
~~~
</p>
</details>

<details><summary> <b>Add Prefix or Suffix to all columns name</b> </summary>
<p>
~~~python
# Add Prefix
df.add_prefix('X_')

# Add Suffix
df.add_suffix('_Y')
~~~
</p>
</details>

<details><summary> <b>Create Rare Category</b> </summary>
<p>
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
</p>
</details>

<details><summary> <b>Select Multiple Slices of Columns from a DataFrame</b> </summary>
<p>
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
</p>
</details>

<details><summary> <b>Remove Duplicated cat/num features</b> </summary>
<p>
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
</p>
</details>


<details><summary> <b>Function</b> for <b>Summary Statistics</b> </summary>
<p>
~~~python
# Credits: https://www.kaggle.com/kabure/eda-feat-engineering-encode-conquer
from scipy import stats

# Summary dataframe
def summary_table(df, sort_col=0):
    summary              = pd.DataFrame({'dtypes': df.dtypes}).reset_index()
    summary.columns      = ['Name', 'dtypes']
    summary['Missing']   = df.isnull().sum().values
    summary['M_Percent'] = round(100 * summary['Missing'] / df.shape[0], 2)
    summary['Uniques']   = df.nunique().values
    summary['First Value'] = df.loc[0].values
    summary['Second Value'] = df.loc[1].values
    summary['Third Value'] = df.loc[2].values

    for name in summary['Name'].value_counts().index:
        summary.loc[summary['Name'] == name, 'Entropy'] = round(stats.entropy(df[name].value_counts(normalize=True), base=2), 2)

    summary = summary.sort_values(by=[sort_col], ascending=False) if sort_col else summary
    
    # Print some smmaries.
    print(f'~> Dataframe has {bg(df.shape[1])} Columns, and {bg(df.shape[0])} Rows.')
    print(f'~> Dataframe has {bg(summary[summary["Missing"] > 0].shape[0], color="red")} Columns have [Missing] Values.')
    print('---'*20)
    for type_name in np.unique(df.dtypes):
        print(f'~> There are {bg(df.select_dtypes(type_name).shape[1])}\t Columns that have [Type] = {bg(type_name, "s", "green")}')


    return summary.style.background_gradient(cmap='summer_r')
~~~
</p>
</details>


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
</p>
</details>


<details><summary> Read <b>specific</b> # rows <b>(if data is large)</b> </summary>
<p>
~~~python
features_sample = pd.read_csv('../input/home-credit-default-risk-feature-tools/feature_matrix.csv', nrows = 20000)
~~~
</p>
</details>

<details><summary> <b>Select Features & Target</b> </summary>
<p style="margin: 0; padding: 0">
[Get The Data 1](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/3_KNN%20Project-Mosaab.html#Get-the-Data) 

<b>NOTE:</b> This method works only if the `Target` class is the last column.

	X = df.iloc[:, :-1]
	y = df.iloc[:, -1]
	
[Get The Data 2](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/2_KNN%20-%20Full%20Pipeline.html#Get-the-Data) 
~~~python
X = df.drop('TARGET CLASS', axis=1)
y = df['TARGET CLASS']
~~~
</p>
</details>

<details><summary> <b>Add Train & Test together</b> </summary>
<p>
~~~python
# Add identifying column
app_train['set'] = 'train'
app_test['set'] = 'test'
app_test["TARGET"] = np.nan

# Append the dataframes
app = app_train.append(app_test, ignore_index = True)

train = app[app['set'] == 'train']
train.head()
~~~
</p>
</details>


<details><summary> <b>De-Ananomitizing</b> </summary>
<p>
[<b>Example</b>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeCoursesOnline.Me]%20Coursera%20-%20How%20to%20Win%20a%20Data%20Science%20Competition%20%20Learn%20from%20Top%20Kagglers/008.Exploratory%20data%20analysis/Ananomized%20Data%20&%20Visualization.html#Importing,-Importing,-Importing:) 
</p>
</details>

<details><summary> Show <b>a specific number of columns in (df.head())</b> </summary>
<p style="margin: 0; padding: 0">
~~~python
pd.options.display.max_columns = 1700
~~~
</p>
</details>

<details><summary>Convert <b>Data Types</b> for <b>LESS</b> memory size</summary>
<p style="margin: 0">
[<b>Check this Article</b>](https://medium.com/@vincentteyssier/optimizing-the-size-of-a-pandas-dataframe-for-low-memory-environment-5f07db3d72e) 
~~~python
import sys

def return_size(df):
    """Return size of dataframe in gigabytes"""
    return round(sys.getsizeof(df) / 1e9, 2)

def convert_types(df, print_info = False):
    
    original_memory = df.memory_usage().sum()
    
    # Iterate through each column
    for c in df:
        
        # Convert ids and booleans to integers
        if ('SK_ID' in c):
            df[c] = df[c].fillna(0).astype(np.int32)
            
        # Convert objects to category
        elif (df[c].dtype == 'object') and (df[c].nunique() < df.shape[0]):
            df[c] = df[c].astype('category')
        
        # Booleans mapped to integers
        elif list(df[c].unique()) == [1, 0]:
            df[c] = df[c].astype(bool)
        
        # Float64 to float32
        elif df[c].dtype == float:
            df[c] = df[c].astype(np.float32)
            
        # Int64 to int32
        elif df[c].dtype == int:
            df[c] = df[c].astype(np.int32)
        
    new_memory = df.memory_usage().sum()
    
    if print_info:
        print(f'Original Memory Usage: {round(original_memory / 1e9, 2)} gb.')
        print(f'New Memory Usage: {round(new_memory / 1e9, 2)} gb.')
        
    return df
~~~

### 2. Much more efficient one.
~~~python
from tqdm import tqdm_notebook

def reduce_mem_usage(df):
    start_mem = df.memory_usage().sum() / 1024**3
    print('~> Memory usage of dataframe is {:.3f} GB'.format(start_mem))

    for col in tqdm_notebook(df.columns):
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
        ## Comment this if you have NaN value in this column.
        # else:
            # df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024**3
    print('~> Memory usage after optimization is: {:.3f} GB'.format(end_mem))
    print('~> Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    print('---'*20)
    return df
~~~
</p>
</details>

<details><summary> Select by <b>Types</b> </summary>
<p style="margin: 0">
~~~python
df.select_dtypes('int').nunique()

# You can use it, to select `Categorical Variables`
college.select_dtypes('object').nunique()

# Returns a number of columns from the same type
college.select_dtypes('float').nunique().count()
~~~
</p>
</details>

<details><summary> Show <b># of Columns</b> for each <b>Type</b> </summary>
<p style="margin: 0">
~~~python
# Number of each type of column
app_train.dtypes.value_counts()

#### Result ####
float64    65
int64      41
object     16
dtype: int64
~~~
</p>
</details>

<details><summary> Show <b># of Unique Values</b> for each <b>Column</b> </summary>
<p>
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
</p>
</details>
<details><summary> Rename <b>Columns Name</b> </summary>
<p>
~~~python
rename = {'Column Name 1':'New Name 1', 
	'Column Name 2': 'New Name 2'}
data.rename(index=str, columns=rename, inplace=True)
~~~

</p>
</details>


<details><summary> <b>Sample, info, describe.</b> </summary>
<p style="margin: 0">
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_%20A%20Data%20Science%20Framework%20to%20achieve%2099%20Accuracy/a-data-science-framework-to-achieve-99-accuracy.html#3.2-Meet-and-Greet-Data">Meet and Greet Data</a> </p>
~~~python
df.sample(10)
df.head()
df.tail()
df.describe(include='all')
df.info()
~~~
</p>
</details>

<details><summary> Show a <b>Beautiful</b> Statistical Result </summary>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/1_Titanic%20Survival/EDA%20To%20Prediction(DieTanic).html#Embarked--%3E-Categorical-Value">See the <b>Result</b></a> <br>
<a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html">See the <b>Doc</b></a> </p>
<p>
~~~python
data.groupby(['Fare_Range'])['Survived'].mean().to_frame().style.background_gradient(cmap='summer_r')

data['Age_band'].value_counts().to_frame().style.background_gradient(cmap='summer')#checking the number of passenegers in each band

pd.crosstab(data.Parch,data.Pclass).style.background_gradient(cmap='summer_r')
~~~
</p>
</details>

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
</p>
</details>

<details><summary>Save List using <b>Pickle</b></summary>
<p>

<h4>1. Save list</h4>
~~~python
# Save the onehot columns to later use.
with open('onehot_cols.pkl', 'wb') as f:
    pickle.dump(onehot_cols, f)
~~~

<h4>2. Load List</h4>
~~~python
with open('onehot_cols.pkl', 'rb') as f:
	myList = pickle.load(f)
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
</p>
</details>

<details><summary><b>Add a record to a DataFrame</b></summary><p>
```
df = train.append(test, ignore_index=True)
```
</p></details>

 </div>


