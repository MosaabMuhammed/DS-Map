<h1 id="nbspcallbacksnbsp">CallBacks</h1>

[<span style='color:#333'>Ex on **Tensorboard** & **EarlyStopping**  & **Checkpoint**</span>](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/solutions/5%20Gradient%20Descent%20Exercises%20Solution.html#Exercise-4) 

<details><summary><strong>ReduceLROnPlateau</strong></summary>
<p>
<p><a href="https://keras.io/callbacks/#reducelronplateau"><strong>Docs</strong></a></p>

- Reduce learning rate when a metric has stopped improving.

<h4 id="1class">1. Class</h4>
~~~python
keras.callbacks.callbacks.ReduceLROnPlateau(
                        monitor='val_loss', 
                        factor=0.1, 
                        patience=10, 
                        verbose=0, 
                        mode='auto', 
                        min_delta=0.0001, 
                        cooldown=0, 
                        min_lr=0)
~~~

<h4 id="2example">2. Example</h4>
~~~python
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                              patience=5, min_lr=0.001)
model.fit(X_train, Y_train, callbacks=[reduce_lr])
~~~
</p>
</details>

<details><summary><strong>EarlyStopping</strong></summary>
<p>
<a href="https://keras.io/callbacks/#earlystopping"><strong>Docs</strong></a>

<h4 id="1class">1. Class</h4>
~~~python
keras.callbacks.callbacks.EarlyStopping(
                        monitor='val_loss', 
                        min_delta=0, 
                        patience=0, 
                        verbose=0, 
                        mode='auto', 
                        baseline=None, 
                        restore_best_weights=False)

~~~

<h4 id="2example">2. Example</h4>
~~~python

~~~
</p>
</details>

<details><summary><b>ModelCheckPointer</b></summary>
<p>
<p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/06.%20Model%20Validation%20in%20Keras.html">Example from DLND</a> </p>
<h4>1. Class</h4>
~~~python
keras.callbacks.callbacks.ModelCheckpoint(
								filepath, 
								monitor='val_loss', 
								verbose=0, 
								save_best_only=False, 
								save_weights_only=False, 
								mode='auto', 
								period=1)

~~~
<h4>2. Nice Example on Saving best weights</h4>
~~~python
# Checkpoint the weights when validation accuracy improves
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
import numpy
numpy.random.seed(seed)
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# checkpoint
filepath="weights-improvement-{epoch:02d}-{val_accuracy:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]
# Fit the model
model.fit(X, Y, validation_split=0.33, epochs=150, batch_size=10, callbacks=callbacks_list, verbose=0)
~~~

<h4>3. Loading the best weights</h4>
~~~python
# How to load and use weights from a checkpoint
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
import numpy
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# load weights
model.load_weights("weights.best.hdf5")
# Compile model (required to make predictions)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print("Created model and loaded weights from file")
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# estimate accuracy on whole dataset using loaded weights
scores = model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
~~~
</p>
</details>

<details><summary><b>Custom Callback</b>- Stopping when reached some loss value</summary><p>
```
import tensorflow as tf
print(tf.__version__)

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('loss')<0.4):
      print("\nReached 60% accuracy so cancelling training!")
      self.model.stop_training = True

callbacks = myCallback()

# Your models here.

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])
```

<h4>You can call the following methods:</h4>
<ul>
<li>on_train_begin()</li>
<li>on_train_end()</li>
<li>on_batch_end()</li>
<li>on_batch_begin()</li>
<li>on_predict_begin()</li>
<li>on_predict_end()</li>
</ul>
</p></details>

<details><summary><b>LR Schedular</b> How to choose the perfect learning rate</summary>
```
lr_schedule = tf.keras.callbacks.LearningRateScheduler(
    lambda epoch: 1e-8 * 10**(epoch / 20))
    
optimizer = tf.keras.optimizers.SGD(lr=1e-8, momentum=0.9)

model.compile(loss="mse", optimizer=optimizer)

history = model.fit(dataset, epochs=100, callbacks=[lr_schedule], verbose=0)
```

```
# Plot lrs along epochs, choose the lowest value.
# Then run your model again with the updated value of the learning rate.
lrs = 1e-8 * (10 ** (np.arange(100) / 20))
plt.semilogx(lrs, history.history["loss"])
plt.axis([1e-8, 1e-3, 0, 300])
```
</details>

<details><summary><b>Tensorboard</b></summary>
```
import os
root_logdir = os.path.join(os.curdir, "my_logs")

def get_run_logdir():
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(root_logdir, run_id)

run_logdir = get_run_logdir()

# 2. Fit the model.
tensorboard_cv = tf.keras.callbacks.TensorBoard(run_logdir)
history = model.fit(X_train_scaled,
                    y_train,
                    epochs=20,
                    validation_data=(X_valid_scaled, y_valid),
                    callbacks=[tensorboard_cv])
                    
# 3. Show Tensorboard
!tensorboard --logdir=./my_logs --port=6006

# Note, the last command won't work in colab, search for it.
```
</details>
