# 3. Data Wrangling

<details><summary><b>Read in</b> Images</summary><p>
~~~python
import numpy as np
import matplotlib.image as mpimg # For reading in images

import matplotlib.pyplot as plt
import cv2 # OpenCV

%matplotlib qt  # Make matplotlib pop-up a plot not inline

image = mpimg.imread('images/waymo_car.jpg')

print('image dimensions:', image.shape)
~~~
</p></details>


<details><summary>Convert to <b>Gray</b> colormap</summary><p>
~~~python
gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

plt.matshow(gray_img)
plt.gray()
~~~
</p></details>

