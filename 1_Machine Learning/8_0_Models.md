<h1 id="mlmodels">ML Models</h1>

<div style='width:1000px;margin:auto'>

<details><summary style='font-size:18px;color:darkcyan'> <b>Important Functions</b> </summary>
<p>

<details><summary><b>Random Model</b></summary><p>
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
</p></details> 

<details><summary>Plot <b>Features Importance</b></summary>
<p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/3_Home%20Credit%20Loans/1_Start%20Here:%20A%20Gentle%20Introduction.html#Model-Interpretation:-Feature-Importances"><b>Result</b></a> </p>

<p><a href="https://www.kaggle.com/willkoehrsen/a-complete-introduction-and-walkthrough"><b>Best Notebook</b></a> </p>
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

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Engineering%20for%20Machine%20Learning/0_code/Section-03-Variable-Characteristics/03.8-Bonus-Machine-Learning-Algorithms-Overview.html" style='font-weight:bold'>Models Comparsion</a> </p></li><hr>


<details><summary><b style="font-size:25px">Binary Classification:</b></summary><p>

<ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Logistic%20Regression.html"><b>Logistic Regression/SGDClassifier</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Random%20Forest.html"><b>Random Forest</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/LightGBM.html"><b>LightGBM</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/BaggingClassifier.html"><b>Bagging Classifier</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Stacking.html"><b>Stacking</b></a> </li>

<li><details><summary><b>Linear SVM</b></summary><p>
<ul>
<li>A smaller "C" value leads to a wider street but more margin violations.</li>
<li>If you SVM model is overfitting, you can try to regularize it by reducing "C".</li>
<li>Unlike Logistic Regression, SVM classifier do not output probabilites for each class.</li>
<li>Make sure to set "dual = False", unless there are more features than training instances.</li>
</ul><pre><code>import numpy as np
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

iris = datasets.load_iris()
print(list(iris.keys()))
X = iris["data"][:, (2, 3)]
y = (iris["target"] == 2).astype(np.float64)

svm_clf = Pipeline([
    ("scaler", StandardScaler()),
    ("linear_svc", LinearSVC(C=1, loss="hinge"))
])

svm_clf.fit(X, y)
</code></pre>
<pre><code># For a huge dataset.
# Supports out-of-core learning.
from sklearn.linear_model import SGDClassifier

svm_clf = Pipeline([
    ("scaler", StandardScaler()),
    ("linear_svc", SGDClassifier(loss="hinge", alpha=1/(m*C)))
])

svm_clf.fit(X, y)
</code></pre>
</p></details></li>

<li><details><summary><b>Non-Linear SVM</b></summary><p>
<ul>
<li>A smaller "C" value leads to a wider street but more margin violations.</li>
<li>If you SVM model is overfitting, you can try to regularize it by reducing "C".</li>
<li>Unlike Logistic Regression, SVM classifier do not output probabilites for each class.</li>
<li>Make sure to set "dual = False", unless there are more features than training instances.</li>
</ul><pre><code>from sklearn.datasets import make_moons
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures

poly_svm_clf = Pipeline([
    ("poly_features", PolynomialFeatures(degree=3)),
    ("scaler", StandardScaler()),
    ("svm_clf", LinearSVC(C=10, loss="hinge"))
])

poly_svm_clf.fit(X, y)
</code></pre>
</p></details></li>

<li><details><summary><b>Polynomial Kernel SVM</b></summary><p>
<ul>
<li>A smaller "C" value leads to a wider street but more margin violations.</li>
<li>If you SVM model is overfitting, you can try to regularize it by reducing "C".</li>
<li>Unlike Logistic Regression, SVM classifier do not output probabilites for each class.</li>
<li>Make sure to set "dual = False", unless there are more features than training instances.</li>
<li><b>coef0</b> controls how much the model is influenced by high-degree polynomials versus low-degree polynomials.</li>
</ul><pre><code>from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import SVC

poly_kernel_svm_clf = Pipeline([
    ("scaler", StandardScaler()),
    ("svm_clf", SVC(kernel="poly", degree=3, coef0=1, C=5))
])

poly_kernel_svm_clf.fit(X, y)
</code></pre>
</p></details></li>
<li><details><summary><b>Gaussian RBF Kernel SVM</b></summary><p>
<ul>
<li>If you training set is very large, you end up with an equally large number of features.</li>
<li><b>gamma</b> acts like a regularization hyperparameter: if your model is overfitting, you should reduce it, and if it's underfitting, you should increase it (similar to C hyperparameter).</li>
</ul><pre><code>from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import SVC

rbf_kernel_svm_clf = Pipeline([
    ("scaler", StandardScaler()),
    ("svm_clf", SVC(kernel="rbf", gamma=5, C=0.001))
])

rbf_kernel_svm_clf.fit(X, y)
</code></pre>
</p></details></li>

<li><details><summary><b>RuleFit</b> [Skope-Rules]</summary><p>
<a href="./9_pipelines/demo_titanic.html"><b>Titanic Example</b></a>
</p></details></li>

<li><details><summary><b>Voting Classifier</b></summary><p>
<p><b>NOTE:</b> When all models can `predict_proba`, you can set voting to `soft`, otherwise set it to `hard`.</p>
<p>For `SVC` to turn on his `predict_proba`, set `probability` to True.</p><pre><code>from sklearn.datasets import make_moons
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = make_moons(n_samples=5000, noise=.1)
X = iris[0]
y = iris[1]

X_train, X_valid, y_train, y_valid = train_test_split(X, y, stratify=y, test_size=.2, random_state=42)

log_clf = LogisticRegression()
rf_clf  = RandomForestClassifier()
svm_clf = SVC(probability=True)

voting_clf = VotingClassifier([
        ("lr", log_clf),
        ("rf", rf_clf),
        ("svc", svm_clf)
], voting="hard")


for clf in (log_clf, rf_clf, svm_clf, voting_clf):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_valid)
    print(clf.__class__.__name__, accuracy_score(y_valid, y_pred))
</code></pre>
</p></details></li>

<li><details><summary><b>Bagging</b> and <b>Pasting</b></summary><p>
<ul>
<li><b>Pasting</b> is like `Bagging` but without bootstrapping, so to use it, set `bootstrap` to False.</li>
<li><b>Random Patches Method</b> Samples both training instances and features.</li>
<li><b>Random Subspaces Method</b> keeps all training instances (i.e. bootstrap=False and max_samples=1.0) but sampling features (i.e. bootstrap_features=True and/or max_features=smaller than 1.0)</li>
</ul><pre><code>from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

bag_clf = BaggingClassifier(DecisionTreeClassifier(), n_estimators=500,
                            max_samples=500, bootstrap=True, n_jobs=-1, oob_score=True)
bag_clf.fit(X_train, y_train)
y_pred = bag_clf.predict(X_valid)
print(accuracy_score(y_valid, y_pred))
print(bag_clf.oob_score_)
</code></pre>
</p></details></li>

<li><details><summary><b>Random Forest</b></summary><p><pre><code>from sklearn.ensemble import RandomForestClassifier

rf_clf = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, n_jobs=-1, oob_score=True)
rf_clf.fit(X_train, y_train)

y_pred = rf_clf.predict(X_valid)
print(accuracy_score(y_valid, y_pred))
print(rf_clf.oob_score_)
</code></pre>

<h4>Feature Importance</h4><pre><code>for name, score in zip(iris["feature_names"], rf_clf.feature_importances_):
    print(name, score)
</code></pre>
</p></details></li>
<li><details><summary><b>Extra-Trees</b></summary><p>
<p>In each tree, RF tries to choose the best feature to split on, but Extra-Trees chooses the features at random.</p><pre><code>from sklearn.ensemble import ExtraTreesClassifier

rf_clf = ExtraTreesClassifier(n_estimators=500, max_leaf_nodes=16, n_jobs=-1, bootstrap=True, oob_score=True)
rf_clf.fit(X_train, y_train)

y_pred = rf_clf.predict(X_valid)
print(accuracy_score(y_valid, y_pred))
print(rf_clf.oob_score_)
</code></pre>
</p></details></li>

<li><details><summary><b>AdaBoost</b></summary><p><pre><code>from sklearn.ensemble import AdaBoostClassifier

ada_clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                             n_estimators=200,
                             algorithm="SAMME.R",
                             learning_rate=.4)
ada_clf.fit(X_train, y_train)
y_pred = ada_clf.predict(X_valid)
print(accuracy_score(y_valid, y_pred))
</code></pre>
</p></details></li>

<li><details><summary><b>MultinomialNB</b></summary><p>
<b>MultinomialNB</b> is more suitable for text classification</b><pre><code>from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB(alpha=0.0, class_prior=[0.4, 0.6])
clf.fit(X_train, y_train)
y_pred = ada_clf.predict(X_valid)
print(accuracy_score(y_valid, y_pred))
</code></pre>
</p></details></li>

<li><details><summary><b>Average Ensemble</b></summary><p>
you always create folds before starting with ensembling.<pre><code># A class to choose the best weights for each model.
import numpy as np
from functools import partial
from scipy.optimize import fmin
from sklearn import metrics

class OptimizeAUC:
    """
    Class for optimizing AUC.
    This class is all you need to find best weights for
    any model and for any metric and for any types of predictions.
    With very small changes, this class can be used for optimization of
    weights in ensemble models of _any_ type of predictions
    """
    def __init__(self):
        self.coef_ = 0
        def _auc(self, coef, X, y):
            """
            This functions calulates and returns AUC.
            :param coef: coef list, of the same length as number of models
            :param X: predictions, in this case a 2d array
            :param y: targets, in our case binary 1d array
            """
            # multiply coefficients with every column of the array
            # with predictions.
            # this means: element 1 of coef is multiplied by column 1
            # of the prediction array, element 2 of coef is multiplied
            # by column 2 of the prediction array and so on!
            x_coef = X * coef
            # create predictions by taking row wise sum
            predictions = np.sum(x_coef, axis=1)
            # calculate auc score
            auc_score = metrics.roc_auc_score(y, predictions)
            # return negative auc
            return -1.0 * auc_score
        def fit(self, X, y):
            # remember partial from hyperparameter optimization chapter?
            loss_partial = partial(self._auc, X=X, y=y)
            # dirichlet distribution. you can use any distribution you want
            # to initialize the coefficients
            # we want the coefficients to sum to 1
            initial_coef = np.random.dirichlet(np.ones(X.shape[1]), size=1)
            # use scipy fmin to minimize the loss function, in our case auc
            self.coef_ = fmin(loss_partial, initial_coef, disp=True)
    def predict(self, X):
        # this is similar to _auc function
        x_coef = X * self.coef_
        predictions = np.sum(x_coef, axis=1)
        return predictions
</code></pre>
<pre><code># How to use it.
import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn import ensemble
from sklearn import linear_model
from sklearn import metrics
from sklearn import model_selection
# make a binary classification dataset with 10k samples
# and 25 features
X, y = make_classification(n_samples=10000, n_features=25)
# split into two folds (for this example)
xfold1, xfold2, yfold1, yfold2 = model_selection.train_test_split(
    X,
    y,
    test_size=0.5,
    stratify=y
)
# fit models on fold 1 and make predictions on fold 2
# we have 3 models:
# logistic regression, random forest and xgboost
logreg = linear_model.LogisticRegression()
rf = ensemble.RandomForestClassifier()
xgbc = xgb.XGBClassifier()
# fit all models on fold 1 data
logreg.fit(xfold1, yfold1)
rf.fit(xfold1, yfold1)
xgbc.fit(xfold1, yfold1)
# predict all models on fold 2
# take probability for class 1
pred_logreg = logreg.predict_proba(xfold2)[:, 1]
pred_rf = rf.predict_proba(xfold2)[:, 1]
pred_xgbc = xgbc.predict_proba(xfold2)[:, 1]

# create an average of all predictions
# that is the simplest ensemble
avg_pred = (pred_logreg + pred_rf + pred_xgbc) / 3
# a 2d array of all predictions
fold2_preds = np.column_stack((
    pred_logreg,
    pred_rf,
    pred_xgbc,
    avg_pred
))
# calculate and store individual AUC values
aucs_fold2 = []
for i in range(fold2_preds.shape[1]):
    auc = metrics.roc_auc_score(yfold2, fold2_preds[:, i])
    aucs_fold2.append(auc)
print(f"Fold-2:
 LR AUC = {aucs_fold2[0]}")
print(f"Fold-2:
 RF AUC = {aucs_fold2[1]}")
print(f"Fold-2:
 XGB AUC = {aucs_fold2[2]}")
print(f"Fold-2:
 Average Pred AUC = {aucs_fold2[3]}")
# now we repeat the same for the other fold
# this is not the ideal way, if you ever have to repeat code,
# create a function!
# fit models on fold 2 and make predictions on fold 1
logreg = linear_model.LogisticRegression()
rf = ensemble.RandomForestClassifier()
xgbc = xgb.XGBClassifier()
logreg.fit(xfold2, yfold2)
rf.fit(xfold2, yfold2)
xgbc.fit(xfold2, yfold2)
pred_logreg = logreg.predict_proba(xfold1)[:, 1]
pred_rf = rf.predict_proba(xfold1)[:, 1]
pred_xgbc = xgbc.predict_proba(xfold1)[:, 1]
avg_pred = (pred_logreg + pred_rf + pred_xgbc) / 3
fold1_preds = np.column_stack((
    pred_logreg,
    pred_rf,
    pred_xgbc,
    avg_pred
))

aucs_fold1 = []
for i in range(fold1_preds.shape[1]):
    auc = metrics.roc_auc_score(yfold1, fold1_preds[:, i])
    aucs_fold1.append(auc)
print(f"Fold-1:
 LR AUC = {aucs_fold1[0]}")
print(f"Fold-1:
 RF AUC = {aucs_fold1[1]}")
print(f"Fold-1:
 XGB AUC = {aucs_fold1[2]}")
print(f"Fold-1:
 Average prediction AUC = {aucs_fold1[3]}")
# find optimal weights using the optimizer
opt = OptimizeAUC()
# dont forget to remove the average column
opt.fit(fold1_preds[:, :-1], yfold1)
opt_preds_fold2 = opt.predict(fold2_preds[:, :-1])
auc = metrics.roc_auc_score(yfold2, opt_preds_fold2)
print(f"Optimized AUC, Fold 2 = {auc}")
print(f"Coefficients = {opt.coef_}")
opt = OptimizeAUC()
opt.fit(fold2_preds[:, :-1], yfold2)
opt_preds_fold1 = opt.predict(fold1_preds[:, :-1])
auc = metrics.roc_auc_score(yfold1, opt_preds_fold1)
print(f"Optimized AUC, Fold 1 = {auc}")
print(f"Coefficients = {opt.coef_}")
</code></pre>
</p></details></li>

</ul></details>

<details><summary><b style="font-size:25px">Multi-Class Classification:</b></summary></p>
<p><b>NOTE:</b> Sklearn detects when you try to use a binary classification algorithm for a multi-class classification task, and it automatically runs OvA (except for SVM classifiers for which it uses OvO).</p>
<details><summary><b>One Vs. All</b></summary></p><pre><code>from sklearn.multiclass import OneVsAllClassifier

ova_clf = OneVsAll(SVC(random_state=42))
ova_clf.fit(X_train, y_train)
</code></pre>
</p></details>

<details><summary><b>One Vs. One</b></summary></p><pre><code>from sklearn.multiclass import OneVsOneClassifier

ovo_clf = OneVsOneClassifier(SGDClassifier(random_state=42))
ovo_clf.fit(X_train, y_train)
ovo_clf.predict([some_digit])
</code></pre>
</p></details>

</p></details>

<details><summary><b style="font-size:25px">Regression:</b></summary><p><ul>

<li><details><summary><b>Linear Regression</b></summary><p><pre><code># Fast when we have large training instance.
# Slow when we have large numer of features.
# Doesn't require scaling!!
from sklearn.linear_models import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, y)

print(lin_reg.intercept_)
print(lin_reg.coef_)
</code></pre>
</p></details></li>

<li><details><summary><b>SGD Regressor</b></summary><p><pre><code># Fast when we have large training instances.
# Fast when we have large number of features too!
# Change the thetas at each instance.
# gives a better thetas than GD, but not the best!
# Requires Scaling!!
from sklearn.linear_model import SGDRegressor

sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3, penalty=None, eta0=0.1)
sgd_reg.fit(X, y.ravel())
sgd_reg.intercept_, sgd_reg.coef_
</code></pre>

<h4>SGD with Early Stopping</h4><pre><code>from sklearn.base import clone
from sklearn.preprocessing import StandardScaler

# Prepare the data.
poly_scaler = Pipeline([
    ("poly_features", PolynomialFeatures(degree=90, include_bias=False)),
    ("std_scaler", StandardScaler())
])
X_train_poly_scaled = poly_scaler.fit_transform(X_train)
X_valid_poly_scaled = poly_scaler.transform(X_valid)

# Note: warm_start=True, when fit() method is called, it just continues training
# where it left off instead of restarting from scratch.
sgd_reg = SGDRegressor(max_iter=1, tol=-np.infty, warm_start=True,
                       penalty=None, learning_rate="constant", eta0=0.0005)

minimum_valid_error = float("inf")
best_epoch          = None
best_model          = None

for epoch in range(1000):
    sgd_reg.fit(X_train_poly_scaled, y_train)   # continues where it left off.
    y_valid_preds = sgd_reg.predict(X_valid_poly_scaled)
    valid_error   = mean_squared_error(y_valid, y_valid_preds)

    if valid_error &lt; minimum_valid_error:
        minimum_valid_error, best_epoch, best_model = valid_error, epoch, clone(sgd_reg)
</code></pre>
</p></details></li>

<li><details><summary><b>Polynomial Regressor</b></summary><p><pre><code># Create the polynomial features.
# WATCH THE NUMBER OF FEATURES = (n + d)!/d! * n!
# where n = number of features.
# where d = degree.

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

poly_model = Pipeline([
        ("poly_features", PolynomialFeatures(degree=10, include_bias=False)),
        ("lin_reg", LinearRegression())
])

poly_model.fit(X, y)
</code></pre>
</p></details></li>

<li><details><summary><b>Ridge Regressor</b> [L2 Regulaizer]</summary><p>
<p><b>NOTE:</b> Requires Scalling and you can make it polynomial as Linear Regression.</p><pre><code># Also called "Tikhonov Regularization", L2.
# if alpha = 0, the Ridge Regression is just a Linear Regression.
# if alpha = v.large, then all weights end up v.close to zero.
# 1. Ridge using Closed-form solution.
from sklearn.linear_model import Ridge

# you can use solver="sag" too.
ridge_reg = Ridge(alpha=1, solver="cholesky", normalize=True)
ridge_reg.fit(X, y)

# 2. Ridge using Gradient Descent.
from sklearn.linear_model import SGDRegressor

sgd_reg = SGDRegressor(penalty="l2")
sgd_reg.fit(X, y.ravel())
sgd_reg.predict([[1.5]])
</code></pre>
</p></details></li>


<li><details><summary><b>Lasso Regressor</b> [L1 Regulaizer]</summary><p>
<p><b>NOTE:</b> Requires Scalling and you can make it polynomial as Linear Regression.</p><pre><code># 1. Lasso using Closed-form solution.
from sklearn.linear_model import Lasso

lasso_reg = Lasso(alpha=0.1)
lasso_reg.fit(X, y)
lasso_reg.predict([[1.5]])

# 2. Ridge using Gradient Descent.
from sklearn.linear_model import SGDRegressor

sgd_reg = SGDRegressor(penalty="l1")
sgd_reg.fit(X, y.ravel())
sgd_reg.predict([[1.5]])
</code></pre>
</p></details></li>

<li><details><summary><b>Elastic Net</b> [L1 + L2 Regulaizer]</summary><p>
<p><b>NOTE:</b> Requires Scalling and you can make it polynomial as Linear Regression.</p><pre><code># when r = 0, Elastic Net = Ridge Regression.
# when r = 1, Elastic Net = Lasso Regression.
# 1. ElasticNet using Closed-form solution.
from sklearn.linear_model import ElasticNet

elastic_net = ElasticNet(alpha=.1, l1_ratio=.5)
elastic_net.fit(X, y)
elastic_net.predict([[1.5]])
</code></pre>
</p></details></li>

<li><details><summary><b>RuleFit</b></summary><p>
The algorithm can be used for predicting an output vector y given an input matrix X. In the first step a tree ensemble is generated with gradient boosting. The trees are then used to form rules, where the paths to each node in each tree form one rule. A rule is a binary decision if an observation is in a given node, which is dependent on the input features that were used in the splits. The ensemble of rules together with the original input features are then being input in a L1-regularized linear model, also called Lasso, which estimates the effects of each rule on the output target but at the same time estimating many of those effects to zero.<pre><code># pip install git+git://github.com/christophM/rulefit.git

# TRAIN the Model.
import numpy as np
import pandas as pd

from rulefit import RuleFit

boston_data = pd.read_csv("boston.csv", index_col=0)

y = boston_data.medv.values
X = boston_data.drop("medv", axis=1)
features = X.columns
X = X.as_matrix()

rf = RuleFit()
rf.fit(X, y, feature_names=features)
</code></pre><pre><code># If you want to have influence on the tree generator you can pass the generator as argument:
from sklearn.ensemble import GradientBoostingRegressor
gb = GradientBoostingRegressor(n_estimators=500, max_depth=10, learning_rate=0.01)
rf = RuleFit(gb)

rf.fit(X, y, feature_names=features)
</code></pre><pre><code># Predict:
rf.predict(X)

# Inspect Rules:
rules = rf.get_rules()

rules = rules[rules.coef != 0].sort_values("support", ascending=False)
rules.head()
</code></pre>
You can create new features with these rules, and then apply linear models or other models and see the result.
</p></details></li>

<li><details><summary><b>Linear SVM</b></summary><p>
<ul>
<li>A smaller "C" value leads to a wider street but more margin violations.</li>
<li>If you SVM model is overfitting, you can try to regularize it by reducing "C".</li>
<li>Unlike Logistic Regression, SVM classifier do not output probabilites for each class.</li>
<li>Make sure to set "dual = False", unless there are more features than training instances.</li>
</ul><pre><code>from sklearn.svm import LinearSVR

svm_reg = LinearSVR(epsilon=1.5)
svm_reg.fit(X, y)
</code></pre>
</p></details></li>

<li><details><summary><b>Kernel SVM</b></summary><p>
<ul>
<li>A smaller "C" value leads to a wider street but more margin violations.</li>
<li>If you SVM model is overfitting, you can try to regularize it by reducing "C".</li>
<li>Unlike Logistic Regression, SVM classifier do not output probabilites for each class.</li>
<li>Make sure to set "dual = False", unless there are more features than training instances.</li>
</ul><pre><code>from sklearn.svm import SVR

svm_poly_reg = SVR(kernel="poly", degree=2, C=100, epsilon=.1)
svm_poly_reg.fit(X, y)
</code></pre>
</p></details></li>

<li><details><summary><b>Gradient Boosting</b></summary><p><pre><code># GBDT with early stopping but run all the iterations.
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import metrics

gbrt = GradientBoostingRegressor(max_depth=2, n_estimators=200)
gbrt.fit(X_train, y_train)

errors = [metrics.mean_squared_error(y_valid, y_pred)
            for y_pred in gbrt.staged_predict(X_valid)]
bst_n_estimators = np.argmin(errors)
print(bst_n_estimators)

gbrt_best = GradientBoostingRegressor(max_depth=2, n_estimators=bst_n_estimators)
gbrt_best.fit(X_train, y_train)
y_pred = gbrt_best.predict(X_valid)
print(metrics.mean_absolute_error(y_valid, y_pred))
</code></pre>
<pre><code># Early Stopping but breaks when there's no improvment.
gbrt = GradientBoostingRegressor(max_depth=2, warm_start=True)

min_valid_error = float("inf")
error_going_up  = 0

for n_estimators in range(1, 120):
    gbrt.n_estimators = n_estimators
    gbrt.fit(X_train, y_train)
    y_pred = gbrt.predict(X_valid)
    valid_error = metrics.mean_squared_error(y_valid, y_pred)

    if valid_error &lt; min_valid_error:
        min_valid_error, error_going_up = valid_error, 0
    else:
        error_going_up += 1
        if error_going_up == 5:
            break   # Early Stopping
</code></pre>
</p></details></li>

<li><details><summary><b>XGBoost</b></summary><p><pre><code>import xgboost 

xgb_reg = xgboost.XGBRegressor(n_estimators=200, max_depth=4)
xgb_reg.fit(X_train, y_train,
            eval_set=[(X_train, y_train), (X_valid, y_valid)],
            early_stopping_rounds=200)
y_pred = xgb_reg.predict(X_valid)
print(metrics.mean_absolute_error(y_valid, y_pred))
</code></pre>
</p></details></li>

<li><details><summary><b>Stacking</b></summary><p><pre><code>X_val_predictions = np.empty((len(X_val), len(estimators)), dtype=np.float32)

for index, estimator in enumerate(estimators):
    X_val_predictions[:, index] = estimator.predict(X_val)

# Meta Model
rnd_forest_blender = RandomForestClassifier(n_estimators=200, oob_score=True, random_state=42)
rnd_forest_blender.fit(X_val_predictions, y_val)

# Predictions
X_test_predictions = np.empty((len(X_test), len(estimators)), dtype=np.float32)

for index, estimator in enumerate(estimators):
    X_test_predictions[:, index] = estimator.predict(X_test)

y_pred = rnd_forest_blender.predict(X_test_predictions)
</code></pre>
</p></details></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/KNN.html"><b>K Nearest Neighbors</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/Decision%20Tree.html"><b>Decision Tree</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/Random%20Forest.html"><b>Random Forest</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/BaggingRegressor.html"><b>Bagging Regressor</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Stacking.html"><b>Stacking</b></a> </li>

<li>Regression Splines - NOT COMPLETE</li>
</ul></details>

<details><summary><b style="font-size:25px">Clustering:</b></summary><p><ul>

<li><details><summary>K-Means</summary><p>
<a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/KMeans.html"><b>K-means</b></a>

<h4>Beside Elbow method, we can use silhouette coefficient too</h4>
<p>The silhouette coefficient is used when the ground-truth about the dataset is unknown, instead computing the density of clusters produced by the model. A silhouette score can then be calculated by averaging the silhouette coefficient for each sample, computed as the difference between the average intracluster distance and the mean nearest-cluster distance for each sample, normalized by the maximum value.<br><br>
This produces a score between 1 and -1, where 1 is highly dense clusters, -1 is completely incorrect clustering, and values near zero indicate overlapping clusters. The higher the score the better, because the clusters are denser and more separate. Negative values imply that samples have been assigned to the wrong cluster, and positive
values mean that there are discrete clusters. The scores can then be plotted to display a measure of how close each point in one cluster is to points in the neighboring clusters.</p><pre><code># silhouette = (b - a) / max(a, b)
# a = mean distance to the other instances in the same cluster.
# b = mean nearest-cluster distance.
# silhouette varies from -1 to +1, +1 means the instance is well inside its own cluster and far from othe clusters, and 0 means it's close to a cluster boundary, and -1 means that the instance may have been assigned to the wrong cluster.
# Visualize silhouette coef. for different k (n of clusters).
# The k with the larger silhouette is the best.
from sklearn.metrics import silhouette_score

silhouette_scores = [silhouette_score(X, model.labels_)
                     for model in kmeans_per_k[1:]]

# Visualize
plt.figure(figsize=(8, 3))
plt.plot(range(2, 10), silhouette_scores, "bo-")
plt.xlabel("$k$", fontsize=14)
plt.ylabel("Silhouette score", fontsize=14)
plt.axis([1.8, 8.5, 0.55, 0.7])
save_fig("silhouette_score_vs_k_plot")
plt.show()
</code></pre>
<pre><code>from sklearn.cluster import KMeans
from yellowbrick.cluster import SilhouetteVisualizer

# Instantiate the clustering model and visualizer
visualizer = SilhouetteVisualizer(KMeans(n_clusters=6))
visualizer.fit(docs)
visualizer.poof()
</code></pre>

<h4>Elbow Methods using Yellowbrick</h4><pre><code>from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
# Instantiate the clustering model and visualizer
visualizer = KElbowVisualizer(KMeans(), metric='silhouette', k=[4,10])
visualizer.fit(docs)
visualizer.poof()
</code></pre>
</p></details></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Agglomerative%20Clustering.html"><b>AgglomerativeClustering</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/DBSCAN.html"><b>DBSCAN</b></a> </li>
</ul></details>

<details><summary><b style='font-size:27px;'>Auto ML</b></summary><p><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/auto-sklearn.html#auto-sklearn"><b><span style='color:#333'>Auto-Sklearn</span></b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/Titanic_Kaggle.html#Data-Analysis-using-TPOT"><b><span style='color:#333'>TPOT</span></b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/automl_binary_classification_product_backorders.html#H2O-AutoML-Binary-Classification-Demo"><b><span style='color:#333'>H2O</span></b></a></li>

</ul></p></details>

<p><a href="https://www.analyticsvidhya.com/blog/2017/08/introduction-to-multi-label-classification/"><b><span style='font-size:25px;color:#333'>Multi-Label Classification</span></b></a> </p>

<details><summary><b style="font-size:25px">Semi-Supervised Learning Models</b></summary><ul>

<li><details><summary><b>Gaussian Mixture</b></summary><pre><code>class sklearn.mixture.GaussianMixture(n_components=1, *, covariance_type='full', tol=0.001, reg_covar=1e-06, max_iter=100, n_init=1, init_params='kmeans', weights_init=None, means_init=None, precisions_init=None, random_state=None, warm_start=False, verbose=0, verbose_interval=10)[source]
</code></pre>
</details></li>

<li><details><summary><b>Self-Learning</b></summary>
Read <b>master ML book</b> - Page: 87<pre><code>nb_samples = X.shape[0]
nb_labeled = 20
nb_unlabeled = nb_samples - nb_labeled
nb_unlabeled_samples = 2
X_train = X[:nb_labeled]
Y_train = Y[:nb_labeled]
X_unlabeled = X[nb_labeled:]
</code></pre>
<pre><code>import numpy as np
from sklearn.naive_bayes import GaussianNB
while X_train.shape[0] &lt;= nb_samples:
    nb = GaussianNB()
    nb.fit(X_train, Y_train)
    if X_train.shape[0] == nb_samples:
        break
    probs = nb.predict_proba(X_unlabeled)
    top_confidence_idxs = np.argsort(np.max(probs, axis=1)).astype(np.
    int64)[::-1]
    selected_idxs = top_confidence_idxs[0:nb_unlabeled_samples]
    X_new_train = X_unlabeled[selected_idxs]
    Y_new_train = nb.predict(X_new_train)
    X_train = np.concatenate((X_train, X_new_train), axis=0)
    Y_train = np.concatenate((Y_train, Y_new_train), axis=0)
    X_unlabeled = np.delete(X_unlabeled, selected_idxs, axis=0)
</code></pre>
</details></li>

<li><details><summary><b>Co-Training</b></summary>

</details></li>

<li><details><summary><b>Contrastive Pessimistic Likelihood Estimation (CPLE)</b></summary>
<p>Read page: <b>104</b> - Book: <b>Mastering Machine Learning Algorithms</b> [Expert Insight]
<pre><code>from sklearn.datasets import load_digits
import numpy as np

X_a, Y_a = load_digits(return_X_y=True)
X = np.vstack((X_a[Y_a == 0], X_a[Y_a == 1]))
Y = np.vstack((np.expand_dims(Y_a, axis=1)[Y_a==0], np.expand_dims(Y_a, axis=1)[Y_a==1]))

nb_samples = X.shape[0]
nb_dimensions = X.shape[1]
nb_unlabeled = 150
Y_true = np.zeros((nb_unlabeled,))

unlabeled_idx = np.random.choice(np.arange(0, nb_samples, 1), replace=False, size=nb_unlabeled)
Y_true = Y[unlabeled_idx].copy()
Y[unlabeled_idx] = -1
</code></pre>

<pre><code>from sklearn.linear_model import LogisticRegression

lr_test = LogisticRegression(solver="lbfgs",
                             max_iter=10_000,
                             multi_class="auto",
                             n_jobs=-1,
                             random_state=1000)
lr_test.fit(X[Y.squeeze() != -1], Y[Y.squeeze() != -1].squeeze())
unlabeled_score = lr_test.score(X[Y.squeeze() == -1], Y_true)
# 0.573333333333
</code></pre>

<pre><code>from sklearn.model_selection import cross_val_score

total_cv_scores = cross_val_score(LogisticRegression(solver="lbfgs", max_iter=10_000, multi_class="auto", random_state=1000), X, Y.squeeze(), cv=10, n_jobs=-1)

print(total_cv_scores)
</code></pre>

<pre><code># Implement CPLE
lr = LogisticRegression(solver="lbfgs", max_iter=10_000,
multi_class="auto",
random_state=1000)

q0 = np.random.uniform(0, 1, size=nb_unlabeled)
trh = np.vectorize(lambda x: 0.0 if x &lt; 0.5 else 1.0)
</code></pre>

<pre><code>def weighted_log_loss(yt, p, w=None, eps=1e-15):
    if w is None:
        w_t = np.ones((yt.shape[0], 2))
    else:
        w_t = np.vstack((w, 1.0 - w)).T
    Y_t = np.vstack((1. - yt.squeeze(), yt.squeeze())).T
    L_t = np.sum(w_t * Y_t * np.log(np.clip(p, eps, 1. - eps)), axis=1)
    return np.mean(L_t)
</code></pre>

<pre><code>def build_dataset(q):
    Y_unlabeled = trh(q)

    X_n = np.zeros((nb_samples, nb_dimensions))
    X_n[0:nb_samples - nb_unlabeled] = X[Y.squeeze() != -1]
    X_n[nb_samples - nb_unlabeled:] = X[Y.squeeze() == -1]

    Y_n = np.zeros((nb_samples, 1))
    Y_n[0:nb_samples - nb_unlabeled] = Y[Y.squeeze() != -1]
    Y_n[nb_samples - nb_unlabeled:] = np.expand_dims(Y_unlabeled, axis=1)
    return X_n, Y_n


def log_likelihood(q):
    X_n, Y_n = build_dataset(q)
    Y_soft = trh(q)
    lr.fit(X_n, Y_n.squeeze())
    p_sup = lr.predict_proba(X[Y.squeeze() != -1])
    p_semi = lr.predict_proba(X[Y.squeeze() == -1])

    l_sup = weighted_log_loss(Y[Y.squeeze() != -1], p_sup)
    l_semi = weighted_log_loss(Y_soft, p_semi, q)

    return l_semi - l_sup
</code></pre>

<pre><code>from scipy.optimize import fmin_bfgs
q_end = fmin_bfgs(f=log_likelihood, x0=q0, maxiter=1000, disp=False)

X_n, Y_n = build_dataset(q_end)

final_semi_cv_scores = cross_val_score(
LogisticRegression(solver="lbfgs", max_iter=10000, multi_
class="auto", random_state=1000),
X_n, Y_n.squeeze(), cv=10, n_jobs=-1)
print(final_semi_cv_scores)

# [0.97297297 0.86486486 0.94594595 0.86486486 0.89189189 0.88571429
# 0.48571429 0.91428571 0.88571429 0.48571429]
</code></pre>
</details></li>

<li><details><summary><b>Semi-Supervised Support Vector Machines (S3VM)</b></summary>

</details></li>

<li><details><summary><b>Transductive Support Vector Machines (TSVM)</b></summary>

</details></li>

</ul></details>

</div>