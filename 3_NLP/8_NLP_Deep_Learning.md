# Deep Learning

<div style='width:1000px;margin:auto'>

<details><summary><b>CNN with GloVe</b></summary><p>
<li><a href='./0_notebooks/CNN.html'>CNN with Text</a></li>
</p></details>

<details><summary><b>LSTM & GRU & Bi-Directional</b></summary><p>
<li><a href='./0_notebooks/LSTM_Toxic.html'>LSTM with Text</a></li>
<h4>Note: For Bi-Directional, do the following:</h4>
```
# you have 2 options:
# 1. return a sequence, then select the max features among them.
# 2. Don't return a sequence, just return the last value, and here there's no neet for GlobalMaxPool1D
x = Bidirectional(LSTM(15, return_sequences=True))(x)
x = GlobalMaxPool1D()(x)
```

</p></details>

<details><summary><b>BERT</b></summary><p>
<li><a href='./0_notebooks/BERT for Humans.html#Comprehensive-BERT-Tutorial'>Tutorials on BERT</a></li>
<li><a href='./0_notebooks/BERT Keras.html#This-is-the-very-first-time-I-would-be-implementing-BERT.'>BERT Keras</a></li>
<li><a href='./0_notebooks/BERT using simple transformers.html'>BERT using simpleTransformers</a></li>
</p></details>

</div>