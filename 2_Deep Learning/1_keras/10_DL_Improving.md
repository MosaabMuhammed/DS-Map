<h1 id="improvingperformance">Improving Performance</h1>

<details><summary><b>Partial Layers</b></summary><p>
```
from functools import partial

RegularizedDense = partial(tf.keras.layers.Dense,
                           activation="elu",
                           kernel_initializer="he_normal",
                           kernel_reqularizer=tf.keras.regularizers.l2(0.01))

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=[28, 28]),
    RegularizedDense(300),
    RegularizedDense(100),
    RegularizedDense(10, activation="softmax",
                     kernel_initializer="glorot_uniform")
])
```

</p></details>

<details><summary><b>Learning Curves</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Learning-curves"><b style='color:#333'>1. Learning Curves</b></a> </p>

</p></details>

<details><summary><b>Batch Normalization</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Batch-Normalization"><b style='color:#333'>Batch Normalization</b></a> </p>

<h4>You can try both of the following, and see which one works best for you</h4>
```
# Adding BatchNormalization after activation.
input1      = tf.keras.layers.Input(shape=[2])
batch_norm1 = tf.keras.layers.BatchNormalization()(input1)
hidden1     = tf.keras.layers.Dense(50, activation="elu", kernel_initializer="he_normal")(batch_norm1)
batch_norm2 = tf.keras.layers.BatchNormalization()(hidden1)
hidden2     = tf.keras.layers.Dense(30, activation="elu", kernel_initializer="he_normal")(batch_norm2)
batch_norm3 = tf.keras.layers.BatchNormalization()(hidden2)
output1     = tf.keras.layers.Dense(1, activation="sigmoid")
```

```
# Adding BatchNormalization BEFORE activation.
input1      = tf.keras.layers.Input(shape=[2])
batch_norm1 = tf.keras.layers.BatchNormalization()(input1)
hidden1     = tf.keras.layers.Dense(50, kernel_initializer="he_normal")(batch_norm1)
batch_norm2 = tf.keras.layers.BatchNormalization()(hidden1)
elu1        = tf.keras.layers.Activation("elu")(batch_norm2)

hidden2     = tf.keras.layers.Dense(30, kernel_initializer="he_normal")(elu1)
batch_norm3 = tf.keras.layers.BatchNormalization()(hidden2)
elu2        = tf.keras.layers.Activation("elu")(batch_norm3)
output1     = tf.keras.layers.Dense(1, activation="sigmoid")
```
</p></details>

<details><summary><b>Dropout</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Weight-Regularization-&amp;-Dropout"><b style='color:#333'>3. Dropout</b></a> </p>
<ul>
<li>Since dropout is only active during training, the training loss is penalized compared to the validation loss, so computing the two can be misleading. In particular, a model maybe overfitting and yet have similar training and validation losses. So make sure to evalute the training loss without dropout.</li>
<li>Alternatively, you can call the fit() method inside a (with tf.keras.backend.learning_phase_scope(1)) block: this will force dropout to be active during both training and validation</li>
</ul>

```
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dropout(rate=0.2),
    keras.layers.Dense(300, activation="elu", kernel_initializer="he_normal"),
    keras.layers.Dropout(rate=0.2),
    keras.layers.Dense(100, activation="elu", kernel_initializer="he_normal"),
    keras.layers.Dropout(rate=0.2),
    keras.layers.Dense(10, activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy", optimizer="nadam", metrics=["accuracy"])
n_epochs = 2
history = model.fit(X_train_scaled, y_train, epochs=n_epochs,
                    validation_data=(X_valid_scaled, y_valid))

```
<li>If you want to regularize a self.normalizing network based on the SELU activation function, you should use <b>AlphaDropout</b>: this is a variant of dropout that preserves the mean and std of its inputs.</li>
```
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.AlphaDropout(rate=0.2),
    keras.layers.Dense(300, activation="selu", kernel_initializer="lecun_normal"),
    keras.layers.AlphaDropout(rate=0.2),
    keras.layers.Dense(100, activation="selu", kernel_initializer="lecun_normal"),
    keras.layers.AlphaDropout(rate=0.2),
    keras.layers.Dense(10, activation="softmax")
])
optimizer = keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True)
model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
n_epochs = 20
history = model.fit(X_train_scaled, y_train, epochs=n_epochs,
                    validation_data=(X_valid_scaled, y_valid))

```
</p></details>

<details><summary><b>Weight Regularization</b></summary>
<p>
<li><a href="https://keras.io/initializers/"><b style='color:#333'>1. Available initializers in Keras</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Deep%20Learning%20Nanodegree/0_Data/deep-learning-master/weight-initialization/weight_initialization.html#Weight-Initialization"><b style='color:#333'>2. Which one is better (Experiment)</b></a> </p>

</p>
</details>

<details><summary><b>Data Augmentation</b></summary>
<p>

<p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/20.%20Image%20Augmentation%20in%20Keras.html"><b style='color:#333'>1. Concept (Udacity)</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Data-augmentation"><b style='color:#333'>2. Code Example</b></a> </p>

</p></details>

<details><summary><b>Gradient Clipping</b> [solving exploding gradient]</summary><p>
```
# Try to use "clipvalue" and "clipnorm", and see which one works best for your data.
optimizer = keras.optimizers.SGD(clipvalue=1.0)
model.compile(loss="mse", optimizer=optimizer)

# now, every gradient will be between -1 and 1.
```
</p></details>

<details><summary><b>Regularization</b></summary><p>
<h4>L1</h4>
```
layer = tf.keras.layers.Dense(100, activation="elu", kernel_initializer="he_normal", kernel_reqularizer=tf.keras.reqularizers.l1(0.01))
```

<h4>L2</h4>
```
layer = tf.keras.layers.Dense(100, activation="elu", kernel_initializer="he_normal", kernel_reqularizer=tf.keras.reqularizers.l2(0.01))
```

<h4>Elastic Net [L1 and L2]</h4>
```
layer = tf.keras.layers.Dense(100, activation="elu", kernel_initializer="he_normal", kernel_reqularizer=tf.keras.reqularizers.l1_l2(0.01))
```
</p></details>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Embeddings"><b style='color:#333'>5. Embedding</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Sentiment-prediction-on-movie-Reviews"><b style='color:#333'>Ex: Sentiment Analysis on Movie Review</b></a> </p>
 