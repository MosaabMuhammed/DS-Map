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

<details><summary><b>Data Augmentation</b></summary><ul>

<li><details><summary><b>Keras</b></summary>
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
</details></li>


<li><details><summary><b>Skimage</b></summary>
<pre><code>from skimage.io import imshow, imread, imsave
from skimage.transform import rotate, AffineTransform, warp,rescale, resize, downscale_local_mean
from skimage import color,data
from skimage.exposure import adjust_gamma
from skimage.util import random_noise

##### Flipping
#Horizontally flipped
hflipped_image= np.fliplr(image) #fliplr reverse the order of columns of pixels in matrix

#Vertically flipped
vflipped_image= np.flipud(image) #flipud reverse the order of rows of pixels in matrix

##### Rotation
# clockwise rotation
rot_clockwise_image = rotate(image, angle=45) 
# Anticlockwise rotation
rot_anticlockwise_image = rotate(image, angle=-45)

##### Cropping
# source: https://www.kaggle.com/safavieh/image-augmentation-using-skimage
import random
import pylab as pl 
def randRange(a, b):
    '''
    a utility function to generate random float values in desired range
    '''
    return pl.rand() * (b - a) + a
def randomCrop(im):
    '''
    croping the image in the center from a random margin from the borders
    '''
    margin = 1/3.5
    start = [int(randRange(0, im.shape[0] * margin)),
             int(randRange(0, im.shape[1] * margin))]
    end = [int(randRange(im.shape[0] * (1-margin), im.shape[0])), 
           int(randRange(im.shape[1] * (1-margin), im.shape[1]))]
    cropped_image = (im[start[0]:end[0], start[1]:end[1]])
    return cropped_image
    
cropped_image = randomCrop(image)

#####  Brightness Manipulation
image_bright = adjust_gamma(image, gamma=0.5,gain=1)
image_dark = adjust_gamma(image, gamma=2,gain=1)

###### Scaling
image_resized = resize(image, (image.shape[0] // 2, image.shape[1] // 2), anti_aliasing=True)
#image_downscaled = downscale_local_mean(image, (4, 3))

##### Noise Addition
noisy_image= random_noise(image)
</code></pre>
</details></li>

<li><details><summary><b>OpenCV-Python</b></summary>
OpenCV essentially stands for Open Source Computer Vision Library. Although it is written in optimized C/C++, it has interfaces for Python and Java along with C++. 
OpenCV-Python is the python API for OpenCV. You can think of it as a python wrapper around the C++ implementation of OpenCV. OpenCV-Python is not only fast (since the background consists of code written in C/C++) but is also easy to code and deploy(due to the Python wrapper in foreground). This makes it a great choice to perform computationally intensive programs.

<pre><code>##### Flipping
#The image is flipped according to the value of flipCode as follows:
#flipcode = 0: flip vertically
#flipcode > 0: flip horizontally
#flipcode < 0: flip vertically and horizontally
#vertical flip
img_flip_ud = cv2.flip(image13, 0)
plt.imshow(img_flip_ud)
#horizontal flip
img_flip_lr = cv2.flip(image13, 1)
plt.imshow(img_flip_lr)

######### Rotation.
# The OpenCV function that rotates the image is cv2.rotate().The following three constants can be specified in rotateCode.
#cv2.ROTATE_90_CLOCKWISE
#cv2.ROTATE_90_COUNTERCLOCKWISE
#cv2.ROTATE_180
img_rotate_90_clockwise = cv2.rotate(image13, cv2.ROTATE_90_CLOCKWISE)
img_rotate_90_counterclockwise = cv2.rotate(image13, cv2.ROTATE_90_COUNTERCLOCKWISE)
img_rotate_180 = cv2.rotate(image13, cv2.ROTATE_180)

########### Scaling.
#RESIZE
def resize_image(image,w,h):
    resized_image = image=cv2.resize(image,(w,h))
    return resized_image
imshow(resize_image(image13, 500,500))

########## Brightness Manipulation.
def add_light(image, gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    image=cv2.LUT(image, table)
    return image
imshow(add_light(image13,2))

########## Cropping.
def crop_image(image,y1,y2,x1,x2):
    image=image[y1:y2,x1:x2]
    return image
imshow(crop_image(image13,200,800,250,1500))

############## Gaussian Blur.
def gaussian_blur(image,blur):
    image = cv2.GaussianBlur(image,(5,5),blur)
    return image
imshow(gaussian_blur(image13,0))
</code></pre>
</details></li>

<li><details><summary><b>imgaug</b></summary>
imgaug is a library for image augmentation in machine learning experiments. It supports a wide range of augmentation techniques, allows to easily combine these and to execute them in random order or on multiple CPU cores, has a simple yet powerful stochastic interface and can not only augment images, but also keypoints/landmarks, bounding boxes, heatmaps and segmentation maps.

<pre><code># imgaug
import imageio
import imgaug as ia
import imgaug.augmenters as iaa

############ Flipping.
hflip= iaa.Fliplr(p=1.0)
hflipped_image2= hflip.augment_image(image2)

#Vertically flipped
vflip= iaa.Flipud(p=1.0) 
vflipped_image2= vflip.augment_image(image2)

############### Rotation.
rot = iaa.Affine(rotate=(-25,25))
rot_clockwise_image2 = rot.augment_image(image2)

################### Cropping.
crop = iaa.Crop(percent=(0, 0.2)) # crop image
corp_image=crop.augment_image(image)

#################### Brightness Manipulation.
# bright
contrast1=iaa.GammaContrast(gamma=0.5)
brightened_image = contrast1.augment_image(image)

#dark
contrast2=iaa.GammaContrast(gamma=2)
darkened_image = contrast2.augment_image(image)

#################### Scaling.
scale_im=iaa.Affine(scale={"x": (1.5, 1.0), "y": (0.5, 1.0)})
scale_image =scale_im.augment_image(image)

#################### Noise Addition.
gaussian_noise=iaa.AdditiveGaussianNoise(15,20)
noise_image=gaussian_noise.augment_image(image)
</code></pre>
2.7 Augmentation pipeline<br>
The imgaug library provides a very useful feature called Augmentation pipeline. Such a pipeline is a sequence of steps that can be applied in a fixed or random order. This also gives the flexibility to apply certain transformations to a few images and other transformations to other images. In the following example, we are applying the flip, sharpen,crop etc transformations on some of the images. The blur and affline transformations will be applied sometimes and all these transformations will be applied in random order.

<pre><code>
# Defining a pipeline.
# The example has been taken from the documentation
aug_pipeline = iaa.Sequential([
    iaa.SomeOf((0,3),[
        iaa.Fliplr(1.0), # horizontally flip
        iaa.Flipud(1.0),# Vertical flip
        iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)), # sharpen images
        iaa.Crop(percent=(0, 0.4)),
        iaa.Sometimes(0.5, iaa.Affine(rotate=5)),
        iaa.Sometimes( 0.5,iaa.GaussianBlur(sigma=(0, 0.5))),
        iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
    ])
], 
random_order=True # apply the augmentations in random order
)

# apply augmentation pipeline to sample image
images_aug = np.array([aug_pipeline.augment_image(image2) for _ in range(16)])
</code></pre>
</details></li>

<li><details><summary><b>Data Augmentation</b></summary>

</details></li>

<li><details><summary><b>Data Augmentation</b></summary>

</details></li>

</ul></details>
</div>
