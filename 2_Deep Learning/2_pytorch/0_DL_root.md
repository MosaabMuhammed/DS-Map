<h1 style='color:#1E3D7F'>Deep Learning [PyTorch]</h1>

<div style='width:1000px;margin:auto'>

<details><summary><b>Functional</b> API</summary>
<p>
~~~python
import torch.nn.functional as F

class Network(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(28*28, 256)
        self.output = nn.Linear(256, 10)
    
    def forward(self, x):
        x = F.sigmoid(self.hidden(x))
        x = F.softmax(self.output(x), dim=1)
        
        return x
~~~
</p>
</details>

<details><summary><b>Sequential</b> API</summary>
<p>
<h4>1. Upload MNIST data</h4>
~~~python
from torchvision import datasets, transforms

# Define a transform to normalize the data
transform = transforms.Compose([transforms.ToTensor(),
                              transforms.Normalize((0.5,), (0.5,)),
                              ])

# Download and load the training data
trainset = datasets.MNIST('~/.pytorch/MNIST_data/', download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
~~~

<h4>2. Design the model</h4>
~~~python
input_size   = 784
hidden_sizes = [128, 64]
output_size  = 10

# Build a feed-forward network
model = nn.Sequential(nn.Linear(input_size, hidden_sizes[0]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[0], hidden_sizes[1]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[1], output_size),
                      nn.Softmax(dim=1))
print(model)

# We can also put it into OrderedDict to give a name to each layer.
from collections import OrderedDict
model = nn.Sequential(OrderedDict([
                      ('fc1', nn.Linear(input_size, hidden_sizes[0])),
                      ('relu1', nn.ReLU()),
                      ('fc2', nn.Linear(hidden_sizes[0], hidden_sizes[1])),
                      ('relu2', nn.ReLU()),
                      ('output', nn.Linear(hidden_sizes[1], output_size)),
                      ('softmax', nn.Softmax(dim=1))]))
# Now we can access like than
print(model.fc1) # Instead of model[0]
~~~

<h4>3. Utitlity Function</h4>
~~~python
def view_classify(img, ps, version="MNIST"):
    ''' Function for viewing an image and it's predicted classes.
    '''
    ps = ps.data.numpy().squeeze()

    fig, (ax1, ax2) = plt.subplots(figsize=(6, 9), ncols=2)
    ax1.imshow(img.resize_(1, 28, 28).numpy().squeeze())
    ax1.axis('off')
    ax2.barh(np.arange(10), ps)
    ax2.set_aspect(0.1)
    ax2.set_yticks(np.arange(10))
    if version == "MNIST":
        ax2.set_yticklabels(np.arange(10))
    elif version == "Fashion":
        ax2.set_yticklabels(['T-shirt/top',
                             'Trouser',
                             'Pullover',
                             'Dress',
                             'Coat',
                             'Sandal',
                             'Shirt',
                             'Sneaker',
                             'Bag',
                             'Ankle Boot'], size='small')
    ax2.set_title('Class Probability')
    ax2.set_xlim(0, 1.1)

    plt.tight_layout()
~~~

<h4>4. Forward pass through the network and display out</h4>
~~~python
# Forward pass through the network and display output.
images, labels = next(iter(trainloader))
images.resize_(images.shape[0], 1, 28*28)
ps = model.forward(images[0, :])
helper.view_classify(images[0].view(1, 28, 28), ps)
~~~
</p>
</details>

<hr>
<ul>
<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/markdown/2_Deep%20Learning/0_html/pytorch/1_Torch_LinReg.html"><font color='#333'><b style='font-size:20px'>Linear Regression</b></font></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/markdown/2_Deep%20Learning/0_html/pytorch/2_Torch_LogReg.html"><font color='#333'><b style='font-size:20px'>Logistic Regression</b></font></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/markdown/2_Deep%20Learning/0_html/pytorch/3_Torch_MLP.html"><font color='#333'><b style='font-size:20px'>MLP</b></font></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/markdown/2_Deep%20Learning/0_html/pytorch/4_Torch_CNN.html"><font color='#333'><b style='font-size:20px'>CNN</b></font></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/markdown/2_Deep%20Learning/0_html/pytorch/5_Torch_RNN.html"><font color='#333'><b style='font-size:20px'>RNN</b></font></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Data%20Science/00_Code/markdown/2_Deep%20Learning/0_html/pytorch/6_Torch_LSTM.html"><font color='#333'><b style='font-size:20px'>LSTM</b></font></a> </li>

</ul>
</div>