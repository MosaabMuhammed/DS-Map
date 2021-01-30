<h1 id="3datawrangling">3. Data Wrangling</h1>

<div style='width:1000px;margin:auto;'>
<details><summary><b>Read in</b> Images</summary><p><pre><code class="python language-python">import numpy as np
import matplotlib.image as mpimg # For reading in images

import matplotlib.pyplot as plt
import cv2 # OpenCV

%matplotlib qt  # Make matplotlib pop-up a plot not inline
</code></pre>
<h4>1. Using matplotlib.image</h4><pre><code class="python language-python">image = mpimg.imread('images/waymo_car.jpg')

print('image dimensions:', image.shape)
</code></pre>

<h4>2. Using CV2</h4><pre><code class="python language-python">img = cv2.imread('path/to/image')

#### Note:
# the channel in cv2 is BGR, so you need to convert it to RGB, using the following code
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
</code></pre>

<h4>3. Using skimage</h4><pre><code class="python language-python">from skimage.io import imshow, imread, imsave

image = imread(Image_Data_Path + file_path)
imshow(image)
</code></pre>
</p></details> 


<details><summary>Convert to <b>Gray</b> colormap</summary><p>
<h4>Using CV2</h4>
<pre><code class="python language-python">gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

plt.matshow(gray_img)
plt.gray()
</code></pre>

<h4>Using skimage</h4>
<pre><code class="python language-python">from skimage import color
from skimage.io import imshow, imread

# Converting image to grayscale.
grayscale_image = color.rgb2gray(image)
grayscale_image.shape
imshow(grayscale_image)
</code></pre>
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

<details><summary><b>Low-Pass Filters</b> [Gaussian Blur]</summary><p>
<blockquote>
- <b>Low-Pass filters</b> used to <b>blur/smooth</b> an image,<br> and block <b>high-frequency</b> parts of an image.
</blockquote>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2003_Convolutional%20Filters%20and%20Edge%20Detection/08.%20Gradients%20and%20Sobel%20Filters.html" style='font-weight:bold'>Gaussian Blur</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_2_Convolutional_Filters_Edge_Detection/3.%20Gaussian%20Blur.html#Gaussian-Blur,-Medical-Images" style='font-weight:bold'>Gaussian Blur <b>Code</b></a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_2_Convolutional_Filters_Edge_Detection/4.%20Fourier%20Transform%20of%20Filters.html#High-and-Low-Pass-Filters" style='font-weight:bold'>High and Low Pass Filters</a></li>
</p></details>

<details><summary><b>Canny</b> Detector</summary><p>
<blockquote>
<ol> 
<li><b>Filters out noise</b> using a Gaussian blur.</li>
<li><b>Finds the strength and direction of edges</b> using Sobel filters.</li>
<li><b>Applies non-maximum suppression</b> to isolate the strongest edges and thin them to one-pixel wide lines.</li>
<li>Uses <b>hysteresis to isolate the best edges</b></li>
</ol>
</blockquote>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2003_Convolutional%20Filters%20and%20Edge%20Detection/15.%20Canny%20Edge%20Detector.html" style='font-weight:bold'>Video tutorial</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_2_Convolutional_Filters_Edge_Detection/5.%20Canny%20Edge%20Detection.html#TODO:-Try-to-find-the-edges-of-this-flower" style='font-weight:bold'>Code</a></li>
</p></details>

<details><summary><b>Hough</b> Space</summary><p>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2003_Convolutional%20Filters%20and%20Edge%20Detection/18.%20Hough%20Transform.html" style='font-weight:bold'>Video tutorial</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_2_Convolutional_Filters_Edge_Detection/6_1.%20Hough%20lines.html#Hough-Lines" style='font-weight:bold'>Detecting lines</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_2_Convolutional_Filters_Edge_Detection/6_2.%20Hough%20circles,%20agriculture.html#Hough-Circle-Detection" style='font-weight:bold'>Detecting Circles</a></li>
</p></details>

<details><summary><b>Haar</b> Cascade</summary><p>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2003_Convolutional%20Filters%20and%20Edge%20Detection/23.%20Haar%20Cascades.html" style='font-weight:bold'>Video tutorial</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_2_Convolutional_Filters_Edge_Detection/7.%20Haar%20Cascade,%20Face%20Detection.html#Face-detection-using-OpenCV" style='font-weight:bold'>Code</a></li>
</p></details>
<hr>
<details><summary><b>Corner</b> Detection</summary><p>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2004_Types%20of%20Features%20%20Image%20Segmentation/02.%20Corner%20Detectors.html" style='font-weight:bold'>Video tutorial</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_3_Types_of_Features_Image_Segmentation/1.%20Harris%20Corner%20Detection.html#Harris-Corner-Detection" style='font-weight:bold'>Code</a></li>
</p></details>


<details><summary><b>Dilation, Erosion, Opening, and Closing</b> [Morphological Operation]</summary><p>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2004_Types%20of%20Features%20%20Image%20Segmentation/04.%20Dilation%20and%20Erosion.html" style='font-weight:bold'>tutorial</a></li>
</p></details>

<details><summary><b>Image  Contours</b></summary><p>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2004_Types%20of%20Features%20%20Image%20Segmentation/06.%20Image%20Contours.html" style='font-weight:bold'>Video tutorial</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_3_Types_of_Features_Image_Segmentation/2.%20Contour%20detection%20and%20features.html#Finding-Contours" style='font-weight:bold'>Code</a></li>
</p></details>

<details><summary><b>K-means Clustering</b> [Segmentation]</summary><p>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2004_Types%20of%20Features%20%20Image%20Segmentation/09.%20K-means%20Clustering.html" style='font-weight:bold'>Video tutorial</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_3_Types_of_Features_Image_Segmentation/3.%20K-means.html#K-means-Clustering" style='font-weight:bold'>Code</a></li>
</p></details>
<hr>
<h4>Feature Vectors</h4>
<details><summary><b>ORB</b> [<b>O</b>riented Fast and <b>R</b>otated <b>B</b>rief]</summary><p>
<blockquote>
<b>FAST</b>: <b>F</b>eatures From <b>A</b>ccelerated <b>S</b>egments <b>T</b>est. <br>
FAST: trys to find the keypoints in an image.<br>
<b>BRIEF</b>: <b>B</b>inary <b>R</b>obust <b>I</b>ndependent <b>E</b>lementary <b>F</b>eatures.<br>
BRIEF: trys to create binary feature vectors from a set of key points.
</blockquote>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2005_Feature%20Vectors/04.%20Introduction%20to%20ORB.html" style='font-weight:bold'>Video [Introduction to ORB]</a></li>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2005_Feature%20Vectors/05.%20FAST.html" style='font-weight:bold'>Video [FAST]</a></li>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2005_Feature%20Vectors/07.%20BRIEF.html" style='font-weight:bold'>Video [BRIEF]</a></li>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2005_Feature%20Vectors/07.%20BRIEF.html" style='font-weight:bold'>Video [Scale & Rotation Invariance]</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_4_Feature_Vectors/2.%20ORB.html#Oriented-FAST-and-Rotated-BRIEF-(ORB)" style='font-weight:bold'>Code</a></li>
</p></details>

<details><summary><b>HOG</b> [<b>H</b>istogram of <b>O</b>riented <b>G</b>radient]</summary><p>
<li><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Computer%20Vision%20Nanodegree%20v1.0.0/Part%2001-Module%2001-Lesson%2005_Feature%20Vectors/13.%20HOG.html" style='font-weight:bold'>Video tutorial</a></li>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_4_Feature_Vectors/3_1.%20HOG.html" style='font-weight:bold'>Code</a></li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/CVND_Exercises-master/1_4_Feature_Vectors/3_2.%20HOG%20Examples.html#Examples" style='font-weight:bold'>Examples</a></li>
</p></details>

</div>