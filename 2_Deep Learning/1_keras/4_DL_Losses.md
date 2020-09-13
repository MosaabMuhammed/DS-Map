# Losses


<div style="width:1000px;margin:auto">


<details><summary><b>binary_crossentropy</b></summary><p><ul>
<li>Used with <b>binary classification</b> problem.</li>
<li>Can be used for <b>Multi-class, multilabel classification</b> problem</li>.
<li>The last layer has only <b>1 neuron</b> [Binary Classification] and <b>n-1 neurons</b> [Multi-Label Classification] where n is the number of classes.</li>
<li>The last layer has <b>sigmoid</b> activation function.</li>
<li>The <b>y_labels</b> is an array of ONLY <b>zeros</b> and <b>ones</b></li></ul>
```
# Last layer.
	keras.layers.Dense(1, activation="sigmoid")
	
model.compile(optimizer="adam",
			loss="binary_crossentropy",
			metrics=["accuracy"])
```

<h4>To predict</h4>
```
result = model.predict(X_valid)
# result is a class 0 or 1.
```
</p></details>

<details><summary><b>categorical_crossentropy</b></summary><p><ul>
<li>Used for <b>binary</b> or <b>multi-class</b> classification problems.</li>
<li>The last layer has nuerons as the <b>number of classes</b> in y_labels.</li>
<li>The last layer must have <b>"softmax"</b> activation function.</li>
<li>The y_labels MUST be <b>one-hot encoded</b>.</li>
</ul>
```
# To one-hot encode the y_labels.
from tensorflow.keras.utils import to_categorical

y_labels = to_categorical(y_labels, len(np.unique(y_labels)))
```
```
# Last Layer.
	keras.layers.Dense(len(np.unique(y_labels)), activation="softmax")
	
model.compile(loss="categorical_crossentropy", ...)
```

```
# To predict.
results = model.predict(X_valid)
class_idx = np.argmax(results)
```
</p></details>

<details><summary><b>sparse_categorical_crossentropy</b></summary><p><ul>
<li>Used for <b>multi-classification classification</b> problem.</li>
<li>The last layer has a number of neurons as the <b>number of classes</b> in y_labels.</li>
<li>The last layer has <b>"softmax"</b> activation function.</li>
<li><b>y_labels</b> MUST be an <b>array of intengers</b>.</li></ul>

```
# Last Layer.
	keras.layers.Dense(len(np.unique(y_labels)), activation="softmax")
	
model.compile(loss="sparse_categorical_crossentropy", ...)
```

```
# To predict.
results = model.predict(X_valid)
class_idx = np.argmax(results)
```
</p></details>
</div>