# Support Vector Machine
[<b>Home<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/0_Code%20Starter.html) 
### ==Starter Code== 

### ==Exploring The Data==

### ==Train Test Split==

### ==Random Forest Model:==
<details><summary><b>SVM Model<b></summary>
[SVM Classifier](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/12_Support%20Vector%20Machine/1_Support%20Vector%20Machines%20Project-Mosaab.html#Train-a-Model) 
<p>

	from sklearn.svm import SVC
	
	svc = SVC()
	
	svc.fit(X_train, y_train)

	y_pred = svc.predict(X_test)
</p>
</details>

<b>*
### ==GridSearchCV:==
<details><summary><b>GridSearchCV<b></summary>
[<b>GridSearch<b> Code](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/12_Support%20Vector%20Machine/1_Support%20Vector%20Machines%20Project-Mosaab.html#Gridsearch-Practice) 
<p>

	from sklearn.model_selection import GridSearchCV
	
	param_grid = dict(C = [.01, .1, 1, 10], gamma = [.1, .01, .001, .0001])
	
	grid = GridSearchCV(svc, param_grid, refit=True, verbose=2, cv=3)
	grid.fit(X_train, y_train)

	y_pred = grid.predict(X_test)

</p>
</details>




