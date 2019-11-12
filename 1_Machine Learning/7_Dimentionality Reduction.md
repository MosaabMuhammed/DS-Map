# 7. Feature Reduction

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
 
<details><summary><b>PCA</b></summary>
<p>

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
 
 </p>
 </details>
 
<details><summary><b>Random Projection</b></summary>
<p>
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
</p>
</details>


- ICA
- t-SNE
- LLE
- UMAP
- SVD
</p>
</details>


<details><summary style='font-size:23px;text-decoration:underline'><b>Feature Selection:</b></summary><p>

<details><summary><b>Filter Methods</b></summary><p><ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/03.2_Constant_features.html#Constant-features"><b>Constant Features</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/03.3_Quasi-constant_features.html#Quasi-constant-features"><b>Quasi-Constant Features</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/03.4_Duplicated_features.html#Duplicated-features"><b>Duplicated Features</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/04.2_Correlation.html#Correlation"><b>Correlation</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.2_Information_gain.html#Information-gain---mutual-information"><b>Mutual Information</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.3_Fisher_score.html#Fisher-Score---chi-square-implementation-in-sklearn"><b>Fisher Score - Chi-Square</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.4_Univariate_selection.html#Univariate-feature-selection"><b>Univariate Feature Selection (ANOVA)</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/05.5_Univariate_roc_auc.html#Univariate-roc-auc-or-mse"><b>Univariate ROC-AUC or MSE</b></a> </li>


</ul></p></details>

<details><summary><b>Wrapper Methods</b></summary><p><ul>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/06.1_Step_forward.html#Step-forward-feature-selection"><b>Step Forward Feature Selection</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/06.2_Step_backward.html#Step-backward-feature-selection"><b>Step Backward Feature Selection</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/06.3_Exhaustive_feature_selection.html#Exhaustive-feature-selection"><b>Exhaustive Feature Selection</b></a> </li>

</ul></p></details>

<details><summary><b>Embedded Methods</b></summary><p><ul>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/07.3_Lasso.html#Lasso-regularisation"><b>LASSO Regularization</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/06.3_Exhaustive_feature_selection.html#Exhaustive-feature-selection"><b>Exhaustive Feature Selection</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Feature%20Selection%20for%20Machine%20Learning/Feature-selection-notebooks/06.3_Exhaustive_feature_selection.html#Exhaustive-feature-selection"><b>Exhaustive Feature Selection</b></a> </li>

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