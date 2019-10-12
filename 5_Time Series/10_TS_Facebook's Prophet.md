# ==8. ML Models==

<details><summary style='font-size:18px;color:darkcyan'> **PipeLines** </summary>
<p>

<details><summary>**Try a bunch of models in a for loop**</summary>
<p>
[**Notebook**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/0_My%20work/1_Mushroom%20Classification/index.html#Data-Modeling) 
#### Import the models libraries.
~~~python
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegressionCV, RidgeClassifierCV
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
~~~

#### Add Models to an array
~~~python
MLA = [
    LinearSVC(),
    GaussianNB(),
    MLPClassifier(),
    LogisticRegressionCV(),
    RidgeClassifierCV(),
    LinearDiscriminantAnalysis(),
    KNeighborsClassifier()
]
~~~

#### Remove Warnings
~~~python
import warnings 
from sklearn.exceptions import ConvergenceWarning

# Filter out warnings from models
warnings.filterwarnings('ignore', category = ConvergenceWarning)
warnings.filterwarnings('ignore', category = DeprecationWarning)
warnings.filterwarnings('ignore', category = UserWarning)
~~~

#### Train the models
~~~python
#create table to compare MLA metrics
MLA_columns = ['MLA_Name', 'MLA_Parameters','MLA_Train_Accuracy_Mean', 
               'MLA_Test_Accuracy_Mean', 'MLA_Test_Accuracy_3*STD' ,'MLA_Time']
MLA_compare = pd.DataFrame(columns=MLA_columns)

MLA_predict = {}

for i, alg in enumerate(MLA):  
    cv_results = cross_validate(alg, train_set, train_labels, cv=10, scoring=scorer, return_train_score=True)

    MLA_compare.loc[i, 'MLA_Name']                = alg.__class__.__name__
    MLA_compare.loc[i, 'MLA_Parameters']          = str(alg.get_params())
    MLA_compare.loc[i, 'MLA_Train_Accuracy_Mean'] = cv_results['train_score'].mean()
    MLA_compare.loc[i, 'MLA_Test_Accuracy_Mean']  = cv_results['test_score'].mean()
    MLA_compare.loc[i, 'MLA_Test_Accuracy_3*STD'] = cv_results['test_score'].std()*3
    MLA_compare.loc[i, 'MLA_Time']                = cv_results['fit_time'].mean()

    
    alg.fit(train_set, train_labels)
    MLA_predict[MLA_name] = alg.predict(train_set)
        
    MLA_compare.sort_values(by=['MLA_Test_Accuracy_Mean'], ascending=False, inplace=True)
MLA_compare  
~~~
</p>
</details>

- [**H2O Auto ML**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/4_catboost_lightgbm_Xgboost/AutoML_H2O.html) 

<details><summary> **General Pipeline Model** </summary>
<p>
[**Notebook**](https://www.kaggle.com/artgor/exploring-categorical-encodings) 
#### Imports
~~~python
import lightgbm as lgb
import xgboost as xgb
from catboost import CatBoostRegressor, CatBoostClassifier
from sklearn import metrics

### For encoders
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

import time
import datetime
from sklearn.model_selection import StratifiedKFold, KFold, RepeatedKFold, GroupKFold, GridSearchCV, train_test_split, TimeSeriesSplit
from sklearn import metrics

from tqdm import tqdm_notebook
from sklearn.preprocessing import StandardScaler, LabelEncoder
~~~

#### 1. Import BG Function
~~~python
from termcolor import colored

# ****************SHOW COLORED text**********
def bg(value, type='num', color='blue'):
    value = str('{:,}'.format(value)) if type == 'num' else str(value)
    return colored(' '+value+' ', color, attrs=['reverse', 'blink'])
~~~

#### Double Validation Class.
~~~python
class DoubleValidationEncoderNumerical:
    """
    Encoder with validation within
    """
    def __init__(self, cols: List, encoder, folds):
        """
        :param cols:    Categorical Columns.
        :param encoder: Encoder Class.
        :param folds:   Folds to split the data.
        """
        self.cols          = cols
        self.encoder       = encoder
        self.folds         = folds
        self.encoders_dict = {}
        
    def fit_transform(self, X: pd.DataFrame, y: np.array) -> pd.DataFrame:
        X = X.reset_index(drop=True)
        y = y.reset_index(drop=True)

        for n_fold, (train_idx, val_idx) in enumerate(self.folds.split(X, y)):
            X_train, X_val = X.loc[train_idx].reset_index(drop=True), X.loc[val_idx].reset_index(drop=True)
            y_train, y_val = y[train_idx], y[val_idx]

            _ = self.encoder.fit_transform(X_train, y_train)

            # Transform validation part and get all necessary cols.
            val_t = self.encoder.transform(X_val)

            if n_fold == 0: 
                cols_representation = np.zeros((X.shape[0], val_t.shape[1]))

            self.encoders_dict[n_fold] = self.encoder
            cols_representation[val_idx, :] += val_t.values

        cols_representation = pd.DataFrame(cols_representation, columns=X.columns)
        return cols_representation
        
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.reset_index(drop=True)

        cols_representation = None

        for encoder in self.encoders_dict.values():
            test_tr = encoder.transform(X)

            if cols_representation is None:
                cols_representation = np.zeros(test_tr.shape)
            cols_representation = cols_representation + test_tr / self.folds.n_splits

        cols_representation = pd.DataFrame(cols_representation, columns=X.columns)
        return cols_representation
~~~

#### 3. Model Function
~~~python
####################### TRAIN MODEL CLASSIFICATION #####################
def train_model_classification(X, X_test, y, params, folds, model_type='lgb', eval_metric='auc', 
                               columns=None, plot_feature_importance=False, model=None, verbose=10000,
                               early_stopping_rounds=200, n_estimators=50000, splits=None, n_folds=3,
                               averaging='usual', n_jobs=-1, encoder=None, enc_val='single'):

    '''
    A function to train a veraity of classification models.
    Returns dictionary with oof predictions, test predictions, scores and, if necessary, feature importance.
    
    :params: X - training data, can be pd.DataFrame or np.ndarray (after normalizing)
    :params: X_test - test data, can be pd.DataFrame or np.ndarray (after normalizing)
    :params: y - target
    :params: folds - folds to split data
    :params: model_type - type of model to use
    :params: eval_metric - metric to use
    :params: columns - columns to use. If None - use all columns
    :params: plot_feature_importance - whether to plot feature importance of LGB
    :params: model - sklearn model, works only for "sklearn" model type
    '''
    columns  = X.columns if columns is None else columns
    n_splits = folds.n_splits if splits is None else n_folds
    X_test   = X_test[columns]
    
    # Set up scoring parameters
    metrics_dict = {'auc': {'lgb_metric_name': eval_metric,
                            'catboost_metric_name': 'AUC',
                            'sklearn_socring_function': metrics.roc_auc_score}}
    result_dict = {}
    

    
        
    # List of scores on folds
    scores = []
    feature_importance = pd.DataFrame()
    
    ## Split and train on folds
    for fold_n, (train_index, valid_index) in enumerate(folds.split(X, y)):
        if verbose:
            print(f'----------------- Fold {bg(fold_n + 1, color="green")} started at {bg(time.ctime(), "s")} ---------------')
        if type(X) == np.ndarray:
            X_train, X_valid  = X[columns][train_index], X[columns][valid_index]
            y_train, y_valid  = y[train_index],          y[valid_index]
        else:
            X_train, X_valid  = X[columns].iloc[train_index], X[columns].iloc[valid_index]
            y_train, y_valid  = y.iloc[train_index],          y.iloc[valid_index]
            
        X_t = X_test.copy()
        
        #################### Encoding (Single, Double). #########################
        if encoder and enc_val == 'single':
            X_train = encoder.fit_transform(X_train, y_train)
            X_valid = encoder.transform(X_valid)
            X_t     = encoder.transform(X_t)
        elif encoder and enc_val == 'double':
            encoder_double = DoubleValidationEncoderNumerical(cols=columns, encoder=encoder, folds=folds)
            X_train        = encoder_double.fit_transform(X_train, y_train)
            X_valid        = encoder_double.transform(X_valid)
            X_t            = encoder_double.transform(X_t)
        
        #################### Models ########################
        ## LightGMB Model. ##
        if model_type == 'lgb':
            model = lgb.LGBMClassifier(**params, n_estimators=n_estimators, n_jobs=n_jobs)
            model.fit(X_train, y_train,
                      eval_set=[(X_valid, y_valid)], 
                      eval_metric=metrics_dict[eval_metric]['lgb_metric_name'], 
                      verbose=verbose, early_stopping_rounds=early_stopping_rounds)
            y_pred_valid = model.predict_proba(X_valid)[:, 1]
            y_pred       = model.predict_proba(X_t, num_iteration=model.best_iteration_)[:, 1]
            
        ## XGBoost Model. ##
        if model_type == 'xgb':
            train_data = xgb.DMatrix(data=X_train, label=y_train, feature_names=X.columns)
            valid_data = xgb.DMatrix(data=X_valid, label=y_valid, feature_names=X.columns)
            watchlist  = [(train_data, 'train'), (valid_data, 'valid_data')]
            
            model       = xgb.train(dtrain=train_data, num_boost_round=n_estimators, evals=watchlist,
                                   early_stopping_rounds=early_stopping_rounds, verbose_eval=verbose,
                                   params=params)
            y_pred_valid = model.predict(xgb.DMatrix(X_valid, feature_names=X.columns), 
                                         ntree_limit=model.best_ntree_limit)
            y_pred       = model.predict(xgb.DMatrix(X_t, feature_names=X.columns),
                                         ntree_limit=model.best_ntree_limit)
        
        ## Sklearn Model. ##
        if model_type == 'sklearn':
            model.fit(X_train, y_train)
            
            y_pred_valid = model.predict(X_valid).reshape(-1,)
            score        = metrics_dict[eval_metric]['sklearn_socring_function'](y_valid, y_pred_val)
            
            print(f'Fold {fold_n}. {eval_metric}: {score:.4f}.')
            y_pred = model_predict_proba(X_t)[:, 1]
        
        ## CatBoost Model ##
        if model_type == 'cat':
            model = CatBoostClassifier(iterations=n_estimators, 
                                       eval_metric=metrics_dict[eval_metric]['catboost_metric_name'],
                                       **params,
                                       loss_funciton='Logloss')
            model.fit(X_train, y_train, eval_set=(X_valid, y_valid), cat_features=[], use_best_model=True, verbose=False)
            
            y_pred_valid = model.predict(X_valid)
            y_pred       = model.predict(X_t)
            
            
        ####################### Averaging ##################
        
        # out-of-fold predictions on train data
        oof = np.zeros((len(X), 1))
        # Averaged predictions on train data.
        prediction = np.zeros((len(X_test), 1))
        
        oof[valid_index] = y_pred_valid.reshape(-1, 1)
        scores.append(metrics_dict[eval_metric]['sklearn_socring_function'](y_valid, y_pred_valid))
        
        prediction += (y_pred.reshape(-1, 1) if averaging == 'usual' else pd.Series(y_pred).rank().values.reshape(-1, 1))

#         ## USUAL
#         if averaging == 'usual':
#             prediction += y_pred.reshape(-1, 1)
        
#         ## RANK
#         elif averaging == 'rank':
#             prediction += pd.Series(y_pred).rank().values.reshape(-1, 1)
            
        ####################### Feature Importance ##################
        ## LightGBM
        if model_type == 'lgb':
            fold_importance               = pd.DataFrame()
            fold_importance['feature']    = columns
            fold_importance['importance'] = model.feature_importances_
            fold_importance['fold']       = fold_n + 1
            feature_importance            = pd.concat([feature_importance, fold_importance], axis=0)
    
    prediction /= n_splits
    
    if verbose:
        print(f'\n~> CV mean score: {bg(np.mean(scores))}, std: {bg(np.std(scores))}.')
        
    result_dict['oof']        = oof
    result_dict['prediction'] = prediction
    result_dict['scores']     = scores
    
    if model_type == 'lgb':
        feature_importance['importance'] /= n_splits
        cols = feature_importance[['feature', 'importance']].groupby('feature')\
                                                            .mean()\
                                                            .sort_values(by=['importance'], ascending=False)[:50]\
                                                            .index
        best_features = feature_importance.loc[feature_importance.feature.isin(cols)]
        
        result_dict['feature_importance'] = feature_importance
        result_dict['top_columns']        = list(cols)
        
        if plot_feature_importance:
            plt.figure(figsize=(16, 12))
            color = sns.color_palette()[0]
            sns.barplot(x='importance', y='feature', data=best_features.sort_values(by=['importance'], ascending=False), color=color, zorder=3);
            plt.title('LightGMB Features (avg over folds)', fontsize=23);
            plt.grid(zorder=0)
    
    return result_dict
~~~

#### 5. How to use.
~~~python
X = train.drop(['id', 'target', 'dataset_type'], axis=1)
y = train['target']
X_test = test.drop(['id', 'dataset_type'], axis=1)
del all_data

n_fold = 5
folds  = StratifiedKFold(n_splits=5)

params = {
    'num_leaves': 256,
    'min_child_samples': 79,
    'objective': 'binary',
    'max_depth': -1,
    'learning_rate': .03,
    'boosting_type': 'gbdt',
    'subsample_freq': 3,
    'subsample': 1.0,
    'bagging_seed': 11,
    'metric': 'auc',
    'verbosity': -1,
    'reg_alpha': .3,
    'reg_lambda': .3,
    'colsample_bytree': 1.0
}

 result_dict_lgb = train_model_classification(X=X, 
                                              X_test=X_test, 
                                              y=y, 
                                              params=params, 
                                              folds=folds, 
                                              model_type='lgb',
                                              eval_metric='auc',
                                              plot_feature_importance=True,
                                              verbose=500,
                                              early_stopping_rounds=200,
                                              n_estimators=100,
                                              averaging='usual',
	                                              n_jobs=-1)
~~~
</p>
</details>

<details><summary> **Optimizer (LGB, XGB, CatBoost** </summary>
<p>

#### Timer Function
~~~python
# Credit: https://www.kaggle.com/tilii7/hyperparameter-grid-search-with-xgboost
## Define the timer function
def timer(start_time=None):
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec      = divmod(temp_sec, 60)
        print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))

### Call the function
# Here we go
# start_time = timer(None) # timing starts from this point for "start_time" variable
# random_search.fit(X, Y)
# timer(start_time) # timing ends here for "start_time" variable
~~~

#### 2. Optimizer Class
~~~python
class ModelOptimizer:
    best_score = None
    opt        = None
    
    def __init__(self, model, X_train, y_train, cat_cols_indices=None, n_fold=3, 
                 seed=2405, early_stopping_rounds=30, is_stratified=True, is_shuffle=True):
        self.model                 = model
        self.X_train               = X_train
        self.y_train               = y_train
        self.cat_cols_indices      = cat_cols_indices
        self.n_fold               = n_fold
        self.seed                  = seed
        self.early_stopping_rounds = early_stopping_rounds
        self.is_stratified         = is_stratified
        self.is_shuffle            = is_shuffle
     
    def update_model(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self.model, k, v)
    
    def evaluate_model(self):
        pass
    
    def optimize(self, param_space, max_evals=10, n_random_starts=2):
        start_time = timer()
        
        @use_named_args(param_space)
        def _minimize(**params):
            self.model.set_params(**params)
            return self.evaluate_model()
        
        opt = gp_minimize(_minimize, param_space, n_calls=max_evals, n_random_starts=n_random_starts, random_state=2405, n_jobs=-1)
        best_values = opt.x  # Best value of given parameters space.
        optimal_values = dict(zip([param.name for param in param_space], best_values))
        best_score = opt.fun
        self.best_score = best_score
        self.opt = opt
        
        print(f'~> Optimal Parameters: {optimal_values}\n~> Optimal Score: {best_score}')
        timer(start_time)
        print('---'*20)
        print('Updating model with optimal values...')
        self.update_model(**optimal_values)
        plot_convergence(opt)
        return optimal_values
    
class XgbOptimizer(ModelOptimizer):
    def evaluate_model(self):
        scores = xgboost.cv(self.model.get_xgb_params(), 
                            xgboost.DMatrix(self.X_train, label=self.y_train),
                            num_boost_round=self.model.n_estimators,
                            metrics='auc', 
                            nfold=self.n_fold,
                            stratified=self.is_stratified,
                            shuffle=self.is_shuffle,
                            seed=self.seed,
                            early_stopping_rounds=self.early_stopping_rounds)
        self.scores = scores
        test_scores = scores.iloc[:, 2]
        best_metric = test_scores.max()
        return 1 - best_metric

class CatboostOptimizer(ModelOptimizer):
    def evaluate_model(self):
        validation_scores = catboost.cv(
                                catboost.Pool(self.X_train,
                                              self.y_train,
                                              cat_features=self.cat_cols_indices),
                                self.model.get_params(),
                                nfold=self.n_fold,
                                stratified=self.is_stratified,
                                seed=self.seed,
                                early_stopping_rounds=self.early_stopping_rounds,
                                shuffle=self.is_shuffle,
                                metrics='auc',
                                plot=False)
        self.scores = validation_scores
        test_scores = validation_scores.iloc[:, 2]
        best_metric = test_scores.max()
        return 1 - best_metric

class LightGBMOptimizer(ModelOptimizer):
    def evaluate_model(self):
        lgb_dataset = lgb.Dataset(self.X_train,
                                  self.y_train,
                                  self.cat_cols_indices)
        eval_hist = lgb.cv(
                        self.model.get_params(),
                        lgb_dataset,
                        self.model.n_estimators,
                        nfold=self.n_fold,
                        seed=self.seed,
                        stratified=self.is_stratified,
                        shuffle=self.is_shuffle,
                        early_stopping_rounds=self.early_stopping_rounds,
                        metrics='auc')
        self.scores = eval_hist
        test_scores = eval_hist[list(eval_hist.keys())[0]]
        best_metric = max(test_scores)
        return 1 - best_metric
~~~

#### 3. How to use
[**Notebook**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/4_catboost_lightgbm_Xgboost/catboost_playground.html#XGBoost) 
</p>
</details>

</p>
</details>

<details><summary style='font-size:18px;color:darkcyan'> **Important Functions** </summary>
<p>

<details><summary>**Random Model**</summary>
<p>
~~~python
# Random model.
def RandomModel(y_test, numOfClasses):
    '''
    This function builds a random model that predicts the class labels randomly.
    INPUT:
        - y_test: (Series) the series which we want to predict.
        - numOfClasses: (int) number of class labels in our dataset.
    OUTPUT:
        - y_pred: (array) contains the probability for each class, and it will be helpful if
        we have metric like 'log loss'.
    '''
    len_y = len(y_test)
    y_pred = np.zeros((len_y, numOfClasses))
    for i in range(len_y):
        rand_probs = np.random.rand(1, numOfClasses)
        y_pred[i] = ((rand_probs/sum(sum(rand_probs)))[0])
    return y_pred
~~~
</p>
</details> 

<details><summary>Plot **Features Importance**</summary>
<p>
[**Result**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/3_Home%20Credit%20Loans/1_Start%20Here:%20A%20Gentle%20Introduction.html#Model-Interpretation:-Feature-Importances) 

[**Best Notebook**](https://www.kaggle.com/willkoehrsen/a-complete-introduction-and-walkthrough) 
~~~python
# Take the important features from the model.
feature_importance_values = rf.feature_importances_
feature_importance = pd.DataFrame({'feature': features, 'importance': feature_importance_values})

def plot_feature_importances(df, n = 10, threshold = None):
    """Plots n most important features. Also plots the cumulative importance if
    threshold is specified and prints the number of features needed to reach threshold cumulative importance.
    Intended for use with any tree-based feature importances. 
    
    Args:
        df (dataframe): Dataframe of feature importances. Columns must be "feature" and "importance".
    
        n (int): Number of most important features to plot. Default is 15.
    
        threshold (float): Threshold for cumulative importance plot. If not provided, no plot is made. Default is None.
        
    Returns:
        df (dataframe): Dataframe ordered by feature importances with a normalized column (sums to 1) 
                        and a cumulative importance column
    
    Note:
    
        * Normalization in this case means sums to 1. 
        * Cumulative importance is calculated by summing features from most to least important
        * A threshold of 0.9 will show the most important features needed to reach 90% of cumulative importance
    
    """
    plt.style.use('fivethirtyeight')
    
    # Sort features with most important at the head
    df = df.sort_values('importance', ascending = False).reset_index(drop = True)
    
    # Normalize the feature importances to add up to one and calculate cumulative importance
    df['importance_normalized'] = df['importance'] / df['importance'].sum()
    df['cumulative_importance'] = np.cumsum(df['importance_normalized'])
    
    plt.rcParams['font.size'] = 12
    
    # Bar plot of n most important features
    df.loc[:n, :].plot.barh(y = 'importance_normalized', 
                            x = 'feature', color = 'darkgreen', 
                            edgecolor = 'k', figsize = (12, 8),
                            legend = False, linewidth = 2)

    plt.xlabel('Normalized Importance', size = 18); plt.ylabel(''); 
    plt.title(f'{n} Most Important Features', size = 18)
    plt.gca().invert_yaxis()
    
    
    if threshold:
        # Cumulative importance plot
        plt.figure(figsize = (8, 6))
        plt.plot(list(range(len(df))), df['cumulative_importance'], 'b-')
        plt.xlabel('Number of Features', size = 16); plt.ylabel('Cumulative Importance', size = 16); 
        plt.title('Cumulative Feature Importance', size = 18);
        
        # Number of features needed for threshold cumulative importance
        # This is the index (will need to add 1 for the actual number)
        importance_index = np.min(np.where(df['cumulative_importance'] > threshold))
        
        # Add vertical line to plot
        plt.vlines(importance_index + 1, ymin = 0, ymax = 1.05, linestyles = '--', colors = 'red')
        plt.show();
        
        print('{} features required for {:.0f}% of cumulative importance.'.format(importance_index + 1, 
                                                                                  100 * threshold))
    
    return df
    
# Call the function
feature_importance_sorted = plot_feature_importance(feature_importance)
~~~
</p>
</details> 

</p>
</details> 

<details><summary style='font-size:18px;color:darkcyan'> **ML Explainability** </summary>
<p>
> **ML Explainability helps in:**
- Debugging
- Informing feature engineering
- Directing future data collection
- Informing human decision-making
- Building Trust

<details><summary> **Permutation Importance** </summary>
<p>
#### Fit a model
~~~python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('../input/fifa-2018-match-statistics/FIFA 2018 Statistics.csv')
y = (data['Man of the Match'] == "Yes")  # Convert from string "Yes"/"No" to binary
feature_names = [i for i in data.columns if data[i].dtype in [np.int64]]
X = data[feature_names]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
my_model = RandomForestClassifier(n_estimators=100,
                                  random_state=0).fit(train_X, train_y)
~~~

#### Apply Permuation Importance
~~~python
# Credits: https://www.kaggle.com/dansbecker/permutation-importance
import eli5
from eli5.sklearn import PermutationImportance

perm = PermutationImportance(my_model, random_state=1).fit(val_X, val_y)
eli5.show_weights(perm, feature_names = val_X.columns.tolist())

### NOTE:
# First Number: shows how much model performance decreased with a random shuffling 
# Second Number: The number after the ± measures how performance varied from one-reshuffling to the next.
# You'll occasionally see negative values for permutation importances. In those cases, the predictions on the shuffled (or noisy) data happened to be more accurate than the real data. This happens when the feature didn't matter (should have had an importance close to 0), but random chance caused the predictions on shuffled data to be more accurate. This is more common with small datasets, like the one in this example, because there is more room for luck/chance.
~~~
</p>
</details>


<details><summary> **Partial Dependance Plots** </summary>
<p>
[**Notebook**](https://www.kaggle.com/dansbecker/partial-plots) 
#### 1. Building a model.
~~~python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('../input/fifa-2018-match-statistics/FIFA 2018 Statistics.csv')
y = (data['Man of the Match'] == "Yes")  # Convert from string "Yes"/"No" to binary
feature_names = [i for i in data.columns if data[i].dtype in [np.int64]]
X = data[feature_names]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
tree_model = DecisionTreeClassifier(random_state=0, max_depth=5, min_samples_split=5).fit(train_X, train_y)
~~~

#### PDP for one feature
~~~python
from matplotlib import pyplot as plt
from pdpbox import pdp, get_dataset, info_plots

# Create the data that we will plot
pdp_goals = pdp.pdp_isolate(model=tree_model, dataset=val_X, model_features=feature_names, feature='Goal Scored')

# plot it
pdp.pdp_plot(pdp_goals, 'Goal Scored')
plt.show()
~~~

#### PDP for 2 features
~~~python
# Similar to previous PDP plot except we use pdp_interact instead of pdp_isolate and pdp_interact_plot instead of pdp_isolate_plot
features_to_plot = ['Goal Scored', 'Distance Covered (Kms)']
inter1  =  pdp.pdp_interact(model=tree_model, dataset=val_X, model_features=feature_names, features=features_to_plot)

pdp.pdp_interact_plot(pdp_interact_out=inter1, feature_names=features_to_plot, plot_type='contour', plot_pdp=True)
plt.show()
~~~
</p>
</details>


<details><summary> **SHAP** Values (One Row & All Features) </summary>
<p>
[**Notebook**](https://www.kaggle.com/dansbecker/shap-values) 
~~~python
# Your Code Here
import shap  # package used to calculate Shap values

data_for_prediction = val_X.iloc[0,:]  # use 1 row of data here. Could use multiple rows if desired

def patient_risk_factors(my_model, row):
    # Create object that can calculate shap values
    explainer = shap.TreeExplainer(my_model)
    shap_values = explainer.shap_values(row)
    shap.initjs()
    return shap.force_plot(explainer.expected_value[0], shap_values[0], row)

patient_risk_factors(my_model, data_for_prediction)
~~~
</p>
</details>

<details><summary> SHAP **Summary Plot** (All Rows & All Features)</summary>
<p>
[**Notebook**](https://www.kaggle.com/dansbecker/advanced-uses-of-shap-values) 
~~~python
import shap  # package used to calculate Shap values

# Create object that can calculate shap values
explainer = shap.TreeExplainer(my_model)

# calculate shap values. This is what we will plot.
# Calculate shap_values for all of val_X rather than a single row, to have more data for plot.
shap_values = explainer.shap_values(val_X)

# Make plot. Index of [1] is explained in text below.
shap.summary_plot(shap_values[1], val_X)
~~~
</p>
</details>

<details><summary> SHAP **Dependence Contribution Plot** (All Rows & One Feature)</summary>
<p>
[**Notebook**](https://www.kaggle.com/dansbecker/advanced-uses-of-shap-values) 
~~~python
import shap  # package used to calculate Shap values

# Create object that can calculate shap values
explainer = shap.TreeExplainer(my_model)

# calculate shap values. This is what we will plot.
shap_values = explainer.shap_values(X)

# make plot.
shap.dependence_plot('Ball Possession %', shap_values[1], X, interaction_index="Goal Scored")
~~~
</p>
</details>
</p>
</details>


</p>
</details>
## Binary Classification:
- [**Logistic Regression/SGDClassifier**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Logistic%20Regression.html) 
- [**Random Forest**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Random%20Forest.html) 
- [**LightGBM**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/LightGBM.html) 

## Multi-Class Classification:

## Regression:
- [**K Nearest Neighbors**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/KNN.html) 
- [**Decision Tree**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/Decision%20Tree.html)
- [**Random Forest**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/Random%20Forest.html) 


## Clustering:
- K-means
- [**AgglomerativeClustering**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Agglomerative%20Clustering.html) 
- [**DBSCAN**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/DBSCAN.html) 

[**<span style='font-size:28px;color:#333'>Multi-Label Classification</span>**](https://www.analyticsvidhya.com/blog/2017/08/introduction-to-multi-label-classification/) 
