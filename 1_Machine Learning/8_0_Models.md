# ML Models

<div style='width:1000px;margin:auto'>

<details><summary style='font-size:18px;color:darkcyan'> <b>Important Functions</b> </summary>
<p>

<details><summary><b>Random Model</b></summary>
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

<li>Decision Tree.</li>

<li>K-Nearest Neighbors.</li>

<li>SVM.</li>

<li>Kernel SVM.</li>
</ul></details>

<details><summary><b style="font-size:25px">Multi-Class Classification:</b></summary></p>
<p><b>NOTE:</b> Sklearn detects when you try to use a binary classification algorithm for a multi-class classification task, and it automatically runs OvA (except for SVM classifiers for which it uses OvO).</p>
<details><summary><b>One Vs. All</b></summary></p>
```
from sklearn.multiclass import OneVsAllClassifier

ova_clf = OneVsAll(SVC(random_state=42))
ova_clf.fit(X_train, y_train)
```
</p></details>

<details><summary><b>One Vs. One</b></summary></p>
```
from sklearn.multiclass import OneVsOneClassifier

ovo_clf = OneVsOneClassifier(SGDClassifier(random_state=42))
ovo_clf.fit(X_train, y_train)
ovo_clf.predict([some_digit])
```
</p></details>

</p></details>

<details><summary><b style="font-size:25px">Regression:</b></summary><p><ul>

<li><details><summary><b>Linear Regression</b></summary><p>
```
# Fast when we have large training instance.
# Slow when we have large numer of features.
# Doesn't require scaling!!
from sklearn.linear_models import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, y)

print(lin_reg.intercept_)
print(lin_reg.coef_)
```
</p></details></li>

<li><details><summary><b>SGD Regressor</b></summary><p>
```
# Fast when we have large training instances.
# Fast when we have large number of features too!
# Change the thetas at each instance.
# gives a better thetas than GD, but not the best!
# Requires Scaling!!
from sklearn.linear_model import SGDRegressor

sgd_reg = SGDRegressor(max_iter=1000, tol=1e-3, penalty=None, eta0=0.1)
sgd_reg.fit(X, y.ravel())
sgd_reg.intercept_, sgd_reg.coef_
```
</p></details></li>

<li><details><summary><b>Polynomial Regressor</b></summary><p>
```
# Create the polynomial features.
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
```
</p></details></li>

<li><details><summary><b>Ridge Regressor</b> [L2 Regulaizer]</summary><p>
<p><b>NOTE:</b> Requires Scalling and you can make it polynomial as Linear Regression.</p>
```
# Also called "Tikhonov Regularization", L2.
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
```
</p></details></li>


<li><details><summary><b>Lasso Regressor</b> [L1 Regulaizer]</summary><p>
<p><b>NOTE:</b> Requires Scalling and you can make it polynomial as Linear Regression.</p>
```
# 1. Lasso using Closed-form solution.
from sklearn.linear_model import Lasso

lasso_reg = Lasso(alpha=0.1)
lasso_reg.fit(X, y)
lasso_reg.predict([[1.5]])

# 2. Ridge using Gradient Descent.
from sklearn.linear_model import SGDRegressor

sgd_reg = SGDRegressor(penalty="l1")
sgd_reg.fit(X, y.ravel())
sgd_reg.predict([[1.5]])
```
</p></details></li>

<li><details><summary><b>Elastic Net</b> [L1 + L2 Regulaizer]</summary><p>
<p><b>NOTE:</b> Requires Scalling and you can make it polynomial as Linear Regression.</p>
```
# when r = 0, Elastic Net = Ridge Regression.
# when r = 1, Elastic Net = Lasso Regression.
# 1. ElasticNet using Closed-form solution.
from sklearn.linear_model import ElasticNet

elastic_net = ElasticNet(alpha=.1, l1_ratio=.5)
elastic_net.fit(X, y)
elastic_net.predict([[1.5]])
```
</p></details></li>


<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/KNN.html"><b>K Nearest Neighbors</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/Decision%20Tree.html"><b>Decision Tree</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/Random%20Forest.html"><b>Random Forest</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/BaggingRegressor.html"><b>Bagging Regressor</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Stacking.html"><b>Stacking</b></a> </li>
</ul></details>

<details><summary><b style="font-size:25px">Clustering:</b></summary><p><ul>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/KMeans.html"><b>K-means</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/Agglomerative%20Clustering.html"><b>AgglomerativeClustering</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/DBSCAN.html"><b>DBSCAN</b></a> </li>
</ul></details>

<details><summary><b style='font-size:27px;'>Auto ML</b></summary><p><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/auto-sklearn.html#auto-sklearn"><b><span style='color:#333'>Auto-Sklearn</span></b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/Titanic_Kaggle.html#Data-Analysis-using-TPOT"><b><span style='color:#333'>TPOT</span></b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/automl_binary_classification_product_backorders.html#H2O-AutoML-Binary-Classification-Demo"><b><span style='color:#333'>H2O</span></b></a></li>

</ul></p></details>

<p><a href="https://www.analyticsvidhya.com/blog/2017/08/introduction-to-multi-label-classification/"><b><span style='font-size:28px;color:#333'>Multi-Label Classification</span></b></a> </p>




</div>