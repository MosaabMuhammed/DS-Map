# 4. Data Preprocessing

<div style='width:1000px;margin:auto;'>
<details><summary><b>Read Images</b> with <b>Keras Generator</b></summary><p>
```
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen  = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_dir,
										target_size=(150, 150), # Resize all images to 150x150
										batch_size=20,
										class_mode='binary')
										
valid_generator = test_datagen.flow_from_directory(valid_dir,
										target_size=(150, 150), # Resize all images to 150x150
										batch_size=20,
										class_mode='binary')				
```

<h4>When fitting the model with generators</h4>
```
history = model.fit_generator(train_generator,
						steps_per_epoch=len(train_df)/batch_size,
						epochs=30,
						validation_data=valid_generator,
						validation_steps=len(valid_df)/batch_size)
```
</p></details>
<details><summary>Deal with <b>small images dataset</b> 2,000 images</b></summary>
<p> if you start with a simple convnet architecuture, your model will overfit quickly, here's how you can mitigate that effect:</p>
<ul>
<li>Data Augmentation.</li>
<li>Add Drop-out Layer after Flatten() layer and before Dense layer.</li>
<li>Add Regularization</li>
</ul>

- Use a pretrained Convent.
</details>

<details><summary><b>Data Augmentation</b></summary>
```
# Note: Validation & Test data shouldn't be augmented.
datagen = ImageDataGenerator(
			rescale=1./255,
			rotation_range=40,
			width_shift_range=0.2,
			height_shift_range=0.2,
			shear_range=0.2,
			zoom_range=0.2,
			horizontal_flip=True,
			fill_mode='nearest')
			
valid_datagen = ImageDataGenerator(rescale=1./255)

# Read the folder of images.
train_generator = datagen.flow_from_directory(
					train_dir,
					target_size=(150, 150),
					batch_size=32,
					class_mode='binary')

```
<h4> Display some images after augmenation</h4>
```
from tensorflow.keras.preprocessing import image

fnames = [os.path.join(train_cats_dir, fname) for fname in os.listdir(train_cats_dir)]

# Select one image.
img_path = fnames[3]

# Read the image and resize it.
img = image.load_img(img_path, target_size=(150, 150))

# Convert it to a Numpy array with shape (150, 150, 3)
x = image.img_to_array(img)

x = x.reshape((1,) + x.shape)

i = 0
for batch in datagen.flow(x, batch_size=1):
	plt.figure(i)
	imgplot = plt.imshow(image.array_to_img(batch[0]))
	i += 1
	if i % 4 == 0:
		break

plt.show()
```
</details>

</div>
