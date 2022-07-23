# ==K-Means==

<details><summary><b>1. Class<b></summary>
<p>
~~~python
class sklearn.cluster.KMeans(n_clusters=8, 
							init=’k-means++’,
							n_init=10, 
							max_iter=300, 
							tol=0.0001, 
							precompute_distances=’auto’, 
							verbose=0, 
							random_state=None, 
							copy_x=True, 
							n_jobs=None, 
							algorithm=’auto’)
~~~
</p>
</details>


<details><summary><b>2. Parameters<b></summary>
[Kmeans parameters on Sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) 
</details>

<details><summary><b>3. Attributes<b></summary>
<p>
<b><span style='background-color:gray;color:white;padding:3px'>cluster_centers_ : array, [n_clusters, n_features]</span><b>
&nbsp;&nbsp;&nbsp;&nbsp;Coordinates of cluster centers. If the algorithm stops before fully converging (see tol and max_iter), these will not be consistent with labels_.

<b><span style='background-color:gray;color:white;padding:3px'>labels_ :</span><b>
&nbsp;&nbsp;&nbsp;&nbsp;Labels of each point

<b><span style='background-color:gray;color:white;padding:3px'>inertia_ : float</span><b>
&nbsp;&nbsp;&nbsp;&nbsp;Sum of squared distances of samples to their closest cluster center.

<b><span style='background-color:gray;color:white;padding:3px'>n_iter_ : int</span><b>
&nbsp;&nbsp;&nbsp;&nbsp;Number of iterations run.
</p>
</details>

- [<span style='color:#333333'><b>4. Sample Code<b></span>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeTutorials.Us]%20machinelearning/21%20K-Means%20Clustering/K-Means.html#K-Means-Alogrithm) 

- [<span style='color:#333333'><b>5. Plot the Elbow method<b></span>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeTutorials.Us]%20machinelearning/21%20K-Means%20Clustering/K-Means.html#Plot-the-clusters) 

- [<span style='color:#333333'><b>6. Plot the Clusters<b></span>](file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/[FreeTutorials.Us]%20machinelearning/21%20K-Means%20Clustering/K-Means.html#Plot-the-clusters) 

- Grid Search/Randomized Search.

<b>*
# ==MiniBatchKMeans==
<details><summary><b>1. Class<b></summary>
<p>
~~~python
class sklearn.cluster.MiniBatchKMeans(
					n_clusters=8, 
					init=’k-means++’, 
					max_iter=100, 
					batch_size=100, 
					verbose=0, 
					compute_labels=True, 
					random_state=None, 
					tol=0.0, 
					max_no_improvement=10, 
					init_size=None, 
					n_init=3, 
					reassignment_ratio=0.01)
~~~
</p>
</details>

- [<b><span style='color:#333'>2. Parameters</span><b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/sklearn.cluster.MiniBatchKMeans.html#sklearn-cluster-minibatchkmeans) 

- [<b><span style='color:#333'>3. Methods</span><b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.__init__) 

<details><summary><b>4. Code Sample<b></summary>
<p>
~~~python
def find_clusters(increment):
    kmeans = MiniBatchKMeans(n_clusters=increment, batch_size=10000,random_state=42).fit(coords)
    frame_with_durations_outliers_removed['pickup_cluster'] = kmeans.predict(frame_with_durations_outliers_removed[['pickup_latitude', 'pickup_longitude']])
    cluster_centers = kmeans.cluster_centers_
    cluster_len = len(cluster_centers)
    return cluster_centers, cluster_len
~~~
</p>
</details>









