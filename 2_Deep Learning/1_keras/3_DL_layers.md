# ==&nbsp;Layers&nbsp;==


<details><summary>**Dense**</summary>
<p>
[**Docs**](https://keras.io/layers/core/) 

- **Dense** is fully connected layer that means all neurons in previous layers will be connected to all neurons in fully connected layer. In the last layer we have to specify output dimensions/classes of the model.
#### 1. Class.
~~~python
keras.layers.Dense(
				units, 
				activation=None, 
				use_bias=True, 
				kernel_initializer='glorot_uniform', 
				bias_initializer='zeros', 
				kernel_regularizer=None, 
				bias_regularizer=None, 
				activity_regularizer=None, 
				kernel_constraint=None, 
				bias_constraint=None
				)
~~~

#### Example.
~~~python
from keras.layers.core import  Dense

model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))   <----
~~~
</p>
</details>


<details><summary>**Lambda**</summary>
<p>
[**Docs**](https://keras.io/layers/core/) 

- **Lambda layer** performs simple arithmetic operations like sum, average, exponentiation etc.

#### 1. Class.
~~~python
keras.layers.Lambda(function, output_shape=None, mask=None, arguments=None)
~~~

#### Example.
~~~python
from keras.layers.core import  Lambda

def standardize(x):
    return (x - mean_px)/std_px

model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))  <--
model.add(Flatten())
model.add(Dense(10, activation='softmax'))
~~~
</p>
</details>


<details><summary>**Flatten**</summary>
<p>
[**Docs**](https://keras.io/layers/core/) 

- **Flatten** will transform input into 1D array.

#### 1. Class.
~~~python
keras.layers.Flatten(data_format=None)
~~~

#### Example.
~~~python
from keras.layers.core import  Flatten

model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))
model.add(Flatten())   <--
model.add(Dense(10, activation='softmax'))
~~~
</p>
</details>

<details><summary>**Dropout**</summary>
<p>
[**Docs**](https://keras.io/layers/core/) 

- **Dropout** consists in randomly setting a fraction rate of input units to 0 at each update during training time, which helps prevent overfitting.

#### 1. Class.
~~~python
keras.layers.Dropout(
				rate, 
				noise_shape=None, 
				seed=None
				)
~~~

#### Example.
~~~python
from keras.layers.core import  Flatten

model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))
model.add(Flatten())   <--
model.add(Dense(10, activation='softmax'))
~~~
</p>
</details>