# Activation Functions


<div style="width:1000px;margin:auto">
<p> <b>SELU</b> > <b>ELU</b> > <b>leaky ReLU</b> (and its variants) > <b>ReLU</b> > <b>tanh</b> > <b>sigmoid</b></p>
<details><summary><b>ReLU</b></summary><p>
```
relu = tf.keras.layers.ReLU(alpha=.2)

layer = tf.keras.laysers.Dense(10, activation=relu)
```
</p></details>

<details><summary><b>Leaky ReLU</b></summary><p>
```
leaky_relu = tf.keras.layers.LeakyReLU(alpha=.2)

layer = tf.keras.layers.Dense(10, activation=leaky_relu, kernel_initializer="he_normal")
```
</p></details>

<details><summary><b>PReLU</b></summary><p>
```
leaky_relu = tf.keras.layers.PReLU(alpha=.2)

layer = tf.keras.layers.Dense(10, activation=leaky_relu, kernel_initializer="he_normal")
```
</p></details>

<details><summary><b>ELU</b></summary><p>
```
layer = tf.keras.layers.Dense(10, activation="elu", kernel_initializer="he_normal")
```
</p></details>

<details><summary><b>SELU</b></summary><p>
```
layer = tf.keras.layers.Dense(10, activation="selu", kernel_initializer="lecun_normal")
```
</p></details>

<details><summary><b>tanh</b></summary><p>
```
layer = tf.keras.layers.Dense(10, activation="tanh")
```
</p></details>

<details><summary><b>sigmoid</b></summary><p>
```
layer = tf.keras.layers.Dense(10, activation="sigmoid")
```
</p></details>

</div>