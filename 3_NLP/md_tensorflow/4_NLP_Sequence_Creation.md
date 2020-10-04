# Sequence Creation

<div style='width:1000px;margin:auto'>
<details><summary><b style='font-size:20px'>1. Tokenizer</b></summary><p>
~~~
# a tokenizer is a utility function to split a sentence into words. 

from keras.preprocessing.text import Tokenizer
## Tokenize the sentences
tokenizer = Tokenizer(num_words=max_features)
tokenizer.fit_on_texts(list(train_X)+list(test_X))
train_X = tokenizer.texts_to_sequences(train_X)
test_X = tokenizer.texts_to_sequences(test_X)
~~~
</p></details>

<details><summary><b style='font-size:20px'>2. pad_sequence</b></summary><p>
~~~
# Normally our model expects that each sequence(each training example) will be of the same length(same number of words/tokens). We can control this using the maxlen parameter.
# NOTE: applied after Tokenizer
# NOTE: you can change 'post' or 'pre'
# Refresher: https://stackoverflow.com/questions/42943291/what-does-keras-io-preprocessing-sequence-pad-sequences-do

from keras.preprocessing.sequence import pad_sequences

train_X = pad_sequences(train_X, maxlen=maxlen, truncating='post',padding='post')
test_X = pad_sequences(test_X, maxlen=maxlen, truncating='post',padding='post')
~~~
</p></details>
</div>