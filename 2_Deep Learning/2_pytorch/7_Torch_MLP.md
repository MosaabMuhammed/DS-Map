# MLP

<div style='width:1000px;margin:auto'>

<details><summary>Core Model</summary>
<p>

<h4>1. Import Libraries</h4>
~~~python
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as dsets
from torch.autograd import Variable
~~~

<h4>2. Upload MNIST Dataset</h4>
~~~python
train_dataset = dsets.MNIST(root='./data', 
                            train=True, 
                            transform=transforms.ToTensor(),
                            download=True)

test_dataset = dsets.MNIST(root='./data', 
                           train=False, 
                           transform=transforms.ToTensor())
~~~

<h4>3. Making Dataset Iterable</h4>
~~~python
batch_size = 100
n_iters = 3000
num_epochs = n_iters / (len(train_dataset) / batch_size)
num_epochs = int(num_epochs)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, 
                                           batch_size=batch_size, 
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset, 
                                          batch_size=batch_size, 
                                          shuffle=False)
~~~

<h4>4. Build the model</h4>
~~~python
class LogisticRegressionModel2(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(LinearRegressionModel2, self).__init__()
        self.fc1    = nn.Linear(input_dim, hidden_dim)
        self.relu1 = nn.ReLU()  # nn.Tanh() or nn.Sigmoid()
        
        self.fc2    = nn.Linear(hidden_dim, hidden_dim)
        self.relu2 = nn.ReLU()
        
        self.fc3    = nn.Linear(hidden_dim, hidden_dim)
        self.relu3 = nn.ReLU()
        
        self.fc4 = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
    	fc1    = self.fc1(x)
    	relu1 = self.relu1(fc1)
    	
    	fc2    = self.fc2(relu1)
    	relu2 = self.relu2(fc2)
    	
    	fc3    = self.fc3(relu2)
    	relu3 = self.relu3(fc3)
    	
        return self.fc4(relu3)
~~~

<h4>5. Instantiate Model Class</h4>
~~~python
input_dim = 28*28
hidden_dim = 100
output_dim = 10

model = LogisticRegressionModel(input_dim, output_dim)

#######################
#  USE GPU FOR MODEL  #
#######################

if torch.cuda.is_available():
    model.cuda()
    
criterion = nn.CrossEntropyLoss()

learning_rate = 0.1

optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
~~~

<h4>6. Loop over epochs</h4>
~~~python
iter = 0
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        
        #######################
        #  USE GPU FOR MODEL  #
        #######################
        if torch.cuda.is_available():
            images = Variable(images.view(-1, 28*28).cuda())
            labels = Variable(labels.cuda())
        else:
            images = Variable(images.view(-1, 28*28))
            labels = Variable(labels)
        
        # Clear gradients w.r.t. parameters
        optimizer.zero_grad()
        
        # Forward pass to get output/logits
        outputs = model(images)
        
        # Calculate Loss: softmax --> cross entropy loss
        loss = criterion(outputs, labels)
        
        # Getting gradients w.r.t. parameters
        loss.backward()
        
        # Updating parameters
        optimizer.step()
        
        iter += 1
        
        if iter % 500 == 0:
            # Calculate Accuracy         
            correct = 0
            total = 0
            # Iterate through test dataset
            for images, labels in test_loader:
                #######################
                #  USE GPU FOR MODEL  #
                #######################
                if torch.cuda.is_available():
                    images = Variable(images.view(-1, 28*28).cuda())
                else:
                    images = Variable(images.view(-1, 28*28))
                
                # Forward pass only to get logits/output
                outputs = model(images)
                
                # Get predictions from the maximum value
                _, predicted = torch.max(outputs.data, 1)
                
                # Total number of labels
                total += labels.size(0)
                
                #######################
                #  USE GPU FOR MODEL  #
                #######################
                # Total correct predictions
                if torch.cuda.is_available():
                    correct += (predicted.cpu() == labels.cpu()).sum()
                else:
                    correct += (predicted == labels).sum()

            
            accuracy = 100 * correct / total
            
            # Print Loss
            print('Iteration: {}. Loss: {}. Accuracy: {}'.format(iter, loss.data, accuracy))
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