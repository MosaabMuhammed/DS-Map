# CNN
<div style='width:1000px;margin:auto'>

<details><summary>How to get<b> Conv & Pooling layer</b> shape:</summary>
<p>
<h4>1. Conv layer shape</h4>
$$O = \frac{W - K + 2 * P}{S}+1$$

<ul>
<li><b>O</b>: Output Height/Length.</li>
<li><b>W</b>: Input Height/Length.</li>
<li><b>K</b>: Filter size.</li>
<li><b>P</b>: Same Padding.</li>
$$P = \frac{K-1}{2}$$
<li><b>S</b>: Stride.</li>
</ul>
<hr>

<h4>2. Pooling Output shape</h4>
$$O = \frac{W}{K}$$

<ul>
<li><b>W</b>: Input Height/Width.</li>
<li><b>K</b>: Filter Size.</li>
</ul>
</p>
</details>

<details><summary>Example on MNIST</summary>
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
class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        
        # Convolution 1
        # Note: we're using 'same' padding.
        # For 'valid' padding --> make padding=0
        self.cnn1 = nn.Conv2d(in_channels=1, 
                              out_channels=16, 
                              kernel_size=5,
                              stride=1, 
                              padding=2)
        self.relu1 = nn.ReLU()
        
        # MaxPool 1
        self.maxpool1 = nn.MaxPool2d(kernel_size=2) # you can use nn.AvgPool2d(kernel_size=2)
        
        # Convolution 2
        self.cnn2 = nn.Conv2d(in_channels=16, 
                              out_channels=32,
                              kernel_size=5,
                              stride=1,
                              padding=2)
        self.relu2 = nn.ReLU()
        
        # MaxPool 2
        self.maxpool2 = nn.MaxPool2d(kernel_size=2)  # you can use nn.AvgPool2d(kernel_size=2)
        
        # Fully Connected layer (readout)
        # Note: You have to calculate the dimensions here yourself.
        self.fc1 = nn.Linear(32 * 7 * 7, 10)
        
    def forward(self, x):
        out = self.cnn1(x)
        out = self.relu1(out)
        out = self.maxpool1(out)
        out = self.cnn2(out)
        out = self.relu2(out)
        out = self.maxpool2(out)
        # Resize:
        # Original Size: (100, 32, 7, 7)
        # out.size(0): 100
        # New out size: (100, 32*7*7)
        out = out.view(out.size(0), -1)
        return self.fc1(out)
~~~

<h4>5. Instantiate Model Class</h4>
~~~python
model = CNNModel()

#######################
#  USE GPU FOR MODEL  #
#######################

if torch.cuda.is_available():
    model.cuda()
    
criterion = nn.CrossEntropyLoss()

learning_rate = 0.001

optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
~~~

<h4>6. Print Weight sizes</h4>
~~~python
for i in range(6):
    print(list(model.parameters())[i].size())
~~~

<h4>7. Loop over epochs</h4>
~~~python
iter = 0
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        
        #######################
        #  USE GPU FOR MODEL  #
        #######################
        if torch.cuda.is_available():
            images = Variable(images.cuda())
            labels = Variable(labels.cuda())
        else:
            images = Variable(images)
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
                    images = Variable(images.cuda())
                else:
                    images = Variable(images)
                
                # Forward pass only to get logits/output
                outputs = model(images)
                
                # Get predictions from the maximum value
                predicted = torch.max(outputs.data, 1)[1]
                
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
             print(f'> {bg("Epoch", "s")}:{epoch}\t{bg("Iteration", "s", "grey")}:{iter} \t{bg("Loss", "s", "red")}:{loss.data:.4}\t{bg("Accuracy", "s", "green")}:{accuracy}')
~~~
</p>
</details>

<li><p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/deep-learning-v2-pytorch/convolutional-neural-networks/cifar-cnn/cifar10_cnn_solution.html#Convolutional-Neural-Networks"><b style='color:#333'>Example on CIFAR</b></a></p></li>

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
