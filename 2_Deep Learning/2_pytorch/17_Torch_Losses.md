<h1>Losses</h1>

<div style='width:1000px;margin:auto'>

<details><summary><b>Mean Squared Error</b></summary><pre><code>import torch
import torch.nn as nn

mse_loss = nn.MSELoss()
outputs  = torch.randn(3, 5, requires_grad=True)
targets  = torch.randn(3, 5)
loss = mse_loss(outputs, targets)
print(loss)
</code></pre>
</p></details>

<details><summary><b>Categorical Cross-Entropy</b></summary><pre><code># Categorical Cross-Entropy.
import torch
import torch.nn as nn

ce_loss = nn.CrossEntropyLoss()
outputs = torch.randn(3, 5, requires_grad=True)
targets = torch.tensor([1, 0, 3], dtype=torch.int64)
loss    = ce_loss(outputs, targets)
print(loss)
</code></pre>
</p></details>

<details><summary><b>Binary Cross-Entropy</b></summary><pre><code>bce_loss = nn.BCELoss()
sigmoid  = nn.Sigmoid()
probabilities = sigmoid(torch.randn(4, 1, requires_grad=True))
targets = torch.tensor([1, 0, 1, 0], dtype=torch.float32).view(4, 1)
loss = bce_loss(probabilities, targets)
print(probabilities)
print(loss)
</code></pre>
</p></details>


</div>