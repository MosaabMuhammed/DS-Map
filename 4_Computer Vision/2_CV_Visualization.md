# Visualization

<div style='width:1000px;margin:auto;'>
<details><summary>Visualizing <b>intermediate activations</b></summary>
<p>This consists of displaying the feature maps that are output by various convolution and pooling layers in a network, given a certain input.<br><br>This gives a view into how an input is decomposed into the different filters learned by the network.</p>

<h4>Load the model</h4>
```
# Or simply use the model that you have used recently.
from tensorflow.keras.models import load_model
model = load_model()
model.summary()
```

<h4>Preprocessing a single image</h4>
```
img_path = 'path/to/image.jpg'

from tensorflow.keras.preprocessing import image
import numpy as np

img = image.load_img(img_path, target_size=(150, 150))
img_tensor = image.img_to_array(img)
img_tensor = np.expand_dims(img_tensor, axis=0)
img_tensor /= 255. # Remeber that the model is trained on inputs like that.

print(img_tensor.shape)
# ex. shape is (1, 150, 150, 3)
```

<h4>Display hte test image</h4>
```
import matplotlib.pyplot as plt

plt.imshow(img_tensor[0])
plt.show()
```
<img src="imgs/20200828-135335.png" height=150 width=150>


<h4>Instantiating a model with one input and multiple outputs (n_conv layers)</h4>
```
from tensorflow.keras import models

# Change the number of 8 based on n_layers in your model.
layer_outputs = [layer.output for layer in model.layers[:8]]
activation_model = models.Model(inputs=model.input, outputs=layer_outputs)

# Running the model in predict mode.
activations = activation_model.predict(img_tensor)
```

<h4>Show individual convolution</h4>
```
first_layer_activation = activations[0]
print(first_layer_activation.shape)
# (1, 148, 148, 32)

# Visualize the features.
plt.matshow(first_layer_activation[0, :, :, 4], cmap='viridis')

# as you can see, this channel encode a diagonal edge detector.
```
<img src="imgs/20200828-135902.png" height=150 width=150>


<h4>Visualizing every channel in every intermediate activation</h4>
```
layer_names = []
for layer in model.layers[:8]:
	layer_name.append(layer.name)
	
images_per_row = 16

for layer_name, layer_activation in zip(layer_names, activations):
	# Number of features in the feature map
	n_features = layer_activation.shape[-1]
	
	# The feature map has shape (I, size, size, n_features).
	size = layer_activation.shape[1]
	
	# Tiles the activation channels in this matrix.
	n_cols = n_features // images_per_row
	display_grid = np.zeros((size*n_cols, images_per_row*size))
	
	# Tiles each filter into a big horizontal grid.
	for col in range(n_cols):
		for row in range(images_per_row):
			channel_image = layer_activation[0, :, :, col * images_per_row + row]
			# Post-processes the feature to make it visually palatable.
			channel_image -= channel_image.mean()
			channel_image /= channel_image.std()
			channel_image *= 64
			channel_image += 128
			channel_image = np.clip(channel_image, 0, 255).astype('uint8')
			display_grid[col*size:(col+1)*size,
					   row*size:(row+1)*size] = channel_image
					   
scale = 1. / size
plt.figure(figsize=(scale*display_grid.shape[1],
			    scale*display_grid.shape[0]))
plt.title(layer_name)
plt.grid(False)
plt.imshow(display_grid, aspect='auto', cmap='viridis')
```
<img src="imgs/20200828-152955.png" height=300 width=200>

<p>Things to note in here:</p>
<ul>
<li>The first layer acts as a collection of various edge detectors. At that stage, the activations retain almost all of the information present in the inital picture.</li>
<li>As you go higher, the activations become increasingly abstract and less visually interpretable. They begin to encode higher-level concepts such as “cat ear” and “cat eye.” Higher presentations carry increasingly less information about the visual contents of the image, and increasingly more information related to the class of the image.</li>
<li>The sparsity of the activations increases with the depth of the layer: in the first layer, all filters are activated by the input image; but in the following layers, more and more filters are blank. This means the pattern encoded by the filter isn’t found in the input image.</li>
</details>

</div>
