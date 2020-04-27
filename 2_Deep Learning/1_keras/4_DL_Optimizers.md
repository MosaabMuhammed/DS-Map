# Optimizers

<div style="width:1000px;margin:auto">
<details><summary><b>SGD</b></summary><p>
<p><a href="https://keras.io/optimizers/"><strong>Docs</strong></a> </p>
```
keras.optimizers.SGD(
				learning_rate=0.01, 
				momentum=0.0, 
				nesterov=False)
```
</p></details>

<details><summary><b>Momentum</b></summary><p>
```
optimizer = tf.keras.optimizers.SGD(lr=0.001, momentum=.9)
```
</p></details>

<details><summary><b>Nesterov Accelerated Gradient (NAG)</b></summary><p>
```
optimizer = tf.keras.optimizers.SGD(lr=0.001, momentum=.9, nesterov=True)
```
</p></details>
<details><summary><b>RMSprop</b></summary><p>
```
optimizer = tf.keras.optimizers.RMSprop(lr=.001, rho=.9)
```
</p></details>

<details><summary><b>Adam</b></summary><p>
```
optimizer = tf.keras.optimizers.Adam(lr=.001, beta_1=.9, beta_1=.999)
```
</p></details>

</div>