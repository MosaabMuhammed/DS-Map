# 3. Data Wrangling

<div style='width:1000px;margin:auto;'>
<details><summary><b>Read in</b> Images</summary><p>
~~~python
import numpy as np
import matplotlib.image as mpimg # For reading in images

import matplotlib.pyplot as plt
import cv2 # OpenCV

%matplotlib qt  # Make matplotlib pop-up a plot not inline
~~~
<h4>1. Using matplotlib.image</h4>
~~~python
image = mpimg.imread('images/waymo_car.jpg')

print('image dimensions:', image.shape)
~~~

<h4>2. Using CV2</h4>
~~~python
img = cv2.imread('path/to/image')

#### Note:
# the channel in cv2 is BGR, so you need to convert it to RGB, using the following code
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
~~~
</p></details> 


<details><summary>Convert to <b>Gray</b> colormap</summary><p>
~~~python
gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

plt.matshow(gray_img)
plt.gray()
~~~
</p></details>
<details><summary><b>Mask Out</b> Image</summary><p></ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_1_Image_Representation/3.%20Blue%20Screen.html#Color-Threshold,-Blue-Screen" style='font-weight:bold'>Blue Channel [RGB]</a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_1_Image_Representation/5_1.%20HSV%20Color%20Space,%20Balloons.html" style='font-weight:bold'>Hue Channel [HSV]</a></li>

</ul></p></details>
<details><summary><b>Fourier</b> Transform</summary><p>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2003_Convolutional%20Filters%20and%20Edge%20Detection/02.%20Frequency%20in%20Images.html" style='font-weight:bold'>Understanding the Concept</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_2_Convolutional_Filters_Edge_Detection/1.%20Fourier%20Transform.html#Fourier-Transforms" style='font-weight:bold'>Code</a></li>
</p></details>

<details><summary><b>High-Pass Filters</b> [Sobel]</summary><p>
<blockquote>
- High-pass filters used to <b>sharpen</b> an image,<br> and enhance <b>high-frequency</b> parts of an image.
</blockquote>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2003_Convolutional%20Filters%20and%20Edge%20Detection/08.%20Gradients%20and%20Sobel%20Filters.html" style='font-weight:bold'>Sobel Filters</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_2_Convolutional_Filters_Edge_Detection/2.%20Finding%20Edges%20and%20Custom%20Kernels.html#Creating-a-Filter,-Edge-Detection" style='font-weight:bold'>Code</a></li>
</p></details>


</div>
