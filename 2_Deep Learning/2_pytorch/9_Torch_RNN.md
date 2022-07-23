# RNN
<div style='width:1000px;margin:auto'>

<details><summary><b>MNIST</b> Example</summary>
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
class RNNModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, layer_dim, output_dim):
        super(RNNModel, self).__init__()
        # Hidden Dimensions
        self.hidden_dim = hidden_dim
        
        # Number of hidden layers.
        self.layer_dim  = layer_dim
        
        # Building Your RNN
        # batch_first=True causes input/output tensors to be of shape
        # (batch_dim, seq_dim, input_dim)
        self.rnn = nn.RNN(input_dim, hidden_dim, layer_dim,
                          batch_first=True, nonlinearity='relu')
        
        # Readout layer
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        # Initialize hidden state with zeros
        # (layer_dim, batch_size, hidden_dim)
        if torch.cuda.is_available():
        	h0 = Variable(torch.zeros(self.layer_dim, 
                                  	x.size(0),  # batch_size
                                  	self.hidden_dim)).cuda()
        else:
        	h0 = Variable(torch.zeros(self.layer_dim, 
                                  	x.size(0),  # batch_size
                                  	self.hidden_dim))
        out, hn = self.rnn(x, h0)
        
        # Index hidden state of last time step.
        # out.size() --> 100, 28, 100
        # out[:, -1, :] --> 100, 100 --> just want last time step hidden states!
        out = self.fc(out[:, -1, :])
        # out.size() --> 100, 10
        return out
~~~

<h4>5. Instantiate Model Class</h4>
~~~python
input_dim  = 28
hidden_dim = 100
layer_dim  = 1                # Number of layers
output_dim = 10

model = RNNModel(input_dim, hidden_dim, layer_dim, output_dim)

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
# Number of steps to unroll
seq_dim = 28



iter = 0
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        
        #######################
        #  USE GPU FOR MODEL  #
        #######################
        if torch.cuda.is_available():
            images = Variable(images.view(-1, seq_dim, input_dim).cuda())
            labels = Variable(labels.cuda())
        else:
	    images = Variable(images.view(-1, seq_dim, input_dim))
            labels = Variable(labels)
        
        # Clear gradients w.r.t. parameters
        optimizer.zero_grad()
        
        # Forward pass to get outputs
        # Output.size() --> 100, 10
        outputs = model(images)
        
        # Calculate Loss: softmax --> cross entropy loss
        loss = criterion(outputs, labels)
        
        # Getting gradients w.r.t. parameters
        loss.backward()
        
        # Updating parameters
        optimizer.step()
        
        iter += 1
        
        if iter % 50 == 0:
            # Calculate Accuracy         
            correct = 0
            total = 0
            # Iterate through test dataset
            for images, labels in test_loader:
                #######################
                #  USE GPU FOR MODEL  #
                #######################
                if torch.cuda.is_available():
                    images = Variable(images.view(-1, seq_dim, input_dim).cuda())
                else:
                    images = Variable(images.view(-1, seq_dim, input_dim))
                
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

            
            acc = 100 * correct / total
            
            # Store loss and iterations
            loss_list.append(loss.data)
            iteration_list.append(iter)
            acc_list.append(acc)
            
            if iter % 500 == 0:
            	# Print Loss
             	print(f'> {bg("Epoch", "s")}:{epoch}\t{bg("Iteration", "s", "grey")}:{iter} \t{bg("Loss", "s", "red")}:{loss.data:.4}\t{bg("Accuracy", "s", "green")}:{accuracy}')
~~~

<h4>7. Visualize loss & Accuracy</h4>
~~~python
# visualization loss 
plt.plot(iteration_list,loss_list)
plt.xlabel("Number of iteration")
plt.ylabel("Loss")
plt.title("CNN: Loss vs Number of iteration")
plt.show()

# visualization accuracy 
plt.plot(iteration_list,accuracy_list,color = "red")
plt.xlabel("Number of iteration")
plt.ylabel("Accuracy")
plt.title("CNN: Accuracy vs Number of iteration")
plt.show()
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
