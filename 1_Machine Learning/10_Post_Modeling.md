<h1 style='color:darkcyan'>8. Interpretability</h1>

<div style='width:1000px;margin:auto'>
<blockquote>
  <p><b>ML Explainability helps in:</b><br></p>
  <ul>
<li>Debugging</li>

<li>Informing feature engineering</li>

<li>Directing future data collection</li>

<li>Informing human decision-making</li>

<li>Building Trust</li>
</ul>
</blockquote>

<p><a href="./10_interpretability/03_Model_Interpretability_Blog_Post.html"><b>Blog Post</b> [Must Read]</a></p>

<details><summary> <b>Permutation Importance</b> </summary>
<p>
<h4> Fit a model</h4>
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

<h4> Apply Permuation Importance</h4>
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
</p></details>


<details><summary> <b>Partial Dependance Plots</b> (PDP)</summary><p>
<p><a href="./10_interpretability/03_Model_Interpretability_Blog_Post.html#PDP-and-ICE-plots"><b>PDP plots</b></a></p>

<p><a href="https://www.kaggle.com/dansbecker/partial-plots"><b>Notebook</b></a> </p>
<h4> 1. Building a model.</h4>
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

<h4> PDP for one feature</h4>
~~~python
from matplotlib import pyplot as plt
from pdpbox import pdp, get_dataset, info_plots

# Create the data that we will plot
pdp_goals = pdp.pdp_isolate(model=tree_model, dataset=val_X, model_features=feature_names, feature='Goal Scored')

# plot it
pdp.pdp_plot(pdp_goals, 'Goal Scored')
plt.show()
~~~

<h4> PDP for 2 features</h4>
~~~python
# Similar to previous PDP plot except we use pdp_interact instead of pdp_isolate and pdp_interact_plot instead of pdp_isolate_plot
features_to_plot = ['Goal Scored', 'Distance Covered (Kms)']
inter1  =  pdp.pdp_interact(model=tree_model, dataset=val_X, model_features=feature_names, features=features_to_plot)

pdp.pdp_interact_plot(pdp_interact_out=inter1, feature_names=features_to_plot, plot_type='contour', plot_pdp=True)
plt.show()
~~~
</p></details>

<details><summary> <b>Individual Conditional Expectation</b> (ICE)</summary><p>
<p><a href="./10_interpretability/03_Model_Interpretability_Blog_Post.html#PDP-and-ICE-plots"><b>ICE & Centered ICE plots</b></a></p>

</p></details>

<details><summary> <b>Accumulated Local Effects</b> (ALE)</summary><p>
<b>NOTE:</b> Read Interpretable Machine Learning - page: 125
```
# install the library.
!pip install alepython
```

```
from alepython import ale_plot

model = RandomForestRegressor(n_estimators=20, bootstrap=True)
model.fit(X, y)

# Create First-Order of ALE plots.
ale_plot(model,
	     X,
	     X.columns[:1],
	     bins=20,
	     monte_carlo=True,
	     monte_carlo_rep=100,
	     monte_carlo_ratio=0.6)
```

```
# Create Second-Order ALE plot.
ale_plot(model, X, X.columns[:2], bins=10)
```
</p></details>

<details><summary> <b>Local Interpretable Model-agnostic Explanations</b> (LIME)</summary><p>
<b>NOTE:</b> Read Interpretable Machine Learning - page: 168

<p><a href="./10_interpretability/03_Model_Interpretability_Blog_Post.html#LIME"><b>LIME Code</b></a></p>

</p></details>


<details><summary> <b>SHAP</b> Values (One Row & All Features) </summary>
<p>
<p><a href="https://www.kaggle.com/dansbecker/shap-values"><b>Notebook</b></a> </p>
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
</p></details>


<details><summary> SHAP <b>Summary Plot</b> (All Rows & All Features)</summary><p>
<p><a href="https://www.kaggle.com/dansbecker/advanced-uses-of-shap-values"><b>Notebook</b></a> </p>
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
</p></details>

<details><summary> SHAP <b>Dependence Contribution Plot</b> (All Rows & One Feature)</summary>
<p>
<p><a href="https://www.kaggle.com/dansbecker/advanced-uses-of-shap-values"><b>Notebook</b></a> </p>
~~~python
import shap  # package used to calculate Shap values

# Create object that can calculate shap values
explainer = shap.TreeExplainer(my_model)

# calculate shap values. This is what we will plot.
shap_values = explainer.shap_values(X)

# make plot.
shap.dependence_plot('Ball Possession %', shap_values[1], X, interaction_index="Goal Scored")
~~~
</p></details>

<details><summary> <b>Different Interpretability techs.</b> using <b>RF</b> </summary><p>
<li><a href="./9_pipelines/lesson2-rf_interpretation.html"><b>notebook</b></a></li>
</p></details>

<details><summary> <b>Learning Curves</b> </summary><p>
<b>NOTE: Things to change:</b> <br>
- Model.<br>
- Hyperparameter.<br>
- Metric.<br>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Machine%20Learning%20Engineer%20Nano-degree/1_Model%20Selection/home/boston_housing.html#Learning-Curves"><b>Credits</b></a> </p>
~~~python
def ModelLearning(X, y):
    """ Calculates the performance of several models with varying sizes of training data.
        The learning and testing scores for each model are then plotted. """
    
    # Create 10 cross-validation sets for training and testing
    cv = ShuffleSplit(X.shape[0], n_iter = 10, test_size = 0.2, random_state = 0)

    # Generate the training set sizes increasing by 50
    train_sizes = np.rint(np.linspace(1, X.shape[0]*0.8 - 1, 9)).astype(int)

    # Create the figure window
    fig = plt.figure(figsize=(10,7))

    # Create three different models based on max_depth
    for k, depth in enumerate([1,3,6,10]):
        
        # Create a Decision tree regressor at max_depth = depth
        regressor = DecisionTreeRegressor(max_depth = depth)

        # Calculate the training and testing scores
        sizes, train_scores, test_scores = curves.learning_curve(regressor, X, y, \
            cv = cv, train_sizes = train_sizes, scoring = 'r2')
        
        # Find the mean and standard deviation for smoothing
        train_std = np.std(train_scores, axis = 1)
        train_mean = np.mean(train_scores, axis = 1)
        test_std = np.std(test_scores, axis = 1)
        test_mean = np.mean(test_scores, axis = 1)

        # Subplot the learning curve 
        ax = fig.add_subplot(2, 2, k+1)
        ax.plot(sizes, train_mean, 'o-', color = 'r', label = 'Training Score')
        ax.plot(sizes, test_mean, 'o-', color = 'g', label = 'Testing Score')
        ax.fill_between(sizes, train_mean - train_std, \
            train_mean + train_std, alpha = 0.15, color = 'r')
        ax.fill_between(sizes, test_mean - test_std, \
            test_mean + test_std, alpha = 0.15, color = 'g')
        
        # Labels
        ax.set_title('max_depth = %s'%(depth))
        ax.set_xlabel('Number of Training Points')
        ax.set_ylabel('Score')
        ax.set_xlim([0, X.shape[0]*0.8])
        ax.set_ylim([-0.05, 1.05])
    
    # Visual aesthetics
    ax.legend(bbox_to_anchor=(1.05, 2.05), loc='lower left', borderaxespad = 0.)
    fig.suptitle('Decision Tree Regressor Learning Performances', fontsize = 16, y = 1.03)
    fig.tight_layout()
    fig.show() 
~~~


<h4>2. More General Function from <a href='https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html#sphx-glr-auto-examples-model-selection-plot-learning-curve-py'>Sklearn</a></h4>
~~~python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit


def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                        n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    """
    Generate a simple plot of the test and training learning curve.

    Parameters
    ----------
    estimator : object type that implements the "fit" and "predict" methods
        An object of that type which is cloned for each validation.

    title : string
        Title for the chart.

    X : array-like, shape (n_samples, n_features)
        Training vector, where n_samples is the number of samples and
        n_features is the number of features.

    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Target relative to X for classification or regression;
        None for unsupervised learning.

    ylim : tuple, shape (ymin, ymax), optional
        Defines minimum and maximum yvalues plotted.

    cv : int, cross-validation generator or an iterable, optional
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:
          - None, to use the default 3-fold cross-validation,
          - integer, to specify the number of folds.
          - :term:`CV splitter`,
          - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : int or None, optional (default=None)
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    train_sizes : array-like, shape (n_ticks,), dtype float or int
        Relative or absolute numbers of training examples that will be used to
        generate the learning curve. If the dtype is float, it is regarded as a
        fraction of the maximum size of the training set (that is determined
        by the selected validation method), i.e. it has to be within (0, 1].
        Otherwise it is interpreted as absolute sizes of the training sets.
        Note that for classification the number of samples usually have to
        be big enough to contain at least one sample from each class.
        (default: np.linspace(0.1, 1.0, 5))
    """
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt


digits = load_digits()
X, y = digits.data, digits.target


title = "Learning Curves (Naive Bayes)"
# Cross validation with 100 iterations to get smoother mean test and train
# score curves, each time with 20% data randomly selected as a validation set.
cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)

estimator = GaussianNB()
plot_learning_curve(estimator, title, X, y, ylim=(0.7, 1.01), cv=cv, n_jobs=4)

title = r"Learning Curves (SVM, RBF kernel, $\gamma=0.001$)"
# SVC is more expensive so we do a lower number of CV iterations:
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
estimator = SVC(gamma=0.001)
plot_learning_curve(estimator, title, X, y, (0.7, 1.01), cv=cv, n_jobs=4)

plt.show()
~~~

</p>
</details>

</div>