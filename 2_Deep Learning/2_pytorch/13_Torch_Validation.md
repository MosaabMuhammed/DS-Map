# Inference & Validation

<details><summary><b>Without</b> Dropout [Normal Case]</summary>
<p>

<h4>1. Design the model</h4>
~~~python
from torch import nn, optim
import torch.nn.functional as F

class Classifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 64)
        self.fc4 = nn.Linear(64, 10)
        
    def forward(self, x):
        # make sure input tensor is flattened
        x = x.view(x.shape[0], -1)
        
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.log_softmax(self.fc4(x), dim=1)
        
        return x
~~~

<h4>2. Inference & Validation</h4>
~~~python
model = Classifier()
criterion = nn.NLLLoss()
optimizer = optim.Adam(model.parameters(), lr=0.003)

epochs = 30
steps = 0

train_losses, test_losses = [], []
for e in range(epochs):
    running_loss = 0
    for images, labels in trainloader:
        
        optimizer.zero_grad()
        
        log_ps = model(images)
        loss = criterion(log_ps, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        
    else:
        test_loss, accuracy = 0, 0
        with torch.no_grad():
            for images, labels in testloader:
                log_ps = model(images)
                test_loss += criterion(log_ps, labels)
                
                ps = torch.exp(log_ps)
                top_class = ps.topk(1, dim=1)[1]
                equals    = top_class == labels.view(*top_class.shape)
                accuracy  += torch.mean(equals.type(torch.FloatTensor))
                
        train_losses.append(running_loss/len(trainloader))
        test_losses.append(test_loss/len(testloader))
        
        print(f'> {bg("Epoch", "s", "gray")}:{e+1}/{epochs}\t{bg("Train Loss", "s", "red")}:{(running_loss/len(trainloader)):.3f} \t{bg("Test Loss", "s", "red")}:{(test_loss/len(testloader)):.4f}\t{bg("Test Accuracy", "s", "green")}:{(accuracy/len(testloader)):.4f}')
~~~

<h4>3. Plot Training & Testing Loss to notice Overfitting</h4>
~~~python
plt.plot(train_losses, label='Training losses')
plt.plot(test_losses, label='Validation Losses')
plt.legend(frameon=False)
~~~
</p>
</details>

<details><summary><b>With</b> Dropout</summary>
<p>

</p>
</details>
