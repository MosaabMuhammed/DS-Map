<h1 id="losses">Losses</h1>

<div style="width:1000px;margin:auto">


<details><summary><b>binary_crossentropy</b></summary><p><ul>
<li>Used with <b>binary classification</b> problem.</li>
<li>Can be used for <b>Multi-class, multilabel classification</b> problem</li>.
<li>The last layer has only <b>1 neuron</b> [Binary Classification] and <b>n-1 neurons</b> [Multi-Label Classification] where n is the number of classes.</li>
<li>The last layer has <b>sigmoid</b> activation function.</li>
<li>The <b>y_labels</b> is an array of ONLY <b>zeros</b> and <b>ones</b></li></ul><pre><code># Last layer.
    keras.layers.Dense(1, activation="sigmoid")

model.compile(optimizer="adam",
            loss="binary_crossentropy",
            metrics=["accuracy"])
</code></pre>

<h4>To predict</h4><pre><code>result = model.predict(X_valid)
# result is a class 0 or 1.
</code></pre>
</p></details>

<details><summary><b>categorical_crossentropy</b></summary><p><ul>
<li>Used for <b>binary</b> or <b>multi-class</b> classification problems.</li>
<li>The last layer has nuerons as the <b>number of classes</b> in y_labels.</li>
<li>The last layer must have <b>"softmax"</b> activation function.</li>
<li>The y_labels MUST be <b>one-hot encoded</b>.</li>
</ul><pre><code># To one-hot encode the y_labels.
from tensorflow.keras.utils import to_categorical

y_labels = to_categorical(y_labels, len(np.unique(y_labels)))
</code></pre><pre><code># Last Layer.
    keras.layers.Dense(len(np.unique(y_labels)), activation="softmax")

model.compile(loss="categorical_crossentropy", ...)
</code></pre>
<pre><code># To predict.
results = model.predict(X_valid)
class_idx = np.argmax(results)
</code></pre>
</p></details>

<details><summary><b>sparse_categorical_crossentropy</b></summary><p><ul>
<li>Used for <b>multi-classification classification</b> problem.</li>
<li>The last layer has a number of neurons as the <b>number of classes</b> in y_labels.</li>
<li>The last layer has <b>"softmax"</b> activation function.</li>
<li><b>y_labels</b> MUST be an <b>array of intengers</b>.</li></ul>
<pre><code># Last Layer.
    keras.layers.Dense(len(np.unique(y_labels)), activation="softmax")

model.compile(loss="sparse_categorical_crossentropy", ...)
</code></pre>
<pre><code># To predict.
results = model.predict(X_valid)
class_idx = np.argmax(results)
</code></pre>
</p></details>

<details><summary>Create <b>Custom Loss Function</b></summary>
<pre><code># Define Huber Loss function
def huber_fn(y_true, y_pred):
    error = y_true - y_pred
    is_small_error = tf.abs(error) &lt; 1
    squared_loss = tf.square(error) / 2
    linear_loss = tf.abs(error) - 0.5
    return tf.where(is_small_error, squared_loss, linear_loss)

# Use the loss.
model.compile(loss=huber_fn, optimizer="nadam")
model.fit(X_train, y_train, [...])

# Load the loss when loading the saved model.
model = keras.models.load_model("my_model_with_a_custom_loss.h5",
                                custom_objects={"huber_fn": huber_fn})
</code></pre>

<pre><code># If you want Keras to save the parameters of your loss.
class HuberLoss(keras.losses.Loss):
    def __init__(self, threshold=1.0, **kwargs):
        self.threshold = threshold
        super().__init__(**kwargs)

    def call(self, y_true, y_pred):
        error = y_true - y_pred
        is_small_error = tf.abs(error) &lt; self.threshold
        squared_loss = tf.square(error) / 2
        linear_loss = self.threshold * tf.abs(error) - self.threshold**2
        / 2
        return tf.where(is_small_error, squared_loss, linear_loss)

    def get_config(self):
        base_config = super().get_config()
        return {**base_config, "threshold": self.threshold}

model.compile(loss=HuberLoss(2.), optimizer="nadam")

model = keras.models.load_model("my_model_with_a_custom_loss_class.h5",
    custom_objects={"HuberLoss": HuberLoss})
</code></pre>
</details>

<details><summary>Create <b>Custom Internal Loss</b> to be calculated at the end of each epoch</summary>
<pre><code>
class ReconstructingRegressor(keras.Model):
	def __init__(self, output_dim, **kwargs):
		super().__init__(**kwargs)
		self.hidden = [keras.layers.Dense(30, activation="selu",
				kernel_initializer="lecun_normal") for _ in range(5)]
		self.out = keras.layers.Dense(output_dim)
	
	def build(self, batch_input_shape):
		n_inputs = batch_input_shape[-1]
		self.reconstruct = keras.layers.Dense(n_inputs)
		super().build(batch_input_shape)

	def call(self, inputs):
		Z = inputs
		for layer in self.hidden:
			Z = layer(Z)
		reconstruction = self.reconstruct(Z)
		recon_loss = tf.reduce_mean(tf.square(reconstruction - inputs))
		self.add_loss(0.05 * recon_loss)
		return self.out(Z)
	
'''	
Epoch 1/5
11610/11610 [=============] [...] loss: 4.3092 - reconstruction_error:
1.7360
Epoch 2/5
11610/11610 [=============] [...] loss: 1.1232 - reconstruction_error:0.8964
[...]
'''
</code></pre>
</details>
</div>