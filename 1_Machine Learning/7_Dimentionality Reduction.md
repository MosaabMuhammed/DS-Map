# 7. Feature Reduction

<div style='width:1000px;margin:auto'>

<details><summary style='font-size:23px;text-decoration:underline'><b>Dimensionality Reduction:</b></summary>
<p>

<ul>
<li><a href="https://scikit-learn.org/stable/modules/decomposition.html"><b>Linear Methods for Dimensionality Reduction</b></a></li>

<li><a href="https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html"><b>Non-Linear Methods for Dimensionality Reduction</b></a> 
<br></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Applied%20ML%20Course/0_Code/8_Dimensionality%20Reduction/mnist_loadData_pca_tsne.html">PCA vs. t-SNE</a></li>
</ul>
 
 <details><summary><b>PCA</b> & <b>ICA</b> & <b>t-SNE</b> & <b>UMAP</b></summary>
<p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Kaggle's%20Notebooks/5_Cargo%20Rican%20HouseHold/1_Costa%20Rican%20Household%20Poverty%20Level%20Prediction.html"><b>Notebook</b></a></p>
<ul>
<li><b>PCA:</b> Principal Components Analysis. Finds the dimensions of greatest variation in the data</li>

<li><b>ICA:</b> Independent Components Analysis. Attempts to separate a mutltivariate signal into independent signals.</li>

<li><b>TSNE:</b> T-distributed Stochastic Neighbor Embedding. Maps high-dimensional data to a low-dimensional manifold attempting to maintain the local structure within the data. It is a non-linear technique and generally only used for visualization.</li>

<li><b>UMAP:</b> Uniform Manifold Approximation and Projection: A relatively new technique that also maps data to a low-dimensional manifold but tries to preserve more global structure than TSNE.</li>
</ul>

<h4>1. Importing Libraries</h4>
~~~python
from umap import UMAP
from sklearn.decomposition import PCA, FastICA
from sklearn.manifold import TSNE

n_components = 3

umap = UMAP(n_components=n_components)
pca = PCA(n_components=n_components)
ica = FastICA(n_components=n_components)
tsne = TSNE(n_components=n_components)
~~~

<h4> 2. Fitting and Transforming</h4>
~~~python
train_df = train_selected.copy()
test_df = test_selected.copy()

for method, name in zip([umap, pca, ica, tsne], 
                        ['umap', 'pca', 'ica', 'tsne']):
    
    # TSNE has no transform method
    if name == 'tsne':
        start = timer()
        reduction = method.fit_transform(train_selected)
        end = timer()
    
    else:
        start = timer()
        reduction = method.fit_transform(train_selected)
        end = timer()
        
        test_reduction = method.transform(test_selected)
    
        # Add components to test data
        test_df['%s_c1' % name] = test_reduction[:, 0]
        test_df['%s_c2' % name] = test_reduction[:, 1]
        test_df['%s_c3' % name] = test_reduction[:, 2]

    # Add components to training data for visualization and modeling
    train_df['%s_c1' % name] = reduction[:, 0]
    train_df['%s_c2' % name] = reduction[:, 1]
    train_df['%s_c3' % name] = reduction[:, 2]
    
    print(f'Method: {name} {round(end - start, 2)} seconds elapsed.')
~~~

<h4> 3. Plot it 3D</h4>
~~~python
from mpl_toolkits.mplot3d import Axes3D

def discrete_cmap(N, base_cmap=None):
    """Create an N-bin discrete colormap from the specified input map
    Source: https://gist.github.com/jakevdp/91077b0cae40f8f8244a"""

    base = plt.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    return base.from_list(cmap_name, color_list, N)

cmap = discrete_cmap(4, base_cmap = plt.cm.RdYlBu)

train_df['label'] = train_labels
~~~

~~~python
# Plot each method
for method, name in zip([umap, pca, ica, tsne], 
                        ['umap', 'pca', 'ica', 'tsne']):
    
    fig = plt.figure(figsize = (8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    p = ax.scatter(train_df['%s_c1' % name], train_df['%s_c2'  % name], train_df['%s_c3'  % name], 
                   c = train_df['label'].astype(int), cmap = cmap)
    
    plt.title(f'{name.capitalize()}', size = 22)
    fig.colorbar(p, aspect = 4, ticks = [1, 2, 3, 4])
~~~
</p>
</details>
 
<details><summary><b>PCA</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/sklearn.decomposition.PCA.html#sklearn-decomposition-pca"><b>Docs</b></a> </p>
 
<h4> PCA inside a pipeline</h4>
~~~python
from sklearn.decomposition import PCA
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline

# Make sure to drop the ids and target
train = train.drop(columns = ['SK_ID_CURR', 'TARGET'])
test = test.drop(columns = ['SK_ID_CURR'])

# Make a pipeline with imputation and pca
pipeline = Pipeline(steps = [('imputer', Imputer(strategy = 'median')),
     ('pca', PCA())])

# Fit and transform on the training data
train_pca = pipeline.fit_transform(train)


# See how each axis preserve variance.
pca.explained_variance_ratio_


# transform the testing data
test_pca = pipeline.transform(test)
~~~

<h4> CDF for # of principle componets</h4>
~~~python
# Extract the pca object
pca = pipeline.named_steps['pca']

# Plot the cumulative variance explained

plt.figure(figsize = (10, 8))
plt.plot(list(range(train.shape[1])), np.cumsum(pca.explained_variance_ratio_), 'r-')
plt.xlabel('Number of PC'); plt.ylabel('Cumulative Variance Explained');
plt.title('Cumulative Variance Explained with PCA');
~~~

<h4> Visualizing the 2 components</h4>
~~~python
# Dataframe of pca results
pca_df = pd.DataFrame({'pc_1': train_pca[:, 0], 'pc_2': train_pca[:, 1], 'target': train_labels})

# Plot pc2 vs pc1 colored by target
sns.lmplot('pc_1', 'pc_2', data = pca_df, hue = 'target', fit_reg=False, size = 10)
plt.title('PC2 vs PC1 by Target');
~~~

<h4> How much those components preserve from the data</h4>
~~~python
print('2 principal components account for {:.4f}% of the variance.'.format(100 * np.sum(pca.explained_variance_ratio_[:2])))
~~~
</p></details>

<details><summary><b>Incremental PCA</b></summary><p>
<h4>1. Using np.array_split()</h4>
```
from sklearn.decomposition import IncrementalPCA

n_batches = 100
inc_pca = IncrementalPCA(n_componenets=154)

for X_batch in np.array_split(X_train, n_batches):
	inc_pca.partial_fit(X_batch)
	
X_reduced = inc_pca.transform(X_train)
```

<h4>2. Using np.memmap()</h4>
```
# np.memmap allows you to manipulate a large
# array store in a binary file on disk as if it were entirely in memory;
# The class loads only the data it needs in memory, when it needs it.
# 1. Let's create the memmap() structure and copy MNIST data into it. This would typically be done by a first program.
filename = "mnist.data"
m, n = X_train.shape

X_mm = np.memmap(filename, dtype="float32", mode="write", shape=(m, n))
X_mm[:] = X_train

# Now deleting the memmap() object will trigger its Python finalizer, which ensures that the data is saved to disk.
del X_mm

# Another program would load the data and use it for training.
X_mm = np.memmap(filename, dtype="float32", mode="readonly", shape=(m, n))

batch_size = m // n_batches
inc_pca = IncrementalPCA(n_components=154, batch_size=batch_size)
inc_pca.fit(X_mm)
```
</p></details>

<details><summary><b>Kernel PCA</b></summary><p>
```
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

clf = Pipeline([
	("kpca", KernelPCA(n_components=2)),
	("log_reg", LogisticRegression())
])

param_grid = [{
	"kpca__gamma": np.linspace(0.03, .05, 10),
	"kpca__kernel": ["rbf", "sigmoid"]
}]

grid_search = GridSearchCV(clf, param_grid, cv=3)
grid_search.fit(X, y)

# Print the best hyperparameters.
print(grid_search.best_params_)
```
</p></details>

<details><summary><b>LLE</b> [LocallyLinearEmbedding]</summary><p>
```
from sklearn.manifold import LocallyLinearEmbedding

lle = LocallyLinearEmbedding(n_components=2, n_neighbors=10)
X_reduced = lle.fit_transform(X)
```
</p></details>

<details><summary><b>KMeans</b></summary><p>
<p>Clustering can be an efficient approach to dimensionality reduction, in particular as a preprocessing step before a supervised learning algorithm</p>
```
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans

pipeline = Pipeline([
    ("kmeans", KMeans(n_clusters=50)),
    ("log_clf", LogisticRegression(random_state=42))
])
pipeline.fit(X_train, y_train)
pipeline.score(X_test, y_test)
```

<h4>Using GridSearch</h4>
```
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans

pipeline = Pipeline([
    ("kmeans", KMeans(n_clusters=50)),
    ("log_clf", LogisticRegression(random_state=42))
])
pipeline.fit(X_train, y_train)
pipeline.score(X_test, y_test)~~~~
```
</p></details>

<details><summary><b>t-SNE</b></summary><p>
<h4>1. Faster Wrapper for t-SNE</h4>
```
# !pip install tsne
from tsne import bh_sne

X_2d = bh_sne(train.drop(['subject', 'Activity', 'ActivityName'], axis=1))

# Plot the 2D reduced data
plt.figure(figsize=(12, 8))
sns.scatterplot(x=X_2d[:, 0], y=X_2d[:, 1], hue=train['ActivityName'], alpha=0.5)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0);
``` 

<h4>2. Sklearn Wrapper</h4>
```
# Performing t-SNE with sklearn-wrapper
from sklearn.manifold import TSNE

def perform_tsne(X_data, y_data, perplexities, n_iter=1000, img_name_prefix='t-sne'):
    for idx, perplexity in enumerate(perplexities):
        print(f'\nPerforming t-SNE with perplexity {perplexity} and with {n_iter} iterations.')
        X_reduced = TSNE(verbose=2, perplexity=perplexity, n_iter=n_iter, n_jobs=-1).fit_transform(X_data)
        print('Done...')

        # Prepare the data for seaborn
        print('Plot the reduced data...')
        df = pd.DataFrame({'x': X_reduced[:, 0], 'y': X_reduced[:, 1], 'label': y_data})

        # Draw the plot in appropriate place in the grid
        sns.lmplot(data=df, x='x', y='y', hue='label', fit_reg=False, size=8, palette='Set1')
        plt.title(f'Perplexity: {perplexity} and max_iterations: {n_iter}')
        plt.show()
```
```
# Perform the t-SNE function
X_pre_tsne = train.drop(['subject', 'Activity', 'ActivityName'], axis=1)
y_pre_tsne = train['ActivityName']
perform_tsne(X_pre_tsne, y_pre_tsne, perplexities=[2, 5, 10, 10, 50])
```
</p></details>
 
<details><summary><b>Random Projection</b></summary><p>
<p><a href="https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection"><b>SparseRandomProjection</b></a> </p>

<p><a href="https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn-random-projection-gaussianrandomprojection"><b>Gaussian Random Projection</b></a> </p>
 
<h4> Sparse Random Projection.</h4>
~~~python
import numpy as np
from sklearn.random_projection import SparseRandomProjection
rng = np.random.RandomState(42)
X = rng.rand(100, 10000)
transformer = SparseRandomProjection(random_state=rng)
X_new = transformer.fit_transform(X)
X_new.shape

# very few components are non-zero
np.mean(transformer.components_ != 0) 
~~~

<h4> Gaussian Random Projection.</h4>
~~~python
import numpy as np
from sklearn.random_projection import GaussianRandomProjection
rng = np.random.RandomState(42)
X = rng.rand(100, 10000)
transformer = GaussianRandomProjection(random_state=rng)
X_new = transformer.fit_transform(X)
X_new.shape
~~~
</p></details>

<details><summary><b>Multiple Correspondence Analysis (MCA)</b></summary><p>
<h4>It's like PCA for categorical features</h4>
```
!pip install prince
import prince

# Let's try drawing first by extracting only 2 components
mca = prince.MCA(n_components=2)
mca.fit(X_train_org[:1000])

# Transform the data
X_train_mca = mca.transform(X_train_org[:1000])
```
```
# Let's plot the generated data
ax = mca.plot_coordinates(
    X=X_train_org[:100],
    ax=None,
    figsize=(6, 6),
    show_row_points=True,
    row_points_size=10,
    show_row_labels=False,
    show_column_points=True,
    column_points_size=30,
    show_column_labels=False,
    legend_n_cols=1
)

# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.);

```
</p></details>

- ICA
- t-SNE
- LLE
- UMAP
- SVD
</p></details>


<details><summary style='font-size:23px;text-decoration:underline'><b>Feature Selection:</b></summary><p>

<details><summary><b>Filter Methods</b></summary><p><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/03.2_Constant_features.html#Constant-features"><b>Constant Features</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/03.3_Quasi-constant_features.html#Quasi-constant-features"><b>Quasi-Constant Features</b></a> </li>

<li><details><summary>Duplicate Features</summary><p>
<a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/03.4_Duplicated_features.html#Duplicated-features"><b>Duplicated Features</b></a>
```
# For big data
from itertools import combinations

duplicated_feats = []
for idx, (col_1, col_2) in enumerate(combinations(train.columns, 2)):
    if train[col_1].equals(train[col_2]):
        duplicated_feats.append(col_2)
```
</p></details></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/03.5_Basic_methods_review.html#Filter-Methods---Basics"><b>Basic Methods Pipeline</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/04.2_Correlation.html#Correlation"><b>Correlation</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/04.3_Basic_methods_plus_correlation_pipeline.html#Basic-methods-plus-correlation-pipeline"><b>Basic Methods + Correlation Pipeline</b></a> </li>


<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.2_Information_gain.html#Information-gain---mutual-information"><b>Mutual Information</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.3_Fisher_score.html#Fisher-Score---chi-square-implementation-in-sklearn"><b>Fisher Score - Chi-Square</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.4_Univariate_selection.html#Univariate-feature-selection"><b>Univariate Feature Selection (ANOVA)</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.5_Univariate_roc_auc.html#Univariate-roc-auc-or-mse"><b>Univariate ROC-AUC or MSE</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.6_Basic_methods_correlation_univariate_rocauc_review.html#Filter-Methods---Basics---Correlations---Univariate-ROC-AUC"><b>Basic Methods + Correlation + others Pipeline</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.7_Bonus_method_used_in_KDD_competition.html#Bonus:-Method-used-in-KDD-2009-competition"><b>Method used in KDD 2009 competition</b></a> </li>

</ul></p></details>

<details><summary><b>Wrapper Methods</b></summary><p><ul>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/06.1_Step_forward.html#Step-forward-feature-selection"><b>Step Forward Feature Selection</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/06.2_Step_backward.html#Step-backward-feature-selection"><b>Step Backward Feature Selection</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/06.3_Exhaustive_feature_selection.html#Exhaustive-feature-selection"><b>Exhaustive Feature Selection</b></a> </li>

</ul></p></details>

<details><summary><b>Embedded Methods</b></summary><p>

<details><summary><b>Linear Models</b></summary><p><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/07.3_Lasso.html#Lasso-regularisation"><b>LASSO Regularization</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/08.2_Logistic_regression_coefficients.html#Logistic-Regression-Coefficients"><b>Logistic Regression Coefficients</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/08.3_Regression_coefficients_and_regularisation.html#Regression-Coefficients-are-affected-by-regularisation"><b>Regression Coefficients are affected by regularisation</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/08.4_Linear_Regression_coefficients.html#Linear-Regression-Coefficients"><b>Linear Regression Coefficients</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/08.5_Feature_selection_with_linear_models_review.html#Feature-selection-with-linear-models,-review"><b>Linear Model Pipeline</b></a> </li>
</ul></p></details>

<details><summary><b>Tree-based Models</b></summary><p><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/09.2_Random_forest_importance.html#Random-Forest-importance"><b>Random Forest importance</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/09.3_Random_Forest_recursive_feature_selection.html#Recursive-feature-selection-using-random-forests-importance"><b>Recursive feature selection using random forests importance</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/09.4_GradientBoosting_importance.html#Gradient-Boosted-trees-importance"><b>Gradient Boosted trees importance</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/09.5_Feature_selection_with_decision_trees_review.html#Feature-selection-with-decision-trees,-review"><b>Tree Models - Pipeline/b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/09.3_Random_Forest_recursive_feature_selection.html#Recursive-feature-selection-using-random-forests-importance"><b>Recursive feature selection using random forests importance</b></a> </li>
</ul></p></details>

</p></details><details><summary><b>Hybrid Methods</b></summary><p><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/11.01_Feature_shuffling.html#Feature-selection-by-random-shuffling"><b>Random Shuffling</b></a> </li><li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/11.02_Hybrid_Recursive_feature_elimination.html#Hybrid-method:-Recursive-feature-elimination"><b>Recursive Feature Elimination</b></a> </li><li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/11.03_Hybrid_Recursive_feature_addition.html#Hybrid-method:-Recursive-feature-addition"><b>Recursive Feature Addition</b></a> </li>
</ul></p></details>

<hr>
<details><summary>1. Remove <b>Highly Correlated</b> Features</summary>
<p>
<h4> Identify Highly Correlated Features</h4>
~~~python
# Threshold for removing correlated variables
threshold = 0.9

# Absolute value correlation matrix
corr_matrix = train.corr().abs()
corr_matrix.head()
~~~
<h4> Drop the columns</h4>
~~~python
# Create correlation matrix
corr_matrix = df.corr().abs()

# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

# Select columns with correlations above threshold
to_drop = [column for column in upper.columns if any(upper[column] > threshold)]

print('There are %d columns to remove.' % (len(to_drop)))

# Drop features 
df.drop(df[to_drop], axis=1)
~~~

</p>
</details>


<details><summary><b>Recursive Feature Elimination CV</b></summary>
<p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/sklearn.feature_selection.RFECV.html#sklearn-feature-selection-rfecv"><span style='color:#333'><b> 2. Recursive Feature Elimination method</b></span></a></p>

~~~python
from sklearn.feature_selection import RFECV

# Create a model for feature selection
estimator = RandomForestClassifier(random_state = 10, n_estimators = 100,  n_jobs = -1)

# Create the object
selector = RFECV(estimator, step = 1, cv = 3, scoring= scorer, n_jobs = -1)
~~~

~~~python
selector.fit(train_set, train_labels)
~~~

~~~python
plt.plot(selector.grid_scores_);

plt.xlabel('Number of Features'); plt.ylabel('Macro F1 Score'); plt.title('Feature Selection Scores');
selector.n_features_
~~~

~~~python
rankings = pd.DataFrame({'feature': list(train_set.columns), 'rank': list(selector.ranking_)}).sort_values('rank')
rankings.head(10)
~~~

~~~python
train_selected = selector.transform(train_set)
test_selected = selector.transform(test_set)
# Convert back to dataframe
selected_features = train_set.columns[np.where(selector.ranking_==1)]
train_selected = pd.DataFrame(train_selected, columns = selected_features)
test_selected = pd.DataFrame(test_selected, columns = selected_features)
~~~
</p>
</details>

<ul>
<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/Step%20Forward%20Feature%20Selection_%20A%20Practical%20Example%20in%20Python.html"><span style='color:#333'><b>3. Forward Feature  Selection<b></span></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/How%20to%20win%20a%20Data%20Science%20Competition/compute_KNN_features.html#Load-data"><span style='color:#333'><b>4. Nearest Neighbors for Feature Extraction<b></span></a></p></li>
</ul>


</p>
</details>

</div>