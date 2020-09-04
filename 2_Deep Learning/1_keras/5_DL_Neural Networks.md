# Nerual Networks

<div style="width:1000px;margin:auto">
<details><summary><strong>1. Linear Model</strong> (Digit Recoginzer)</summary>

<p>

<h4 id="1importrequiredlibraries">1. Import required libraries.</h4>
~~~python
from keras.models import Sequential
from keras.layers.core import Lambda, Dense, Flatten, Dropout
~~~

<h4 id="2desingthearchitectureofthemodel">2. Desing the architecture of the model.</h4>

~~~python
def standardize(x):
    return (x - mean_px)/std_px
~~~
~~~python
model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

print('~> Input Shape:', model.input_shape)
print('~> Output Shape:', model.output_shape)
~~~

<h4 id="3setoptimizermetricandlossfunction">3. Set Optimizer, Metric, and loss function.</h4>
~~~Python
from keras.optimizers import RMSprop

model.compile(optimizer=RMSprop(lr=.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])
~~~

<h4 id="4dataagumentation">4. Data Agumentation.</h4>
~~~python
from keras.preprocessing import image

gen = image.ImageDataGenerator()

from sklearn.model_selection import train_test_split

X = X_train
y = y_train

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=.1, random_state=42)
train_batches = gen.flow(X_train, y_train, batch_size=64)
val_batches   = gen.flow(X_val, y_val, batch_size=64)
~~~

<h4 id="5fitthemodel">5. Fit the model.</h4>
~~~python
history = model.fit_generator(generator=train_batches, 
                              steps_per_epoch=train_batches.n, 
                              epochs=5,
                              validation_data=val_batches,
                              validation_steps=val_batches.n)
~~~
</p></details>


<details><summary><strong>2. Fully Connected Model</strong> (Digit Recoginzer)</summary><p>
<h4 id="desingthearchitectureofthemodel">Desing the architecture of the model.</h4>
~~~python
def get_fc_model():
    model = Sequential([
        Lambda(standardize, input_shape=(28, 28, 1)),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='Adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model
~~~

<h4 id="callandhypertune">Call and hypertune.</h4>
~~~python
fc = get_fc_model()
fc.optimizer.lr=0.01
~~~

#### Run
~~~python
history=fc.fit_generator(generator=batches, steps_per_epoch=batches.n, epochs=1, 
                    validation_data=val_batches, validation_steps=val_batches.n)
~~~
</p></details>

<details><summary><strong>3. Functional API</strong></summary><p>
<h4>Strucuture of the model</h4>
```
import tensorflow as tf

input_A = tf.keras.layers.Input(shape=[5], name="Input_A")
input_B = tf.keras.layers.Input(shape=[6], name="Input_B")

hidden1 = tf.keras.layers.Dense(30, activation="relu", name="Hidden_1")(input_B)
hidden2 = tf.keras.layers.Dense(30, activation="relu", name="Hidden_2")(hidden1)
concat  = tf.keras.layers.concatenate([input_A, hidden2])
output  = tf.keras.layers.Dense(1, activation="linear", name="Output")(concat)
aux_out = tf.keras.layers.Dense(1, activation="linear", name="Aux_Output")(hidden2)

model = tf.keras.models.Model(inputs=[input_A, input_B], outputs=[output, aux_out])

# Visualize the structure of the model.
tf.keras.utils.plot_model(model)
```

<h4>Reset the dataset to be fed</h4>
```
X_train_A, X_train_B = X_train_scaled[:, :5], X_train_scaled[:, 2:]
X_valid_A, X_valid_B = X_valid_scaled[:, :5], X_valid_scaled[:, 2:]
X_test_A, X_test_B   = X_test_scaled[:, :5],  X_test_scaled[:, 2:]

# Fit and Compile.
# you can use a dictionary to feed the losses like this:
# {"output1": "mse", "output2": "cross_entropy"}, but you have to name those output layers.
# Secondly, try to figure out the loss_weights for each loss.
model.compile(loss=["mse", "mse"],
              loss_weights=[.9, .1],
              optimizer="sgd")

history = model.fit([X_train_A, X_train_B],
                    [y_train, y_train],
                    epochs=20,
                    validation_data=([X_valid_A, X_valid_B], [y_valid, y_valid]))
```
</p></details>

<details><summary><strong>4. SubClass API</strong></summary><p>
```
# In call(), you can use if statements, for loops, whatever you want!
class WideAndDeepModel(tf.keras.models.Model):
    def __init__(self, units=30, activation="relu", **kwargs):
        super().__init__(**kwargs)  # Handles standard args (e.g., name)
        self.hidden1     = tf.keras.layers.Dense(units, activation=activation)
        self.hidden2     = tf.keras.layers.Dense(units, activation=activation)
        self.main_output = tf.keras.layers.Dense(1)
        self.aux_output  = tf.keras.layers.Dense(1)

    def call(self, inputs):
        input_A, input_B = inputs

        hidden1 = self.hidden1(input_B)
        hidden2 = self.hidden2(hidden1)
        concat  = tf.keras.layers.concatenate([input_A, hidden2])
        min_out = self.main_output(concat)
        aux_out = self.aux_output(hidden2)

        return main_output, aux_output

model = WideAndDeepModel()
```
</p></details>

<a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/5%20Gradient%20Descent.html#Logistic-Regression-Model">Manual Hyperparameter Tunning</a>

</div>