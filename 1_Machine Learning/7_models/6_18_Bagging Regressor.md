# ==Bagging Regressor==

<details><summary><b>Class<b></summary>
<p>
~~~python
class sklearn.ensemble.BaggingRegressor(
								base_estimator=None, 
								n_estimators=10,
								max_samples=1.0, 
								max_features=1.0,
								bootstrap=True,
								bootstrap_features=False, 
								oob_score=False, 
								warm_start=False, 
								n_jobs=None, 
								random_state=None, 
								verbose=0)
~~~
</p>
</details>

- [<b><span style='color:#333'>Sklearn Page</span><b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/sklearn.ensemble.BaggingRegressor.html#sklearn-ensemble-baggingregressor)

<details><summary><b>Manual Bagging<b></summary>
<p>
~~~python
model = RandomForestClassifier()
bags    = 10
seed    = 1

bagged_pred = np.zeros(test.shape[0])

for i in range(0, bags):
	model.set_params(random_state=seed+i)
	model.fit(train, y)
	preds = model.predict(test)
	bagged_pred += preds

bagged_pred /= bags
~~~
</p>
</details>
<b>*






