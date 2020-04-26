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
</div>