# Random Forest
[<b>Home<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/0_Code%20Starter.html) 
### ==Starter Code==

### ==Exploring The Data==

### ==Train Test Split==

### ==Random Forest Model:==
<details><summary><b>RF Model<b></summary>
<p>

	from sklearn.ensemble import RandomForestClassifier
	
	rfc = RandomForestClassifier(n_estimators=100)
	
	rfc.fit(X_train, y_train)

	rfc_pred = rfc.predict(X_test)
</p>
</details>
<b>*






