# Decision Tree
[<b>Home<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/0_Code%20Starter.html) 
### ==Starter Code==

### ==Exploring The Data==

### ==Train Test Split==

### ==Decision Tree Model:==
<details><summary><b>DT Model<b></summary>
<p>
[See <b>Code<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/11_Decision%20Tree,%20Random%20Forest/1_Decision%20Trees%20and%20Random%20Forests_Basic_.html#Decision-Trees) 

	from sklearn.tree import DecisionTreeClassifier
	
	dtree = DecisionTreeClassifier()
	
	dtree.fit(X_train,y_train)

	y_pred = dtree.predict(X_test)

</p>
</details>
<b>*

### ==Plotting Decision Tree:==
<details><summary><b>Plotting Code<b></summary>
<p>
[See the <b>Plotting<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/11_Decision%20Tree,%20Random%20Forest/1_Decision%20Trees%20and%20Random%20Forests_Basic_.html#Tree-Visualization) 

	from IPython.display import Image  
	from sklearn.externals.six import StringIO  
	from sklearn.tree import export_graphviz
	import pydot 

	features = list(df.columns[1:])
	features

	dot_data = StringIO()  
	export_graphviz(dtree, out_file=dot_data,feature_names=features,filled=True,rounded=True)

	graph = pydot.graph_from_dot_data(dot_data.getvalue())  
	Image(graph[0].create_png())

</p>
</details>
<b>*





































