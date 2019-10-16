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


</div>
