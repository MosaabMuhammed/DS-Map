<h1 style='color:darkcyan;text-decoration:underline'>2. Data Problems</h1>


<div style='width:1000px;margin:auto'>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_%20A%20Data%20Science%20Framework%20to%20achieve%2099%20Accuracy/a-data-science-framework-to-achieve-99-accuracy.html#3.21-The-4-C's-of-Data-Cleaning:-Correcting,-Completing,-Creating,-and-Converting">Explanation of the 4'C of <b>Data Cleaning</b>.</a> </p>


<details><summary><span style='color:#333;font-size:25px;font-weight:bold;text-decoration:underline'>1. Related to Dataset:</span></summary>
<p>

<details><summary><b>1. Imbalanced Data set:</b></summary>
<p>

<ul>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Applied%20ML%20Course/0_Code/11_Classification%20Algorithms%20in%20Real-World%20problems/1_Dealing%20with%20Imbalanced%20Datasets.html"><span style='color:#333333'><b>1. Imbalanced Data set:</b></span></a> </p></li>

<li><p><a href="https://imbalanced-learn.org/en/stable/over_sampling.html"><span style='color:#333333'><b>2. Another way</b> (better)</span></a> </p></li>
</ul>

</p>
</details>

<details><summary><b>2. Large Dataset:</b></summary>
<p>
<details><summary>Using <b>Chunksize</b> in pd.read_csv()</summary>
<p>
~~~python
df = pd.read_csv('/kaggle/input/train.csv', chunksize=1000)
~~~
</p>
</details>
<details><summary>From<b>CSV</b> To <b>HDF5</b></summary>
<p>
<ul>
<li><a href="https://stackoverflow.com/questions/27203161/convert-large-csv-to-hdf5"><b>After reading csv</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/7_From%20Large%20CSV%20to%20small%20HDF5/__notebook__.html"><b>When we can't read the csv</b></a> </li>
</ul>

</p>
</details>

<details><summary>From<b>CSV</b> To <b>npz</b></summary>
<p>
<ul>
<li><a href="https://docs.scipy.org/doc/numpy/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed"><b>np.savez_compressed</b></a> </li>
</ul>
</p>
</details>


<details><summary><b>Reduced size of dataset</b></summary>
<p>
~~~python
from tqdm import tqdm_notebook

def reduce_mem_usage(df):
    start_mem = df.memory_usage().sum() / 1024<b>3
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

    end_mem = df.memory_usage().sum() / 1024<b>3
    print('~> Memory usage after optimization is: {:.3f} GB'.format(end_mem))
    print('~> Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    print('---'*20)
    return df
~~~
</p>
</details>


</p>
</details>

</p>
</details>

<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>2. Categorical ~> Numerical:</b></summary>
<p>

<details><summary> <b>1. Response Coding</b> </summary>
<p>
~~~python
## Note: Modify [X_train] to fit your code
## NOTE: Modify the dataframe at the end.
def ResponseCoding(train_df, feature, target, alpha=10):
    feature_count = train_df[feature].value_counts()
    n_classes     = train_df[target].nunique()
    feature_dict  = dict()

    # Compute the Response Coding / Mean Replacement.
    for i, denominator in feature_count.items():
        vec = []
        for k in range(0, n_classes):
            nominator         = len(train_df.loc[(train_df[target]==k) & (train_df[feature]==i)])
            laplace_smoothing = (nominator + alpha)/(denominator+(n_classes*alpha))
            vec.append(laplace_smoothing)
        feature_dict[i] = vec
    return feature_dict, feature_count, n_classes


def assignResponseCoding(df, col_id, feature, feature_dict, feature_count, n_classes):
    feature_final = [[] for i in range(n_classes)]
    for idx, row in df.iterrows():
        for i in range(n_classes):
            if row[feature] in dict(feature_count).keys():
                feature_final[i].append(feature_dict[row[feature]][i])
            else:
                feature_final[i].append(1/n_classes)

    return pd.DataFrame({str(col_id): df[col_id],
                         str(feature)+'_responseCoding_0': feature_final[0],
                         str(feature)+'_responseCoding_1': feature_final[1]})
~~~
~~~python
def add_df(df, df_encoding):
    return df.merge(df_encoding, on='id', how='left')
~~~
~~~python
## Response Coding for [Train] & [Test] dataset
# Note: Specify the features here below to be encoded.
features = ['nom_5', 'nom_6', 'nom_7', 'nom_8', 'nom_9']
nom_responseCoding_train = pd.DataFrame({'id': train.id})
nom_responseCoding_test = pd.DataFrame({'id': test.id})

for col in features:
    print(f'~> ResponseCoding for {bg(col+str("..."), "s", "green")}')
    feature_dict, feature_count, n_classes = ResponseCoding(train, 'nom_5', 'target')
   
    print(f'- Assigning {bg("Train", "s")}')
    temp_train = assignResponseCoding(train, 'id', col, feature_dict, feature_count, n_classes)
    nom_responseCoding_train = add_df(nom_responseCoding_train, temp_train)
    
    print(f'- Assigning {bg("Test", "s")}')
    temp_test = assignResponseCoding(test, 'id', col, feature_dict, feature_count, n_classes)
    nom_responseCoding_test = add_df(nom_responseCoding_test, temp_test)
~~~
</p>
</details>

<details><summary><b>2.1 One-Hot Encoding (Nominal)</b> </summary>
<p>
~~~

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in df_copy.columns:
    df_copy[col] = le.fit_transform(df_copy[col])
~~~ 
</p>
</details>


<details><summary><b>2.2 One-Hot Encoding (Ordinal)</b></summary>
<p style="margin: 0">
<p><a href="https://www.kaggle.com/jemseow/machine-learning-to-predict-app-ratings">See <b>Code</b> in Kaggle</a> </p>

~~~python
#Cleaning of content rating classification
RatingL = df['Content Rating'].unique()
RatingDict = {}

for i in range(len(RatingL)):
    RatingDict[RatingL[i]] = i
   
df['Content Rating'] = df['Content Rating'].map(RatingDict).astype(int)
~~~
</p>
</details>



<details><summary><b>2.3 Dummy</b> Variables</summary>
<p style="margin: 0">
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/11_Decision%20Tree,%20Random%20Forest/2_Decision%20Trees%20and%20Random%20Forest%20Project-Mosaab.html#Get-Dummy-Variable">Dummy Variable in Action</a> </p>

~~~python
# Always remove one column of the dummy variables.
cat_feats = ['Categorical Column name']

final_data = pd.get_dummies(whole_dataset, columns=cat_feats, drop_first=True)
~~~

~~~python
# Select all the categorical variables then get the dummy variables out of them
cat_vars = df.select_dtypes(include=['object']).copy().columns
for var in cat_vars:
	# For each cat add dummy var, drop original column
	df = pd.concat([df.drop(var, axis=1), pd.get_dummies(df[var], prefix=var, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)
~~~

<h4>We can make the dummy variables sparse in order to make it fit into memory, then convert it back to form which suitable for models to handle.</h4>
<h4>Note: (.sparse.to_coo().tocsr()) is responsible to make it suitable for models to handle.</h4>
~~~python
X_comb_onehot = pd.get_dummies(pd.concat([X_train, X_test]), sparse=True, columns=X_train.columns)
X_train_sparse = X_comb_onehot.loc[y_train.index].sparse.to_coo().tocsr()
X_test_sparse = X_comb_onehot.drop(index=y_train.index).sparse.to_coo().tocsr()

lr_params = dict(solver="lbfgs", C=0.2, max_iter=5000, random_state=0)
models = [LogisticRegression(**lr_params).fit(X_train_sparse[t], y_train[t])
          for t, _ in KFold(5, random_state=0).split(X_train_sparse)]
~~~
</p>
</details>

<details><summary>From <b>One-Hot Encoding</b> To <b>Ordinal</b></summary>
<p>
~~~
ind['inst'] = np.argmax(np.array(ind[[c for c in ind if c.startswith('instl')]]), axis = 1)
~~~ 
</p>
</details>

<details><summary><b>3. Label Encoder</b></summary>
<p style="margin: 0">
~~~python
df[col] = df[col].factorize()[0]
~~~
~~~python
# Create a label encoder object
le = LabelEncoder()
le_count = 0

# Iterate through the columns
for col in app_train:
    if app_train[col].dtype == 'object':
        # If 2 or fewer unique categories
        if len(list(app_train[col].unique())) <= 2:
            # Train on the training data
            le.fit(app_train[col])
            # Transform both training and testing data
            app_train[col] = le.transform(app_train[col])
            app_test[col] = le.transform(app_test[col])
            
            # Keep track of how many columns were label encoded
            le_count += 1
            
print('%d columns were label encoded.' % le_count)
~~~
<h4> 2. A Better Version</h4>
~~~python
from tqdm import tqdm_notebook

cat_columns = [col for col in train.columns if col not in ['id', 'target', 'dataset_type']]
for col in tqdm_notebook(cat_columns):
    le = LabelEncoder()
    le.fit(list(train[col].astype(str).values) + list(test[col].astype(str).values))
    train[col] = le.transform(list(train[col].astype(str).values))
    test[col] = le.transform(list(test[col].astype(str).values))   
~~~
</p>
</details>

<details><summary> <b>4. Thermometer Encoding [Ordinal]</b></summary>
<p>
<h4>Note:</h4>
<p class='alert alert-info'>&nbsp;&nbsp;&nbsp;&nbsp;You can encode ordinal data using the thermometer trick. If there are 𝑁 possible values for the variable, then you map each value to a 𝑁-vector, where you put a 1 in the position that matches the value of the variable and all subsequent position.
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;For instance: first place ↦(1,1,1), second place ↦(0,1,1), third place ↦(0,0,1).</p>

<h4>1. Build the Class.</h4>
~~~python
from sklearn.base import TransformerMixin
from itertools import repeat
import scipy


class ThermometerEncoder(TransformerMixin):
    """
    Assumes all values are known at fit
    """
    def __init__(self, sort_key=None):
        self.sort_key = sort_key
        self.value_map_ = None
    
    def fit(self, X, y=None):
        self.value_map_ = {val: i for i, val in enumerate(sorted(X.unique(), key=self.sort_key))}
        return self
    
    def transform(self, X, y=None):
        values = X.map(self.value_map_)
        
        possible_values = sorted(self.value_map_.values())
        
        idx1 = []
        idx2 = []
        
        all_indices = np.arange(len(X))
        
        for idx, val in enumerate(possible_values[:-1]):
            new_idxs = all_indices[values > val]
            idx1.extend(new_idxs)
            idx2.extend(repeat(idx, len(new_idxs)))
            
        result = scipy.sparse.coo_matrix(([1] * len(idx1), (idx1, idx2)), shape=(len(X), len(possible_values)), dtype="int8")
            
        return result
~~~

<h4>2. How to use</h4>
~~~python
thermos=[]
for col in ["ord_1", "ord_2", "ord_3", "ord_4", "ord_5a", "day", "month"]:
    if col=="ord_1":
        sort_key=['Novice', 'Contributor', 'Expert', 'Master', 'Grandmaster'].index
    elif col=="ord_2":
        sort_key=['Freezing', 'Cold', 'Warm', 'Hot', 'Boiling Hot', 'Lava Hot'].index
    elif col in ["ord_3", "ord_4", "ord_5a"]:
        sort_key=str
    elif col in ["day", "month"]:
        sort_key=int
    else:
        raise ValueError(col)
    
    enc=ThermometerEncoder(sort_key=sort_key)
    thermos.append(enc.fit_transform(X[col]))
~~~
</p>
</details>

<details><summary> <b>5. Feature Hashing</b></summary>
<p>
<h4> Using FeatureHasher (Multiple Columns)</h4>
~~~python
from sklearn.feature_extraction import FeatureHasher

X_train_hash=X.copy()
for c in X.columns:
    X_train_hash[c]=X[c].astype('str')
    
hashing=FeatureHasher(input_type='string')
train=hashing.transform(X_train_hash.values)

print('train data set has got {} rows and {} columns'.format(train.shape[0],train.shape[1]))
<h4><h4># Result <h4><h4><h4>
train data set has got 300000 rows and 1048576 columns
~~~

<h4> Using Hash Function (One Column)</h4>
~~~python
for col in high_card_feats:
    enc_nom_1 = train[col].value_counts(normalize=True)
    train[f'freq_{col}'] = train[col].apply(lambda x: enc_nom_1[x])
~~~
</p>
</details>


<details><summary> <b>6. Encoding with dataset statistics</b></summary>
<p>
~~~python
## The easiest way to do it is replace every category with the number of times that we saw it in the dataset. 

X_train_stat=X.copy()
for c in X_train_stat.columns:
    if(X_train_stat[c].dtype=='object'):
        X_train_stat[c]=X_train_stat[c].astype('category')
        counts=X_train_stat[c].value_counts()
        counts=counts.sort_index()
        counts=counts.fillna(0)
        counts += np.random.rand(len(counts))/1000
        X_train_stat[c].cat.categories=counts
~~~
</p>
</details>


<details><summary> <b>7. Encoding Cyclic Features (Day, Month, ...)</b></summary>
<p>
~~~python
X_train_cyclic=X.copy()
columns=['day','month']
for col in columns:
    X_train_cyclic[col+'_sin']=np.sin((2*np.pi*X_train_cyclic[col])/max(X_train_cyclic[col]))
    X_train_cyclic[col+'_cos']=np.cos((2*np.pi*X_train_cyclic[col])/max(X_train_cyclic[col]))
X_train_cyclic=X_train_cyclic.drop(columns,axis=1)
~~~
</p>
</details>

<details><summary> <b>8. Target Encoding</b></summary>
<p>

<details><summary> <b>8. Target Encoding (similar to Response Coding)</b></summary>
<p>
<blockquote>
  <p><b>NOTE</b>: Target-based encoding is numerization of categorical variables via target. In this method, we replace the categorical variable with just one new numerical variable and replace each category of the categorical variable with its corresponding probability of the target (if categorical) or average of the target (if numerical). The main drawbacks of this method are its dependency to the distribution of the target, and its lower predictability power compare to the binary encoding method.</p>
</blockquote>
~~~python
X_target=df_train.copy()
X_target['day']=X_target['day'].astype('object')
X_target['month']=X_target['month'].astype('object')
for col in X_target.columns:
    if (X_target[col].dtype=='object'):
        target= dict ( X_target.groupby(col)['target'].agg('sum')/X_target.groupby(col)['target'].agg('count'))
        X_target[col]=X_target[col].replace(target).values
~~~
</p>
</details>

</p>
</details>

<details><summary> <b>Target Encoding with smoothing</b></summary>
<p>

<p><a href="https://www.kaggle.com/delafields/a-thorough-guide-on-categorical-feature-encoding"><b>Credits</b></a> </p>
~~~python
def encode_target_smooth(data, target, categ_variables, smooth):
    """    
    Apply target encoding with smoothing.
    
    Parameters
    ----------
    data: pd.DataFrame
    target: str, dependent variable
    categ_variables: list of str, variables to encode
    smooth: int, number of observations to weigh global average with
    
    Returns
    --------
    encoded_dataset: pd.DataFrame
    code_map: dict, mapping to be used on validation/test datasets 
    defaul_map: dict, mapping to replace previously unseen values with
    """
    train_target = data.copy()
    code_map = dict()    # stores mapping between original and encoded values
    default_map = dict() # stores global average of each variable
    
    for col in categ_variables:
        prior = data[target].mean()
        n = data.groupby(col).size()
        mu = data.groupby(col)[target].mean()
        mu_smoothed = (n * mu + smooth + prior) / (n + smooth)
        
        train_target.loc[:, col] = train_target[col].map(mu_smoothed)
        code_map[col] = mu_smoothed
        default_map[col] = prior
    return train_target, code_map, default_map
~~~
<<<<<<< HEAD

~~~python
# additive smoothing
train_target_smooth, target_map, default_map = encode_target_smooth(df_train, 'target', hc_nom_columns, 500)
test_target_smooth = df_train.copy()
for col in hc_nom_columns:
    encoded_col = test_target_smooth[col].map(target_map[col])
    mean_encoded = pd.DataFrame({f'{col}_mean_enc': encoded_col})
    df_train = pd.concat([df_train, mean_encoded], axis=1)
    
df_train.filter(regex='nom_[5-9]_mean_enc').head()
~~~
=======
>>>>>>> b81d04277683614ee144107a15b1dc9eded6cb1b
</p>
</details>

<details><summary><b>10. Encoding [Ordinal] Features</b></summary>
<p>

~~~python
# Importing categorical options of pandas
from pandas.api.types import CategoricalDtype 

# seting the orders of our ordinal features
ord_1 = CategoricalDtype(categories=['Novice', 'Contributor','Expert', 
                                     'Master', 'Grandmaster'], ordered=True)
ord_2 = CategoricalDtype(categories=['Freezing', 'Cold', 'Warm', 'Hot',
                                     'Boiling Hot', 'Lava Hot'], ordered=True)
ord_3 = CategoricalDtype(categories=['a', 'b', 'c', 'd', 'e', 'f', 'g',
                                     'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'], ordered=True)
ord_4 = CategoricalDtype(categories=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                                     'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                                     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], ordered=True)
~~~

~~~python
# Transforming ordinal Features
df_train.ord_1 = df_train.ord_1.astype(ord_1)
df_train.ord_2 = df_train.ord_2.astype(ord_2)
df_train.ord_3 = df_train.ord_3.astype(ord_3)
df_train.ord_4 = df_train.ord_4.astype(ord_4)

# test dataset
df_test.ord_1 = df_test.ord_1.astype(ord_1)
df_test.ord_2 = df_test.ord_2.astype(ord_2)
df_test.ord_3 = df_test.ord_3.astype(ord_3)
df_test.ord_4 = df_test.ord_4.astype(ord_4)
~~~
</p>
</details>

<details><summary><b>11. Encoding</b> using <b>ASCII Code</b> (Ordinal Features)</summary>
<p>

~~~python
### Credit of this features to: 
## https://www.kaggle.com/gogo827jz/catboost-baseline-with-feature-importance

import string

# Then encode 'ord_5' using ACSII values

# Option 1: Add up the indices of two letters in string.ascii_letters
df_train['ord_5_oe_add'] = df_train['ord_5'].apply(lambda x:sum([(string.ascii_letters.find(letter)+1) for letter in x]))
df_test['ord_5_oe_add'] = df_test['ord_5'].apply(lambda x:sum([(string.ascii_letters.find(letter)+1) for letter in x]))

# Option 2: Join the indices of two letters in string.ascii_letters
df_train['ord_5_oe_join'] = df_train['ord_5'].apply(lambda x:float(''.join(str(string.ascii_letters.find(letter)+1) for letter in x)))
df_test['ord_5_oe_join'] = df_test['ord_5'].apply(lambda x:float(''.join(str(string.ascii_letters.find(letter)+1) for letter in x)))

# Option 3: Split 'ord_5' into two new columns using the indices of two letters in string.ascii_letters, separately
df_train['ord_5_oe1'] = df_train['ord_5'].apply(lambda x:(string.ascii_letters.find(x[0])+1))
df_test['ord_5_oe1'] = df_test['ord_5'].apply(lambda x:(string.ascii_letters.find(x[0])+1))

df_train['ord_5_oe2'] = df_train['ord_5'].apply(lambda x:(string.ascii_letters.find(x[1])+1))
df_test['ord_5_oe2'] = df_test['ord_5'].apply(lambda x:(string.ascii_letters.find(x[1])+1))

for col in ['ord_5_oe1', 'ord_5_oe2', 'ord_5_oe_add', 'ord_5_oe_join']:
    df_train[col]= df_train[col].astype('float64')
    df_test[col]= df_test[col].astype('float64')
~~~

~~~python
train[['ord_5', 'ord_5_oe_add', 'ord_5_oe_join', 'ord_5_oe1', 'ord_5_oe2']].head()
~~~
</p>
</details>

<details><summary> <b>12. Frequency Encoding</b></summary>
<p>
~~~python
for col in high_card_feats:
    enc_nom_1 = train[col].value_counts(normalize=True)
    train[f'freq_{col}'] = train[col].apply(lambda x: enc_nom_1[x])
~~~
~~~python
encoding  = df.groupby(col).size()
encoding /= len(df)
df[col]      = df[col].map(encoding)
~~~
</p>
</details>

<details><summary><b>13. Encoding Librariy</b></summary>
<p>
~~~python
from category_encoders.ordinal import OrdinalEncoder
from category_encoders.woe import WOEEncoder
from category_encoders.target_encoder import TargetEncoder
from category_encoders.sum_coding import SumEncoder
from category_encoders.m_estimate import MEstimateEncoder
from category_encoders.backward_difference import BackwardDifferenceEncoder
from category_encoders.leave_one_out import LeaveOneOutEncoder
from category_encoders.helmert import HelmertEncoder
from category_encoders.cat_boost import CatBoostEncoder
from category_encoders.james_stein import JamesSteinEncoder
from category_encoders.one_hot import OneHotEncoder
~~~
</p>
</details>


</p>
</details>

<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>3. Outliers</b></summary>
<p>

<p><a href="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html">1. Local Outlier Factor</a></p>

<details><summary><b>Winsorization</b></summary>
<p>
~~~python
UPPERBOUND, LOWERBOUND = np.percentile(x, [1, 99])
y = np.clip(x, UPPERBOUND, LOWERBOUND)
pd.Series(y).hist(bins=30);
~~~
</p>
</details>

</p>
</details>


<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>4. Data Preprocessing:</b></summary>
<p>
 <b>NOTE:</b> Review <b>Numeric Features</b> from how to win kaggle competition course.
<details><summary><b>1. Normalization</b></summary>
<p>
~~~python
sklearn.preprocessing.MinMaxScaler
~~~
</p>
</details>

 
<details><summary><b>2. Standardization</b></summary>
<p>
~~~python
sklearn.preprocessing.StandardScaler
~~~
</p>
</details>

 
<details><summary><b>3. Rank</b></summary>
<p>
~~~python
scipy.stats.rankdata
~~~
</p>
</details>

 
<details><summary><b>1. Logrithmic & Square Root</b></summary>
<p>
~~~python
np.log(1+x)

np.sqrt(1+x)
~~~
</p>
</details>



</p>
</details>

<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>5. Missing Values</b></summary>
<p>

<details><summary><b>Table contains # of Missing values & its percentage</b></summary>
<p>
~~~python
# Function to calculate missing values by column# Funct 
def missing_values_table(df):
    # total missing values
    mis_val = df.isnull().sum()
    
    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    
    # Make a table with results
    mis_val_table_ren_columns = pd.concat([mis_val, mis_val_percent], axis=1, keys=['Missing Values', 'Percent'])
    
    # Rename the columns
    # mis_val_table_ren_columns.rename(columns={0:'Missing Values', 1:'Percent'}, inplace=1)
    
    # Sort the table based on the percentage of missing data
    mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(by=['Percent'], ascending=0).round(1)
    
    # Print some summary information
    print('Your selected dataframe has '+str(df.shape[1])+' Columns.\nThere are '+str(mis_val_table_ren_columns.shape[0])+' Columns that have missing values.')
    
    # Reutrn the dataframe with missing information
    return mis_val_table_ren_columns
        
# Missing values statistics
missing_values = missing_values_table(app_train)
missing_values.head(20)
~~~
</p>
</details>
<details><summary><b>Finding</b> NaN values</summary>
<p>1) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/9_Logistic%20Regression/1_Titanic-Logistic%20Regression.html#Missing-Data">See the <b>Result</b>.</a></p>
<p style="margin: 0">
~~~python
df.isnull().sum()
~~~
~~~python
plt.figure(figsize=(12, 8))
sns.heatmap(train.isnull(), cmap='viridis', yticklabels=False, cbar=False)
~~~
</p>
</details>

<details><summary><b>Fill out</b> the *missing* data</summary>
<p style="margin: 0">
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors%20/1_step-by-step-diabetes-classification-knn-detailed.html#Skewness">Explanation for when to choose <b>Mean</b>, <b>Median</b>, or <b>Mode</b> to fill out the missing data.</a></p>
~~~python
data['Column Name'].fillna('Text to FIll', inplace=True)

# Replace values (here: from -1 to NaN)
data.Column_name.replace(-1, None, inplace=True)
~~~
</p>
</details>

<details><summary><b>Drop</b> the *missing* data <b>(skewness)</b></summary>
<p style="margin: 0">

~~~python
# Remove all the rows that contain any number of missing values
data.dropna(axis=0)

# Remove all the columns that contain any number of missing values
data.dropna(axis=1)

# Remove ONLY the rows that each cell in it has no value
data.dropna(how='all', axis=0)

# Drop ONLY the rows with missing values in column 3 or column 1
# Note: The default for `how` is `any`.
data.dropna(how='any', subset=['column 3', 'column 1'], axis=0)
~~~
</p>
</details>

<details><summary><b>Remove</b> missing values with <b>Threshold</b></summary>
<p style="margin: 0">
~~~python
def remove_missing_columns(train, test, threshold = 90):
    # Calculate missing stats for train and test (remember to calculate a percent!)
    train_miss = pd.DataFrame(train.isnull().sum())
    train_miss['percent'] = 100 * train_miss[0] / len(train)
    
    test_miss = pd.DataFrame(test.isnull().sum())
    test_miss['percent'] = 100 * test_miss[0] / len(test)
    
    # list of missing columns for train and test
    missing_train_columns = list(train_miss.index[train_miss['percent'] > threshold])
    missing_test_columns = list(test_miss.index[test_miss['percent'] > threshold])
    
    # Combine the two lists together
    missing_columns = list(set(missing_train_columns + missing_test_columns))
    
    # Print information
    print('There are %d columns with greater than %d%% missing values.' % (len(missing_columns), threshold))
    
    # Drop the missing columns and return
    train = train.drop(columns = missing_columns)
    test = test.drop(columns = missing_columns)
    
    return train, test
~~~
</p>
</details>

<details><summary><b>Add</b> a column containing the number of <b>NaN</b>s for a specific column</summary>
<p style="margin: 0">
~~~python
# NOTE: It treats NaN like a categorical variable, so it creates a column for it.
dummy_cols_df = pd.get_dummies(df['col 1'], dummy_na=True)
~~~
</p>
</details>

<details><summary><b>Sklearn Imputer</b> </summary>
<p style="margin: 0">
~~~python
# Make a new dataframe for polynomial features
poly_features = app_train[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH', 'TARGET']]
poly_features_test = app_test[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'DAYS_BIRTH']]

# imputer for handling missing values
from sklearn.preprocessing import Imputer
imputer = Imputer(strategy = 'median')

poly_target = poly_features['TARGET']

poly_features = poly_features.drop(columns = ['TARGET'])

# Need to impute missing values
poly_features = imputer.fit_transform(poly_features)
poly_features_test = imputer.transform(poly_features_test)
~~~
</p>
</details>

</p>
</details>

<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>6. Multi-Collinearity</b></summary>
<p>

 <details><summary><b>1. Using Variance Inflation Fator</b></summary>
<p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2012-Module%2001-Lesson%2015_Multiple%20Linear%20Regression/17.%20Screencast%20Multicollinearity%20%20VIFs.html">See the <b>video</b></a> </p>
<p>
~~~python
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor

def vif(df, target):
    df = df._get_numeric_data() #drop non-numeric cols
    cols = list(df.columns[:30])
    cols.remove(target)
    features = "+".join(cols)
    
    y, X = dmatrices(str(target)+'~'+str(features), df, return_type='dataframe')
    
    vif_df = pd.DataFrame()
    vif_df['Feature']    = X.columns
    vif_df['VIF Factor'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    
    return vif_df.round(3).sort_values(by=['VIF Factor'], ascending=False)
~~~
</p>
</details>

 <details><summary><b>2. Using Correlation matrix (pearson)</b></summary>
<p>

 <details><summary><b>2.1 Pearson Correlation</b></summary>
<p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/3_Home%20Credit%20Loans/1_Start%20Here:%20A%20Gentle%20Introduction.html#Exterior-Sources">See <b>Notebook</b></a> </p>

~~~python
plt.figure(figsize = (8, 6))

# Heatmap of correlations
sns.heatmap(data_train.corr(), cmap = plt.cm.RdYlBu_r, vmin = -0.25, annot = True, vmax = 0.6, fmt='d')
plt.title('Correlation Heatmap');
~~~

~~~python
# Calculate all correlations in dataframe
corrs = abs(train.corr())
corrs = corrs.sort_values('TARGET', ascending = False)

# Ten most positive correlations
pd.DataFrame(corrs['TARGET'].head(10))
~~~

~~~python
## Remove the colinear variables ###
# Set the threshold
threshold = 0.8

# Empty dictionary to hold correlated variables
above_threshold_vars = {}

# For each column, record the variables that are above the threshold
for col in corrs:
    above_threshold_vars[col] = list(corrs.index[corrs[col] > threshold])

# Track columns to remove and columns already examined
cols_to_remove = []
cols_seen = []
cols_to_remove_pair = []

# Iterate through columns and correlated columns
for key, value in above_threshold_vars.items():
    # Keep track of columns already examined
    cols_seen.append(key)
    for x in value:
        if x == key:
            next
        else:
            # Only want to remove one in a pair
            if x not in cols_seen:
                cols_to_remove.append(x)
                cols_to_remove_pair.append(key)
            
cols_to_remove = list(set(cols_to_remove))
print('Number of columns to remove: ', len(cols_to_remove))

# remove the variables
train_corrs_removed = train.drop(columns = cols_to_remove)
test_corrs_removed = test.drop(columns = cols_to_remove)

print('Training Corrs Removed Shape: ', train_corrs_removed.shape)
print('Testing Corrs Removed Shape: ', test_corrs_removed.shape)
~~~
</p>
</details>

 <details><summary><b>2.2 Spearman Correlation</b></summary>
<p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/5_Cargo%20Rican%20HouseHold/1_Costa%20Rican%20Household%20Poverty%20Level%20Prediction.html"><b>Notebook</b></a> </p>

<h4> 1. Compute Spearman & P-value</h4>
~~~python
import warnings
warnings.filterwarnings('ignore', category = RuntimeWarning)

feats = []
scorr = []
pvalues = []

# Iterate through each column
for c in heads:
    # Only valid for numbers
    if heads[c].dtype != 'object':
        feats.append(c)
        
        # Calculate spearman correlation
        scorr.append(spearmanr(train_heads[c], train_heads['Target']).correlation)
        pvalues.append(spearmanr(train_heads[c], train_heads['Target']).pvalue)

scorrs = pd.DataFrame({'feature': feats, 'scorr': scorr, 'pvalue': pvalues}).sort_values('scorr')

print('Most negative Spearman correlations:')
print(scorrs.head())
print('\nMost positive Spearman correlations:')
print(scorrs.dropna().tail())
~~~

<h4> 2. Calculate differences b/w spearman and pearson</h4>
~~~python
corrs = pcorrs.merge(scorrs, on = 'feature')
corrs['diff'] = corrs['pcorr'] - corrs['scorr']

corrs.sort_values('diff').head()
~~~
</p>
</details>

 <details><summary>2.2 Find <b>Correlation</b> b/w every 2 features</summary>
<p>
~~~python
correlations = train_df[features].corr().abs().unstack().sort_values(kind="quicksort").reset_index()
correlations = correlations[correlations['level_0'] != correlations['level_1']]
correlations.head(10)
~~~
</p>
</details>

</p>
</details>