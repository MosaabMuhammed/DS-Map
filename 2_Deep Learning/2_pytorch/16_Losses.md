<h1>Activations</h1>

<div style='width:1000px;margin:auto'>

<details><summary><b>Sigmoid</b></summary><pre><code>import torch
import matplotlib.pyplot as plt

x = torch.range(-5, 5, .1)
y = torch.sigmoid(x)
plt.plot(x.numpy(), y.numpy())
plt.show()
</code></pre>
</p></details>

<details><summary><b>tanh</b></summary><pre><code>x = torch.range(-5, 5, .1)
y = torch.tanh(x)

plt.plot(x.numpy(), y.numpy())
plt.grid()
plt.show()
</code></pre>
</p></details>

<details><summary><b>ReLU</b></summary><pre><code>import torch

relu = torch.nn.functional.relu
x = torch.range(-5, 5, .1)
y = relu(x)

plt.plot(x.numpy(), y.numpy())
plt.grid(); plt.show()
</code></pre>
</p></details>

<details><summary><b>PReLU</b></summary><pre><code>import torch

prelu = torch.nn.PReLU(num_parameters=1)
x = torch.range(-5, 5, .1)
y = prelu(x)

plt.plot(x.detach().numpy(), y.detach().numpy())
plt.grid(); plt.show()
</code></pre>
</p></details>

<details><summary><b>Softmax</b></summary><pre><code>import torch.nn as nn
import torch

softmax = nn.Softmax(dim=1)
x_input = torch.randn(1, 3)
y_output = softmax(x_input)

print(x_input)
print(y_output)
print(torch.sum(y_output, dim=1))
</code></pre>
</p></details>

</p></details>

</div>