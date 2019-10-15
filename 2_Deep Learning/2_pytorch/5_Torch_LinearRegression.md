# Linear Regression

<div style='width:1000px;margin:auto'>

<details><summary>Core Model</summary>
<p>

<h4>1. Import Libraries</h4>
~~~python
import torch
import torch.nn as nn
from torch.autograd import Variable
~~~

<h4>2. Build the model</h4>
~~~python
class LinearRegressionModel2(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegressionModel2, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)
        
    def forward(self, x):
        return self.linear(x)
~~~

<h4>3. Define Optimizer, Loss</h4>
~~~python
input_dim  = 1
output_dim = 1

model = LinearRegressionModel2(input_dim, output_dim)

criterian = nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(), lr=.01)
~~~

<h4>4. Loop over epochs</h4>
~~~python
epochs = 100

for epoch in range(1, epochs):
    inputs = Variable(torch.from_numpy(x_values)).float()
    labels = Variable(torch.from_numpy(y_values)).float()
    
    optimizer.zero_grad()
    
    outputs = model(inputs)
    
    loss = criterian(outputs, labels)
    
    loss.backward()
    
    optimizer.step()
    
    print(f'~> Epoch: {epoch}, loss: {loss:.3f}.')
~~~

<h4>5. Predict Labels</h4>
~~~python
# Purely Inference
y_pred = model(Variable(torch.from_numpy(x_values)).float()).data.numpy()
y_pred
~~~

<h4>6. Plot true labels vs. predictions</h4>
~~~python
with plt.xkcd():
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, 'go', label='True Labels')
    plt.plot(x_values, y_pred, '--', label='Predicted Labels')
    plt.title('Model Output', size=20)
    plt.legend()
~~~
</p>
</details>

<details><summary><b>Save</b> & <b>Load</b> weights</summary>
<p>
<h4>1. Save weights</h4>
~~~python
torch.save(model.state_dict(), 'linearReg_model.pkl')
~~~

<h4>2. Load Weights</h4>
~~~python
model.load_state_dict(torch.load('linearReg_model.pkl'))
~~~
</p>
</details>

</div>