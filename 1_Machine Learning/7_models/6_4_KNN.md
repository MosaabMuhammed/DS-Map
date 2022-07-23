# K-Nearest Neighbors
[<b>Home<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/0_Code/0_Code%20Starter.html) 
### ==Starter Code==

### ==Exploring The Data==

### ==Standardiaze Variables:==
- We use this method when the gap between the values in a column is very large.

<details><summary> <b>StandardScaler<b> </summary>
<p>
[More Illustration](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/1_step-by-step-diabetes-classification-knn-detailed.html#Scaling-the-data) 

	from sklearn.preprocessing import StandardScaler
	# Create a StandardScaler() object
	scaler = StandardScaler()
	# Fit Scaler to Features
	scaler.fit(X)
	# Use the .transfrom() method to transform the featues to a scaled version.
	scaled_features = scaler.transform(X)
	# Convert the scaled featues to a dataframe
	X = pd.DataFrame(scaled_features, columns=df.columns[:-1])
	X.head()

</p>
</details>
### ==Train Test Split==
### ==Plot where Best K value:==

<details><summary> <b>Code<b> </summary>
<p>
[Choosing the Best K value (1)](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/2_KNN%20-%20Full%20Pipeline.html#Choosing-besk-%22K%22-for-KNN) 

	from sklearn.neighbors import KNeighborsClassifier
	
	neighbors = np.arange(1, 30)
	train_accuracy = np.empty(len(neighbors))
	test_accuracy = np.empty(len(neighbors))
	
	for i, k in enumerate(neighbors):
	    knn = KNeighborsClassifier(n_neighbors=k)
	    
	    knn.fit(X_train, y_train)
	    
	    train_accuracy[i] = knn.score(X_train, y_train)
	    test_accuracy[i] = knn.score(X_test, y_test)
	    
	# Generate a plot
	plt.figure(figsize=(16, 6))
	plt.title('K-NN Varying number of neighbors')
	plt.plot(neighbors, test_accuracy, label='Testing Accuracy', marker='o')
	plt.plot(neighbors, train_accuracy, label='Training Accuracy', marker='*')
	plt.legend()
	plt.xlabel('Number of neighbors')
	plt.ylabel('Accuracy')
	plt.xlim([0, 30])

[Choosing the best (K) (2)](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/10_%20K-Nearest%20Neighbors/2_KNN%20-%20Full%20Pipeline.html#Another-Way-of-Choosing-best-%22K%22) 

	error_rate = []
	
	for i in neighbors:
	    knn = KNeighborsClassifier(n_neighbors=i)
	    knn.fit(X_train, y_train)
	    pred_i = knn.predict(X_test)
	    error_rate.append(np.mean(pred_i != y_test))
	
	# Generate Plot
	plt.figure(figsize=(10, 6))
	plt.plot(range(1, 30), error_rate, color='blue', linestyle='--',
	         marker='o', markerfacecolor='red', markersize=10)
	plt.title('Error Rate vs. K value')
	plt.xlabel('K Values')
	plt.ylabel('Error Rate')

</p>
</details>

### ==KNN Model:==
<details><summary><b>KNN Model<b></summary>
<p>

	knn = KNeighborsClassifier(n_neighbors=16)
	
	knn.fit(X_train, y_train)

	# Get Accuracy
	knn.score(X_test, y_test)
	
	y_pred = knn.predict(X_test)
	
</p>
</details>







































