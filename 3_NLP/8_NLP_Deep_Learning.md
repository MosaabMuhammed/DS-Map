# Deep Learning

<div style='width:1000px;margin:auto'>

<details><summary><b>CNN with GloVe</b></summary><p>
<li><a href='./0_notebooks/CNN.html'>CNN with Text</a></li>
</p></details>

<details><summary><b>LSTM & GRU & Bi-Directional</b></summary><p>
<li><a href='./0_notebooks/LSTM_Toxic.html'>LSTM with Text</a></li>
<h4>Note: For Bi-Directional, do the following:</h4>
```
x = Bidirectional(LSTM(15, return_sequences=True))(x)
x = GlobalMaxPool1D()(x)
```

</p></details>

</div>