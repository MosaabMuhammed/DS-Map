<h1 style='color:darkcyan;text-decoration:underline'>2. Data Problems</h1>

<div style='width:1000px;margin:auto'>

<p><a href="./1_starter/a-data-science-framework-to-achieve-99-accuracy.html#3.21-The-4-C's-of-Data-Cleaning:-Correcting,-Completing,-Creating,-and-Converting">Explanation of the 4'C of <b>Data Cleaning</b>.</a> </p>


<details><summary><span style='color:#333;font-size:25px;font-weight:bold;text-decoration:underline'>1. Related to Dataset:</span></summary>
<p>
<details><summary><b>1. Imbalanced Data set:</b></summary>
<p>
<ul>
<li><p><a href="./2_data_problems/1_Dealing%20with%20Imbalanced%20Datasets.html"><span style='color:#333333'><b>1. Imbalanced Data set:</b></span></a> </p></li>
<li><p><a href="https://imbalanced-learn.org/en/stable/over_sampling.html"><span style='color:#333333'><b>2. Another way</b> (better)</span></a> </p></li>
</ul>
</p>
</details><details><summary><b>2. Large Dataset:</b></summary><p>

<details><summary>See the data before <b>READING</b> it</summary><p><pre><code># Take a look at samples of the data
# Run it multiple times, to get the intution of each column.
!shuf -n 5 {PATH}train.csv

# Define a type for each column.
types = {'id': 'int64',
         'item_nbr': 'int32',
         'store_nbr': 'int8',
         'unit_sales': 'float32',
         'onpromotion': 'object'}

# Then read the data.
df = pd.read_csv(f'{PATH}train.csv', dtypes=types)

# Convert it to feather dataset.
df.to_feather('new_df')
</code></pre>
</p></details>

<details><summary>Using <b>Chunksize</b> in pd.read_csv()</summary><p><pre><code>df = pd.read_csv('/kaggle/input/train.csv', chunksize=1000)
</code></pre>
</p>
</details>
<details><summary>From<b>CSV</b> To <b>HDF5</b></summary>
<p>
<ul>
<li><a href="https://stackoverflow.com/questions/27203161/convert-large-csv-to-hdf5"><b>After reading csv</b></a> </li>
<li><a href="./2_data_problems/from_large_csv_to_small_HDFS.html"><b>When we can't read the csv</b></a> </li>
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

<details><summary>From<b>CSV</b> To <b>pyarray</b></summary>
<p>
<ul>
<li><a href="https://github.com/Far0n/kaggletils/blob/7819a26973a25990f479e7b7f01f40de31a64b34/kaggletils/utils/data.py#L20"><b>Credits [Github]</b></a> </li>
</ul><pre><code>def csv_to_pyarray(csv_in, file_out=None, array_name=None, enquote_elements=True, header=None, wrap=50):
    csv_filename, csv_file_extension = os.path.splitext(csv_in)
    csv_basename = ntpath.basename(csv_in).replace(csv_file_extension, '')
    file_out = file_out or csv_in.replace(csv_file_extension, '.py')
    array_name = array_name or csv_basename

    data = np.array(pd.read_csv(csv_in, header=header)).ravel()
    pyarray = '{0} = ['.format(array_name)
    length = 0
    for i, x in enumerate(data):
        length += len(str(x))
        if length &gt; wrap:
            pyarray = "{0}{1}".format(pyarray, '\n')
            length = 0
        pyarray = "{0}'{1}', ".format(pyarray, x) if enquote_elements else "{0}{1}, ".format(pyarray, x)

    pyarray = '{0}]'.format(pyarray.rstrip()[:-1])
    with open(file_out, "w") as text_file:
        text_file.write("{0}".format(pyarray))
</code></pre>
</p></details>

<details><summary>Best Type for <b>Save & Read [Feather]</b></summary><p><pre><code>## Save
# Make a directory first
os.makedirs('tmp', exist_ok=True)

### NOTE: Feather format requires the columns to be in float32 or int32, so
X_train.reset_index().astype('float32', errors='ignore').to_feather(f"{path}/X_train_encoded")



## Read 
df_raw = pd.read_feather('tmp/bulldozers-raw')

# Remove the redundant columns. [index]
for df in [df_raw, df_raw2]:
    df.drop('index', axis=1, inplace=True)
    df = reduce_mem_usage(df)
</code></pre>
</p></details>

<details><summary><b>Reduced size of dataset</b></summary><p><pre><code>from tqdm import tqdm_notebook

def reduce_mem_usage(df):
    start_mem = df.memory_usage().sum() / 1024&lt;b&gt;3
    print('~&gt; Memory usage of dataframe is {:.3f} GB'.format(start_mem))

    for col in tqdm_notebook(df.columns):
        col_type = df[col].dtype
        if col_type != object:
                c_min = df[col].min()
                c_max = df[col].max()
                if str(col_type)[:3] == 'int':
                    if c_min &gt; np.iinfo(np.int8).min and c_max &lt; np.iinfo(np.int8).max:
                        df[col] = df[col].astype(np.int8)
                    elif c_min &gt; np.iinfo(np.uint8).min and c_max &lt; np.iinfo(np.uint8).max:
                        df[col] = df[col].astype(np.uint8)
                    elif c_min &gt; np.iinfo(np.int16).min and c_max &lt; np.iinfo(np.int16).max:
                        df[col] = df[col].astype(np.int16)
                    elif c_min &gt; np.iinfo(np.uint16).min and c_max &lt; np.iinfo(np.uint16).max:
                        df[col] = df[col].astype(np.uint16)
                    elif c_min &gt; np.iinfo(np.int32).min and c_max &lt; np.iinfo(np.int32).max:
                        df[col] = df[col].astype(np.int32)
                    elif c_min &gt; np.iinfo(np.uint32).min and c_max &lt; np.iinfo(np.uint32).max:
                        df[col] = df[col].astype(np.uint32)                    
                    elif c_min &gt; np.iinfo(np.int64).min and c_max &lt; np.iinfo(np.int64).max:
                        df[col] = df[col].astype(np.int64)
                    elif c_min &gt; np.iinfo(np.uint64).min and c_max &lt; np.iinfo(np.uint64).max:
                        df[col] = df[col].astype(np.uint64)
                else:
                    if c_min &gt; np.finfo(np.float16).min and c_max &lt; np.finfo(np.float16).max:
                        df[col] = df[col].astype(np.float16)
                    elif c_min &gt; np.finfo(np.float32).min and c_max &lt; np.finfo(np.float32).max:
                        df[col] = df[col].astype(np.float32)
                    else:
                        df[col] = df[col].astype(np.float64)
        ## Comment this if you have NaN value in this column.
        # else:
            # df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024&lt;b&gt;3
    print('~&gt; Memory usage after optimization is: {:.3f} GB'.format(end_mem))
    print('~&gt; Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    print('---'*20)
    return df
</code></pre>
</p></details>

</p></details>
</p></details>

<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>2. Categorical ~> Numerical:</b></summary><p>

<ul><li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-03-Variable-Characteristics/03.2-Cardinality.html#Cardinality"><b>Cardinality, How affects Model Performance</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-03-Variable-Characteristics/03.3-Rare-Labels.html#Rare-Labels"><b>Rare Labels</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.09-Comparison-categorical-encoding-techniques.html#Comparison-of-Categorical-Variable-Encodings"><b> Comparsion b/w different Encodings</b></a> </li>

</ul>

<details><summary><b>Entity Embedding for Cat Features</b></summary><ul>
<li><a href="./2_data_problems/Entity_Embedding.html"><b>for ONLY Categorical Features</b></a> </li>
<li><a href="./2_data_problems/entity_embedding_mixed_df.html"><b>for Mixed Features</b></a> </li>
<li><a href="./2_data_problems/entity_embedding_num_converted_to_cat.html"><b>Num converted to Cat</b></a> </li>
</ul></details>

<details><summary> <b>OneHotEncoding [Nominal]</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.01-One-hot-encoding.html#One-Hot-Encoding"><b>Pandas - Sklearn - Feature-Engine</b></a> </p>

<details><summary> <b>Heuristics</b> </summary><p>
<details><summary><b>Dummy</b> Variables</summary>
<p style="margin: 0">
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/11_Decision%20Tree,%20Random%20Forest/2_Decision%20Trees%20and%20Random%20Forest%20Project-Mosaab.html#Get-Dummy-Variable">Dummy Variable in Action</a> </p>
<pre><code># Always remove one column of the dummy variables.
cat_feats = ['Categorical Column name']

final_data = pd.get_dummies(whole_dataset, columns=cat_feats, drop_first=True)
</code></pre>
<pre><code># Select all the categorical variables then get the dummy variables out of them
cat_vars = df.select_dtypes(include=['object']).copy().columns
for var in cat_vars:
    # For each cat add dummy var, drop original column
    df = pd.concat([df.drop(var, axis=1), pd.get_dummies(df[var], prefix=var, prefix_sep='_', drop_first=True, dummy_na=dummy_na)], axis=1)
</code></pre>

<h4>We can make the dummy variables sparse in order to make it fit into memory, then convert it back to form which suitable for models to handle.</h4>
<h4>Note: (.sparse.to_coo().tocsr()) is responsible to make it suitable for models to handle.</h4><pre><code>X_comb_onehot = pd.get_dummies(pd.concat([X_train, X_test]), sparse=True, columns=X_train.columns)
X_train_sparse = X_comb_onehot.loc[y_train.index].sparse.to_coo().tocsr()
X_test_sparse = X_comb_onehot.drop(index=y_train.index).sparse.to_coo().tocsr()

lr_params = dict(solver="lbfgs", C=0.2, max_iter=5000, random_state=0)
models = [LogisticRegression(**lr_params).fit(X_train_sparse[t], y_train[t])
          for t, _ in KFold(5, random_state=0).split(X_train_sparse)]
</code></pre>
</p>
</details>

<details><summary>From <b>One-Hot Encoding</b> To <b>Ordinal</b></summary><p><pre><code>ind['inst'] = np.argmax(np.array(ind[[c for c in ind if c.startswith('instl')]]), axis = 1)
</code></pre> 
</p></details>
</p></details>
</p></details>

<details><summary><b>OneHotEncoding for Top Categories</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.02-One-hot-encoding-frequent_categories.html#One-Hot-Encoding-of-Frequent-Categories">Using Manual & Feature-Engine</a> </p>
</p></details>

<details><summary> <b>Binary Encoder</b> </summary><p>
<p><a href="https://contrib.scikit-learn.org/categorical-encoding/binary.html"><b>category_encodors</b></a> </p>
</p></details>

<details><summary><b>  Label Encoder</b></summary>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.03-Integer-Encoding.html#Integer-Encoding">Using Manual & Sklearn & Feature-Engine</a> </p>

<p style="margin: 0">
<h4>1. Convert each object feature to category feature</h4><pre><code>from pandas.api.types import is_string_dtype, is_numeric_dtype, is_categorical_dtype

def train_cats(df):
    for n,c in df.items():
        if is_string_dtype(c): df[n] = c.astype('category').cat.as_ordered()


## Usage
train_cats(df_raw)

## If you have ordinal variable, you can do the following.
df_raw.col_name.cat.set_categories(['High', 'Medium', 'Low'], ordered=True, inplace=True)
</code></pre><pre><code>df[col] = df[col].factorize()[0]
</code></pre><pre><code># Create a label encoder object
le = LabelEncoder()
le_count = 0

# Iterate through the columns
for col in app_train:
    if app_train[col].dtype == 'object':
        # If 2 or fewer unique categories
        if len(list(app_train[col].unique())) &lt;= 2:
            # Train on the training data
            le.fit(app_train[col])
            # Transform both training and testing data
            app_train[col] = le.transform(app_train[col])
            app_test[col] = le.transform(app_test[col])

            # Keep track of how many columns were label encoded
            le_count += 1

print('%d columns were label encoded.' % le_count)
</code></pre>
<h4> 2. A Better Version</h4><pre><code>from tqdm import tqdm_notebook

cat_columns = [col for col in train.columns if col not in ['id', 'target', 'dataset_type']]
for col in tqdm_notebook(cat_columns):
    le = LabelEncoder()
    le.fit(list(train[col].astype(str).values) + list(test[col].astype(str).values))
    train[col] = le.transform(list(train[col].astype(str).values))
    test[col] = le.transform(list(test[col].astype(str).values))
</code></pre>
</p>
</details>

<details><summary> <b> Frequency Encoding</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.04_Count_or_frequency_encoding.html#Count-or-frequency-encoding"><b>Manual & Feature-Engine</b></a> </p>
<pre><code>for col in high_card_feats:
    enc_nom_1 = train[col].value_counts(normalize=True)
    train[f'freq_{col}'] = train[col].apply(lambda x: enc_nom_1[x])
</code></pre><pre><code>encoding  = df.groupby(col).size()
encoding /= len(df)
df[col]      = df[col].map(encoding)
</code></pre>
</p></details>

<details><summary> <b>Ordered Label Encoder</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.05-Ordered-Integer-Encoding.html#Target-guided-encodings"><b>Manual & Feature-Engine</b></a> </p>
</p></details>


<details><summary> <b> Thermometer Encoding [Ordinal]</b></summary>
<p>
<p><a href="https://www.kaggle.com/superant/oh-my-cat"><b>Credits</b></a> </p>
<h4>Note:</h4>
<p class='alert alert-info'>&nbsp;&nbsp;&nbsp;&nbsp;You can encode ordinal data using the thermometer trick. If there are 𝑁 possible values for the variable, then you map each value to a 𝑁-vector, where you put a 1 in the position that matches the value of the variable and all subsequent position.
<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;For instance: first place ↦(1,1,1), second place ↦(0,1,1), third place ↦(0,0,1).</p>

<h4>1. Build the Class.</h4><pre><code>from sklearn.base import TransformerMixin
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
            new_idxs = all_indices[values &gt; val]
            idx1.extend(new_idxs)
            idx2.extend(repeat(idx, len(new_idxs)))

        result = scipy.sparse.coo_matrix(([1] * len(idx1), (idx1, idx2)), shape=(len(X), len(possible_values)), dtype="int8")

        return result
</code></pre>

<h4>2. How to use</h4><pre><code>thermos=[]
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
</code></pre>
<pre><code># convert all coo_matrix to csr matrix in order to make the models be able to train
ohc=scipy.sparse.hstack([ohc1] + thermos).tocsr()
</code></pre>

<h4>3. Another trial: Returns dataframe</h4>
<p><a href="https://stackoverflow.com/questions/49080613/numpy-thermometer-encoding/49081131#49081131"><b>Credits</b></a> </p><pre><code>def ThemometerEncoder(df, ord_cols):
    enc_cols = []
    df_enc   = pd.DataFrame()

    for col in tqdm(ord_cols):
        enc_cols = []

        # Thermometer Encoder Step ~&gt; 5 == [1, 1, 1, 1, 1, 0, 0, 0]
        result = ((sorted(df[col].unique()) &lt; np.array(df[col])\
                               .reshape(-1, 1))\
                               .astype('int8'))

        for val in sorted(df[col].unique()):
            enc_cols.append(f'thermo_{col}_{val}')

        df_enc = pd.concat([df_enc, 
                            pd.DataFrame(result, columns=enc_cols)],
                            axis=1)
    return df_enc
</code></pre>
</p>
</details>

<details><summary> <b>Mean/Target Encoding</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.06-Mean-Encoding.html#Target-guided-encodings"><b>Manual & Feature-Engine</b></a> </p>
<hr>
<ul>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/How%20to%20win%20a%20Data%20Science%20Competition/Week%203/mean_encoding_week_3.html#Mean-encodings-without-regularization"><b>1. Mean Encoding Without Regularization</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/How%20to%20win%20a%20Data%20Science%20Competition/Week%203/mean_encoding_week_3.html#1.-KFold-scheme"><b>2. Using KFold Scheme</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/How%20to%20win%20a%20Data%20Science%20Competition/Week%203/mean_encoding_week_3.html#2.-Leave-one-out-scheme"><b>3. Leave-One-Out Scheme</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/How%20to%20win%20a%20Data%20Science%20Competition/Week%203/mean_encoding_week_3.html#3.-Smoothing"><b>4. With Smoothing</b></a> </p></li>

<li><p><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/How%20to%20win%20a%20Data%20Science%20Competition/Week%203/mean_encoding_week_3.html#4.-Expanding-mean-scheme"><b>5. Expanding Mean Scheme</b></a> </p></p></li>
</ul>

<details><summary> <b>1 Target Encoding (similar to Response Coding)</b></summary>
<p>
<blockquote>
  <p><b>NOTE</b>: Target-based encoding is numerization of categorical variables via target. In this method, we replace the categorical variable with just one new numerical variable and replace each category of the categorical variable with its corresponding probability of the target (if categorical) or average of the target (if numerical). The main drawbacks of this method are its dependency to the distribution of the target, and its lower predictability power compare to the binary encoding method.</p>
</blockquote><pre><code>X_target=df_train.copy()
X_target['day']=X_target['day'].astype('object')
X_target['month']=X_target['month'].astype('object')
for col in X_target.columns:
    if (X_target[col].dtype=='object'):
        target= dict ( X_target.groupby(col)['target'].agg('sum')/X_target.groupby(col)['target'].agg('count'))
        X_target[col]=X_target[col].replace(target).values
</code></pre>

<h4>2. Another way of doing so</h4><pre><code>'''
     Differently to `.target.mean()` function `transform` 
   will return a dataframe with an index like in `all_data`.
   Basically this single line of code is equivalent to the first two lines from of Method 1.
'''
all_data['item_target_enc'] = all_data.groupby('item_id')['target'].transform('mean')
</code></pre>
</p></details>

<details><summary> <b>2 Target Encoding with smoothing</b></summary>
<p>

<p><a href="https://www.kaggle.com/delafields/a-thorough-guide-on-categorical-feature-encoding"><b>Credits</b></a> </p><pre><code>def encode_target_smooth(data, target, categ_variables, smooth):
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
</code></pre>
<pre><code># additive smoothing
train_target_smooth, target_map, default_map = encode_target_smooth(df_train, 'target', hc_nom_columns, 500)
test_target_smooth = df_train.copy()
for col in hc_nom_columns:
    encoded_col = test_target_smooth[col].map(target_map[col])
    mean_encoded = pd.DataFrame({f'{col}_mean_enc': encoded_col})
    df_train = pd.concat([df_train, mean_encoded], axis=1)

df_train.filter(regex='nom_[5-9]_mean_enc').head()
</code></pre>
</p>
</details>

</p></details>

<details><summary> <b>Probability Ratio Encoding</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.07-Probability-Ratio-Encoding.html#Target-guided-encodings"><b>Manual & Feature-Engine</b></a> </p>
</p></details>

<details><summary> <b>Weight of Evidence Ratio Encoding</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.08-Weight-of-Evidence.html#Weight--of-evidence"><b>Manual & Feature-Engine</b></a> </p>
</p></details>

<details><summary> <b>Entity Embedding</b> </summary><p>
<p><a href="./2_data_problems/Embedding for Cat.html"><b>Notebook using Keras</b></a> </p>
</p></details>

<br>

<details><summary> <b>Rare Labels Encoding</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-06-Categorical-Encoding/06.10-Engineering-Rare-Categories.html#Engineering-Rare-Categories"><b>Manual & Feature-Engine</b></a> </p>
</p></details>



<details><summary> <b>Feature Hashing</b></summary>
<p>
<p><a href="https://contrib.scikit-learn.org/categorical-encoding/hashing.html#hashing"><b>Manual & Feature-Engine</b></a> </p>
</p>
<h4> Using FeatureHasher (Multiple Columns)</h4><pre><code>from sklearn.feature_extraction import FeatureHasher

X_train_hash=X.copy()
for c in X.columns:
    X_train_hash[c]=X[c].astype('str')

hashing=FeatureHasher(input_type='string')
train=hashing.transform(X_train_hash.values)

print('train data set has got {} rows and {} columns'.format(train.shape[0],train.shape[1]))
&lt;h4&gt;&lt;h4&gt;# Result &lt;h4&gt;&lt;h4&gt;&lt;h4&gt;
train data set has got 300000 rows and 1048576 columns
</code></pre>

<h4> Using Hash Function (One Column)</h4><pre><code>for col in high_card_feats:
    enc_nom_1 = train[col].value_counts(normalize=True)
    train[f'freq_{col}'] = train[col].apply(lambda x: enc_nom_1[x])
</code></pre>
</p>
</details>


<details><summary> <b>Encoding Cyclic Features (Day, Month, ...)</b></summary>
<p><pre><code>X_train_cyclic=X.copy()
columns=['day','month']
for col in columns:
    X_train_cyclic[col+'_sin']=np.sin((2*np.pi*X_train_cyclic[col])/max(X_train_cyclic[col]))
    X_train_cyclic[col+'_cos']=np.cos((2*np.pi*X_train_cyclic[col])/max(X_train_cyclic[col]))
X_train_cyclic=X_train_cyclic.drop(columns,axis=1)
</code></pre>
</p>
</details>


<details><summary><b>Encoding</b> using <b>ASCII Code</b> (Ordinal Features)</summary>
<p>
<pre><code>### Credit of this features to: 
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
</code></pre>
<pre><code>train[['ord_5', 'ord_5_oe_add', 'ord_5_oe_join', 'ord_5_oe1', 'ord_5_oe2']].head()
</code></pre>
</p></details>

<details><summary><b>Combination of cat features</b></summary><p><pre><code>import itertools

def create_combinations(df, cat_cols):
    combi = list(itertools.combinations(cat_cols, 2))
    for c1, c2 in combi:
        df.loc[:, c1 + "_" + c2] = df[c1].astype(str) + "_" + df[c2].astype(str)
    return df
</code></pre>
</p></details>


<details><summary><b>Encoding Librariy</b></summary>
<p><pre><code>from category_encoders.ordinal import OrdinalEncoder
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
</code></pre>
</p>
</details>


</p>
</details>

<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>3. Outliers</b></summary>
<p>
<p><img src="imgs/20191106-124543.png" alt="" /></p>
<p><a href="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html"><b>1. Local Outlier Factor</b></a></p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-03-Variable-Characteristics/03.6-Outliers.html#Outliers" style='font-weight:bold'>2. Detecting Outliers for [Normal, Skewed, Extremely Skewed]</a></p>

<details><summary><b>Trimming</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-09-Outlier-Engineering/09.01-Outlier-Trimming.html#Outlier-Engineering" style='font-weight:bold'>Trimming Outliers</a></p>
</p></details>

<details><summary><b>Clipping</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-09-Outlier-Engineering/09.02-Capping-IQR-proximity-rule.html#Outlier-Engineering" style='font-weight:bold'>Capping IQR Proximity Rule</a></p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-03-Variable-Characteristics/03.6-Outliers.html#Outliers" style='font-weight:bold'>Capping Gaussian Approximiation</a></p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-09-Outlier-Engineering/09.04-Capping-Quantiles.html#Outlier-Engineering" style='font-weight:bold'>Capping Quantiles</a></p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-09-Outlier-Engineering/09.05-Capping-Arbitrary.html#Outlier-Engineering" style='font-weight:bold'>Capping Aribrary</a></p>
</p></details>


<details><summary><b>Winsorization</b></summary><p><pre><code>UPPERBOUND, LOWERBOUND = np.percentile(x, [1, 99])
y = np.clip(x, UPPERBOUND, LOWERBOUND)
pd.Series(y).hist(bins=30);
</code></pre>
</p></details>

<details><summary><b>RANSAC Algorithm</b></summary><p><pre><code>import numpy as np
from matplotlib import pyplot as plt

from sklearn import linear_model, datasets


n_samples = 1000
n_outliers = 50


X, y, coef = datasets.make_regression(n_samples=n_samples, n_features=1,
                                      n_informative=1, noise=10,
                                      coef=True, random_state=0)

# Add outlier data
np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)

# Fit line using all data
lr = linear_model.LinearRegression()
lr.fit(X, y)

# Robustly fit linear model with RANSAC algorithm
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)

# Predict data of estimated models
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)

# Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)

lw = 2
plt.scatter(X[inlier_mask], y[inlier_mask], color='yellowgreen', marker='.',
            label='Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask], color='gold', marker='.',
            label='Outliers')
plt.plot(line_X, line_y, color='navy', linewidth=lw, label='Linear regressor')
plt.plot(line_X, line_y_ransac, color='cornflowerblue', linewidth=lw,
         label='RANSAC regressor')
plt.legend(loc='lower right')
plt.xlabel("Input")
plt.ylabel("Response")
plt.show()
</code></pre>
</p></details>

<details><summary><b>z-score</b></summary><p>
The <b>z-score</b> of value x is a measure of how many standard deviations x is away from the mean.<br> <b>z-score</b> is a normalization technique used in the preprocessing of features. It helps the ML model to learn better from data.<br><br> High <b>z-score</b> values in a sample indicate that the sample value is far away from the mean and could be an outlier. Here's how we calculate zscore mathematically: z-score = (x - mean(x)) / std(x) <br><br>

Most used in Time-Series problem.
<pre><code>df['mean']       = df['#Passengers'].mean()
df['std']        = df['#Passengers'].std()
df['zscore']     = (df['#Passengers'] - df['mean']) / df['std']
df['zscore_abs'] = abs(df['zscore'])
df.sort_values(by='zscore_abs', ascending=False).head()
</code></pre>
<pre><code># Select by high and low z-scores.
anamlous_df_high = df.sort_values(by='zscore', ascending=False).head(10)
anamlous_df_high['Date'] = pd.to_datetime(anamlous_df_high['Date'])

anamlous_df_low  = df.sort_values(by='zscore', ascending=True).head(10)
anamlous_df_low['Date'] = pd.to_datetime(anamlous_df_low['Date'])
</code></pre>
<pre><code># Plot it.
plt.figure(figsize=(15, 8))
plt.grid=True
plt.title('Top 10 high Traffic passenger count')
ax = sns.lineplot(x='Date', y='#Passengers', data=df)
ax = sns.scatterplot(x='Date', y='#Passengers', data=anamlous_df_high, size='#Passengers')
ax = sns.lineplot(x='Date', y='mean', data=df)
ax.text(pd.to_datetime('1950'), 290, 'Mean Line', ha='left', size='large', color='Blue')
ax = sns.scatterplot(x='Date', y='#Passengers', data=anamlous_df_low, size='#Passengers')
ax.grid()
</code></pre>
<img src="./imgs/zscore.png">
</p></details>
</p></details>

<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>4. Data Scaling:</b></summary><p>



 <details><summary><b>How Scaling Affects Models Performance</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-03-Variable-Characteristics/03.7-Variable-magnitude.html#Variable-magnitude" style='font-weight:bold'>Check this</a> </p>
<p><img src="imgs/20191030-134414.png" alt="" /></p>
</p></details><br>

<details><summary><b>1. Normalization</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-10-Feature-Scaling/10.03-MinMaxScaling.html#Scaling-to-Minimum-and-Maximum-values---MinMaxScaling" style='font-weight:bold'>Pandas - Sklearn</a> </p>
</p>
</details>


<details><summary><b>2. Standardization</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-10-Feature-Scaling/10.01-Standardisation.html#Feature-Scaling" style='font-weight:bold'>Check this</a> </p>
</p></details>

<details><summary><b>3. Mean Normalization</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-10-Feature-Scaling/10.02-Mean-normalisation.html#Mean-Normalisation" style='font-weight:bold'>Pandas - Sklearn</a> </p>
</p></details>


<details><summary><b>4. Max Absolute Scaling</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-10-Feature-Scaling/10.04-Maximum-Absolute-Scaling.html#Scaling-to-maximum-value---MaxAbsScaling" style='font-weight:bold'>Sklearn</a> </p>
</p></details>


<details><summary><b>5. Robust Scaler</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-10-Feature-Scaling/10.05-Robust-Scaling.html#Scaling-to-quantiles-and-median---RobustScaling" style='font-weight:bold'>Sklearn</a> </p>
</p></details>

<details><summary><b>6. Scaling to vector unit length / unit norm</b></summary><p>
Read <b>mastering ml book</b> page: 12<br><br>
Scikit-learn recommends this scaling procedures for text classification or clustering. For example, they quote the dot product of two l2-normalized TF-IDF vectors is the cosine similarity of the vectors and is the base similarity metric for the Vector Space Model commonly used by the Information Retrieval community.

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-10-Feature-Scaling/10.06-Scaling-to-unit-length.html#Scaling-to-vector-unit--length-/-unit-norm" style='font-weight:bold'>Sklearn</a> </p>
</p></details>

<details><summary><b>7. Whitening</b></summary><p>
<b>NOTE:</b> It is provided in PCA in sklearn<br>
Read <b>mastering ml book</b> page: 15<br><br>
<pre><code>import numpy as np

def zero_center(X):
    return X - np.mean(X, axis=0)

def whiten(X, correct=True):
    Xc = zero_center(X)
    _, L, V = np.linalg.svd(Xc)
    W = np.dot(V.T, np.diag(1.0 / L))
    return np.dot(Xc, W) * np.sqrt(X.shape[0]) if correct else 1.0
</code></pre>
</p></details>


</p>
</details>

<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>5. Missing Values</b></summary><p>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-03-Variable-Characteristics/03.1-Missing-Data.html#Missing-Data-Mechanisms"><b style='color:#333'>Missing Data Mechanisms</b></a> </p></li>



<details><summary><b>Missing Data Imputing</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/24.%20Overview%20of%20missing%20value%20imputation%20methods.html"><b style='color:#333'>Filling Missing Data Comparsion</b></a> </p></li>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/25.%20Conclusion%20when%20to%20use%20each%20missing%20data%20imputation%20method.html"><b style='color:#333'>Guidelines</b></a> </p></li>

<details><summary><b>Categorical Variables</b></summary><p>

<details><summary><b>1. Complete Case Analysis [CCA]</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.01-Complete-Case-Analysis.html#Complete-Case-Analysis"><b style='color:#333'>Manual</b></a> </p></li>
</p></details>

<details><summary><b>2. Arbitrary Value Imputation</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.03-Arbitrary-Value-Imputation.html#Arbitrary-value-imputation"><b style='color:#333'>Manual</b> ['Missing']</a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.12-Missing-Category-Imputation-Sklearn.html#Missing-Category-imputation-with-Scikit-learn:-SimpleImputer"><b style='color:#333'>Sklearn</b> ['Missing']</a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.20-Missing-Category-Imputation-Feature-Engine.html#Missing-Category-Imputation-==%3E-Feature-Engine"><b style='color:#333'>Feature-Engine</b> ['Missing']</a> </p></li>
</p></details>



<details><summary><b>3. Frequent category imputation | Mode imputation</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.05-Frequent-Category-Imputation.html#Frequent-category-imputation-|-Mode-imputation"><b style='color:#333'>Manual</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.11-Frequent-Category-Imputation-Sklearn.html#Frequent-category-imputation-with-Scikit-learn-==%3E-SimpleImputer"><b style='color:#333'>Sklearn</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.19-Frequent-Category-Imputation-Feature-Engine.html#Frequent-Category-Imputation-==%3E-Feature-Engine"><b style='color:#333'>Feature-Engine</b></a> </p></li>
</p></details>

<details><summary><b>4. Random sample imputation</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.07-Random-Sample-Imputation.html#Random-Sampling-for-Categorical-Variables"><b style='color:#333'>Manual</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.20-Missing-Category-Imputation-Feature-Engine.html#Missing-Category-Imputation-==%3E-Feature-Engine"><b style='color:#333'>Feature-Engine</b></a> </p></li>
</p></details>

<details><summary><b>5. Missing Binary Indicator</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.07-Random-Sample-Imputation.html#Random-Sampling-for-Categorical-Variables"><b style='color:#333'>Manual</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.13-MissingIndicator-Sklearn.html#Adding-a-Missing-Indicator-variable-with-Scikit-learn-==%3E-MissingIndicator"><b style='color:#333'>Sklearn</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.22-Missing-Indicator-Feature-Engine.html#Missing-Indicator-==%3E-Feature-Engine"><b style='color:#333'>Feature-Engine</b></a> </p></li>
</p></details>

<details><summary><b>6. Automatic Imputing [GridSearch]</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.14-Automatic-Imputation-Method-Detection-Sklearn.html#Automatic-selection-of-best-imputation-technique-with-Sklearn"><b style='color:#333'>Sklearn</b></a> </p></li>

</p></details>

</p></details>

<details><summary><b>Numerical Variables</b></summary><p>

<details><summary><b>1. Complete Case Analysis [CCA]</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.01-Complete-Case-Analysis.html#Complete-Case-Analysis"><b style='color:#333'>1. Manual</b></a> </p></li>
</p></details>

<details><summary><b>2. Arbitrary Value Imputation</b></summary><p>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.06-Missing-Category-Imputation.html#Arbitrary-value-imputation-for-categorical-variables"><b style='color:#333'>1. Manual</b> [999/-1]</a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.10-Arbitrary-Value-Imputation-Sklearn.html#Arbitrary-value-imputation-with-Scikit-learn-==%3E-SimpleImputer"><b style='color:#333'>2. Sklearn</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.17-Arbitrary-Value-Imputation-Feature-Engine.html#Arbitrary-Imputation-==%3E-Feature-Engine"><b style='color:#333'>Feature-Engine</b></a> </p></li>

</p></details>

<details><summary><b>3. Mean / Median Imputation</b></summary><p>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.02-Mean-Median-Imputation.html#Mean-/-Median-imputation"><b style='color:#333'>1. Manual</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.09-Mean-Median-Imputation-Sklearn.html#Mean-/-median-imputation-with-Scikit-learn-==%3E-SimpleImputer"><b style='color:#333'>2. Sklearn</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.16-Mean-Median-Imputation-Feature-Engine.html#What-is-Feature-Engine"><b style='color:#333'>Featuer-Engine</b></a> </p></li>

</p></details>

<details><summary><b>4. End of Distribution Imputation</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.04-End-Distribution-Imputation.html#End-of-distribution-imputation"><b style='color:#333'>Manual</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.18-End-Tail-Imputation-Feature-Engine.html#End-of-distribution-Imputation-==%3E-Feature-Engine"><b style='color:#333'>Feature-Engine</b></a> </p></li>
</p></details>

<details><summary><b>5. Frequent category imputation | Mode imputation</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.05-Frequent-Category-Imputation.html#Frequent-category-imputation-|-Mode-imputation"><b style='color:#333'>Manual</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.11-Frequent-Category-Imputation-Sklearn.html#Frequent-category-imputation-with-Scikit-learn-==%3E-SimpleImputer"><b style='color:#333'>Sklearn</b></a> </p></li>
</p></details>

<details><summary><b>6. Random sample imputation</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.07-Random-Sample-Imputation.html#Random-sample-imputation"><b style='color:#333'></b>Manual</a></p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.20-Missing-Category-Imputation-Feature-Engine.html#Missing-Category-Imputation-==%3E-Feature-Engine"><b style='color:#333'>Feature-Engine</b></a> </p></li>
</p></details>

<details><summary><b>7. Missing Binary Indicator</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.07-Random-Sample-Imputation.html#Random-Sampling-for-Categorical-Variables"><b style='color:#333'>Manual</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.13-MissingIndicator-Sklearn.html#Adding-a-Missing-Indicator-variable-with-Scikit-learn-==%3E-MissingIndicator"><b style='color:#333'>Sklearn</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.22-Missing-Indicator-Feature-Engine.html#Missing-Indicator-==%3E-Feature-Engine"><b style='color:#333'>Feature-Engine</b></a> </p></li>
</p></details>

<details><summary><b>8. Automatic Imputing [GridSearch]</b></summary><p>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-04-Missing-Data-Imputation/04.14-Automatic-Imputation-Method-Detection-Sklearn.html#Automatic-selection-of-best-imputation-technique-with-Sklearn"><b style='color:#333'>Sklearn</b></a> </p></li>
</p></details>

<details><summary><b>9. KNN Imputer</b></summary><p><pre><code>from sklearn import impute

knn_imputer = impute.KNNImputer(n_neighbors=2)
knn_imputer.fit_transfrom(X)
</code></pre>
</p></details>


</p></details><br>

<details><summary><b>Misc Techniques</b></summary><p>

<details><summary><b>Table contains # of Missing values & its percentage</b></summary>
<p><pre><code># Function to calculate missing values by column# Funct 
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
</code></pre>

<h4>Simple way</h4><pre><code># alternatively, we can use the mean method after isnull
# to visualise the percentage of
# missing values for each variable

data.isnull().mean()
</code></pre>
</p>
</details>
<details><summary><b>Finding</b> NaN values</summary>
<p>1) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/9_Logistic%20Regression/1_Titanic-Logistic%20Regression.html#Missing-Data">See the <b>Result</b>.</a></p>
<p style="margin: 0"><pre><code>df.isnull().sum()
</code></pre><pre><code>plt.figure(figsize=(12, 8))
sns.heatmap(train.isnull(), cmap='viridis', yticklabels=False, cbar=False)
</code></pre>
</p>
</details>

<details><summary><b>Fill out</b> the *missing* data</summary>
<p style="margin: 0">
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors%20/1_step-by-step-diabetes-classification-knn-detailed.html#Skewness">Explanation for when to choose <b>Mean</b>, <b>Median</b>, or <b>Mode</b> to fill out the missing data.</a></p><pre><code>data['Column Name'].fillna('Text to FIll', inplace=True)

# Replace values (here: from -1 to NaN)
data.Column_name.replace(-1, None, inplace=True)
</code></pre>
</p>
</details>

<details><summary><b>Drop</b> the missing data <b>(skewness)</b></summary>
<p style="margin: 0">
<pre><code># Remove all the rows that contain any number of missing values
data.dropna(axis=0)

# Remove all the columns that contain any number of missing values
data.dropna(axis=1)

# Remove ONLY the rows that each cell in it has no value
data.dropna(how='all', axis=0)

# Drop ONLY the rows with missing values in column 3 or column 1
# Note: The default for `how` is `any`.
data.dropna(how='any', subset=['column 3', 'column 1'], axis=0)
</code></pre>
</p>
</details>

<details><summary><b>Remove</b> missing values with <b>Threshold</b></summary>
<p style="margin: 0"><pre><code>def remove_missing_columns(train, test, threshold = 90):
    # Calculate missing stats for train and test (remember to calculate a percent!)
    train_miss = pd.DataFrame(train.isnull().sum())
    train_miss['percent'] = 100 * train_miss[0] / len(train)

    test_miss = pd.DataFrame(test.isnull().sum())
    test_miss['percent'] = 100 * test_miss[0] / len(test)

    # list of missing columns for train and test
    missing_train_columns = list(train_miss.index[train_miss['percent'] &gt; threshold])
    missing_test_columns = list(test_miss.index[test_miss['percent'] &gt; threshold])

    # Combine the two lists together
    missing_columns = list(set(missing_train_columns + missing_test_columns))

    # Print information
    print('There are %d columns with greater than %d%% missing values.' % (len(missing_columns), threshold))

    # Drop the missing columns and return
    train = train.drop(columns = missing_columns)
    test = test.drop(columns = missing_columns)

    return train, test
</code></pre>
</p>
</details>

<details><summary><b>Add</b> a column containing the number of <b>NaN</b>s for a specific column</summary>
<p style="margin: 0"><pre><code># NOTE: It treats NaN like a categorical variable, so it creates a column for it.
dummy_cols_df = pd.get_dummies(df['col 1'], dummy_na=True)
</code></pre>
</p>
</details>

<details><summary><b>Sklearn Imputer</b> </summary>
<p style="margin: 0"><pre><code># Make a new dataframe for polynomial features
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
</code></pre>
</p>
</details>
</p></details>

</p>
</details>

</p></details>




<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>6. Multi-Collinearity</b></summary>
<p>

 <details><summary><b>1. Using Variance Inflation Fator</b></summary>
<p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Data%20Scientist%20Nanodegree%20nd025%20v1.0.0/Part%2012-Module%2001-Lesson%2015_Multiple%20Linear%20Regression/17.%20Screencast%20Multicollinearity%20%20VIFs.html">See the <b>video</b></a> </p>
<p><pre><code>from patsy import dmatrices
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
</code></pre>
</p>
</details>

 <details><summary><b>2. Using Correlation matrix (pearson)</b></summary>
<p>

 <details><summary><b>2.1 Pearson Correlation</b></summary>
<p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/3_Home%20Credit%20Loans/1_Start%20Here:%20A%20Gentle%20Introduction.html#Exterior-Sources">See <b>Notebook</b></a> </p>
<pre><code>plt.figure(figsize = (8, 6))

# Heatmap of correlations
sns.heatmap(data_train.corr(), cmap = plt.cm.RdYlBu_r, vmin = -0.25, annot = True, vmax = 0.6, fmt='d')
plt.title('Correlation Heatmap');
</code></pre>
<pre><code># Calculate all correlations in dataframe
corrs = abs(train.corr())
corrs = corrs.sort_values('TARGET', ascending = False)

# Ten most positive correlations
pd.DataFrame(corrs['TARGET'].head(10))
</code></pre>
<pre><code>## Remove the colinear variables ###
# Set the threshold
threshold = 0.8

# Empty dictionary to hold correlated variables
above_threshold_vars = {}

# For each column, record the variables that are above the threshold
for col in corrs:
    above_threshold_vars[col] = list(corrs.index[corrs[col] &gt; threshold])

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
</code></pre>
</p>
</details>

<details><summary><b>2.2 Spearman Correlation</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/5_Cargo%20Rican%20HouseHold/1_Costa%20Rican%20Household%20Poverty%20Level%20Prediction.html"><b>Notebook</b></a> </p>

<h4> 1. Compute Spearman & P-value</h4><pre><code>import warnings
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
</code></pre>

<h4> 2. Calculate differences b/w spearman and pearson</h4><pre><code>corrs = pcorrs.merge(scorrs, on = 'feature')
corrs['diff'] = corrs['pcorr'] - corrs['scorr']

corrs.sort_values('diff').head()
</code></pre>
</p>
</details>

 <details><summary>2.2 Find <b>Correlation</b> b/w every 2 features</summary>
<p><pre><code>correlations = train_df[features].corr().abs().unstack().sort_values(kind="quicksort").reset_index()
correlations = correlations[correlations['level_0'] != correlations['level_1']]
correlations.head(10)
</code></pre>
</p></details>
</p></details>

<details><summary>3. Correlation b/w <b>Nominal</b> features using [<b>Cramer’s V</b>]</summary><p>
Cramer’s V is a measure of association between two nominal variables, giving a value between 0 and +1 (inclusive). It is based on Pearson's chi-squared statistic and was published by Harald Cramér in 1946.<br>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/Misc/1_Cat%20Features%20Encoding%20Challenge.html"><b>Credits</b></a> </p>
<pre><code>from scipy.stats import chi2_contingency, kruskal, ks_2samp

def coef_vcramer(contingency_df):
    chi2 = chi2_contingency(contingency_df)[0]
    n = contingency_df.sum().sum()
    r, k = contingency_df.shape
    return np.sqrt(chi2 / (n * min((r-1), (k-1))))
</code></pre>
<pre><code>def fit_describe_infos(train, test, __featToExcl = [], target_for_vcramer = None):
    '''Describe data and difference between train and test datasets.'''

    stats = []
    __featToAnalyze = [v for v in list(train.columns) if v not in __featToExcl]

    for col in tqdm_notebook(__featToAnalyze):

        dtrain = dict(train[col].value_counts())
        dtest = dict(test[col].value_counts())

        set_train_not_in_test = set(dtest.keys()) - set(dtrain.keys())
        set_test_not_in_train = set(dtrain.keys()) - set(dtest.keys())

        dict_train_not_in_test = {key:value for key, value in dtest.items() if key in set_train_not_in_test}
        dict_test_not_in_train = {key:value for key, value in dtrain.items() if key in set_test_not_in_train}

        nb_moda_test, nb_var_test = len(dtest), pd.Series(dtest).sum()
        nb_moda_abs, nb_var_abs = len(dict_train_not_in_test), pd.Series(dict_train_not_in_test).sum()
        nb_moda_train, nb_var_train = len(dtrain), pd.Series(dtrain).sum()
        nb_moda_abs_2, nb_var_abs_2 = len(dict_test_not_in_train), pd.Series(dict_test_not_in_train).sum()

        if not target_for_vcramer is None:
            vc = coef_vcramer(pd.crosstab(train[target_for_vcramer], train[col].fillna(-1)))       
        else:
            vc = 0

        stats.append((col, round(vc, 3), train[col].nunique()
            , str(nb_moda_abs) + '   (' + str(round(100 * nb_moda_abs / nb_moda_test, 1))+'%)'
            , str(nb_moda_abs_2) +'   (' + str(round(100 * nb_moda_abs_2 / nb_moda_train, 1))+'%)'
            , str(train[col].isnull().sum()) +'   (' + str(round(100 * train[col].isnull().sum() / train.shape[0], 1))+'%)'
            , str(test[col].isnull().sum()) +'   (' + str(round(100 * test[col].isnull().sum() / test.shape[0], 1))+'%)'
            , str(round(100 * train[col].value_counts(normalize = True, dropna = False).values[0], 1))
            , train[col].dtype))

    df_stats = pd.DataFrame(stats, columns=['Feature', "Target Cramer's V"
        , 'Unique values (train)', "Unique values in test not in train (and %)"
        , "Unique values in train not in test (and %)"
        , 'NaN in train (and %)', 'NaN in test (and %)', '% in the biggest cat. (train)'
        , 'dtype'])

    if target_for_vcramer is None:
        df_stats.drop("Target Cramer's V", axis=1, inplace=True)

    return df_stats, dict_train_not_in_test, dict_test_not_in_train
</code></pre>

<h4>3. How to use</h4><pre><code>dfi, _, _ = fit_describe_infos(train, test, __featToExcl=['target'], target_for_vcramer='target')
dfi
</code></pre>

<h4>4. Get Correlation b/w every 2 features</h4><pre><code>print("Biggest Cramer'V in train\n-------------------------")
lfeat = [v for v in list(train.columns) if v not in ["target"]]
done=[]
for v1 in lfeat:
    done.append(v1)
    for v2 in [v for v in lfeat if v not in done]:
        c = coef_vcramer(pd.crosstab(train[v1], train[v2]))
        if c &gt; 0.08:
            print("{}, {}, {:.5f}".format(v1, v2, c))
</code></pre>
</p></details>
</p></details>

<hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>7. Linear Model Assumptions</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-03-Variable-Characteristics/03.4-Linear-Model-Assumptions.html#Linear-Model-Assumptions"><b>Notebook [MUST READ]</b></a> </p>
<ul>
<li>There is a <b>linear</b> relationship between X and the outcome Y</li>
<li>The independent variables X are <b>normally</b> distributed</li>
<li>There is no or little <b>co-linearity</b> among the independent variables</li>
<li><b>Homoscedasticity</b> (homogeneity of variance)</li>
</ul>
<hr>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-07-Variable-Transformation/07.01-Gaussian-transformation.html#Gaussian-Transformation"><b>Gaussian Transformation [Numpy]</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-07-Variable-Transformation/07.01-Gaussian-transformation.html#Gaussian-Transformation"><b>Gaussian Transformation [Sklearn]</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-07-Variable-Transformation/07.03-Gaussian-transformation-feature-engine.html#Gaussian-Transformation-with-Feature-Engine"><b>Gaussian Transformation [Feature-Engine]</b></a> </p>
</p></details>
<hr>
<details><summary style='font-size:23px;text-decoration:underline'><b>8. Mixed Variables</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-11-Mixed-Variables/11.01-Engineering-mixed-variables.html#Engineering-mixed-variables"><b>The observations of the variable contain either numbers or strings</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-11-Mixed-Variables/11.01-Engineering-mixed-variables.html#Example-1:-the-observations-of-the-variable-contain-numbers-and-strings"><b>The observations of the variable contain numbers and strings</b></a> </p>

</p></details>
<hr>
<details><summary style='font-size:23px;text-decoration:underline'><b>9. Cold-Start Problem</b></summary><p>
<h4>1. Check the cold-start problem</h4><pre><code>result = pd.DataFrame(columns=['col', 'Train', 'Test'])

for col in X_train:
    trY_teN = set(X_train[col].unique()) - set(X_test[col].unique())
    trN_teY = set(X_test[col].unique()) - set(X_train[col].unique())
    result = result.append({'col': col, 'Train': len(trY_teN), 'Test': len(trN_teY)}, ignore_index=True)
</code></pre>
</p></details><hr>

<details><summary style='font-size:23px;text-decoration:underline'><b>10. Underfitting & Overfitting</b></summary><p>
<h4>1. Fix Overfitting</h4>
<ul>
<li>To simplify the model <br>&nbsp;&nbsp;&nbsp;&nbsp;by selecting one with fewer parameters (e.g., a linear model rather than a high-degree polynomial
model), <br>&nbsp;&nbsp;&nbsp;&nbsp;by reducing the number of attributes in the training data or<br>&nbsp;&nbsp;&nbsp;&nbsp;by constraining the model (Adding Regularization)<br> &nbsp;&nbsp;&nbsp;&nbsp; In DL, reduce the number of layers/neurons or add a drop-out layer.</li>
<li>To gather more training data.</li>
<li>To reduce the noise in the training data (e.g., fix data errors
and remove outliers)</li>
</ul>

<h4>2. Fix Underfitting</h4>
<ul>
<li>Selecting a more powerful model, with more parameters</li>
<li>Feeding better features to the learning algorithm (feature engineering)</li>
<li>Reducing the constraints on the model (e.g., reducing the regularization hyper‐
parameter)</li>
</ul><hr>

<h4>Learning Curves to check Overfitting or Underfitting</h4><pre><code>from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def plot_learning_curves(model, X, y):
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2)
    train_errors, valid_errors = [], []

    for m in range(1, len(X_train)):
        model.fit(X_train[:m], y_train[:m])
        y_train_preds = model.predict(X_train[:m])
        y_valid_preds = model.predict(X_valid)

        train_errors.append(mean_squared_error(y_train[:m], y_train_preds))
        valid_errors.append(mean_squared_error(y_valid, y_valid_preds))

    plt.figure(figsize=(8, 6))
    plt.plot(np.sqrt(train_errors), "r-+", lw=2, label="train")
    plt.plot(np.sqrt(valid_errors), "b-", lw=3, label="valid")
    plt.xlabel('Training Size', size=18)
    plt.ylabel('RMSE', size=18)
    plt.legend(); plt.grid()
    return plt
</code></pre>

<h4>Using sklearn</h4><pre><code># Get data.
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=500,
                           n_classes=5,
                           n_features=50,
                           n_informative=10,
                           n_redundant=5,
                           n_clusters_per_class=3,
                           random_state=1000)
ss = StandardScaler()
X  = ss.fit_transform(X)
</code></pre>
<pre><code># choose model and run learning curves.
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve, StratifiedKFold

lr          = LogisticRegression(solver="lbfgs", random_state=1000)
splits      = StratifiedKFold(n_splits=10, shuffle=True, random_state=1000)
train_sizes = np.linspace(.1, 1.0, 20)

lr_train_sizes, lr_train_scores, lr_test_scores = \
    learning_curve(lr, X, y, cv=splits, train_sizes=train_sizes,
                   n_jobs=-1, scoring='accuracy',
                   shuffle=True, random_state=1000)
</code></pre>
<pre><code># Plot the scores
sns.set()

fig, ax = plt.subplots(figsize=(15, 8))

ax.plot(lr_train_sizes, np.mean(lr_train_scores, axis=1), "o-", label="Training")
ax.plot(lr_train_sizes, np.mean(lr_test_scores, axis=1), "o-", label="Test")
ax.set_xlabel('Training set size', fontsize=18)
ax.set_ylabel('Average accuracy', fontsize=18)
ax.set_xticks(lr_train_sizes)
ax.grid(True)
ax.legend(fontsize=16)

plt.show()
</code></pre>
<img src="imgs/20200916-161740.png" height=200 width=400>
</p></details>
</div>