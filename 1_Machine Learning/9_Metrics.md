# 8. Metrices

<details><summary style='font-size:18px;color:red'> <b>1. Important Functions</b></summary>
<p>
```
# This function plots the confusion matrices given y_i, y_i_hat.
# NOTE: make sure the predicted labels are NOT probabilities.
# predicted_y =np.argmax(test_predicted_y, axis=1)
# plot_confusion_matrix(y_test, predicted_y+1)
def plot_confusion_matrix(y_test, y_pred):
  C = confusion_matrix(y_test, y_pred)
  A = (((C.T)/(C.sum(axis=1))).T)
  B = (C/C.sum(axis=0))

  liOfMat    = [C, B, A]
  liOfTitles = ['Confusion Matrix', 'Precision Matrix (Column Sum = 1)', 'Recall Matrix (Row sum = 1)']
  labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Change this based on problem.

  # Representing matrices in heatmap format.  
  for i, mat in enumerate(liOfMat):
    plt.figure(figsize=(20, 7))
    sns.heatmap(mat, annot=True, cmap='viridis', fmt='.3f', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted Class')
    plt.ylabel('Original Class')
    plt.title(liOfTitles[i])
    plt.show(
```
</p></details>


<details><summary> <b>Accuracy Score</b></summary><p>
```
accuracy = model.score(y_test, y_pred)
```
</p></details>

<details><summary> <b>Confusion Matrix</b> </summary><p>
```
pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)

# Another way with Background
pd.crosstab(data.Pclass,data.Survived,margins=True).style.background_gradient(cmap='summer_r')
```
```
from sklearn.metrics import confusion_matrix

sns.heatmap(confusion_matrix(y_test, y_pred), cmap='viridis', annot=True)
```
</p></details>

<details><summary> <b>Classification Report</b> </summary><p>
```
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```
</p></details>

<details><summary> <b>Ploting the ROC Curve</b> </summary><p>
```
# Extract the prediction probabilities
y_pred_proba = knn.predict_proba(X_test)[:, 1]

# Calculate the roc_curve
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# Generate the plot
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr, label='knn')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('KNN (n_neighbors = 16) ROC Curve')
```
</p></details>

<details><summary> <b>ROC Area Under Curve (AUC)</b> </summary><p>
```
from sklearn.metrics import roc_auc_score

print('{:.2f}'.format(roc_auc_score(y_test, y_pred_proba)*100))
```
</p>
</details>

<details><summary> <b>Confidance Interval</b> </summary><p>
```
from scipy import stats

confidence = 0.95

squared_errors = (final_predictions - y_test) ** 2

np.sqrt(stats.t.interval(confidence, len(squared_errors) - 1, loc=squared_errors.mean(), scale=stats.sem(squared_errors)))

### Returns
#array([45685.10470776, 49691.25001878])
```
</p></details>

<details><summary> <b>Precision</b> </summary><p>
<p><b>Precision</b> is simply the accuracy of the positive predictions.</p>
```
from sklearn.metrics import precision_score

precision_score(y_train_5, y_train_pred)
```
</p></details>

<details><summary> <b>Recall</b> </summary><p>
```
from sklearn.metrics import recall_score

recall_score(y_train_5, y_train_pred)
```
</p></details>

- Mean Absolute Error (Regression).
- Mean Squared Error (Regression).
- Square Root Mean Square Error (Regression).