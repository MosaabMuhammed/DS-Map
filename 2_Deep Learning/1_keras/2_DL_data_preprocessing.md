# ==&nbsp;Data Preprocessing&nbsp;==

<details><summary>**1. One-Hot Encoding (to_categorical)**</summary>
<p>
~~~python
from keras.utils.np_utils import to_categorical

## y_train (before).unique() = [0, 1, ... , 9]
y_train     = to_categorical(y_train)
num_classes = y_train.shape[1]
num_classes

#### Result ######
10
~~~
</p>
</details>

<details><summary>**2. Data Augmentation (Images)**</summary>
<p>
[**Docs**](file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Sklearn/Image%20Preprocessing%20-%20Keras%20Documentation.html)

#### 1. Import the class ImageDataGenerator.
**NOTE:** you can specify its parameters. - see the docs -.
~~~python
from keras.preprocessing import image

gen = image.ImageDataGenerator()
~~~

#### 2. Test split before generating.
~~~python
from sklearn.model_selection import train_test_split

X = X_train
y = y_train

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=.1, random_state=42)
train_batches = gen.flow(X_train, y_train, batch_size=64)
val_batches   = gen.flow(X_val, y_val, batch_size=64)
~~~

#### 3. After you defined your model using `Sequential`.
~~~python
history=model.fit_generator(generator=batches, steps_per_epoch=batches.n, epochs=3, 
                    validation_data=val_batches, validation_steps=val_batches.n)
~~~
</p>
</details>