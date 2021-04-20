# ==&nbsp;Layers&nbsp;==


<details><summary>**Dense**</summary><p>
[**Docs**](https://keras.io/layers/core/) 

- **Dense** is fully connected layer that means all neurons in previous layers will be connected to all neurons in fully connected layer. In the last layer we have to specify output dimensions/classes of the model.
#### 1. Class.
```python
keras.layers.Dense(
				units, 
				activation=None, 
				use_bias=True, 
				kernel_initializer='glorot_uniform', 
				bias_initializer='zeros', 
				kernel_regularizer=None, 
				bias_regularizer=None, 
				activity_regularizer=None, 
				kernel_constraint=None, 
				bias_constraint=None
				)
```

#### Example.
```python
from keras.layers.core import  Dense

model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))   <----
```
</p>
</details>


<details><summary>**Lambda**</summary>
<p>
[**Docs**](https://keras.io/layers/core/) 

- **Lambda layer** performs simple arithmetic operations like sum, average, exponentiation etc.

#### 1. Class.
```python
keras.layers.Lambda(function, output_shape=None, mask=None, arguments=None)
```

#### Example.
```python
from keras.layers.core import  Lambda

def standardize(x):
    return (x - mean_px)/std_px

model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))  <--
model.add(Flatten())
model.add(Dense(10, activation='softmax'))
```
</p>
</details>


<details><summary>**Flatten**</summary>
<p>
[**Docs**](https://keras.io/layers/core/) 

- **Flatten** will transform input into 1D array.

#### 1. Class.
```python
keras.layers.Flatten(data_format=None)
```

#### Example.
```python
from keras.layers.core import  Flatten

model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))
model.add(Flatten())   <--
model.add(Dense(10, activation='softmax'))
```
</p>
</details>

<details><summary>**Dropout**</summary>
<p>
[**Docs**](https://keras.io/layers/core/) 

- **Dropout** consists in randomly setting a fraction rate of input units to 0 at each update during training time, which helps prevent overfitting.

#### 1. Class.
```python
keras.layers.Dropout(
				rate, 
				noise_shape=None, 
				seed=None
				)
```

#### Example.
```python
from keras.layers.core import  Flatten

model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))
model.add(Flatten())   <--
model.add(Dense(10, activation='softmax'))
```
</p>
</details>

<details><summary>Create **Custom** Layer</summary><p>
```
# A layer with no weights.
exponential_layer = keras.layers.Lambda(lambda x: tf.exp(x))
```

```
# A layer with weights using SubClass.
class MyDense(keras.layers.Layer):
	def __init__(self, units, activation=None, **kwargs):
		super().__init__(**kwargs)
		self.units = units
		self.activation = keras.activations.get(activation)
	
	def build(self, batch_input_shape):
		self.kernel = self.add_weight(name="kernel", shape=[batch_input_shape[-1], self.units], initializer="glorot_normal")
		self.bias = self.add_weight(name="bias", shape=[self.units], initializer="zeros")
		super().build(batch_input_shape) # must be at the end
	
	def call(self, X):
		return self.activation(X @ self.kernel + self.bias)

	def compute_output_shape(self, batch_input_shape):
		return tf.TensorShape(batch_input_shape.as_list()[:-1] + [self.units])
	
	def get_config(self):
		base_config = super().get_config()
		return {**base_config, "units": self.units, "activation":
				keras.activations.serialize(self.activation)}
```

```
# Another example.
class MyGaussianNoise(keras.layers.Layer):
	def __init__(self, stddev, **kwargs):
		super().__init__(**kwargs)
		self.stddev = stddev

	def call(self, X, training=None):
		if training:
			noise = tf.random.normal(tf.shape(X), stddev=self.stddev)
			return X + noise
		else:
			return X

	def compute_output_shape(self, batch_input_shape):
		return batch_input_shape
```
</p></details>

<details><summary>Create **Custom** activation, weight initializer, regularizer, constraints</summary><p>

```
def my_softplus(z): # return value is just tf.nn.softplus(z)
	return tf.math.log(tf.exp(z) + 1.0)

def my_glorot_initializer(shape, dtype=tf.float32):
	stddev = tf.sqrt(2. / (shape[0] + shape[1]))
	return tf.random.normal(shape, stddev=stddev, dtype=dtype)

def my_l1_regularizer(weights):
	return tf.reduce_sum(tf.abs(0.01 * weights))

def my_positive_weights(weights): # return value is just
tf.nn.relu(weights)
	return tf.where(weights < 0., tf.zeros_like(weights), weights)

layer = keras.layers.Dense(30, activation=my_softplus,
							kernel_initializer=my_glorot_initializer,
							kernel_regularizer=my_l1_regularizer,
							kernel_constraint=my_positive_weights)
```

```
# If you want to make the parameters be saved, use SubClass API.
# Note that you must implement the call() method for losses, layers (including activation functions), and models, or the __call__() method 
# for regularizers, initializers, and constraints. For metrics, things are a bit different
class MyL1Regularizer(keras.regularizers.Regularizer):
	def __init__(self, factor):
		self.factor = factor
	def __call__(self, weights):
		return tf.reduce_sum(tf.abs(self.factor * weights))
	def get_config(self):
		return {"factor": self.factor}
```
</p></details>

<details><summary>Create **Custom** Model (Multiple Layers contained together)</summary><p>
```
# Create a Residual Block.
class ResidualBlock(keras.layers.Layer):
	def __init__(self, n_layers, n_neurons, **kwargs):
		super().__init__(**kwargs)
		self.hidden = [keras.layers.Dense(n_neurons, activation="elu", kernel_initializer="he_normal")
						for _ in range(n_layers)]
	
	def call(self, inputs):
		Z = inputs
		for layer in self.hidden:
			Z = layer(Z)
		return inputs + Z
```
```
class ResidualRegressor(keras.Model):
	def __init__(self, output_dim, **kwargs):
		super().__init__(**kwargs)
		self.hidden1 = keras.layers.Dense(30, activation="elu", kernel_initializer="he_normal")
		self.block1 = ResidualBlock(2, 30)
		self.block2 = ResidualBlock(2, 30)
		self.out = keras.layers.Dense(output_dim)

	def call(self, inputs):
		Z = self.hidden1(inputs)
		for _ in range(1 + 3):
			Z = self.block1(Z)
		Z = self.block2(Z)
		return self.out(Z)
```
</p></details>

<details><summary>Create **Custom** Training Loop</summary><p>
```
# <h4>Build your model</h4>
l2_reg = keras.regularizers.l2(0.05)
model = keras.models.Sequential([
	keras.layers.Dense(30, activation="elu",
						kernel_initializer="he_normal",
						kernel_regularizer=l2_reg),
	keras.layers.Dense(1, kernel_regularizer=l2_reg)
])
```

```
# <h4>Define random_batch & status_bar function</h4>
def random_batch(X, y, batch_size=32):
	idx = np.random.randint(len(X), size=batch_size)
	return X[idx], y[idx]
	
def print_status_bar(iteration, total, loss, metrics=None):
	metrics = " - ".join(["{}: {:.4f}".format(m.name, m.result())
						for m in [loss] + (metrics or [])])
	end = "" if iteration < total else "\n"
	print("\r{}/{} - ".format(iteration, total) + metrics, end=end)
```

```
# <h4>Define your hyperparameters</h4>
n_epochs = 5
batch_size = 32
n_steps = len(X_train) // batch_size
optimizer = keras.optimizers.Nadam(lr=0.01)
loss_fn = keras.losses.mean_squared_error
mean_loss = keras.metrics.Mean()
metrics = [keras.metrics.MeanAbsoluteError()]
```


```
# <h4>Write the training loop</h4>
for epoch in range(1, n_epochs + 1):
	print("Epoch {}/{}".format(epoch, n_epochs))
	for step in range(1, n_steps + 1):
		X_batch, y_batch = random_batch(X_train_scaled, y_train)
		with tf.GradientTape() as tape:
			y_pred = model(X_batch, training=True)
			main_loss = tf.reduce_mean(loss_fn(y_batch, y_pred))
			loss = tf.add_n([main_loss] + model.losses)
		gradients = tape.gradient(loss, model.trainable_variables)
		optimizer.apply_gradients(zip(gradients, model.trainable_variables))
		mean_loss(loss)

		for metric in metrics:
			metric(y_batch, y_pred)
		print_status_bar(step * batch_size, len(y_train), mean_loss, metrics)
	print_status_bar(len(y_train), len(y_train), mean_loss, metrics)
	for metric in [mean_loss] + metrics:
		metric.reset_states()
```
</p></details>
