# Starter

<div style='width:1000px;margin:auto'>


<details><summary><b>Plot Shape of The Model</b></summary><p>
```
from tensorflow.keras.utils import plot_model

plot_model(model, to_file='model_plot4a.png', show_shapes=True, show_layer_names=True)
```
</p></details>

<details><summary><b>Save & Load Model</b></summary><p>
```
#NOTE: This is only available for Sequential and Functional API and NOT for Subclass API.
# But you can use save_weights() and load_weights() to save and restore the model parameters!
# Save Model.
model.save("my_keras_model.h5")

# Load Model.
model = tf.keras.models.load_model("my_keras_model.h5")
```

```
# Using Checkpints
checkpoint_cb = keras.callbacks.ModelCheckpoint("my_keras_model.h5",
save_best_only=True)

history = model.fit(X_train, y_train, epochs=10,
				validation_data=(X_valid, y_valid),
				callbacks=[checkpoint_cb])

model = keras.models.load_model("my_keras_model.h5") # rollback to best model

```
</p></details>

<details><summary><b>Plot Training & Validation Losses</b></summary><p>
```
import matplotlib as mpl
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

```
</p></details>
<details><summary><b>Random Seeder</b></summary><p>
```
SEED = 42
tf.keras.backend.clear_session()
np.random.seed(SEED)
tf.random.set_seed(SEED)
```
</p></details>
</div>