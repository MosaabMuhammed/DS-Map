<h1 id="nbspcallbacksnbsp">CallBacks</h1>

<div style="width:1000px;margin:auto">

<a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/solutions/5%20Gradient%20Descent%20Exercises%20Solution.html#Exercise-4"><span style='color:#333'>Ex on Tensorboard & EarlyStopping  & Checkpoint</span></a>


<details><summary><strong>ReduceLROnPlateau</strong></summary>
<p>
<p><a href="https://keras.io/callbacks/#reducelronplateau"><strong>Docs</strong></a></p>

- Reduce learning rate when a metric has stopped improving.

<h4 id="1class">1. Class</h4><pre><code class="python language-python">keras.callbacks.callbacks.ReduceLROnPlateau(
                        monitor='val_loss', 
                        factor=0.1, 
                        patience=10, 
                        verbose=0, 
                        mode='auto', 
                        min_delta=0.0001, 
                        cooldown=0, 
                        min_lr=0)
</code></pre>

<h4 id="2example">2. Example</h4><pre><code class="python language-python">reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                              patience=5, min_lr=0.001)
model.fit(X_train, Y_train, callbacks=[reduce_lr])
</code></pre>
</p>
</details>

<details><summary><strong>EarlyStopping</strong></summary>
<p>
<a href="https://keras.io/callbacks/#earlystopping"><strong>Docs</strong></a>

<h4 id="1class">1. Class</h4><pre><code class="python language-python">keras.callbacks.callbacks.EarlyStopping(
                        monitor='val_loss', 
                        min_delta=0, 
                        patience=0, 
                        verbose=0, 
                        mode='auto', 
                        baseline=None, 
                        restore_best_weights=False)
</code></pre>

<h4 id="2example">2. Example</h4><pre><code class="python language-python">
</code></pre>
</p>
</details>

<details><summary><b>ModelCheckPointer</b></summary>
<p>
<p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/06.%20Model%20Validation%20in%20Keras.html">Example from DLND</a> </p>
<h4>1. Class</h4><pre><code class="python language-python">keras.callbacks.callbacks.ModelCheckpoint(
                                filepath, 
                                monitor='val_loss', 
                                verbose=0, 
                                save_best_only=False, 
                                save_weights_only=False, 
                                mode='auto', 
                                period=1)
</code></pre>
<h4>2. Nice Example on Saving best weights</h4><pre><code class="python language-python"># Checkpoint the weights when validation accuracy improves
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
</code></pre>

<h4>3. Loading the best weights</h4><pre><code class="python language-python"># How to load and use weights from a checkpoint
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
</code></pre>
</p>
</details>

<details><summary><b>Custom Callback</b>- Stopping when reached some loss value</summary><p><pre><code>import tensorflow as tf
print(tf.__version__)

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('loss')&lt;0.4):
      print("\nReached 60% accuracy so cancelling training!")
      self.model.stop_training = True
      # You can access validation data too.
      # self.validation_data --&gt; The value of what was passed to fit as validation data.

callbacks = myCallback()

# Your models here.

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])
</code></pre>

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

<details><summary><b>ActivationLogger</b> [Custom]</summary><p><pre><code>class ActivationLogger(keras.callbacks.Callback):

    def set_model(self, model):
        self.model = model
        layer_outputs = [layer.output for layer in model.layers]
        self.activations_model = keras.models.Model(model.input, layer_outputs)

    def on_epoch_end(self, epoch, logs=None):
        if self.validation_data is None:
            raise RuntimeError("Required validation_data.")
        validation_sample = self.validation_data[0][0:1]
        activations = self.activations_model.predict(validation_sample)
        f = open('activations_at_epoch_' + str(epoch) + '.npz', 'w')
        np.savez(f, activations)
        f.close()
</code></pre>
</p></details>

<details><summary><b>LR Schedular</b> How to choose the perfect learning rate</summary><ul>
<li><details><summary><b>Power Scheduling</b></summary><p><pre><code># lr(t) = lr_0(t) / ( + t/s)**c
# t  = number of epoch.
# s = number of steps, after s steps, lr = lr/2, and so on.
# c = 1
optimizer = tf.keras.optimizers.SGD(lr=0.01, decay=1e-4)
</code></pre>

</p></details></li>

<li><details><summary><b>Exponential Scheduling</b></summary><p>
<h4>First Method</h4><pre><code>lr_schedule = tf.keras.callbacks.LearningRateScheduler(
    lambda epoch: 1e-8 * 10**(epoch / 20))

optimizer = tf.keras.optimizers.SGD(lr=1e-8, momentum=0.9)

model.compile(loss="mse", optimizer=optimizer)

history = model.fit(dataset, epochs=100, callbacks=[lr_schedule], verbose=0)
</code></pre>
<pre><code># Plot lrs along epochs, choose the lowest value.
# Then run your model again with the updated value of the learning rate.
lrs = 1e-8 * (10 ** (np.arange(100) / 20))
plt.semilogx(lrs, history.history["loss"])
plt.axis([1e-8, 1e-3, 0, 300])
</code></pre>
<h4>Another way to do it</h4><pre><code>s = 20 * len(X_train) // 32 # number of steps in 20 epochs (batch size = 32)
learning_rate = keras.optimizers.schedules.ExponentialDecay(0.01, s, 0.1)
optimizer = keras.optimizers.SGD(learning_rate)
</code></pre>
</p></details></li>

<li><details><summary><b>Piecewise Constant Scheduling</b></summary><p><pre><code>def piecewise_constant_fn(epoch):
    if epoch &lt; 5:
        return 0.01
    elif epoch &lt; 15:
        return 0.005
    else:
        return 0.001
</code></pre>
<pre><code>def piecewise_constant(boundaries, values):
    boundaries = np.array([0] + boundaries)
    values = np.array(values)
    def piecewise_constant_fn(epoch):
        return values[np.argmax(boundaries &amp;gt; epoch) - 1]
    return piecewise_constant_fn

piecewise_constant_fn = piecewise_constant([5, 15], [0.01, 0.005, 0.001])
</code></pre>
<pre><code>lr_scheduler = keras.callbacks.LearningRateScheduler(piecewise_constant_fn)
# ...
history = model.fit(X_train_scaled, y_train, epochs=n_epochs,
                    validation_data=(X_valid_scaled, y_valid),
                    callbacks=[lr_scheduler])
</code></pre>
</p></details></li>

<li><details><summary><b>Performance Scheduling</b></summary><p><pre><code>lr_scheduler = keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=5)
</code></pre>
<pre><code># Visualize Learing_rate vs. validation loss.
plt.plot(history.epoch, history.history["lr"], "bo-")
plt.xlabel("Epoch")
plt.ylabel("Learning Rate", color='b')
plt.tick_params('y', colors='b')
plt.gca().set_xlim(0, n_epochs - 1)
plt.grid(True)

ax2 = plt.gca().twinx()
ax2.plot(history.epoch, history.history["val_loss"], "r^-")
ax2.set_ylabel('Validation Loss', color='r')
ax2.tick_params('y', colors='r')

plt.title("Reduce LR on Plateau", fontsize=14)
plt.show()
</code></pre>
</p></details></li>

<li><details><summary><b>One Cycle Policy</b></summary><p><pre><code># Functions.
def find_learning_rate(model, X, y, epochs=1, batch_size=32, min_rate=10**-5, max_rate=10):
    init_weights = model.get_weights()
    iterations = len(X) // batch_size * epochs
    factor = np.exp(np.log(max_rate / min_rate) / iterations)
    init_lr = K.get_value(model.optimizer.lr)
    K.set_value(model.optimizer.lr, min_rate)
    exp_lr = ExponentialLearningRate(factor)
    history = model.fit(X, y, epochs=epochs, batch_size=batch_size,
                        callbacks=[exp_lr])
    K.set_value(model.optimizer.lr, init_lr)
    model.set_weights(init_weights)
    return exp_lr.rates, exp_lr.losses

def plot_lr_vs_loss(rates, losses):
    plt.plot(rates, losses)
    plt.gca().set_xscale('log')
    plt.hlines(min(losses), min(rates), max(rates))
    plt.axis([min(rates), max(rates), min(losses), (losses[0] + min(losses)) / 2])
    plt.xlabel("Learning rate")
    plt.ylabel("Loss")
</code></pre>
<pre><code># One Cycle Policy
class OneCycleScheduler(keras.callbacks.Callback):
    def __init__(self, iterations, max_rate, start_rate=None,
                 last_iterations=None, last_rate=None):
        self.iterations = iterations
        self.max_rate = max_rate
        self.start_rate = start_rate or max_rate / 10
        self.last_iterations = last_iterations or iterations // 10 + 1
        self.half_iteration = (iterations - self.last_iterations) // 2
        self.last_rate = last_rate or self.start_rate / 1000
        self.iteration = 0
    def _interpolate(self, iter1, iter2, rate1, rate2):
        return ((rate2 - rate1) * (self.iteration - iter1)
                / (iter2 - iter1) + rate1)
    def on_batch_begin(self, batch, logs):
        if self.iteration &amp;lt; self.half_iteration:
            rate = self._interpolate(0, self.half_iteration, self.start_rate, self.max_rate)
        elif self.iteration &amp;lt; 2 * self.half_iteration:
            rate = self._interpolate(self.half_iteration, 2 * self.half_iteration,
                                     self.max_rate, self.start_rate)
        else:
            rate = self._interpolate(2 * self.half_iteration, self.iterations,
                                     self.start_rate, self.last_rate)
            rate = max(rate, self.last_rate)
        self.iteration += 1
        K.set_value(self.model.optimizer.lr, rate)
</code></pre>
<h4>How to use</h4><pre><code># 1. run the first 2 functions to show which learning rate has the lowest loss.
keras.backend.clear_session()
tf.random.set_seed(42)
np.random.seed(42)

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[32, 32, 3]))
for _ in range(20):
    model.add(keras.layers.Dense(100,
                                 kernel_initializer="lecun_normal",
                                 activation="selu"))

model.add(keras.layers.AlphaDropout(rate=0.1))
model.add(keras.layers.Dense(10, activation="softmax"))

optimizer = keras.optimizers.SGD(lr=1e-3)
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=optimizer,
              metrics=["accuracy"])


####### Visualize
batch_size = 128
rates, losses = find_learning_rate(model, X_train_scaled, y_train, epochs=1, batch_size=batch_size)
plot_lr_vs_loss(rates, losses)
plt.axis([min(rates), max(rates), min(losses), (losses[0] + min(losses)) / 1.4])
</code></pre>

<h4>Refit the mode again with the new learning rate, and apply One Cycle Policy</h4><pre><code>keras.backend.clear_session()
tf.random.set_seed(42)
np.random.seed(42)

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[32, 32, 3]))
for _ in range(20):
    model.add(keras.layers.Dense(100,
                                 kernel_initializer="lecun_normal",
                                 activation="selu"))

model.add(keras.layers.AlphaDropout(rate=0.1))
model.add(keras.layers.Dense(10, activation="softmax"))

optimizer = keras.optimizers.SGD(lr=1e-2)
model.compile(loss="sparse_categorical_crossentropy",
              optimizer=optimizer,
              metrics=["accuracy"])

### Apply One Cycle Policy
n_epochs = 15
onecycle = OneCycleScheduler(len(X_train_scaled) // batch_size * n_epochs, max_rate=0.05)
history = model.fit(X_train_scaled, y_train, epochs=n_epochs, batch_size=batch_size,
                    validation_data=(X_valid_scaled, y_valid),
                    callbacks=[onecycle])
</code></pre>
</p></details></li>

<li><details><summary><b>Another Strategy</b></summary><p>
<pre><code> # Set up the learning rate strategy.
LR_START = 0.0001
LR_MAX = 0.00005 * 8
LR_MIN = 0.0001
LR_RAMPUP_EPOCHS = 4
LR_SUSTAIN_EPOCHS = 6
LR_EXP_DECAY = .8

def lrfn(epoch):
    if epoch &amp;lt; LR_RAMPUP_EPOCHS:
        lr = (LR_MAX - LR_START) / LR_RAMPUP_EPOCHS * epoch + LR_START
    elif epoch &amp;lt; LR_RAMPUP_EPOCHS + LR_SUSTAIN_EPOCHS:
        lr = LR_MAX
    else:
        lr = (LR_MAX - LR_MIN) * LR_EXP_DECAY**(epoch - LR_RAMPUP_EPOCHS - LR_SUSTAIN_EPOCHS) + LR_MIN
    return lr

lr_callback = tf.keras.callbacks.LearningRateScheduler(lrfn, verbose=True)

rng = [i for i in range(EPOCHS)]
y = [lrfn(x) for x in rng]
plt.plot(rng, y)
print("Learning rate schedule: {:.3g} to {:.3g} to {:.3g}".format(y[0], max(y), y[-1]))
</code></pre>
<p><img src="imgs/20210205-170659.png" alt="" /></p>
</p></details></li>

</ul></details>

<details><summary><b>Tensorboard</b></summary><pre><code>import os
root_logdir = os.path.join(os.curdir, "my_logs")

def get_run_logdir():
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(root_logdir, run_id)

run_logdir = get_run_logdir()

# 2. Fit the model.
tensorboard_cv = tf.keras.callbacks.TensorBoard(run_logdir,
                                      # histogram_freq=1, Records activation histogram every 1 epoch.
                                      # embeddings_freq=1) Record embedding data every 1 epoch.
history = model.fit(X_train_scaled,
                    y_train,
                    epochs=20,
                    validation_data=(X_valid_scaled, y_valid),
                    callbacks=[tensorboard_cv])

# 3. Show Tensorboard
!tensorboard --logdir=./my_logs --port=6006

# Note, the last command won't work in colab, search for it.
</code></pre>
</details>

</div>