<h1 id="starter">Starter</h1>

<div style='width:1000px;margin:auto'>


<details><summary><b>Plot Shape of The Model</b></summary><p><pre><code>from tensorflow.keras.utils import plot_model

plot_model(model, to_file='model_plot4a.png', show_shapes=True, show_layer_names=True)
</code></pre>
</p></details>

<details><summary><b>Save & Load Model</b></summary><p>
<h4>1. using save()</h4><pre><code>#NOTE: This is only available for Sequential and Functional API and NOT for Subclass API.
# But you can use save_weights() and load_weights() to save and restore the model parameters!
# Save Model.
model.save("my_keras_model.h5")

# Load Model.
model = tf.keras.models.load_model("my_keras_model.h5")
</code></pre>

<h4>2. using checkpoint</h4><pre><code># Using Checkpints
checkpoint_cb = keras.callbacks.ModelCheckpoint("my_keras_model.h5",
save_best_only=True)

history = model.fit(X_train, y_train, epochs=10,
                validation_data=(X_valid, y_valid),
                callbacks=[checkpoint_cb])

model = keras.models.load_model("my_keras_model.h5") # rollback to best model
</code></pre>

<h4>3. saving model in json</h4><pre><code>## WRITE model &amp; weights
model_structure = model.to_json()
with open("cnn_model.json", "w") as json_file:
    json_file.write(model_structure)

model.save_weights("cnn_weights.h5")


## READ model &amp; weights
from keras.models import model_from_json
with open("cnn_model.json", "r") as json_file:
    json_string = json_file.read()
model = model_from_json(json_string)
model.load_weights('cnn_weights.h5')
</code></pre>
</p></details>

<details><summary><b>Plot Training & Validation Losses</b></summary><p><pre><code>import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_learning_curves(loss, val_loss):
    plt.plot(np.arange(len(loss)) + 0.5, loss, "b.-", label="Training loss")
    plt.plot(np.arange(len(val_loss)) + 1, val_loss, "r.-", label="Validation loss")
    plt.gca().xaxis.set_major_locator(mpl.ticker.MaxNLocator(integer=True))
    plt.axis([1, 20, 0, 0.05])
    plt.legend(fontsize=14)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.grid(True)
    return plt

plt.figure(figsize=(12, 5))
plot_learning_curves(history.history["loss"], history.history["val_loss"])
plt.show()
</code></pre>
</p></details>
<details><summary><b>Random Seeder</b></summary><p><pre><code>SEED = 42
tf.keras.backend.clear_session()
np.random.seed(SEED)
tf.random.set_seed(SEED)
</code></pre>
</p></details>

<details><summary>Using <b>TensorBoard</b> in Colab</summary><p><pre><code># Load the TensorBoard notebook extension
%load_ext tensorboard

%tensorboard --logdir runs
</code></pre>
</p></details>

<details><summary>Configure <b>TPU/GPU</b></summary><pre><code># TPU or GPU detection.
# Detect hardware, return appropriate distribution strategy.
try:
    AUTO = tf.data.experimental.AUTOTUNE
    tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
    print(f"Running on TPU {tpu.master()}")
except ValueError:
    tpu = None
    
if tpu:
    tf.config.experimental_connect_to_cluster(tpu)
    tf.tpu.experimental.initialize_tpu_system(tpu)
    strategy = tf.distribute.experimental.TPUStrategy(tpu)
else:
    strategy = tf.distribute.get_strategy()
    
print(f"REPLICAS: {strategy.num_replicas_in_sync}")

# Configuration.
EPOCHS = 40
BATCH_SIZE = 16 * strategy.num_replicas_in_sync
</code></pre>

<pre><code> Apply the changes to the datasets.
train_dataset = (
tf.data.Dataset
    .from_tensor_slices((train_paths, train_labels))
    .map(decode_image, num_parallel_calls=AUTO)
    .cache()
    .map(data_augment, num_parallel_calls=AUTO)
    .repeat()
    .shuffle(512)
    .batch(BATCH_SIZE)
    .prefetch(AUTO)
)

valid_dataset = (
    tf.data.Dataset
    .from_tensor_slices((valid_paths, valid_labels))
    .map(decode_image, num_parallel_calls=AUTO)
    .batch(BATCH_SIZE)
    .cache()
    .prefetch(AUTO)
)

test_dataset = (
    tf.data.Dataset
    .from_tensor_slices(test_paths)
    .map(decode_image, num_parallel_calls=AUTO)
    .map(data_augment, num_parallel_calls=AUTO)
    .batch(BATCH_SIZE)
)
</code></pre>

<pre><code> # Set up the learning rate strategy.
LR_START = 0.0001
LR_MAX = 0.00005 * strategy.num_replicas_in_sync
LR_MIN = 0.0001
LR_RAMPUP_EPOCHS = 4
LR_SUSTAIN_EPOCHS = 6
LR_EXP_DECAY = .8

def lrfn(epoch):
    if epoch < LR_RAMPUP_EPOCHS:
        lr = (LR_MAX - LR_START) / LR_RAMPUP_EPOCHS * epoch + LR_START
    elif epoch < LR_RAMPUP_EPOCHS + LR_SUSTAIN_EPOCHS:
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

<pre><code>
with strategy.scope():
    model = tf.keras.Sequential([
        InceptionResNetV2(
            input_shape=(image_size, image_size, 3),
            weights="imagenet",
            include_top=False
        ),
        L.GlobalMaxPooling2D(),
        L.Dense(4, activation="softmax")
    ])
    
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=['categorical_accuracy']
    )
    model.summary()
</code></pre>
</details>
</div>