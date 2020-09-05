# Models

<div style='width:1000px;margin:auto;'>

<details><summary><b>Bi-Directional LSTM</b> for Images</summary><p>
```
from keras.models import Model
from keras.layers import Input, LSTM, GRU, Bidirectional, GlobalMaxPooling1D, Lambda, Concatenate, Dense
import keras.backend as K
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if len(K.tensorflow_backend._get_available_gpus()) > 0:
  from keras.layers import CuDNNLSTM as LSTM
  from keras.layers import CuDNNGRU as GRU


def get_mnist(limit=None):
  if not os.path.exists('../large_files'):
    print("You must create a folder called large_files adjacent to the class folder first.")
  if not os.path.exists('../large_files/train.csv'):
    print("Looks like you haven't downloaded the data or it's not in the right spot.")
    print("Please get train.csv from https://www.kaggle.com/c/digit-recognizer")
    print("and place it in the large_files folder.")

  print("Reading in and transforming data...")
  df = pd.read_csv('../large_files/train.csv')
  data = df.values
  np.random.shuffle(data)
  X = data[:, 1:].reshape(-1, 28, 28) / 255.0 # data is from 0..255
  Y = data[:, 0]
  if limit is not None:
    X, Y = X[:limit], Y[:limit]
  return X, Y




# get data
X, Y = get_mnist()

# config
D = 28
M = 15


# input is an image of size 28x28
input_ = Input(shape=(D, D))

# up-down
rnn1 = Bidirectional(LSTM(M, return_sequences=True))
x1 = rnn1(input_) # output is N x D x 2M
x1 = GlobalMaxPooling1D()(x1) # output is N x 2M

# left-right
rnn2 = Bidirectional(LSTM(M, return_sequences=True))

# custom layer
permutor = Lambda(lambda t: K.permute_dimensions(t, pattern=(0, 2, 1)))

x2 = permutor(input_)
x2 = rnn2(x2) # output is N x D x 2M
x2 = GlobalMaxPooling1D()(x2) # output is N x 2M

# put them together
concatenator = Concatenate(axis=1)
x = concatenator([x1, x2]) # output is N x 4M

# final dense layer
output = Dense(10, activation='softmax')(x)

model = Model(inputs=input_, outputs=output)

# testing
# o = model.predict(X)
# print("o.shape:", o.shape)

# compile
model.compile(
  loss='sparse_categorical_crossentropy',
  optimizer='adam',
  metrics=['accuracy']
)

# train
print('Training model...')
r = model.fit(X, Y, batch_size=32, epochs=10, validation_split=0.3)


# plot some data
plt.plot(r.history['loss'], label='loss')
plt.plot(r.history['val_loss'], label='val_loss')
plt.legend()
plt.show()

# accuracies
plt.plot(r.history['acc'], label='acc')
plt.plot(r.history['val_acc'], label='val_acc')
plt.legend()
plt.show()

```
</p></details>

<details><summary><b>Transfer Learning</b></summary>
<p><ul>
<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/25.%20Transfer%20Learning.html"><b>How to choose Transfer Learning Model</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/26.%20Transfer%20Learning%20in%20Keras.html"><b>How to use Transfer Learning</b></a> </p></li>
	
<li><p><a href="https://github.com/alexisbcook/keras_transfer_cifar10/blob/master/Keras_Transfer_CIFAR10.ipynb"><b>1. Inception</b></a> </p></li></ul>

<details><summary><b>2. VGG16</b></summary><p>
<h4>1. Import VGG16</h4>
~~~python
from keras import applications

# This will load the whole VGG16 network, including the top Dense layers.
# Note: by specifying the shape of top layers, input tensor shape is forced
# to be (224, 224, 3), therefore you can use it only on 224x224 images.
vgg_model = applications.VGG16(weights='imagenet', include_top=True)

# If you are only interested in convolution filters. Note that by not
# specifying the shape of top layers, the input tensor shape is (None, None, 3),
# so you can use them for any size of images.
vgg_model = applications.VGG16(weights='imagenet', include_top=False)

# If you want to specify input tensor
from keras.layers import Input
input_tensor = Input(shape=(160, 160, 3))
vgg_model = applications.VGG16(weights='imagenet',
                               include_top=False,
                               input_tensor=input_tensor)

# To see the models' architecture and layer names, run the following
vgg_model.summary()
~~~

<h4>2. Create a new network with bottom layers taken from VGG</h4>
<p>Assume that for some specific task for images with the size (160, 160, 3), you want to use pre-trained bottom layers of VGG, up to layer with the name block2_pool.</p>
~~~python
vgg_model = applications.VGG16(weights='imagenet',
                               include_top=False,
                               input_shape=(160, 160, 3))

# Creating dictionary that maps layer names to the layers
layer_dict = dict([(layer.name, layer) for layer in vgg_model.layers])

# Getting output tensor of the last VGG layer that we want to include
x = layer_dict['block2_pool'].output

# Stacking a new simple convolutional network on top of it    
x = Conv2D(filters=64, kernel_size=(3, 3), activation='relu')(x)
x = MaxPooling2D(pool_size=(2, 2))(x)
x = Flatten()(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(10, activation='softmax')(x)

# Creating new model. Please note that this is NOT a Sequential() model.
from keras.models import Model
custom_model = Model(input=vgg_model.input, output=x)

# Make sure that the pre-trained bottom layers are not trainable
for layer in custom_model.layers[:7]:
    layer.trainable = False

# Do not forget to compile it
custom_model.compile(loss='categorical_crossentropy',
                     optimizer='rmsprop',
                     metrics=['accuracy'])
~~~
</p></details>

<p>After taking only the convolution base (Top Layers), you have 2 options to proceed:</p>
<ul>
<li>Running the convolutional base over your dataset, recording its output to a
Numpy array on disk, and then using this data as input to a standalone, densely connected classifier similar to those you saw in part 1 of this book. This solution is fast and cheap to run, because it only requires running the convolutional base once for every input image, and the convolutional base is by far the most expensive part of the pipeline. But for the same reason, this technique won’t allow you to use data augmentation.</li><br>

<details><summary><b>Feature Extraction WITHOUT Data Augmentation</b></summary>
<h4>Fetch the pretrained model</h4>
```
# you can choose from [Xception, Inception V3, ResNet50, VGG16, VGG19, MobileNet, ...]
from tensorflow.keras.applications import VGG16

conv_base = VGG16(weights='imagenet',
				 include_top=False,
				 input_shape=(150, 150, 3))

# weights: specifies the weight checkpoint from which to initialize the model.
# include_top: refers to including (or not) the densely connected layers.
# input_shape: is the shape of the image tensor that you'll feed to the network.  --> This is purely OPTIONAL.
```
<h4>Extracting features using the pretrained convolutional base</h4>
```
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

base_dir = '/cats_and_dogs_small'
train_dir = os.path.join(base_dir, 'train')
valid_dir = os.path.join(base_dir, 'valid')
test_dri   = os.path.join(base_dir, 'test')

datagen = ImageDataGenerator(rescale=1./255)
batch_size = 20

def extract_features(directory, sample_count):
	# This is the final shape of the conv_base, you can check it by using
	# conv_base.summary()
	features = np.zeros(shape=(sample_count, 4, 4, 512))
	labels     = np.zeros(shape=(sample_count))
	generator = datagen.flow_from_directory(
						directory,
						target_size=(150, 150),
						batch_size=batch_size,
						class_mode='binary')
	i = 0
	for inputs_batch, labels_batch in generator:
		features_batch = conv_base.predict(inputs_batch)
		features[i*batch_size:(i+1)*batch_size] = features_batch
		labels[i*batch_size:(i+1)*batch_size] = labels_batch
		i += 1
		if i * batch_size >= sample_count:
			break
	return features, labels
	
# generate features for training, validation, and testing.
# 2000 is the number of training rows.
train_features, train_labels = extract_features(train_dir, 2000)
valid_features, valid_labels = extract_features(valid_dir, 1000)
test_features, test_labels    = extract_features(test_dir, 1000)
```

<h4>Change the shape, to feed it to Dense layers</h4>
```
train_features = np.reshape(train_features, (2000, 4*4*512))
valid_features = np.reshape(valid_features, (1000, 4*4*512))
test_features  = np.reshape(test_features, (1000, 4*4*512))
```

<h4>Create the Dense layers</h4>
```
from tensorflow.keras import models, layers, optimizers

mode = models.Sequential()
model.add(layers.Dense(256, activation='relu', input_dim=4*4*512))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=optimizers.RMSprop(lr=2e-5),
			loss='binary_crossentropy',
			metrics=['accuracy'])
			
history = model.fit(train_features, train_labels,
			      epochs=30,
			      batch_size=20,
			      validation_data=(valid_features, valid_labels))
# Training will be fast!
```
</details><br><br>
<li>Extending the model you have (conv_base) by adding Dense layers on top, and
running the whole thing end to end on the input data. This will allow you to use
data augmentation, because every input image goes through the convolutional
base every time it’s seen by the model. But for the same reason, this technique is
far more expensive than the first.</li><br>

<details><summary><b>Feature Extraction WITH Data Augmentation</b></summary>
<h4>Fetch the pretrained model</h4>
```
# you can choose from [Xception, Inception V3, ResNet50, VGG16, VGG19, MobileNet, ...]
from tensorflow.keras.applications import VGG16

conv_base = VGG16(weights='imagenet',
				 include_top=False,
				 input_shape=(150, 150, 3))

# weights: specifies the weight checkpoint from which to initialize the model.
# include_top: refers to including (or not) the densely connected layers.
# input_shape: is the shape of the image tensor that you'll feed to the network.  --> This is purely OPTIONAL.
```

<h4>Adding a densly connected classifier on top of convolutional base</h4>
```
from tensorflow.keras import models, layers.

model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(254, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
```

<h4>Freeze the convoluational base's weights</h4>
```
print(f"~> Number of trainable weights before freezing conv base: {len(model.trainable_weights}"))

conv_base.trainable = False

print(f"~> Number of trainable weights After freezing conv base: {len(model.trainable_weights}"))
```

<h4>Data Augmenation</h4>
```
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers

train_datagen = ImageDataGenerator(
					rescale=1./255,
					rotation_range=40,
					width_shift_range=.2,
					height_shift_range=.2,
					shear_range=.2,
					zoom_range=.2,
					horizontal_flip=True,
					fill_mode='nearest')
					
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
					train_dir,
					target_size=(150, 150),
					batch_size=20,
					class_model='binary')
					
valid_generator = test_datagen.flow_from_directory(
					valid_dir,
					target_size=(150, 150),
					batch_size=20,
					class_mode='binary')
					
model.compile(loss='binary_crossentropy',
			optimizer=optimizers.RMSprop(lr=2-e5),
			metrics=['accuracy'])
			
history = model.fit_generator(
				train_generator,
				steps_per_epoch=100,
				epochs=30,
				validation_data=validation_generator,
				validation_steps=50)
```
</p></details></ul>
<details><summary><b>Fine-Tunning</b> a Transfer learning mode</summary>
<ol><li>Add your custom network on top of an already-trained base network</li>
<li>Freeze the base network.</li>
<li>Train the part you added. (Dense Layers)</li>
<li>Unfreeze some layers in the base network.</li>
<li>Jointly train both these layers and the part you added.</li></ol>

<h4>Freezing all layers up to a specific point</h4>
```
# to know the name of the layers, do the following.
conv_base.summary()

conv_base.trainable = True

set_trainable = False
for layer in conv_base.layers:
	if layer.name == 'block5_conv1':
		set_trainable = True
	if set_trainable:
		layer.trainable = True
	else:
		layer.trainable = False
```

<h4>Fine-tuning the model</h4>
```
# Make sure to use a small learning rate, to avoid changing the weight too much.
model.compile(loss='binary_crossentropy',
			optimizer=optimizers.RMSprop(lr=1e-5),
			metrics=['accuracy'])
			
history = model.fit_generator(
				train_generator,
				steps_per_epoch=100,
				epochs=100,
				validation_data=validation_generator,
				validation_steps=50)
```

<h4>Test the model</h4>
```
test_generator = test_datagen.flow_from_directory(
					test_dir,
					target_size=(150, 150),
					batch_size=20,
					class_mode='binary')
					
test_loss, test_acc = model.evaluate_generator(test_generator, steps=50)
print(f"test acc: {test_acc}")
```
</p></details>
</p></details>

<a href="./notebooks/deepdream.html" style="color:#333;font-size:17px;font-weight:bold;padding:15px">DeepDream</a>
</div>
