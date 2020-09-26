<h1>Hyperparameter Optimization</h1>

<div style='width:1000px;margin:auto'>

<details><summary> <b style='font-size:20px'>GridSearchCV</b> </summary>
<p style="margin: 0">
<p>1) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/1_step-by-step-diabetes-classification-knn-detailed.html#Hyper-Parameter-optimization">Explanation of <b>GridSearch</b>.</a> <br>
2) <a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/2_KNN%20-%20Full%20Pipeline.html#Hyperparameter-Tunning-&amp;-Cross-Validation">Hyperparameter Tunning &amp; Cross validation</a> </p>
<pre><code>
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
</code></pre>
</p></details>

<details><summary> <b style='font-size:20px'>Randomized Search</b></summary><p>
<h4>NOTE:</h4>
<p><b>Reciprocal Distribution</b> is useful when you have no idea what the scale of the hyperparameter should be.</p>
<p><b>Exponential Distribution</b> is best when you know (more or less) what the scale of the hyperparameter should be.</p>
see more distributions from <a href="https://docs.scipy.org/doc/scipy/reference/stats.html">here</a><br>

<ul><details><summary> <b>MultiNomial</b> </summary><p><pre><code># Import Libraries
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
</code></pre>
</p></details>

<details><summary> <b>SVR</b> </summary><p><pre><code>from sklearn.model_selection import RandomizedSearchCV
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
</code></pre>
</p></details>

</ul></p></details>

<details><summary><b style='font-size:20px'>Bayesian Optimization</b> </summary><p><ul>

<details><summary> <b>Which parameters to optimize</b> </summary><p>
<img src="imgs/20200725-170244.png" alt="" />
</p></details>

<details><summary> <b>BayesianOptimization</b> </summary>
<pre><code>!pip install bayesian-optimization
from bayes_opt import BayesianOptimization
</code></pre>

<details><summary> <b>LogisticRegression</b> </summary><p><pre><code># Define LogisticRegression CV
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

    print(f"~&gt; Best parameters: {optimizer.max}")
    return optimizer.max['params']

# Run the optimization
best_params = optimize_lg(X_train, y_train)
</code></pre>
</p></details>

<details><summary><b> LinearSVC</b></summary><p><pre><code>def svc_cv(C, loss, data, targets):
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

    print(f"~&gt; Final Result: {optimizer.max}")

# Optimize
optimize_svc(X_train, y_train)
</code></pre>
</p></details>

<details><summary><b> Kernel SVM</b></summary><p><pre><code>def svc_cv(C, kernel, data, targets):
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

    print(f"~&gt; Final Result: {optimizer.max}")

# Optimize
optimize_svc(X_train, y_train)
</code></pre>
</p></details>

<details><summary> <b>RidgeClassifier</b> </summary><p><pre><code># Define Ridge CV
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

    print(f"~&gt; Best parameters: {optimizer.max}")

# Run the optimization
optimize_ridge(X, y)
</code></pre>
</p></details>

<details><summary> <b>LassoClassifier</b> </summary><p><pre><code>from sklearn.linear_models import Lasso

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

    print(f"~&gt; Best parameters: {optimizer.max}")

# Run the optimization
optimize_lasso(X, y)
</code></pre>
</p></details>

<details><summary> <b>Multi-nomial Naive Bayes</b> </summary><p><pre><code># CV Strategy
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

print(f"~&gt; Best Result: {optimizer.max}")
</code></pre>
</p></details>

<details><summary> <b>Gaussian Naive Bayes</b> </summary><p><pre><code># CV Strategy
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

print(f"~&gt; Best Result: {optimizer.max}")
</code></pre>
</p></details>

<details><summary><b> Decision Tree</b></summary><p><pre><code># CV Strategy
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
    print(f"~&gt; Best Result: {optimizer.max}")

optimize_dt(X_train, y_train)
</code></pre>
</p></details>

<details><summary> <b>XGBoostClassifier</b> </summary><p><pre><code># Importing
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
</code></pre>
</p></details>

<details><summary> <b>Stacking</b> </summary><p><pre><code>from mlxtend.classifier import StackingClassifier

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

print(f"~&gt; Final Result: {optimizer.max}")
</code></pre>
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

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Bayesian%20Optimization%20From%20Scratch/0_html/1_Bayesian%20Optimization.html">For <b>Sklearn Models</b></a></li>
</p></details>

<details><summary> <b>skopt</b></summary><ul>
<li><details><summary> <b>Random Forest</b></summary><p>
<pre><code>
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
</code></pre>
<pre><code>## Show the plot of iterations.
from skopt.plots import plot_convergence
plot_convergence(result)
</code></pre>
</p></details></li>
</ul></details>

<details><summary> <b>hyperopt</b></summary><ul>

<li><details><summary> <b>Random Forest</b></summary><p><pre><code>from functools import partial
from sklearn import ensemble, metrics, model_selection
from hyperopt import hp, fmin, tpe, Trials
from hyperopt.pyll.base import scope

def optimize(params, X, y):
    # initialize model with current paramters.
    model = ensemble.RandomForestClassifier(**params)

    # Initialize stratified k-fold.
    kf = model_selection.StratifiedKFold(n_splits=5)

    .
    . # see skopt part to know what to do in this part.
    . 

    return -1 * np.mean(accuracies)

if __name__ == "__main__":
    # Read the training data.
    df = pd.read_csv("...")

    X = ...
    y = ...

    # Define a parameters space.
    param_space = {
        # quniform gives round(uniform(low, high) / q) * q
        # We want int values for depth and estimators.
        "max_depth": scope.int(hp.quniform("max_depth", 1, 15, 1)),
        "n_estimators": scope.int(hp.quniform("n_estimators", 100, 1500, 1)),
        # choice chooses from a list of values.
        "criterion": hp.choice("criterion", ["gini", "entropy"]),
        # uniform chooses a value between two values.
        "max_features": hp.uniform("max_featuers", 0, 1)
    }

    # Partial function.
    optimization_function = partial(optimize, X=X, y=y)

    # Initialize trials to keep logging information.
    trials = Trials()

    # Run hyperopt.
    hopt = fmin(fn=optimization_function,
                space=param_space,
                algo=tpe.suggest,
                max_evals=15,
                trials=trials)
    print(hopt)
</code></pre>
</p></details></li>
</ul></details>

<details><summary> <b>Optuna</b></summary><ul>

<li><details><summary> <b>Random Forest</b></summary><p><pre><code>from functools import partial
from sklearn import ensemble, metrics, model_selection
import optuna

def optimize(trial, X, y):
    criterion = trail.suggest_categorical("criterion", ['gini', 'entropy'])
    n_estimators = trail.suggest_int("n_estimators", 100, 1500)
    max_depth  = trial.suggest_int("max_depth", 3, 15)
    max_features = trail.suggest_uniform('max_features', 0.01, 1.0)

    model = ensemble.RandomForestClassifier(
    			n_estimators=n_estimators,
    			max_depth=max_depth,
    			max_features=max_featuers,
    			criterion=criterion
    )
    
    # Initialize stratified k-fold.
    kf = model_selection.StratifiedKFold(n_splits=5)

    .
    . # see skopt part to know what to do in this part.
    . 

    return -1 * np.mean(accuracies)

if __name__ == "__main__":
    # Read the training data.
    df = pd.read_csv("...")

    X = ...
    y = ...
   
    optimization_function = partial(optimize, x=X, y=y)
   
    study = optuna.create_study(direction="minimize") # or "maximize"

    study.optimize(optimization_function, n_trials=15)
</code></pre>
</p></details></li>
</ul></details>

</ul></p></details>

</div>