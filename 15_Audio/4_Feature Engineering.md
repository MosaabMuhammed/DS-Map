# 4. Feature Engineering
 
<div style='width:1000px;margin:auto'>
<details><summary style='color:#72A;'><b>Merge</b> to <b>Original Data</b></summary>
<p>
~~~python
# Bin the age data
train = train.merge(cash_by_client, on = 'SK_ID_CURR', how = 'left')
test = test.merge(cash_by_client, on = 'SK_ID_CURR', how = 'left')
~~~
</p>
</details>

<ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/How%20to%20win%20a%20Data%20Science%20Competition/compute_KNN_features.html#The-task"><b><span style='color:#333'>Implement Features, based on Nearest Neighbours</span></b></a> </li>
</ul>

<details><summary><b>Feature transformations with ensembles of trees</b></summary>
<p>
<p><a href="https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html"><b>Example Sklearn</b> (Important)</a> </p>
</p>
</details>

<details><summary><b>Discretisation</b></summary><p>

<details><summary><b>Unsupervised</b></summary><p>
<details><summary><b>Equal-Width</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-08-Discretisation/08.01-Equal-width-discretisation.html#Discretisation"><b>Pandas & Sklearn & Feature-Engine</b></a> </p>

<blockquote><p>
Equal width discretisation divides the scope of possible values into N bins of the same width.
$$Width = \frac{max - min}{N}$$
</p></blockquote>
</p></details>
<details><summary><b>Equal-Frequency</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-08-Discretisation/08.02-Equal-frequency-discretisation.html#Equal-frequency-discretisation"><b>Pandas & Sklearn & Feature-Engine</b></a> </p>

<blockquote><p>
Divides the range based on quantiles.
</p></blockquote>
</p></details>
<details><summary><b>K-means</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-08-Discretisation/08.03-Discretisation-with-kmeans.html#Discretisation-with-k-means-clustering"><b>Sklearn</b></a> </p>

<blockquote><p>
This method consists in applying k-means clustering to the continuous variable.
</p></blockquote>
</p></details>
<a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-08-Discretisation/08.04-Discretisation-plus-Encoding.html#Discretisation-plus-Encoding"><b>Applying Cat Encoders on Discretised Features</b></a>
</p></details>

<details><summary><b>Supervised</b></summary><p>

<details><summary><b>Decision Tree</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-08-Discretisation/08.05-Discretisation-using-Decision-Trees.html#Discretisation-with-Decision-Trees"><b>Sklearn</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-08-Discretisation/08.06-Discretisation-using-Decision-Trees-and-Feature-Engine.html#Discretisation-with-Decision-Trees-using-Feature-Engine"><b>Feature-Engine</b></a> </p>

<blockquote><p>
Decision tree creates a discrete output, which values are the predictions at each of its n leaves, and which it's monotonic to the target variable.
</p></blockquote>
</p></details>

</p></details>

<details><summary><b>Domain-Knowledge</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-08-Discretisation/08.07-Domain-knowledge-discretisation.html#Domain-knowledge-discretisation"><b>Notebook</b></a> </p>

</p></details>

</p></details><details><summary><b>Polynomial Features</b></summary><p>

<details><summary><b>Core Code</b></summary>
<p>
~~~python
from sklearn.preprocessing import PolynomialFeatures

# Make a new dataframe for polynomial features
poly_features = app_train[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH', 'TARGET']]
poly_features_test = app_test[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH']]
                         
# Create the polynomial object with specified degree
poly_transformer = PolynomialFeatures(degree = 3)
# Train the polynomial features
poly_transformer.fit(poly_features)

# Transform the features
poly_features = poly_transformer.transform(poly_features)
poly_features_test = poly_transformer.transform(poly_features_test)
print('Polynomial Features shape: ', poly_features.shape)

<h4><h4><h4> Result <h4><h4><h4>##
Polynomial Features shape:  (307511, 35)
~~~
</p>
</details>


<details><summary>See <b>Features name</b></summary>
<p>
~~~python
## Get the name of the features
poly_transformer.get_feature_names(input_features = ['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH'])[:15]

####### Result
['1',
 'EXT_SOURCE_1',
 'EXT_SOURCE_2',
 'EXT_SOURCE_3',
 'DAYS_BIRTH',
 'EXT_SOURCE_1^2',
 'EXT_SOURCE_1 EXT_SOURCE_2',
 'EXT_SOURCE_1 EXT_SOURCE_3',
 'EXT_SOURCE_1 DAYS_BIRTH',
 'EXT_SOURCE_2^2',
 'EXT_SOURCE_2 EXT_SOURCE_3',
 'EXT_SOURCE_2 DAYS_BIRTH',
 'EXT_SOURCE_3^2',
 'EXT_SOURCE_3 DAYS_BIRTH',
 'DAYS_BIRTH^2']
~~~
</p>
</details>

<details><summary><b>See if the NEW features are corrleated with TARGET or not</b></summary><p>
~~~python
# Create a dataframe of the features 
poly_features = pd.DataFrame(poly_features, 
                             columns = poly_transformer.get_feature_names(['EXT_SOURCE_1', 'EXT_SOURCE_2', 
                                                                           'EXT_SOURCE_3', 'DAYS_BIRTH']))

# Add in the target
poly_features['TARGET'] = poly_target

# Find the correlations with the target
poly_corrs = poly_features.corr()['TARGET'].sort_values()

# Display most negative and most positive
print(poly_corrs.head(10))
print(poly_corrs.tail(5))

<h4><h4><h4>## Result <h4><h4><h4>#
EXT_SOURCE_2 EXT_SOURCE_3                -0.193939
EXT_SOURCE_1 EXT_SOURCE_2 EXT_SOURCE_3   -0.189605
EXT_SOURCE_2 EXT_SOURCE_3 DAYS_BIRTH     -0.181283
EXT_SOURCE_2^2 EXT_SOURCE_3              -0.176428
EXT_SOURCE_2 EXT_SOURCE_3^2              -0.172282
EXT_SOURCE_1 EXT_SOURCE_2                -0.166625
EXT_SOURCE_1 EXT_SOURCE_3                -0.164065
EXT_SOURCE_2                             -0.160295
EXT_SOURCE_2 DAYS_BIRTH                  -0.156873
EXT_SOURCE_1 EXT_SOURCE_2^2              -0.156867
Name: TARGET, dtype: float64

DAYS_BIRTH     -0.078239
DAYS_BIRTH^2   -0.076672
DAYS_BIRTH^3   -0.074273
TARGET          1.000000
1                    NaN
Name: TARGET, dtype: float64
~~~
</p></details>


<details><summary>Add the <b>new</b> features to the <b>main</b> dataframe</summary><p>
~~~python
# Put test features into dataframe
poly_features_test = pd.DataFrame(poly_features_test, 
                                  columns = poly_transformer.get_feature_names(['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH']))

# Merge polynomial features into training dataframe
poly_features['SK_ID_CURR'] = app_train['SK_ID_CURR']
app_train_poly = app_train.merge(poly_features, on = 'SK_ID_CURR', how = 'left')

# Merge polnomial features into testing dataframe
poly_features_test['SK_ID_CURR'] = app_test['SK_ID_CURR']
app_test_poly = app_test.merge(poly_features_test, on = 'SK_ID_CURR', how = 'left')

# Align the dataframes
app_train_poly, app_test_poly = app_train_poly.align(app_test_poly, join = 'inner', axis = 1)

# Print out the new shapes
print('Training data with polynomial features shape: ', app_train_poly.shape)
print('Testing data with polynomial features shape:  ', app_test_poly.shape)

###### Result
Training data with polynomial features shape:  (307511, 275)
Testing data with polynomial features shape:   (48744, 275)
~~~
</p></details>
</p></details><details><summary><b>Numeric Aggregation</b> [count, min, max, mean, sum]</summary><p>
~~~python
def agg_numeric(df, group_var, df_name):
    """Aggregates the numeric values in a dataframe. This can
    be used to create features for each instance of the grouping variable.
    
    Parameters
    --------
        df (dataframe): 
            the dataframe to calculate the statistics on
        group_var (string): 
            the variable by which to group df
        df_name (string): 
            the variable used to rename the columns
        
    Return
    --------
        agg (dataframe): 
            a dataframe with the statistics aggregated for 
            all numeric columns. Each instance of the grouping variable will have 
            the statistics (mean, min, max, sum; currently supported) calculated. 
            The columns are also renamed to keep track of features created.
    
    """
    # Remove id variables other than grouping variable
    for col in df:
        if col != group_var and 'SK_ID' in col:
            df = df.drop(columns = col)
            
    group_ids = df[group_var]
    numeric_df = df.select_dtypes('number')
    numeric_df[group_var] = group_ids

    # Group by the specified variable and calculate the statistics
    agg = numeric_df.groupby(group_var).agg(['count', 'mean', 'max', 'min', 'sum']).reset_index()

    # Need to create new column names
    columns = [group_var]

    # Iterate through the variables names
    for var in agg.columns.levels[0]:
        # Skip the grouping variable
        if var != group_var:
            # Iterate through the stat names
            for stat in agg.columns.levels[1][:-1]:
                # Make a new column name for the variable and stat
                columns.append('%s_%s_%s' % (df_name, var, stat))

    agg.columns = columns
    
    # Remove the columns with all redundant values
    _, idx = np.unique(agg, axis = 1, return_index=True)
    agg = agg.iloc[:, idx]
    
    return agg
    
###### To use it
bureau_agg_new = agg_numeric(bureau.drop(columns = ['SK_ID_BUREAU']), group_var = 'SK_ID_CURR', df_name = 'bureau')
bureau_agg_new.head()
~~~
</p></details><details><summary><b>Categorical Aggregation</b> [_count_, _norm_count_]</summary><p>
~~~python
def count_categorical(df, group_var, df_name):
    """Computes counts and normalized counts for each observation
    of `group_var` of each unique category in every categorical variable
    
    Parameters
    --------
    df : dataframe 
        The dataframe to calculate the value counts for.
        
    group_var : string
        The variable by which to group the dataframe. For each unique
        value of this variable, the final dataframe will have one row
        
    df_name : string
        Variable added to the front of column names to keep track of columns

    
    Return
    --------
    categorical : dataframe
        A dataframe with counts and normalized counts of each unique category in every categorical variable
        with one row for every unique value of the `group_var`.
        
    """
    
    # Select the categorical columns
    categorical = pd.get_dummies(df.select_dtypes('category'))

    # Make sure to put the identifying id on the column
    categorical[group_var] = df[group_var]

    # Groupby the group var and calculate the sum and mean
    categorical = categorical.groupby(group_var).agg(['sum', 'mean'])
    
    column_names = []
    
    # Iterate through the columns in level 0
    for var in categorical.columns.levels[0]:
        # Iterate through the stats in level 1
        for stat in ['count', 'norm_count']:
            # Make a new column name
            column_names.append('%s_%s_%s' % (df_name, var, stat))
    
    categorical.columns = column_names
    
    # Remove duplicate columns by values
    _, idx = np.unique(categorical, axis = 1, return_index = True)
    categorical = categorical.iloc[:, idx]
    
    return categorical
bureau_counts = count_categorical(bureau, group_var = 'SK_ID_CURR', df_name = 'bureau')
bureau_counts.head()
~~~
</p>
</details><details><summary><b>Aggregation</b> b/w 2 datasets having 2 <b>Different IDs</b></summary><p>
~~~python
def aggregate_client(df, group_vars, df_names):
    """Aggregate a dataframe with data at the loan level 
    at the client level
    
    Args:
        df (dataframe): data at the loan level
        group_vars (list of two strings): grouping variables for the loan 
        and then the client (example ['SK_ID_PREV', 'SK_ID_CURR'])
        names (list of two strings): names to call the resulting columns
        (example ['cash', 'client'])
        
    Returns:
        df_client (dataframe): aggregated numeric stats at the client level. 
        Each client will have a single row with all the numeric data aggregated
    """
    
    # Aggregate the numeric columns
    df_agg = agg_numeric(df, parent_var = group_vars[0], df_name = df_names[0])
    
    # If there are categorical variables
    if any(df.dtypes == 'category'):
    
        # Count the categorical columns
        df_counts = agg_categorical(df, parent_var = group_vars[0], df_name = df_names[0])

        # Merge the numeric and categorical
        df_by_loan = df_counts.merge(df_agg, on = group_vars[0], how = 'outer')

        gc.enable()
        del df_agg, df_counts
        gc.collect()

        # Merge to get the client id in dataframe
        df_by_loan = df_by_loan.merge(df[[group_vars[0], group_vars[1]]], on = group_vars[0], how = 'left')

        # Remove the loan id
        df_by_loan = df_by_loan.drop(columns = [group_vars[0]])

        # Aggregate numeric stats by column
        df_by_client = agg_numeric(df_by_loan, parent_var = group_vars[1], df_name = df_names[1])

        
    # No categorical variables
    else:
        # Merge to get the client id in dataframe
        df_by_loan = df_agg.merge(df[[group_vars[0], group_vars[1]]], on = group_vars[0], how = 'left')
        
        gc.enable()
        del df_agg
        gc.collect()
        
        # Remove the loan id
        df_by_loan = df_by_loan.drop(columns = [group_vars[0]])
        
        # Aggregate numeric stats by column
        df_by_client = agg_numeric(df_by_loan, parent_var = group_vars[1], df_name = df_names[1])
        
    # Memory management
    gc.enable()
    del df, df_by_loan
    gc.collect()

    return df_by_client
    
<h4>## Calling the Function <h4><h4>#
cash_by_client = aggregate_client(cash, group_vars = ['SK_ID_PREV', 'SK_ID_CURR'], df_names = ['cash', 'client'])
~~~

</p></details><details><summary><b>Date & Time-Series </b>Features</summary><p>
<ul><li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-12-Engineering-Date-Time/12.01_Engineering_dates.html#Engineering-Dates"><b>Date Features</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-12-Engineering-Date-Time/12.02_Engineering_time.html#Engineering-Time"><b>Time Features</b></a></li>

<li><h4>tsfresh</h4> for time-series feature-engineering
<p>Read the documentation for more details.</p>
```
from tsfresh.feature_extraction import feature_calculators as fc

# tsfreash based features.
feature_dict["abs_energy"] = fc.abs_energy(x)
feature_dict['count_above_mean'] = fc.count_above_mean(x)
feature_dict['count_below_mean'] = fc.count_below_mean(x)
feature_dict['mean_abs_change'] = fc.mean_abs_change(x)
feature_dict['mean_change'] = fc.mean_change(x)
```
</li></ul>


```
# Import add_datepart function
from fastai.tabular import add_datepart

# Put in the dataframe and name of date column
add_datepart(df_raw, 'saledate')
```

</p></details><details><summary><b>Automated</b> Feature Engineering <b>(Featuretools)</b></summary><p>

<details><summary>Convert limited <b>discrete nums</b> into <b>Booleans</b> using <b>FeatureTools</b></summary><p>
~~~python
app_types = {}

# Iterate through the columns and record the Boolean columns
for col in app_train:
    # If column is a number with only two values, encode it as a Boolean
    if (app_train[col].dtype != 'object') and (len(app_train[col].unique()) <= 2):
        app_types[col] = ft.variable_types.Boolean

print('Number of boolean variables: ', len(app_types))
~~~
</p>
</details>

<details><summary><b>1. Entities & EntitySet</b></summary><p>
~~~python
import featuretools as tf

es = ft.EntitySet(id = 'clients')

es = es.entity_from_dataframe(entity_id = 'loans', dataframe = loans, 
                              variable_types = {'repaid': ft.variable_types.Categorical},
                              index = 'loan_id', 
                              time_index = 'loan_start')


# Entities with a unique index
es = es.entity_from_dataframe(entity_id = 'app', dataframe = app, index = 'SK_ID_CURR')

# Entities that do not have a unique index
es = es.entity_from_dataframe(entity_id = 'bureau_balance', dataframe = bureau_balance, 
                              make_index = True, index = 'bureaubalance_index')
~~~
</p></details>

<details><summary><b>1.2 Entities & EntitySet for DataFrame with 2 Ids</b></summary><p>
```
import featuretools as tf

# Create and entity set 'es'
es = ft.EntitySet(id='sales')  ## --> "sales" is made-up name.

# Adding a dataframe
es.entity_from_dataframe(entity_id='bigmart',
                         dataframe=df,
                         index='id')   ## --> Actual column name in your dataframe
# Realize the second id
es.normalize_entity(base_entity_id='bigmart',
                    new_entity_id='outlet',
                    index='Outlet_Identifier',
                    additional_variables=['Outlet_Establishment_Year',
                                          'Outlet_Size', 
                                          'Outlet_Location_Type',
                                          'Outlet_Type'])

print(es)
```
</p></details>

<details><summary><b>2. Table Relationships</b></summary><p>
~~~python
# Relationship between app and bureau
r_app_bureau = ft.Relationship(es['app']['SK_ID_CURR'], es['bureau']['SK_ID_CURR'])

# Relationship between bureau and bureau balance
r_bureau_balance = ft.Relationship(es['bureau']['SK_ID_BUREAU'], es['bureau_balance']['SK_ID_BUREAU'])

# Add in the defined relationships
es = es.add_relationships([r_app_bureau, r_bureau_balance, r_app_previous,
                           r_previous_cash, r_previous_installments, r_previous_credit])
# Print out the EntitySet
es

####### RESULT ###
Entityset: clients
  Entities:
    app [Rows: 2002, Columns: 123]
    bureau [Rows: 1001, Columns: 17]
    previous [Rows: 1001, Columns: 37]
    bureau_balance [Rows: 1001, Columns: 4]
    cash [Rows: 1001, Columns: 9]
    installments [Rows: 1001, Columns: 9]
    credit [Rows: 1001, Columns: 24]
  Relationships:
    bureau.SK_ID_CURR -> app.SK_ID_CURR
    bureau_balance.SK_ID_BUREAU -> bureau.SK_ID_BUREAU
    previous.SK_ID_CURR -> app.SK_ID_CURR
    cash.SK_ID_PREV -> previous.SK_ID_PREV
    installments.SK_ID_PREV -> previous.SK_ID_PREV
    credit.SK_ID_PREV -> previous.SK_ID_PREV
~~~
</p></details>

<details><summary><b>3. Feature Primitives</b></summary><p>
~~~python
# List the primitives in a dataframe
primitives = ft.list_primitives()
pd.options.display.max_colwidth = 100
primitives[primitives['type'] == 'aggregation'].head(10)
primitives[primitives['type'] == 'transform'].head(10)

~~~
</p></details>

<details><summary><b>4. Deep Feature Synthesis</b></summary><p>
~~~python
### Know the features names before performing them ##
# Default primitives from featuretools
default_agg_primitives =  ["sum", "std", "max", "skew", "min", "mean", "count", "percent_true", "num_unique", "mode"]
default_trans_primitives =  ["day", "year", "month", "weekday", "haversine", "numwords", "characters"]

# DFS with specified primitives
# target_entity is nothing but the entity ID for which we wish to create new features (in this case, it is the entity ‘app’).
# The parameter max_depth controls the complexity of the features being generated by stacking the primitives.
feature_names = ft.dfs(entityset = es, target_entity = 'app',
                       trans_primitives = default_trans_primitives,
                       agg_primitives=default_agg_primitives, 
                       max_depth = 2, features_only=True)

print('%d Total Features' % len(feature_names))
~~~
~~~python
# DFS with default primitives
feature_matrix, feature_names = ft.dfs(entityset = es, target_entity = 'app',
                                       trans_primitives = default_trans_primitives,
                                       agg_primitives=default_agg_primitives, 
                                        max_depth = 2, features_only=False, verbose = True)

pd.options.display.max_columns = 1700
feature_matrix.head(10)
~~~
~~~python
# Perform deep feature synthesis without specifying primitives
features, feature_names = ft.dfs(entityset=es, target_entity='clients', 
                                 max_depth = 2)
~~~
</p></details>

<details><summary><b>4.1 DFS</b> using <b>chunk_size</b></summary><p>
<p><a href="https://docs.featuretools.com/guides/performance.html#adjust-chunk-size"><b>Know More</b></a> </p>
~~~python
time_features, time_feature_names = ft.dfs(entityset = es, target_entity = 'app_train', 
                                           trans_primitives = ['cum_sum', 'time_since_previous'], max_depth = 2,
                                           agg_primitives = ['trend'] ,
                                           features_only = False, verbose = True,
                                           chunk_size = len(app_train),
                                           ignore_entities = ['app_test'])
~~~
</p>
</details>

<details><summary><b>4.2</b> Using <b>Interesting Values</b></summary><p>
<p><a href="https://docs.featuretools.com/guides/tuning_dfs.html#add-interesting-values-to-variables"><b>Know More</b></a> </p>
~~~python
time_features, time_feature_names = ft.dfs(entityset = es, target_entity = 'app_train', 
                                           trans_primitives = ['cum_sum', 'time_since_previous'], max_depth = 2,
                                           agg_primitives = ['trend'] ,
                                           features_only = False, verbose = True,
                                           chunk_size = len(app_train),
                                           ignore_entities = ['app_test'])
~~~
</p>
</details>


<details><summary><b>4.3</b> Using <b>Seed Features</b></summary>
<p>
<p><a href="https://docs.featuretools.com/guides/tuning_dfs.html#using-seed-features"><b>Know More</b></a> </p>
~~~python
# Late Payment seed feature
late_payment = ft.Feature(es['installments']['installments_due_date']) < ft.Feature(es['installments']['installments_paid_date'])

# Rename the feature
late_payment = late_payment.rename("late_payment")

# DFS with seed features
seed_features, seed_feature_names = ft.dfs(entityset = es,
                                           target_entity = 'app_train',
                                           agg_primitives = ['percent_true', 'mean'],
                                           trans_primitives = [], 
                                           seed_features = [late_payment],
                                           features_only = False, verbose = True,
                                           chunk_size = len(app_train),
                                           ignore_entities = ['app_test'])
~~~
~~~python
<h4><h4>### Another Example <h4><h4><h4>#
# Create a feed representing whether the loan is past due
past_due = ft.Feature(es['bureau_balance']['STATUS']).isin(['1', '2', '3', '4', '5'])
past_due = past_due.rename("past_due")

# DFS with specified seed feature
seed_features, seed_feature_names = ft.dfs(entityset = es,
                                           target_entity = 'app_train',
                                           agg_primitives = ['percent_true', 'mean'],
                                           trans_primitives = [], 
                                           seed_features = [past_due],
                                           features_only = False, verbose = True,
                                           chunk_size = len(app_train),
                                           ignore_entities = ['app_test'])
~~~
</p>
</details>

<details><summary><b>4.4</b> Using </b>Custom Feature Primitive</b></summary>
<p>
<p><a href="https://docs.featuretools.com/automated_feature_engineering/primitives.html#defining-custom-primitives"><b>Know More</b></a> </p>
~~~python
from featuretools.variable_types import (
    Boolean, Datetime,
    DatetimeTimeIndex,
    Discrete,
    Index,
    Numeric,
    Variable,
    Id
)

from featuretools.primitives import AggregationPrimitive, make_agg_primitive
from datetime import datetime, timedelta

from collections import Counter


def normalized_mode_count(x):
    """
    Return the fraction of total observations that 
    are the most common observation. For example, 
    in an array of ['A', 'A', 'A', 'B', 'B'], the 
    function will return 0.6."""
    
    if x.mode().shape[0] == 0:
        return np.nan
            
    # Count occurence of each value
    counts = dict(Counter(x.values))
    # Find the mode
    mode = x.mode().iloc[0]
    # Divide the occurences of mode by the total occurrences
    return counts[mode] / np.sum(list(counts.values()))
    

NormalizedModeCount = make_agg_primitive(function = normalized_mode_count, 
                                         input_types = [Discrete],
                                         return_type = Numeric)

# Function from https://codereview.stackexchange.com/a/15095
def longest_repetition(x):
    """
    Returns the item with most consecutive occurrences in `x`. 
    If there are multiple items with the same number of conseqcutive occurrences,
    it will return the first one. If `x` is empty, returns None. 
    """
    
    x = x.dropna()
    
    if x.shape[0] < 1:
        return None
    
    # Set the longest element
    longest_element = current_element = None
    longest_repeats = current_repeats = 0
    
    # Iterate through the iterable
    for element in x:
        if current_element == element:
            current_repeats += 1
        else:
            current_element = element
            current_repeats = 1
        if current_repeats > longest_repeats:
            longest_repeats = current_repeats
            longest_element = current_element
            
    return longest_element

LongestSeq = make_agg_primitive(function = longest_repetition,
                                     input_types = [Discrete],
                                     return_type = Discrete)   
~~~

~~~python
def s_corr_calc(numeric1, numeric2):
    return spearmanr(numeric1, numeric2)[0]

scorr_ = make_agg_primitive(function=s_corr_calc,
                            input_types=[ft.variable_types.Numeric, ft.variable_types.Numeric],
                            return_type=ft.variable_types.Numeric)
~~~

~~~python
def p_corr_calc(numeric1, numeric2):
    return np.corrcoef(numeric1, numeric2)[0, 1]

pcorr_ = make_agg_primitive(function=p_corr_calc,
                            input_types=[ft.variable_types.Numeric, ft.variable_types.Numeric],
                            return_type=ft.variable_types.Numeric)
~~~

~~~python
# Custom primitive
def range_calc(numeric):
    return np.max(numeric)  - np.min(numeric)

range_ = make_agg_primitive(
            function=range_calc,
            input_types=[ft.variable_types.Numeric],
            return_type=ft.variable_types.Numeric)
~~~

~~~python
# DFS with custom features
custom_features, custom_feature_names = ft.dfs(entityset = es,
                                              target_entity = 'app_train',
                                              agg_primitives = [NormalizedModeCount, LongestSeq],
                                              max_depth = 2,
                                              trans_primitives = [],
                                              features_only = False, verbose = True,
                                              chunk_size = len(app_train),
                                              ignore_entities = ['app_test'])

custom_features.iloc[:, -40:].head()
~~~
</p>
</details>

<details><summary><b>5. Remove Low Inforamtion Features</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/3_Home%20Credit%20Loans/4_Tuning%20Automated%20Feature%20Engineering%20(Explo%2099027d.html#Remove-Features"><b>Know More</b></a></p>
~~~python
from featuretools import selection

# Remove low information features
feature_matrix2 = selection.remove_low_information_features(feature_matrix)
print('Removed %d features from training features'  % (feature_matrix.shape[1] - feature_matrix2.shape[1]))
~~~
</p>
</details>

</p>
</details>


<details><summary><b>Graph-based Featuers</b></summary><p>
<a href="./4_feature_engineering/Social network Graph Link Prediction - Facebook Challenge.html"><b>notebook</b></a>
</p></details>

</div>