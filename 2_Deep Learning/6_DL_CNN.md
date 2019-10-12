# CNN
<div style='width:1000px;margin:auto'>

<details><summary><b>Tutorials</b></summary>
<p>

<ul>
<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/09.%20Local%20Connectivity.html"><b>1. Difference b/w MLP & CNN</b></a> </p></li>
</ul>

<details><summary>2. Understanding <b>Model.summary()</b> in <b> [Keras]</b></summary>
<p>
<h4>1. Output of model.summary()</h4>
~~~python
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
conv2d_1 (Conv2D)            (None, 222, 222, 32)      896
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 220, 220, 64)      18496
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 218, 218, 128)     73856
_________________________________________________________________
dense_9 (Dense)              (None, 218, 218, 10)      1290
~~~

<h4>2. Output Shape</h4>
<p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b style='font-size:16px;'><center>(None, 222, 222, 32)</center></b><br>
<ol>
1. <b>None</b>: &nbsp;Corresponds to <b>Batch Size</b><br>
2. <b>222</b>: &nbsp;&nbsp;&nbsp;&nbsp;Corresponds to <b>Height</b> of convolution layer<br>
3. <b>222</b>: &nbsp;&nbsp;&nbsp;&nbsp;Corresponds to <b>Width</b> of convolution layer<br>
4. <b>32</b>: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Corresponds to <b>Depth</b>of convolution layer<br>
</ol>
</p>

<h4>3. Num. of Parameters:</h4>
<p>
- When we define the Conv2D, we assign the following parameters:<br>
1. <b>Filters (K)</b>: Number of the filters in the conv layer.<br>
2. <b>Kernel Size (F)</b>: The height and Width of the conv layer.<br>
3. <b>Input Shape (D_in)</b>: The depth of the previous layer.<br>

~~~python
# Formula
(K * F * F * D_in) + K

assert 32 * (3 * (3*3) + 1) == 896
assert 64 * (32 * (3*3) + 1) == 18496
assert 128 * (64 * (3*3) + 1) == 73856
assert num_classes * (128 + 1) == 1290	
~~~

- Since there are <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>F * F * D_in</span> weights per filter, and the conv layer is composed of <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K</span> filters, the total number of weights in the conv layer is <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K * F * F * D_in</span>.<br>
- Since there is one bias term per filter, the conv layer has <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K</span> biases. We can generate the formula above.
</p>

<h4>4. Shape of the Convolution layer (formula):</h4>
<p>
<ol>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K</span> - the number of <b>filters</b> in the convolutional layer</li>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>F</span> - the <b>height</b> and <b>width</b> of the convolutional filters</li>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>S</span> - the <b>stride</b> of the convolution</li>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>H_in</span> - the <b>height</b> of the <b>previous</b> layer</li>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>W_in</span> - the <b>width</b> of the <b>previous</b> layer</li>
</ol>
</p>

The depth of the convolutional layer will always equal the number of filters <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K</span>.<br><br>

If <b>padding = 'same'</b>, then the spatial dimensions of the convolutional layer are the following:
~~~python
height = ceil(float(H_in) / float(S))
width = ceil(float(W_in) / float(S))
~~~

If <b>padding = 'valid'</b>, then the spatial dimensions of the convolutional layer are the following:
~~~python
height = ceil(float(H_in - F + 1) / float(S))
width = ceil(float(W_in - F + 1) / float(S))
~~~
</p>
</details>

</p>
</details>

<details><summary><b>Refreshing Examples</b></summary>
<p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/6%20Convolutional%20Neural%20Networks.html"><b>1. MNIST Example</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/solutions/6%20Convolutional%20Neural%20Networks%20Exercises%20Solution.html#Exercise-2"><b>2. CIFAR Example</b></a> </p>

</p>
</details>

<details><summary><b>Practical Notes</b> when building <b>An Architecture</b></summary>
<p>
1. Use <b>activation = 'relu'</b> at each convolutional layer.<br>
2. Use <b>padding = 'Same'</b>, most likely to get better results. This is not the default in Keras.<br>
3. The number of filters increases over each convolution layer. Ex: 16, 32, 64, and so on.
</p>
</details>

<details><summary><b>Transfer Learning</b></summary>
<p>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/25.%20Transfer%20Learning.html"><b>How to choose Transfer Learning Model</b></a> </p></li>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/26.%20Transfer%20Learning%20in%20Keras.html"><b>How to use Transfer Learning</b></a> </p></li>
	
<li><p><a href="https://github.com/alexisbcook/keras_transfer_cifar10/blob/master/Keras_Transfer_CIFAR10.ipynb"><b>Ex: Inception</b></a> </p></li>

</p>
</details>

</div>
