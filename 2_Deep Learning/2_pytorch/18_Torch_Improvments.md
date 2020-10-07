<h1>Improvments</h1>

<div style='width:1000px;margin:auto'>

<details><summary><b>Batch Normalization</b></summary><pre><code>import torch.nn as nn

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


</div>