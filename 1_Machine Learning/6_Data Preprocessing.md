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

<details><summary> <b>Train Test Split (Stratified)</b> [Categorical]</summary>
<p style="margin: 0">
<p>1) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/1_step-by-step-diabetes-classification-knn-detailed.html#Test-Train-Split-and-Cross-Validation-methods">Explanation for <b>Train<em>Test</em>Split</b></a> <br>
2) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/2_KNN%20-%20Full%20Pipeline.html#Train-Test-Split">Train Test Split notebook</a></p>
~~~
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    df_feat, y, test_size=0.4, stratify=y, random_state=42)
~~~

<p>Another way to split, by hashing the unique identifier of each row, to make sure that at the next run, the training and test sets will be the same</p>
```
from zlib import crc32

def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids         = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

housing_with_id = housing.reset_index()    # Since housing doesn't have identifier.
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

print(len(train_set)/housing.shape[0], len(test_set)/housing.shape[0])
```

</p></details>

<details><summary> <b>Train Test Split (Stratified)</b> [Regression]</summary><p>

<details><summary> <b>Manually Chosen bins</b></summary><p>
<h5>Descritize the target column into n bins.</h5>
```
housing['income_cat'] = pd.cut(housing['median_income'],
                               bins=[0., 1.5, 3., 4.5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])
```

<h5>Split based on the new categorical binned column</h5>
```
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['income_cat']):
    strat_train_set = housing.loc[train_index]
    strat_test_set  = housing.loc[test_index]
```

<h5>Then, remove the binned column.</h5>
```
# Remove the "income_cat".
for set_ in (strat_train_set , strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)
```
</p></details>

<details><summary> <b>Bins chosen by Sturge's rule</b></summary><p>
```
from sklearn import model_selection 

def create_folds(data):
    # Create a new column called kfold and fill it with -1.
    data["kfold"] = -1

    # Randomize the rows of the data.
    data = data.sample(frac=1).reset_index(drop=True)

    # Calculate number of bins by Sturge's rule.
    n_bins = np.floor(1 + np.log2(len(data)))

    # Bin targets.
    data.loc[:, "bins"] = pd.cut(data["target"],
                                 bins=n_bins,
                                 labels=False)
    
    # Initiate the kfold class from model_selection module.
    kf = model_selection.StratifiedKFold(n_splits=5)

    # Fill the new kfold column.
    for f, (t_, v_) in enumerate(kf.split(X=data, y=data.bins.values)):
        data.loc[v_, 'kfold'] = f

    # Drop the bins column.
    data = data.drop("bins", axis=1)

    return data
```
</p></details>
</p></details>

<details><summary> <b>Temporal Splitting (Time Based  Splitting)</b> </summary><p>
~~~python
split_train = int(len(data) * .8)
split_test  = int(len(data) * .2)

X_train = data[:split_train]
y_train = data[:split_train]['Target']

X_test = data[-split_test:]
y_test = data[-split_test:]['Target']
~~~
</p></details>

<details><summary> <b>Make Scorer</b> </summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/sklearn.metrics.make_scorer.html#sklearn-metrics-make-scorer"><b>Sklearn Docs</b></a> </p>
~~~python
from sklearn.metrics import f1_score, make_scorer

scorer = make_scorer(f1_score, greater_is_better=True, average='macro')

~~~
</p></details>

<details><summary> Create a <b>Pipeline</b> </summary><p>
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
</p></details>

<details><summary> <b>Random K-Fold CV</b> </summary><p>
```
# We can use this method with almost all kinds of datasets.
from sklearn import model_selection

# Create a new column called kfold and fill it with -1.
df['kfold'] = -1

# Randomize the rows of the data.
df = df.sample(frac=1).reset_index(drop=True)

# Initiate the kfold class from model_selection module
kf = model_selection.KFold(n_splits=5)

# fill the new kfold column.
for fold, (trn_, val_) in enumerate(kf.split(X=df)):
    df.loc[val_, 'kfold'] = fold

# Save the new csv with kfold column.
df.to_csv("train_folds.csv", index=False)
```
</p></details>

<details><summary> <b>Stratified K-Fold CV</b> </summary><p>
```
# Using Custom Stratified K-folds
def Stratified_kfolds(alg, X, y):
    score_valid = 0
    skf = StratifiedKFold(n_splits=2, shuffle=True, random_state=33)
    
    for train_idx, valid_idx in skf.split(X, y):
        X_train, X_valid = X.iloc[train_idx], X.iloc[valid_idx]
        y_train, y_valid = y.iloc[train_idx], y.iloc[valid_idx]

        # One-Hot Encoding
        ohe_enc_keyword  = CountVectorizer()
#         ohe_enc_location = CountVectorizer()
        ohe_enc_text     = CountVectorizer(max_df=.9, min_df=3)

        # Transform Train data
        keyword_train    = ohe_enc_keyword.fit_transform(X_train['keyword'])
#         location_train   = ohe_enc_location.fit_transform(X_train['location'])
        text_train       = ohe_enc_text.fit_transform(X_train['text'])

        # Transform Validation data.
        keyword_valid    = ohe_enc_keyword.transform(X_valid['keyword'])
#         location_valid   = ohe_enc_location.transform(X_valid['location'])
        text_valid       = ohe_enc_text.transform(X_valid['text'])

        ## Merge Training data.
        X_train = hstack((keyword_train, text_train)).tocsr()

        ## Merge Validation data
        X_valid = hstack((keyword_valid, text_valid)).tocsr()

        # ML Models.
        alg.fit(X_train.todense(), y_train)
        y_pred_valid = alg.predict(X_valid.todense())
        score_valid  += f1_score(y_valid, y_pred_valid)
        
    return score_valid/skf.n_splits
```
<h4>Another simple solution</h4>
```
# We can use this method with almost all kinds of datasets.
from sklearn import model_selection

# Create a new column called kfold and fill it with -1.
df['kfold'] = -1

# Randomize the rows of the data.
df = df.sample(frac=1).reset_index(drop=True)
y  = df.target.values

# Initiate the kfold class from model_selection module
kf = model_selection.StratifiedKFold(n_splits=5)

# fill the new kfold column.
for fold, (trn_, val_) in enumerate(kf.split(X=df, y=y)):
    df.loc[val_, 'kfold'] = fold

# Save the new csv with kfold column.
df.to_csv("train_folds.csv", index=False)
```
</p></details>

<details><summary> <b>Group K-Fold CV</b> </summary><p>
<p>K-fold iterator variant with non-overlapping groups.</p>

<p>The same group will not appear in two different folds (the number of distinct groups has to be at least equal to the number of folds).</p>

<p>The folds are approximately balanced in the sense that the number of distinct groups is approximately the same in each fold.</p>
```
import numpy as np
from sklearn.model_selection import GroupKFold
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4])
groups = np.array([0, 0, 2, 2])
group_kfold = GroupKFold(n_splits=2)
group_kfold.get_n_splits(X, y, groups)

print(group_kfold)

for train_index, test_index in group_kfold.split(X, y, groups):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    print(X_train, X_test, y_train, y_test)
    
### Result ####
TRAIN: [0 1] TEST: [2 3]
[[1 2]
 [3 4]] [[5 6]
 [7 8]] [1 2] [3 4]
TRAIN: [2 3] TEST: [0 1]
[[5 6]
 [7 8]] [[1 2]
 [3 4]] [3 4] [1 2]
```
</p></details>

<details><summary> <b>Cross_val_score</b> </summary><p>
```
model = RF(n_estimators=100, n_jobs=-1)

# 10 Fold cross validation
cv_results = cross_val_score(model, train_set, train_labels, cv=10, scoring=scorer)

print(f'~> 10 Fold Cross Validation F1 Score = {bg(round(cv_results.mean(), 4), "s")} with std = {bg(round(cv_results.std(), 4), "s")}')
```
</p></details>

<details><summary> <b>cross_val_predict</b> </summary><p>
```
# Returns the predictions 
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3, n_jobs=-1, verbose=1, method="predict")

# Predict Proba
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3, n_jobs=-1, verbose=1, method="predict_proba")

# Predict decision function
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3, n_jobs=-1, verbose=1, method="decision_function")
```
</p></details>


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

# Show all resutls.
resutls = pd.DataFrame(knn_cv.cv_results_)[['params', 'mean_test_score', rank_test_score']]

# Sort by test score
results.sort_values('rank_test_score')

# Get the best model.
knn_cv.best_estimator_
~~~
</p>
</details>


<details><summary> <b>Custom Transformer</b> </summary><p>
```
from sklearn.base import BaseEstimator, TransformerMixin

rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
	def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
		self.add_bedrooms_per_room = add_bedrooms_per_room
	def fit(self, X, y=None):
		return self # nothing else to do
	def transform(self, X, y=None):
		rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
		population_per_household = X[:, population_ix] / X[:, households_ix]
		if self.add_bedrooms_per_room:
			bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
			return np.c_[X, rooms_per_household,
					   population_per_household,
				 	   bedrooms_per_room]
		else:
			return np.c_[X, rooms_per_household, population_per_household]
			
			
attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)
```
</p></details> 


<details><summary> <b>Paralleism</b> </summary><p>
```
# Prepare the logging.
import logging

# Logging configuration.
logging.basicConfig(
    level=logging.INFO,
    format="%(processName)-10s %(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
```
```
# Prepare Timing function.
from functools import wraps
import time

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        return result, time.time() - start
    return wrapper
```

```
# Prepare validation strategy.
from sklearn.externals import joblib
from sklearn.model_selection import cross_val_score

@timeit
def train_model(path, model, saveto=None, cv=2):
    # Load the corpus data and labels for classification.
    X = df["sample"].values
    y = df['intent'].values

    # Compute cross validation scores.
    scores = cross_val_score(model, X, y, cv=cv)

    # Fit the model on entire dataset.
    model.fit(X, y)

    # Write to disk if specified
    if saveto:
        joblib.dump(model, saveto)

    # Return scores as well as training time via decorator.
    return scores
```

```
# Prepare model.s
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier

def fit_naive_bayes(path, saveto=None, cv=2):
    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", MultinomialNB())
    ])

    if saveto is None:
        saveto = f"naive_bayes_{time.time()}.pkl"

    scores, delta = train_model(path, model, saveto, cv)

    logger.info((
        f"\nnaive bayes training took {delta:0.2f} seconds."
        f"with an average score of {scores.mean():0.3f}"
    ))

def fit_logistic_regression(path, saveto=None, cv=2):
    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression())
    ])

    if saveto is None:
        saveto = f"log_reg_{time.time()}.pkl"
    
    scores, delta = train_model(path, model, saveto, cv)
    logger.info((
        f"\nlogistic regression training took {delta:0.2f} seconds"
        f"with an average score of {scores.mean():.3f}"
    ))


def fit_multilayer_perceptron(path, saveto=None, cv=2):
    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", MLPClassifier(hidden_layer_sizes=(10, 10), early_stopping=True))
    ])

    if saveto is None:
        saveto = f"multilayer_perceptron_{time.time()}.pkl"

    scores, delta = train_model(path, model, saveto, cv)

    logger.info((
        f"\nmultilayer perceptron training took {delta:.2f} seconds"
        f" with an average score of {scores.mean():.3f}"
    ))
```

```
# Paralleism.
import multiprocessing as mp

def run_parallel(path):
    tasks = [
        fit_naive_bayes, fit_logistic_regression, fit_multilayer_perceptron
    ]
    logger.info("\nbeginning parallel tasks")
    start = time.time()

    procs = []
    for task in tasks:
        proc = mp.Process(name=task.__name__, target=task, args=(path,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    delta = time.time() - start
    logger.info(f"\ntotal parallel fit time: {delta:.2f} seconds.\n")

run_parallel("./")
```
</p></details> 

<hr>

<details><summary><b style='font-size:20px'>Bayesian Optimization</b> </summary><p><ul>
```
!pip install bayesian-optimization
from bayes_opt import BayesianOptimization
```
<details><summary> <b>LogisticRegression</b> </summary><p>
```
# Define LogisticRegression CV
def lg_cv(C, 
          penalty, 
          solver, 
          data, targets):
    alg = LogisticRegression(C=C,
                                         penalty=penalty,
                                         solver=solver,
                                         random_state=42)
    alg.fit(data, targets)
    y_pred = alg.predict(X_test)
    score = metrics.accuracy_score(y_test, y_pred)
    return score

# Optimization Strategy
def optimize_lg(data, targets):
    def lg_crossval(expC, 
                    expPenalty,
                    expSolver
                    ):
        penalty_dict = {0: "l1",
                        1: "l2",
                        2: "none"}
        solver_dict  = {0: "newton-cg",
                        1: "lbfgs",
                        2: "sag",
                        3: "saga"}

        C       = 10 ** expC
        penalty = penalty_dict[int(expPenalty)]
        if penalty in ["l2", "none"]:
            solver = solver_dict[int(expSolver)]
        else:
            solver = "liblinear"
        return lg_cv(C=C, 
                     penalty=penalty,
                     solver=solver,
                     data=data, targets=targets)

    optimizer = BayesianOptimization(
        f=lg_crossval,
        pbounds={'expC': (-2, .5),
                 'expPenalty': (0, 2.9),
                 'expSolver': (0, 3.9)
                 },
        random_state=42,
        verbose=2
    )
    optimizer.maximize(n_iter=20, init_points=10)

    print(f"~> Best parameters: {optimizer.max}")
    return optimizer.max['params']

# Run the optimization
best_params = optimize_lg(X_train, y_train)
```
</p></details>

<details><summary><b> LinearSVC</b></summary><p>
```
def svc_cv(C, loss, data, targets):
    alg = Pipeline([
        ("scaler", MinMaxScaler()),
        ("linear_svc", OneVsRestClassifier(LinearSVC(C=C,
                                                     penalty="l2",
                                                     loss=loss,
                                                     random_state=42)))
    ])
    alg.fit(data, targets)
    y_pred = alg.predict(X_test)
    return metrics.accuracy_score(y_test, y_pred)

def optimize_svc(data, targets):
    def svc_crossval(expC, expLoss):
        loss_dict = {0: "hinge",
                     1: "squared_hinge"}
        C = 10 ** expC
        loss    = loss_dict[int(expLoss)]
        return svc_cv(C=C, loss=loss, data=data, targets=targets)

    optimizer = BayesianOptimization(
        f=svc_crossval,
        pbounds={'expC': (-6, 5),
                 'expLoss': (0, 1.9)},
        random_state=42,
        verbose=2,

    )
    optimizer.maximize(n_iter=40, init_points=10)

    print(f"~> Final Result: {optimizer.max}")

# Optimize
optimize_svc(X_train, y_train)
```
</p></details>

<details><summary><b> Kernel SVM</b></summary><p>
```
def svc_cv(C, kernel, data, targets):
    alg = Pipeline([
        ("scaler", StandardScaler()),
        ("linear_svc", OneVsOneClassifier(SVC(C=C,
                                              kernel=kernel,
                                              random_state=42)))
    ])
    alg.fit(data, targets)
    y_pred = alg.predict(X_test)
    return metrics.accuracy_score(y_test, y_pred)

def optimize_svc(data, targets):
    def svc_crossval(expC, expKernel):
        kernel_dict = {0: "poly",
                       1: "rbf",
                       2: "sigmoid",
                    #    3: "precomputed",
                       }
        C      = 10 ** expC
        kernel = kernel_dict[int(expKernel)]
        return svc_cv(C=C, kernel=kernel, data=data, targets=targets)

    optimizer = BayesianOptimization(
        f=svc_crossval,
        pbounds={'expC': (-6, 5),
                 'expKernel': (0, 2.999)},
        random_state=42,
        verbose=2,

    )
    optimizer.maximize(n_iter=40, init_points=10)

    print(f"~> Final Result: {optimizer.max}")

# Optimize
optimize_svc(X_train, y_train)
```
</p></details>

<details><summary> <b>RidgeClassifier</b> </summary><p>
```
# Define Ridge CV
def ridge_cv(alpha, data, targets):
    alg = RidgeClassifier(alpha=alpha, random_state=33)
    score = Stratified_kfolds(alg, data, targets)
    return score
    
# Optimization Strategy
def optimize_ridge(data, targets):
    def ridge_crossval(expAlpha):
        alpha = 10 ** expAlpha
        return ridge_cv(alpha=alpha, data=data, targets=targets)
    
    optimizer = BayesianOptimization(
        f=ridge_crossval,
        pbounds={'expAlpha': (-7, 5)},
        random_state=33,
        verbose=2
    )
    optimizer.maximize(n_iter=20, init_points=5)
    
    print(f"~> Best parameters: {optimizer.max}")
    
# Run the optimization
optimize_ridge(X, y)
```
</p></details>

<details><summary> <b>LassoClassifier</b> </summary><p>
```
from sklearn.linear_models import Lasso

# Define Lasso CV
def lasso_cv(alpha, data, targets):
    alg = Lasso(alpha=alpha, random_state=33)
    score = Stratified_kfolds(alg, data, targets)
    return score
    
# Optimization Strategy
def optimize_lasso(data, targets):
    def lasso_crossval(expAlpha):
        alpha = 10 ** expAlpha
        return lasso_cv(alpha=alpha, data=data, targets=targets)
    
    optimizer = BayesianOptimization(
        f=ridge_crossval,
        pbounds={'expAlpha': (-7, 5)},
        random_state=33,
        verbose=2
    )
    optimizer.maximize(n_iter=20, init_points=5)
    
    print(f"~> Best parameters: {optimizer.max}")
    
# Run the optimization
optimize_lasso(X, y)
```
</p></details>

<details><summary> <b>Multi-nomial Naive Bayes</b> </summary><p>
```
# CV Strategy
def nb_cv(alpha, data, targets):
    alg = MultinomialNB(alpha=alpha)
    return Stratified_kfolds(alg, data, targets)
    
def nb_crossval(expAlpha):
    alpha = 10**expAlpha
    return nb_cv(alpha=alpha, data=X, targets=y)

optimizer = BayesianOptimization(
    f=nb_crossval,
    pbounds={'expAlpha': (-6, 5)},
    random_state=33,
    verbose=2
)

# Optimize
optimizer.maximize(
    n_iter=30,
    init_points=5
)

print(f"~> Best Result: {optimizer.max}")
```
</p></details>

<details><summary> <b>Gaussian Naive Bayes</b> </summary><p>
```
# CV Strategy
def nb2_cv(alpha, data, targets):
    alg = GaussianNB(var_smoothing=alpha)
    return Stratified_kfolds(alg, data, targets)

def nb2_crossval(expAlpha):
    alpha = 10**expAlpha
    return nb2_cv(alpha=alpha, data=X, targets=y)

optimizer = BayesianOptimization(
    f=nb2_crossval,
    pbounds={'expAlpha': (-9, 5)},
    random_state=33,
    verbose=2
)
# Optimize
optimizer.maximize(
    n_iter=30,
    init_points=5
)

print(f"~> Best Result: {optimizer.max}")
```
</p></details>

<details><summary><b> Decision Tree</b></summary><p>
```
# CV Strategy
def dt_cv(criterion,
          splitter,
          max_depth,
          min_samples_split,
          min_samples_leaf,
          max_features,
          data, targets):
    alg = DecisionTreeClassifier(criterion=criterion,
                                 splitter=splitter,
                                 max_depth=max_depth,
                                 min_samples_split=min_samples_split,
                                 min_samples_leaf=min_samples_leaf,
                                 max_features=max_features,
                                 random_state=42)
    alg.fit(data, targets)
    y_pred = alg.predict(X_test)
    return metrics.accuracy_score(y_test, y_pred)

def optimize_dt(data, targets):
    def dt_crossval(criterion, splitter, max_depth, min_samples_split, min_samples_leaf, max_features):
        criterion_dict = {0: "gini",
                          1: "entropy"}
        splitter_dict  = {0: "best",
                          1: "random"}
        maxFeat_dict   = {0: "sqrt",
                          1: "log2",
                          2: None}

        criterion    = criterion_dict[int(criterion)]
        splitter     = splitter_dict[int(splitter)]
        max_depth    = int(max_depth)
        max_features = maxFeat_dict[int(max_features)]

        return dt_cv(criterion=criterion,
                    splitter=splitter,
                    max_depth=max_depth,
                    min_samples_split=min_samples_split,
                    min_samples_leaf=min_samples_leaf,
                    max_features=max_features,
                    data=data, targets=targets)

    optimizer = BayesianOptimization(
        f=dt_crossval,
        pbounds={'criterion': (0, 1.999),
                 'splitter': (0, 1.999),
                 'max_depth': (1, 50),
                 "min_samples_split": (0.05, 1),
                 "min_samples_leaf": (0.05, .5),
                 "max_features": (0, 2.999)},
        random_state=42,
        verbose=2
    )
    # Optimize
    optimizer.maximize(
        n_iter=50,
        init_points=60
    )
    print(f"~> Best Result: {optimizer.max}")

optimize_dt(X_train, y_train)
```
</p></details>

<details><summary> <b>XGBoostClassifier</b> </summary><p>
```
# Importing
from sklearn.model_selection import cross_val_score
from bayes_opt import BayesianOptimization

def xgboost_cv(max_depth,
               learning_rate,
               n_estimators,
               gamma,
               min_child_weight,
               max_delta_step,
               subsample,
               colsample_bytree,
               silent=True,
               nthread=-1):
    return cross_val_score(xgb.XGBClassifier(max_depth=int(max_depth),
                                             learning_rate=learning_rate,
                                             n_estimators=int(n_estimators),
                                             silent=silent,
                                             nthread=nthread,
                                             gamma=gamma,
                                             min_child_weight=min_child_weight,
                                             max_delta_step=max_delta_step,
                                             subsample=subsample,
                                             colsample_bytree=colsample_bytree),
                          X_train,
                          y_train,
                          scoring="f1",
                          cv=3).mean()

# Define Bayesian Optimization
optimizer = BayesianOptimization(xgboost_cv,
                                 {'max_depth': (5, 10),
                                  'learning_rate': (0.01, 0.3),
                                  'n_estimators': (50, 1000),
                                  'gamma': (1., 0.01),
                                  'min_child_weight': (2, 10),
                                  'max_delta_step': (0, 0.1),
                                  'subsample': (0.7, 0.8),
                                  'colsample_bytree' :(0.5, 0.99)
                                  })
# Run the optimization
optimizer.maximize(n_iter=20,
                   init_points=5)

print(optimizer.max)

# Check the score of the tunned model
params                 = optimizer.max['params']
params['max_depth']    = int(params['max_depth'])
params['n_estimators'] = int(params['n_estimators'])

alg = xgb.XGBClassifier(**params)
alg.fit(X_train, y_train)

y_pred_train = alg.predict(X_train)
y_pred_valid = alg.predict(X_valid)

print(f"F1_score on train data: {bg(f1_score(y_train, y_pred_train))}")
print(f"F1_score on Valid data: {bg(f1_score(y_valid, y_pred_valid))}")
```
</p></details>

<details><summary> <b>Stacking</b> </summary><p>
```
from mlxtend.classifier import StackingClassifier

def stacking1_cv(C, data, targets):
    lr    = LogisticRegression(C=C, penalty='l2', n_jobs=-1)
    sclf  = StackingClassifier(classifiers=[alg1, alg2, alg3], meta_classifier=lr)
    return  Stratified_kfolds(sclf, data, targets)
    
def stacking1_crossval(expC):
    C = 10 ** expC
    return stacking1_cv(C=C, data=X, targets=y)

optimizer = BayesianOptimization(
    f=stacking1_crossval,
    pbounds={'expC': (-9, 5)},
    random_state=33,
    verbose=2,

)
optimizer.maximize(n_iter=10, init_points=10)

print(f"~> Final Result: {optimizer.max}")
```
</p></details>

<details><summary> <b>LightGBM</b> </summary><p>
<ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Bayesian%20Optimization%20From%20Scratch/0_html/2_Bayesian%20Optimization%20for%20LightGBM.html">Using<b> Bayesian Optimization</b> library</a></li>

<li><a href="./6_data_processing/hyperopt_for_lightgbm_with_f1_score.html">Using<b> hyperopt</b> library</a></li>
</ul>
</p></details>

<details><summary> <b>Catboost</b> </summary><p><ul>
<li><a href="./6_data_processing/hyperopt_for_catboost.html">Using<b> hyperopt</b> library</a></li>
</ul></p></details>

<details><summary> <b>Random Forest</b> [skopt]</summary><p>
```
from functools import partial
from sklearn import ensemble, metrics, model_selection

from skopt import gp_minimize
from skopt import space

def optimize(params, param_names, X, y):
    # convert params to dictionary.
    params = dict(zip(param_names, params))

    # initialize model with current parameters.
    model = ensemble.RandomForestClassifier(**params)

    # Initialize stratified k-fold.
    kf = model_selection.StratifiedKFold(n_splits=5)

    # initliaze accuracy list.
    accuracies = []

    # Loop over all folds.
    for train_idx, test_idx in kf.split(X=X, y=y):
        X_train, y_train = X[train_idx], y[train_idx]
        X_test,  y_test  = X[test_idx],  y[test_idx]

        # Fit model for current fold.
        model.fit(X_train, y_train)

        # Create predictions.
        y_preds = model.predict(X_test)

        # Calaculate and append accuracy.
        fold_accuracy = metrics.accuracy_score(y_test, y_preds)
        accuracies.append(fold_accuracy)

    # Return negative accuracy.
    return -1 * np.mean(accuracies)

if __name__ == "__main__":
    # Read the training data.
    df = pd.read_csv("../input/mobile_train.csv")

    X = ...
    y = ...

    # Define a parameter space.
    param_space = [space.Integer(3, 15, name="max_depth"),
                   space.Integer(100, 1500, name="n_estimators"),
                   space.Categorical(["gini", "entropy"], name="criterion"),
                   space.Real(0.01, 1, prior="uniform", name="max_features")]

    param_names = ["max_depth",
                   "n_estimators",
                   "criterion",
                   "max_features"]

    optimization_function = partial(optimize, param_names=param_names, X=X, y=y)

    result = gp_minimize(optimization_function,
                         dimensions=param_space,
                         n_calls=15,
                         n_random_starts=10,
                         verbose=10)
    # Create best params dict and print it.
    best_params = dict(zip(param_names,
                           result.x))
    print(best_params)
```

```
## Show the plot of iterations.
from skopt.plots import plot_convergence
plot_convergence(result)
```
</p></details>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Bayesian%20Optimization%20From%20Scratch/0_html/1_Bayesian%20Optimization.html">For <b>Sklearn Models</b></a></li>
</ul></p></details>

<details><summary> <b style='font-size:20px'>Randomized Search</b></summary><p>
<h4>NOTE:</h4>
<p><b>Reciprocal Distribution</b> is useful when you have no idea what the scale of the hyperparameter should be.</p>
<p><b>Exponential Distribution</b> is best when you know (more or less) what the scale of the hyperparameter should be.</p>
see more distributions from <a href="https://docs.scipy.org/doc/scipy/reference/stats.html">here</a><br>

<ul><details><summary> <b>MultiNomial</b> </summary><p>
```
# Import Libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from scipy.stats import expon, reciprocal, geom, uniform

# Make the pipeline
pipe = make_pipeline(CounterVectorizer(), MultinomialNB())

# Cross-validate the pipeline using default parameters.
from sklearn.model_selection import cross_val_score
cross_val_score(pipe, X, y, cv=5, scoring='accuracy').mean()

# Specifiy parameter values to search (use a distribution for any continous parameters)
import scipy as sp
params = {}
params['countvectorizer__min_df'] = [1, 2, 3, 4]
params['countvectorizer__lowercase'] = [True, False]
params['multinomialnb__alpha'] = sp.stats.uniform(scale=1)

# try "n_iter" random combinations of those parameter values.
from sklearn.model_selection import RandomizedSearchCV
rand = RandomizedSearchCV(pipe, params, n_iter=10, cv=5, scoring='accuracy', random_state=1)
rand.fit(X, y)

# What was the best score found during the search?
rand.best_score_

# Which combination of parameters produced the best score.
rand.best_params_
```
</p></details>

<details><summary> <b>SVR</b> </summary><p>
```
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import expon, reciprocal

# see https://docs.scipy.org/doc/scipy/reference/stats.html
# for `expon()` and `reciprocal()` documentation and more probability distribution functions.

# Note: gamma is ignored when kernel is "linear"
param_distribs = {
        'kernel': ['linear', 'rbf'],
        'C': reciprocal(20, 200000),
        'gamma': expon(scale=1.0),
    }

svm_reg = SVR()
rnd_search = RandomizedSearchCV(svm_reg, param_distributions=param_distribs,
                                n_iter=50, cv=5, scoring='neg_mean_squared_error',
                                verbose=2, random_state=42)
rnd_search.fit(housing_prepared, housing_labels)
```
</p></details>

</ul></p></details>


</div>



