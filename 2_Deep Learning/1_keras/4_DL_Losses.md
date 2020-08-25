# Activation Functions


<div style="width:1000px;margin:auto">


<details><summary><b>binary_crossentropy</b></summary><p><ul>
<li>Used with ONLY <b>binary classification</b> problem.</li>
<li>The last layer has only <b>1 neuron</b>.</li>
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

<details><summary><b>categorical_crossentropy</b></summary><p>

</p></details>

<details><summary><b>sparse_categorical_crossentropy</b></summary><p>

</p></details>

</div>