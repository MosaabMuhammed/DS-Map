<!doctype HTML><html><head><meta charset="utf-8"><title>Made with Remarkable!</title><link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.1/styles/github.min.css"><style type='text/css'>body,table tr{background-color:#fff}table tr td,table tr th{border:1px solid #ccc;text-align:left;padding:6px 13px;margin:0}pre code,table,table tr{padding:0}hr,pre code{background:0 0}body{font:16px Helvetica,Arial,sans-serif;line-height:1.4;color:#333;word-wrap:break-word;padding:10px 15px}strong,table tr th{font-weight:700}h1{font-size:2em;margin:.67em 0;text-align:center}h2{font-size:1.75em}h3{font-size:1.5em}h4{font-size:1.25em}h1,h2,h3,h4,h5,h6{font-weight:700;position:relative;margin-top:15px;margin-bottom:15px;line-height:1.1}h1,h2{border-bottom:1px solid #eee}hr{height:0;margin:15px 0;overflow:hidden;border:0;border-bottom:1px solid #ddd}a{color:#4183C4}a.absent{color:#c00}ol,ul{padding-left:15px;margin-left:5px}ol{list-style-type:lower-roman}table tr{border-top:1px solid #ccc;margin:0}table tr:nth-child(2n){background-color:#aaa}table tr td :first-child,table tr th :first-child{margin-top:0}table tr td:last-child,table tr th :last-child{margin-bottom:0}img{max-width:100%}blockquote{padding:0 15px;border-left:4px solid #ccc}code,tt{margin:0 2px;padding:0 5px;white-space:nowrap;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px}pre code{margin:0;white-space:pre;border:none}.highlight pre,pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px}</style></head><body><h1>CNN</h1>
<div style='width:1000px;margin:auto'>

<details><summary><b>Tutorials</b></summary><p><ul>

<li><p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/09.%20Local%20Connectivity.html"><b>1. Difference b/w MLP & CNN</b></a> </p></li>
</ul>

<details><summary>2. Understanding <b>Model.summary()</b> in <b> [Keras]</b></summary>
<p>
<h4>1. Output of model.summary()</h4>

<pre><code class="python">_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
conv2d_1 (Conv2D)            (None, 222, 222, 32)      896
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 220, 220, 64)      18496
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 218, 218, 128)     73856
_________________________________________________________________
dense_9 (Dense)              (None, 218, 218, 10)      1290
</code></pre>


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


<pre><code class="python"># Formula
(K * F * F * D_in) + K

assert 32 * (3 * (3*3) + 1) == 896
assert 64 * (32 * (3*3) + 1) == 18496
assert 128 * (64 * (3*3) + 1) == 73856
assert num_classes * (128 + 1) == 1290  
</code></pre>


- Since there are <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>F * F * D_in</span> weights per filter, and the conv layer is composed of <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K</span> filters, the total number of weights in the conv layer is <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K * F * F * D_in</span>.<br>
- Since there is one bias term per filter, the conv layer has <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K</span> biases. We can generate the formula above.
</p>

<h4>4. Shape of the Convolution layer (formula):</h4>
<p><ol>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K</span> - the number of <b>filters</b> in the convolutional layer</li>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>F</span> - the <b>height</b> and <b>width</b> of the convolutional filters</li>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>S</span> - the <b>stride</b> of the convolution</li>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>H_in</span> - the <b>height</b> of the <b>previous</b> layer</li>
<li><span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>W_in</span> - the <b>width</b> of the <b>previous</b> layer</li>
</ol></p>

The depth of the convolutional layer will always equal the number of filters <span style='color:white;background-color:#2F3D48;padding:3px;border-radius:4px;font-weight:bold'>K</span>.<br><br>

If <b>padding = 'same'</b>, then the spatial dimensions of the convolutional layer are the following:

$$Height = ceil(\frac{float(H_{in})}{float(S)})$$

$$Weight = ceil(\frac{float(W_{in})}{float(S)})$$

If <b>padding = 'valid'</b>, then the spatial dimensions of the convolutional layer are the following:

$$Height = ceil(\frac{float(H_{in} - F + 1)}{float(S)})$$

$$Weight = ceil(\frac{float(W_{in} - F + 1)}{float(S)})$$

</p></details>

<p></p></details></p>
<details><summary><b>Refreshing Examples</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/6%20Convolutional%20Neural%20Networks.html"><b>1. MNIST Example</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/solutions/6%20Convolutional%20Neural%20Networks%20Exercises%20Solution.html#Exercise-2"><b>2. CIFAR Example</b></a> </p>

</p></details>

<details><summary><b>Practical Notes</b> when building <b>An Architecture</b></summary>
<p>
1. Use <b>activation = 'relu'</b> at each convolutional layer.<br>
2. Use <b>padding = 'Same'</b>, most likely to get better results. This is not the default in Keras.<br>
3. The number of filters increases over each convolution layer. Ex: 16, 32, 64, and so on.
</p></details>

<details><summary><b>MaxPooling</b> layer for <b>Depth</b></summary><p>
<ul>
<li>This can allow the CNN to learn to be invariant to various
features.</li>
<li> For example, it could learn multiple filters, each detecting a
different rotation of the same pattern</li>
<li> the depthwise max pooling layer would ensure that the
output is the same regardless of the rotation</li>
<li>The CNN could similarly
learn to be invariant to anything else: thickness, brightness, skew, color,
and so on.</li>
</ul>

<h4>1. Using a class</h4>

<pre><code># Notice the depth of the layer should be divisor by the depth of the previous layer.
# here we can use 3, since we have a RGB image.
class DepthMaxPool(keras.layers.Layer):
    def __init__(self, pool_size, strides=None, padding=&quot;VALID&quot;, **kwargs):
        super().__init__(**kwargs)
        if strides is None:
            strides = pool_size
        self.pool_size = pool_size
        self.strides = strides
        self.padding = padding
    def call(self, inputs):
        return tf.nn.max_pool(inputs,
                              ksize=(1, 1, 1, self.pool_size),
                              strides=(1, 1, 1, self.pool_size),
                              padding=self.padding)

# Use the class
depth_pool = DepthMaxPool(3)
with tf.device(&quot;/cpu:0&quot;): # there is no GPU-kernel yet
    depth_output = depth_pool(cropped_images)
depth_output.shape
</code></pre>


<h4>2. Using Lambda</h4>

<pre><code>depth_pool = keras.layers.Lambda(lambda X: tf.nn.max_pool(
    X, ksize=(1, 1, 1, 3), strides=(1, 1, 1, 3), padding=&quot;VALID&quot;))
with tf.device(&quot;/cpu:0&quot;): # there is no GPU-kernel yet
    depth_output = depth_pool(cropped_images)
depth_output.shape

</code></pre>

</p></details>

</div><script src="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.1/highlight.min.js"></script><script>hljs.initHighlightingOnLoad();</script><script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script><script type="text/javascript">MathJax.Hub.Config({"showProcessingMessages" : false,"messageStyle" : "none","tex2jax": { inlineMath: [ [ "$", "$" ] ] }});</script></body></html>