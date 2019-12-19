# Data Preprocessing

<div style='width:1000px;margin:auto'>

<details><summary> <b>Functions Data Processing</b> </summary>
<p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/5_Cargo%20Rican%20HouseHold/2_Featuretools%20for%20Good.html"><b>Notebook</b></a> </p>

<ol>
<li>Remove any <b>duplicated</b> columns.</li>

<li>Replace <b>infinite</b> values with <b>np.nan</b></li>

<li>Remove columns with a <b>missing percentage </b>above the <em>missing_threshold</em></li>

<li>Remove columns with only a <b>single unique value.</b></li>

<li>Remove one out of every pair of columns with a <b>correlation</b> threshold above the correlation_threshold</li>

<li>Extract the <b>training</b> and <b>testing</b> data along with <b>labels</b> and <b>ids</b> (needed for making submissions)</li>
</ol>

~~~python
def post_process(feature_matrix, missing_threshold=.95, correlation_threshold=.95):
    # Remove duplicated features.
    start_features  = feature_matrix.shape[1]
    feature_matrix = feature_matrix.loc[:, ~feature_matrix.columns.duplicated()]
    n_duplicated   = start_features - feature_matrix.shape[1]
    print(f'~> There were {bg(n_duplicated)} duplicated features.')
    
    feature_matrix = feature_matrix.replace({np.inf: np.nan, -np.inf: np.nan}).reset_index()
    
    # Extract the Id and Target Columns.
    ids    = list(feature_matrix.pop('idhogar'))
    labels = list(feature_matrix.pop('Target'))
    
    # Drop any columns drived from column 'Target'
    drop_cols = []
    for col in feature_matrix:
        if col == 'Target':
            pass
        elif 'Target' in col:
            drop_cols.append(col)
    
    feature_matrix = feature_matrix[[x for x in feature_matrix if x not in drop_cols]]
    
    # One-Hot Encoding (if necessery)
    feature_matrix  = pd.get_dummies(feature_matrix, drop_first=True)
    n_start_feature = feature_matrix.shape[1]
    print(f'~> Original Shape: {bg(n_start_feature)}.')
    
    
    # Find the missing values
    missing             = pd.DataFrame(feature_matrix.isnull().sum())
    missing['fraction'] = missing[0] / feature_matrix.shape[0]
    missing.sort_values('fraction', ascending=False, inplace=True)
    
    # Missing Above threshold
    missing_cols   = list(missing[missing['fraction'] > missing_threshold].index)
    n_missing_cols = len(missing_cols)
    
    # Remove missing columns
    feature_matrix = feature_matrix[[col for col in feature_matrix if col not in missing_cols]]
    print(f'~> There were {bg(n_missing_cols)} missing columns above threshold = {colored(missing_threshold, "green")}.')
    
    unique_counts        = pd.DataFrame(feature_matrix.nunique()).sort_values(0, ascending=False)
    zero_variance_cols   = list(unique_counts[unique_counts[0] == 1].index)
    n_zero_variance_cols = len(zero_variance_cols)
    
    # Remove zero variance columns
    feature_matrix = feature_matrix[[col for col in feature_matrix if col not in zero_variance_cols]]
    print(f'~> There were {bg(n_zero_variance_cols)} columns with zero variance.')
    
    # Correlations.
    corr_matrix = feature_matrix.corr().abs()
    upper       = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
    to_drop     = [column for column in upper.columns if any(upper[column] > correlation_threshold)]
    
    n_collinear = len(to_drop)
    
    feature_matrix = feature_matrix[[x for x in feature_matrix if x not in to_drop]]
    print(f'~> There were {bg(n_collinear)} highly correlated columns above threshold = {colored(correlation_threshold, "green")}.')
    
    # Total number of columns removed.
    total_removed = n_collinear + n_duplicated + n_missing_cols + n_zero_variance_cols
    print(f'~> Total Number columns removed = {bg(total_removed)}.')
    print(f'~> Shape after removing: {bg(feature_matrix.shape, "s")}.')
    
    # Add the ids and target
    feature_matrix['idhogar'] = ids
    feature_matrix['Target']  = labels
    
    # Extract traing and test datasets.
    train = feature_matrix[feature_matrix.Target.notnull()]
    test  = feature_matrix[feature_matrix.Target.isnull()]
    
    # Subset to houses with a head of household
    train = train[train['idhogar'].isin(list(train_valid['idhogar']))]
    test = test[test['idhogar'].isin(list(test_valid['idhogar']))]
    
    train_labels = np.array(train.pop('Target')).reshape((-1,))
    test_ids     = list(test.pop('idhogar'))
    
    train, test = train.align(test, join='inner', axis=1)
    
    assert (len(train_labels) == train.shape[0]), 'Labels must be the same length as number of training.'
    assert (len(test_ids) == test.shape[0]), 'Test ids must equal the number of test observations.'
    
    return train, train_labels, test, test_ids
~~~

</p>
</details>

<hr>

<details><summary> <b>Train Test Split</b> </summary>
<p style="margin: 0">
<p>1) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/1_step-by-step-diabetes-classification-knn-detailed.html#Test-Train-Split-and-Cross-Validation-methods">Explanation for <b>Train<em>Test</em>Split</b></a> <br>
2) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/2_KNN%20-%20Full%20Pipeline.html#Train-Test-Split">Train Test Split notebook</a></p>
~~~
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    df_feat, y, test_size=0.4, random_state=42)
~~~
</p>
</details>

<details><summary> <b>Temporal Splitting (Time Based  Splitting)</b> </summary>
<p>
~~~python
split_train = int(len(data) * .8)
split_test  = int(len(data) * .2)

X_train = data[:split_train]
y_train = data[:split_train]['Target']

X_test = data[-split_test:]
y_test = data[-split_test:]['Target']
~~~
</p>
</details>

<details><summary> <b>Make Scorer</b> </summary>
<p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/sklearn.metrics.make_scorer.html#sklearn-metrics-make-scorer"><b>Sklearn Docs</b></a> </p>
~~~python
from sklearn.metrics import f1_score, make_scorer

scorer = make_scorer(f1_score, greater_is_better=True, average='macro')

~~~
</p>
</details>

<details><summary> Create a <b>Pipeline</b> </summary>
<p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/5_Cargo%20Rican%20HouseHold/1_Costa%20Rican%20Household%20Poverty%20Level%20Prediction.html"><b>Notebook</b></a> </p>
~~~python
from sklearn.preprocessing import Imputer, MinMaxScaler
from sklearn.pipeline import Pipeline

pipeline = Pipeline([('imputer', Imputer(strategy='meadian')),
                     ('scaler', MinMaxScaler())])

# Fit and transform the training data
train_set = pipeline.fit_transform(train_set)
test_st   = pipeline.transform(test_set)
~~~
</p>
</details>

<details><summary> <b>K-Fold CV</b> </summary>
<p>

</p>
</details>

<details><summary> <b>Cross_val_score</b> </summary>
<p>
~~~python
model = RF(n_estimators=100, n_jobs=-1)

# 10 Fold cross validation
cv_results = cross_val_score(model, train_set, train_labels, cv=10, scoring=scorer)

print(f'~> 10 Fold Cross Validation F1 Score = {bg(round(cv_results.mean(), 4), "s")} with std = {bg(round(cv_results.std(), 4), "s")}')
~~~
</p>
</details>

<details><summary><b>Cross Validation</b></summary>
<p style="margin: 0">
<p>1) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/1_step-by-step-diabetes-classification-knn-detailed.html#Test-Train-Split-and-Cross-Validation-methods">Explanation for <b>Cross Validation</b></a> </p>
</p>
</details>

<details><summary> <b>GridSearchCV</b> </summary>
<p style="margin: 0">
<p>1) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/1_step-by-step-diabetes-classification-knn-detailed.html#Hyper-Parameter-optimization">Explanation of <b>GridSearch</b>.</a> <br>
2) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/2_KNN%20-%20Full%20Pipeline.html#Hyperparameter-Tunning-&amp;-Cross-Validation">Hyperparameter Tunning &amp; Cross validation</a> </p>
~~~
# Load the model
from sklearn.model_selection import GridSearchCV

# Select the range of parameters
param_grid = {'n_neighbors': np.arange(1, 50)}

# Activate the GridSearchCV
knn = KNeighborsClassifier()
knn_cv = GridSearchCV(knn, param_grid, cv=5)
knn_cv.fit(X, y)

# Calculate the Training score
print('The Best Score for training =', knn_cv.best_score_*100,'%')

# See the Best K value
print('The Best parameters (K) =', knn_cv.best_params_['n_neighbors'])
~~~
</p>
</details>

<details><summary> <b>Randomized Search</b> </summary><p>

</p></details>

<details><summary> <b>Bayesian Optimization</b> </summary><p><ul>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Bayesian%20Optimization%20From%20Scratch/0_html/1_Bayesian%20Optimization.html">For <b>Sklearn Models</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Bayesian%20Optimization%20From%20Scratch/0_html/2_Bayesian%20Optimization%20for%20LightGBM.html">For <b> LightGBM</b></a></li>

</ul></p></details>

</div>



