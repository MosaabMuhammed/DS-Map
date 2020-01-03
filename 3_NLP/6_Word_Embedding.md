# Word Embedding

<div style='width:1000px;margin:auto'>
<details><summary><b style='font-size:20px'>1. GloVe</b></summary><p>
<h4>1. Read GloVe Vectors</h4>
```
embedding_dict = {}
with open('../../../Personal/Development/Courses Docs/GloVe - Pretrained Word Representation/glove.6B.100d.txt') as f:
    for line in f:
        values  = line.split()
        word    = values[0]
        vectors = np.asarray(values[1:], 'float32')
        embedding_dict[word] = vectors
        
f.close()
```

<h4>2. Tokenize & Add Padding</h4>
```
def create_corpus(df):
    corpus = []
    
    for text in tqdm(df.text):
        words = [word.lower() for word in word_tokenize(text) if word.isalpha() and word not in stop]
        corpus.append(words)
    return corpus

corpus = create_corpus(tweet)
```
```
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

MAX_LEN = 50
tokensizer = Tokenizer()
tokensizer.fit_on_texts(corpus)
sequences  = tokensizer.texts_to_sequences(corpus)

tweet_pad = pad_sequences(sequences, maxlen=MAX_LEN, truncating='post', padding='post')

# Print number of words
word_index = tokensizer.word_index
print(f'~> Number of Unique words: {bg(len(word_index))}')
```

<h4>3. Create Embedding Matrix</h4>
```
num_words = len(word_index)+1
embedding_matrix = np.zeros((num_words, 100))

for word, i in tqdm(word_index.items()):
    if i > num_words:
        continue
        
    emb_vec = embedding_dict.get(word)
    if emb_vec is not None:
        embedding_matrix[i] = emb_vec
``` 

<h4>4. LSTM Model with Embedding</h4>
```
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, SpatialDropout1D
from keras.initializers import Constant
from keras.optimizers import Adam

model = Sequential([
    Embedding(num_words, 100, embeddings_initializer=Constant(embedding_matrix), input_length=MAX_LEN),
    SpatialDropout1D(0.2),
    LSTM(64, dropout=0.2, recurrent_dropout=0.2),
    Dense(1, activation='relu')
])
model.summary()
```
```
# Compile the model
model.compile(loss='binary_crossentropy',
              optimizer=Adam(learning_rate=1e-5),
              metrics=['acc', f1_m])
```
```
# Train Test Split
train = tweet_pad[:tweet.shape[0]]
test  = tweet_pad[tweet.shape[0]:]

X_train, X_test, y_train, y_test = train_test_split(train,
                                                    tweet['target'].values,
                                                    test_size=0.15)

shape(X_train, X_test)
```
```
# Fit the model.
history = model.fit(X_train, y_train,
                    batch_size=4,
                    epochs=20,
                    validation_data=(X_test, y_test),
                    verbose=2)
```
</p></details>
</div>