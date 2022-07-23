<h1>Improvments</h1>

<div style='width:1000px;margin:auto'>

<details><summary><b>Batch Normalization</b></summary>
Batch normalization, or BatchNorm, is an often­used tool in designing CNNs. BatchNorm applies a
transformation to the output of a CNN by scaling the activations to have zero mean and unit variance.
The mean and variance values it uses for the Z­transform
9
are updated per batch such that
fluctuations in any single batch won’t shift or affect it too much. BatchNorm allows models to be less
sensitive to initialization of the parameters and simplifies the tuning of learning rates
<pre><code>import torch.nn as nn

# ...
	self.conv1 = nn.Conv1d(in_channels=1, out_channels=10,
	kernel_size=5,
	stride=1)
	self.conv1_bn = nn.BatchNorm1d(num_features=10)
# ...
def forward(self, x):
# ...
	x = F.relu(self.conv1(x))
	x = self.conv1_bn(x)
# ...
</code></pre>
</p></details>

<details><summary><b>Network-in-Network Connections</b> (1x1 Convolutions)</summary>
Network­in­network (NiN) connections are convolutional kernels with kernel_size=1 and have a
few interesting properties. In particular, a 1×1 convolution acts like a fully connected linear layer
across the channels.
0
This is useful in mapping from feature maps with many channels to shallower
feature maps. In igure 4­14, we show a single NiN connection being applied to an input matrix. As
you can see, it reduces the two channels down to a single channel. Thus, NiN or 1×1 convolutions
provide an inexpensive way to incorporate additional nonlinearity with few parameters
<pre><code>import torch.nn as nn

# ...
	self.conv1 = nn.Conv1d(in_channels=1, out_channels=10,
	kernel_size=1,
	stride=1)
# ...
def forward(self, x):
# ...
	x = F.relu(self.conv1(x))
# ...
</code></pre>
</p></details>


</div>