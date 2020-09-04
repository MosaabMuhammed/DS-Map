<h1 id="improvingperformance">Improving Performance</h1>

<div style="width:1000px;margin:auto">
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

<details><summary><b>Depthwise Separable Convoluation</b></summary><p>
It performs a spatial convolution on each channel of its input, independently, before mising output channels via a pointwise convolution (1x1 convolution).<br><br>This is equivalent to separating the learning of spatial features and the learning of channel-wise features, which makes a lot of sense if you assume that spatial locations in the input are highly correlated, but different channels are fairly independent.<br><br>It requires significantly fewer parameters and involves fewer computations, thus resulting in smaller, speedier models.<br><br>These advantanges become especially important when you're training small models from scratch on limited data.

```
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras import layers 

height = 64
width = 64
channels = 3
num_classes = 10

model = Sequential()
model.add(layers.SeparableConv2D(32, 3, activation="relu", input_shape=(height, width, channels,)))
model.add(layers.SeparableConv2D(64, 3, activation="relu"))
model.add(layers.MaxPooling2D(2))

model.add(layers.SeparableConv2D(64, 3, activation='relu'))
model.add(layers.SeparableConv2D(128, 3, activation='relu'))
model.add(layers.MaxPooling2D(2))

model.add(layers.SeparableConv2D(64, 3, activation='relu'))
model.add(layers.SeparableConv2D(128, 3, activation='relu'))
model.add(layers.GlobalAveragePooling2D())

model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

```
</p></details>

<details><summary><b>Batch Normalization</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Batch-Normalization"><b style='color:#333'>Batch Normalization</b></a> </p>

<p>You can try both of the following, and see which one works best for you:<br>You can use it after Convolutional layer too.</p>
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

<details><summary><b>Monte-Carlo Dropout</b></summary><p>
<p><b>MC Dropout</b> simply is applying dropout on testing data, and taking n number of predictions for testing data, then averging them.</p>
<h4>1. If you have a model trained on a normal Droptout</h4>
```
with tf.keras.backend.learning_phase_scope(1):  # Force training mode = dropout on
    y_probas = np.stack([model.predict(X_test) for sample in range(500)])

# Take the mean along the first axis, which is number of samples.
y_proba = y_probas.mean(axis=0) 

# From probabilities to classes.
y_pred = np.round(y_proba)
# OR
y_pred = np.argmax(y_proba)
```

<h4>2. MC Dropout Implementation</h4>
```
class MCDropout(tf.keras.layers.Dropout):
    def call(self, inputs):
        return super().call(inputs, training=True)

class MCAlphaDropout(tf.keras.layers.AlphaDropout):
    def call(self, inputs):
        return super().call(inputs, training=True)
```
```
# Build the model as normal
tf.random.set_seed(42)
np.random.seed(42)

mc_model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(50, activation="elu", kernel_initializer="he_normal", input_shape=[10]),
    MCDropout(0.2),
    tf.keras.layers.Dense(30, activation="elu", kernel_initializer="he_normal"),
    MCDropout(.2),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
```
```
# Then Predict.
y_probas = np.stack([mc_model.predict(X_test) for _ in range(100)])

y_pred = np.round(y_probas.mean(axis=0))
print(metrics.accuracy_score(y_test, y_pred))
```
</p></details>

<details><summary><b>Max-Norm Regularization</b></summary><p>
```
layer = tf.keras.layers.Dense(100,
                              activation="selu",
                              kernel_initializer="lecun_normal",
                              kernel_constraint=tf.keras.constraints.max_norm(1., axis=0))

MaxNormDense = partial(tf.keras.layers.Dense,
                       activation="selu",
                       kernel_initializer="lecun_normal",
                       kernel_constraint=tf.keras.constraints.max_norm(1.))

model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=[10]),
    MaxNormDense(50),
    MaxNormDense(30),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
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

<details><summary><b>Residual Conncetions</b></summary><p>
- It helps with <b>vanishing gradient</b> and <b>representational bottlenecks</b> problems.<br>
- Adding it to any model that has more than <b>10 layers</b> is likely to be beneficial.
```
from tensorflow.keras import layers

x = ...
y = layers.Conv2D(128, 3, activation="relu", padding="same")(x)
y = layers.Conv2D(128, 3, activation="relu", padding="same")(y)
y = layers.Conv2D(128, 3, activation="relu", padding="same")(y)

y = layers.add([y, x])
```

<h4>If they don't have the same shape</h4>
```
# Note, if the 2 layers that are going to be added have different length/sizes, do the following: Dense layer without activation / convolutional feature maps 1x1 convolutions without activation, to insure they have the same shape.
from tensorflow.keras import layers

x = ...
y = layers.Conv2D(128, 3, activation="relu", padding="same")(x)
y = layers.Conv2D(128, 3, activation="relu", padding="same")(y)
y = layers.MaxPooling2D(2, stride=2)(y)

residual = layers.Conv2D(128, 1, strides=2, padding='same')(x)
y = layers.add([y, residual])
```
</p></details>

<details><summary><b>Hyperparamter Optimization</b> [Hyperas]</summary><p>
```
!pip install hyperas

from hyperopt import Trials, STATUS_OK, tpe
from keras.datasets import mnist
from keras.layers.core import Dense, Dropout, Activation
from keras.models import Sequential
from keras.utils import np_utils

from hyperas import optim
from hyperas.distributions import choice, uniform


def data():
    """
    Data providing function:

    This function is separated from create_model() so that hyperopt
    won't reload data for each evaluation run.
    """
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    nb_classes = 10
    y_train = np_utils.to_categorical(y_train, nb_classes)
    y_test = np_utils.to_categorical(y_test, nb_classes)
    return x_train, y_train, x_test, y_test


def create_model(x_train, y_train, x_test, y_test):
    """
    Model providing function:

    Create Keras model with double curly brackets dropped-in as needed.
    Return value has to be a valid python dictionary with two customary keys:
        - loss: Specify a numeric evaluation metric to be minimized
        - status: Just use STATUS_OK and see hyperopt documentation if not feasible
    The last one is optional, though recommended, namely:
        - model: specify the model just created so that we can later use it again.
    """
    model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation('relu'))
    model.add(Dropout({{uniform(0, 1)}}))
    model.add(Dense({{choice([256, 512, 1024])}}))
    model.add(Activation({{choice(['relu', 'sigmoid'])}}))
    model.add(Dropout({{uniform(0, 1)}}))

    # If we choose 'four', add an additional fourth layer
    if {{choice(['three', 'four'])}} == 'four':
        model.add(Dense(100))

        # We can also choose between complete sets of layers

        model.add({{choice([Dropout(0.5), Activation('linear')])}})
        model.add(Activation('relu'))

    model.add(Dense(10))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', metrics=['accuracy'],
                  optimizer={{choice(['rmsprop', 'adam', 'sgd'])}})

    result = model.fit(x_train, y_train,
              batch_size={{choice([64, 128])}},
              epochs=2,
              verbose=2,
              validation_split=0.1)
    #get the highest validation accuracy of the training epochs
    validation_acc = np.amax(result.history['val_acc']) 
    print('Best validation acc of epoch:', validation_acc)
    return {'loss': -validation_acc, 'status': STATUS_OK, 'model': model}


if __name__ == '__main__':
    best_run, best_model = optim.minimize(model=create_model,
                                          data=data,
                                          algo=tpe.suggest,
                                          max_evals=5,
                                          trials=Trials())
    X_train, Y_train, X_test, Y_test = data()
    print("Evalutation of best performing model:")
    print(best_model.evaluate(X_test, Y_test))
    print("Best performing model chosen hyper-parameters:")
    print(best_run)
```
</p></details>


<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Embeddings"><b style='color:#333'>5. Embedding</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Sentiment-prediction-on-movie-Reviews"><b style='color:#333'>Ex: Sentiment Analysis on Movie Review</b></a> </p>
 
</div>