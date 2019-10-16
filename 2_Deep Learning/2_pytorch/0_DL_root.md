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