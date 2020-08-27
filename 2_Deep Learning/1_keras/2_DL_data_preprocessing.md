# Data Preprocessing

<div style="width:1000px;margin:auto">
<details><summary><b>One-Hot Encoding (to_categorical)</b></summary><p>
```
from keras.utils.np_utils import to_categorical

## y_train (before).unique() = [0, 1, ... , 9]
y_train     = to_categorical(y_train)
num_classes = y_train.shape[1]
num_classes

#### Result ######
10
```
</p></details>

<details><summary><b>Data Augmentation (Images)</b></summary><p>
[**Docs**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/Image%20Preprocessing%20-%20Keras%20Documentation.html)

#### 1. Import the class ImageDataGenerator.
**NOTE:** you can specify its parameters. - see the docs -.
```
from keras.preprocessing import image

gen = image.ImageDataGenerator()
```

#### 2. Test split before generating.
```
from sklearn.model_selection import train_test_split

X = X_train
y = y_train

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=.1, random_state=42)
train_batches = gen.flow(X_train, y_train, batch_size=64)
val_batches   = gen.flow(X_val, y_val, batch_size=64)
```

#### 3. After you defined your model using `Sequential`.
```
history=model.fit_generator(generator=batches, steps_per_epoch=batches.n, epochs=3, 
                    validation_data=val_batches, validation_steps=val_batches.n)
```
</p></details>

<details><summary><b>Loading Large Dataset</b></summary><p>

<h4>1. Load the data</h4>
```
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from utils import *
import os, numpy as np, pandas as pd

housing = fetch_california_housing()

X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data,
                                                              housing.target[..., None],
                                                              random_state=42)
X_train, X_valid, y_train, y_valid = train_test_split(X_train_full,
                                                      y_train_full,
                                                      random_state=42)
shape(X_train, X_valid, X_test, y_train, y_valid, y_test)
scaler = StandardScaler()
scaler.fit(X_train)
X_mean = scaler.mean_
X_std  = scaler.scale_
```

<h4>2. Split the data into multiple csv files</h4>
```
import os, numpy as np, pandas as pd
def save_to_multiple_csv_files(data, name_prefix, header=None, n_parts=10):
    housing_dir = os.path.join("datasets", "housing")  # Write where to save the new csv files.
    os.makedirs(housing_dir, exist_ok=True)
    path_format = os.path.join(housing_dir, "my_{}_{:02d}.csv")

    filepaths = []
    m = len(data)
    for file_idx, row_indices in enumerate(np.array_split(np.arange(m), n_parts)):
        part_csv = path_format.format(name_prefix, file_idx)
        filepaths.append(part_csv)

        with open(part_csv, "wt", encoding="utf-8") as f:
            if header is not None:
                f.write(header)
                f.write("\n")
            for row_idx in row_indices:
                f.write(",".join([repr(col) for col in data[row_idx]]))
                f.write("\n")
    return filepaths
```

```
train_data  = np.c_[X_train, y_train]
valid_data  = np.c_[X_valid, y_valid]
test_data   = np.c_[X_test, y_test]
header_cols = housing.feature_names + ["MedianHouseValue"]
header      = ",".join(header_cols)

train_filepaths = save_to_multiple_csv_files(train_data, "train", header, n_parts=20)
valid_filepaths = save_to_multiple_csv_files(valid_data, "valid", header, n_parts=10)
test_filepaths  = save_to_multiple_csv_files(test_data, "test", header, n_parts=10)
```

<h4>3. Handle how to read the multiple files</h4>
```
n_inputs = 8

@tf.function
def preprocess(line):
    defs   = [0.]*n_inputs + [tf.constant([], dtype=tf.float32)]
    fields = tf.io.decode_csv(line, record_defaults=defs)
    X      = tf.stack(fields[:-1])
    y      = tf.stack(fields[-1:])
    return (X - X_mean) / X_std, y
```

```
def csv_reader_dataset(filepaths, repeat=1, n_readers=5,
                       n_read_threads=tf.data.experimental.AUTOTUNE,
                       shuffle_buffer_size=10_000,
                       n_parse_threads=5, batch_size=32):
    dataset = tf.data.Dataset.list_files(filepaths).repeat(repeat)
    dataset = dataset.interleave(
        lambda filepath: tf.data.TextLineDataset(filepath).skip(1),
        cycle_length=n_readers,
        num_parallel_calls=n_read_threads
    )
    dataset = dataset.shuffle(shuffle_buffer_size)
    dataset = dataset.map(preprocess, num_parallel_calls=n_parse_threads)
    dataset = dataset.batch(batch_size)
    return dataset.prefetch(1)
```
```
train_set = csv_reader_dataset(train_filepaths, repeat=None)
valid_set = csv_reader_dataset(valid_filepaths)
test_set  = csv_reader_dataset(test_filepaths)
```

<h4>4. Modelling</h4>
```
tf.keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(30, activation="relu", input_shape=X_train.shape[1:]),
    tf.keras.layers.Dense(30, activation="relu"),
    tf.keras.layers.Dense(1)
])
```
```
model.compile(loss="mse",
              optimizer=tf.keras.optimizers.Adam(lr=1e-3))
batch_size = 16
model.fit(train_set,
          steps_per_epoch=len(X_train) // batch_size,
          epochs=10,
          validation_data=valid_set)
```

<h4>5. Predict & Evaluate</h4>
```
model.evaluate(test_set, steps=len(X_test) // batch_size)
```
```
new_set = test_set.map(lambda X, y: X) # we could instead just pass test_set, Keras would ignore the labels
X_new = X_test
model.predict(new_set, steps=len(X_new) // batch_size)
```
</p></details>

<details><summary><b>Hold-out Validation</b></summary><p>
<p>NOTE: use this method if you have enough data.</p>
<p>If this method is used on little data, then your validation and test sets may contain too few samles to be statistically representative of the data at hand.</p>
<p>Apply K-fold or Iterated K-fold in small datasets.</p>
```
#### Hold-out Validation.
num_validation_samples = 10_000

# Shuffling the data is usually appropiate.
np.random.shuffle(data)

X_valid = data[:num_validation_samples]
X_train = data[num_validation_samples:]

# Traing the model with training data, and validate it with
# validation data.
model.train(X_train)
validation_score = model.evaluate(X_valid)

# At this point, you can tune your model,
# retrain it, evaluate it, tune it again...
# Once you've tuned your hyperparameters, it's common
# to train your final model from scratch on 
# all non-test data available.
model = get_model()
model.train(np.concatenate([X_train, X_valid]))
test_score = model.evaluate(X_test)
```
</p></details>

<details><summary><b>K-Fold cross-validation</b></summary><p>
<h4>K-Folds</h4>
```
# K-fold cross-validation
import numpy as np

# Shuffling the data is usually appropiate.
np.random.shuffle(train_data)

k = 4
num_val_samples = len(train_data) // k
num_epochs      = 500
all_scores      = []

for i in range(k):
    print(f'processing fold #{i}')
    val_data   = train_data[i * num_val_samples: (i+1)*num_val_samples]
    val_labels = train_labels[i * num_val_samples: (i+1)*num_val_samples]

    partial_train_data = np.concatenate([train_data[:i*num_val_samples],
                                         train_data[(i+1)*num_val_samples:]], axis=0)
    partial_train_labels = np.concatenate([train_labels[:i*num_val_samples],
                                           train_labels[(i+1)*num_val_samples:]], axis=0)
    
    history = model.fit(partial_train_data,
              partial_train_labels,
              epochs=num_epochs,
              batch_size=1,
              validation_data=(val_data, val_labels),
              verbose=0)
    # metric_history = history.history['val_mae']
    val_mse, val_mae = model.evaluate(val_data, val_labels, verbose=0)
    all_scores.append(val_mae)
```

<h4>Building the history of successive mean K-fold validation</h4>
```
average_metric_history = [np.mean([x[i] for x in all_scores]) for i in range(num_epochs)]
```

<h4>Plotting validation Scores</h4>
```
import matplotlib.pyplot as plt

plt.plot(range(1, len(average_metric_history)+1), average_metric_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()
```
<p> if the plotting is a little bit difficult to read, due to scaling issues and relatively high variance, you can do the following</p>
```
def smooth_curve(points, factor=0.9):
	smoothed_points = []
	for point in points:
		if smoothed_points:
			previous = smoothed_points[-1]
			smoothed_points.append(previous * factor + point * (1 - factor))
		else:
			smoothed_points.append(point)
	return smoothed_points
	
	
smooth_mae_history = smooth_curve(average_metric_history[10:])

plt.plot(range(1, len(average_metric_history) + 1), smooth_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()
```
<p>Then from this plot, you can figure out, which number of epochs you model doesn't overfit, and build your model normally</p>
```
model = build_model()

model.fit(train_data, train_targets, epochs=80, batch_size=16, verbose=0)

test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)

```
</p></details>
</div>