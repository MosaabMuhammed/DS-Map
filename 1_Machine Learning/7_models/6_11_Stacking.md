# ==Stacking==

<details><summary><b>Manual Stacking<b></summary>
<p>
~~~python
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split
~~~

~~~python
 # Split train data into 2 parts, training and testing
 X_train, X_valid, y_train, y_valid  = train_test_split(train, y, test_size=.5)
 
 # Specify models
 model1 = RandomForestRegressor()
 model2 = LinearRegression()
 
 # Fit models
 model1.fit(X_train, y_train)
 model2.fit(X_train, y_train)
 
 # Make predictions for validation
 preds1 = model1.predict(X_valid)
 preds2 = model2.predict(X_valid)
 
 # make predictions for test data.
 test_pred1 = model1.predict(test)
 test_pred2 = model2.predict(test)
 
 # Form a new dataset for valid and test via stacking the predictions
 stacked_preds = np.column_stack((preds1, preds2))
 stacked_test_preds = np.column_stack((test_preds1, test_preds2))
 
 # Specify meta model
 meta_model = LinearRegression()
 
 # Fit meta model on stacked predictions
 meta_model.fit(stacked_predictions, y_valid)
 
 # Make predictions on the stacked predictions of the test data
 final_preds = meta_model.predict(stacked_test_preds)
~~~
</p>
</details>

<details><summary><b>mlxtend stacking Class<b></summary>
<p>
[<b>Notebook<b>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Applied%20ML%20Course/0_Code/0_Case%20Studies/6_Personalized%20Cancer%20Diagnosis/1_Course%20Code/PersonalizedCancerDiagnosis.html) 
~~~python
clf1 = SGDClassifier(alpha=0.001, penalty='l2', loss='log', class_weight='balanced', random_state=0)
clf1.fit(train_x_onehotCoding, train_y)
sig_clf1 = CalibratedClassifierCV(clf1, method="sigmoid")

clf2 = SGDClassifier(alpha=1, penalty='l2', loss='hinge', class_weight='balanced', random_state=0)
clf2.fit(train_x_onehotCoding, train_y)
sig_clf2 = CalibratedClassifierCV(clf2, method="sigmoid")


clf3 = MultinomialNB(alpha=0.001)
clf3.fit(train_x_onehotCoding, train_y)
sig_clf3 = CalibratedClassifierCV(clf3, method="sigmoid")

sig_clf1.fit(train_x_onehotCoding, train_y)
print("Logistic Regression :  Log Loss: %0.2f" % (log_loss(cv_y, sig_clf1.predict_proba(cv_x_onehotCoding))))
sig_clf2.fit(train_x_onehotCoding, train_y)
print("Support vector machines : Log Loss: %0.2f" % (log_loss(cv_y, sig_clf2.predict_proba(cv_x_onehotCoding))))
sig_clf3.fit(train_x_onehotCoding, train_y)
print("Naive Bayes : Log Loss: %0.2f" % (log_loss(cv_y, sig_clf3.predict_proba(cv_x_onehotCoding))))
print("-"*50)
alpha = [0.0001,0.001,0.01,0.1,1,10] 
best_alpha = 999
for i in alpha:
    lr = LogisticRegression(C=i)
    sclf = StackingClassifier(classifiers=[sig_clf1, sig_clf2, sig_clf3], meta_classifier=lr, use_probas=True)
    sclf.fit(train_x_onehotCoding, train_y)
    print("Stacking Classifer : for the value of alpha: %f Log Loss: %0.3f" % (i, log_loss(cv_y, sclf.predict_proba(cv_x_onehotCoding))))
    log_error =log_loss(cv_y, sclf.predict_proba(cv_x_onehotCoding))
    if best_alpha > log_error:
        best_alpha = log_error
~~~
</p>
</details>