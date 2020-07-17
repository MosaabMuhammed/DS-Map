# Modeling

<div style='width:1000px;margin:auto'>

<details><summary><b>CNN with Embedding</b></summary><p><ul>
<li><a href='./0_notebooks/CNN.html'>CNN with GloVe</a></li>
<li><a href='./0_notebooks/ch07.html'>CNN with GoogleNews <b>word2vec</b></a></li>
</ul></p></details>

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

<details><summary><b>Sentiment Analysis</b> using <b>Rule-based</b></summary><p>
```
# !pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sa = SentimentIntensityAnalyzer()
# sa.lexicon --> Print the lexicons

sa.polarity_scores(text="Python is very readable and it's great for NLP.")
```
```
corpus = ["Absolutely perfect! Love it! :-) :-) :-)",
          "Horrible! Completely useless. :(",
          "It was OK. some good and some bad things."]

for doc in corpus:
    scores = sa.polarity_scores(doc)
    print(f"{scores['compound']:+}: {doc}")
```
</p></details>

<details><summary><b>Latent Discriminant Analysis</b></summary><p>
<p>NOTE: you can use it in sklearn. (sklearn.discriminant_analysis.LinearDiscriminantAnalysis), but here we show the manual calculations on spam filter.</p>
<p>LDA is very useful when we have more columns and less rows, specially in text analysis</p>

```
# 1. Calculate the TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize.casual import casual_tokenize
tfidf_model = TfidfVectorizer(tokenizer=casual_tokenize)
tfidf_docs  = tfidf_model.fit_transform(sms.text).toarray()

# 2. Calculate the mean for spam and ham.
mask = sms.spam.astype(bool).values
spam_centriod = tfidf_docs[mask].mean(axis=0)
ham_centriod  = tfidf_docs[~mask].mean(axis=0)

# 3. Dot product with TF_IDF matrix.
spamminess_score = tfidf_docs.dot(spam_centriod - ham_centriod)
spamminess_score.round(2)

# 4. Normalize to predict.
from sklearn.preprocessing import MinMaxScaler
sms["lda_score"]   = MinMaxScaler().fit_transform(spamminess_score.reshape(-1, 1))
sms["lda_predict"] = (sms.lda_score > .5).astype(int)
sms["spam lda_predict lda_score".split()].round(2).head(6)~~~~
```
</p></details>

<details><summary><b>Language Model</b></summary><p>
<h4>1. Load the corpus</h4>
```
import nltk
nltk.download("gutenberg")
from nltk.corpus import gutenberg
gutenberg.fileids()

# Concatenate the samples into one corpus
text = ''
for txt in gutenberg.fileids():
    if 'shakespeare' in txt:
        text += gutenberg.raw(txt).lower()

chars = sorted(list(set(text)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

print(f"corpus length: {bg(len(text))}, total chars: {bg(len(chars))}")
```

<h4>2. Prepare the input & output</h4>
```
maxlen = 40
step   = 3
sentences  = []
next_chars = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i+maxlen])
    next_chars.append(text[i+maxlen])

print(f"nb sequences: {bg(len(sentences))}, {bg(len(next_chars))}")
```

<h4>3. Create One-Hot encoding</h4>
```
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1
```

<h4>3. Create the model</h4>
```
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.layers import LSTM
from tensorflow.keras.optimizers import RMSprop

model = Sequential([
    LSTM(128, input_shape=(maxlen, len(chars))),
    Dense(len(chars), activation="softmax")
])

optimizer = RMSprop(lr=.01)
model.compile(loss="categorical_crossentropy", optimizer=optimizer)
model.summary()

# Train the model.
epochs          = 6
batch_size      = 128
model_structure = model.to_json()
with open("shakes_lstm_model.json", "w") as json_file:
    json_file.write(model_structure)

for i in range(5):
    model.fit(X, y,
              batch_size=batch_size,
              epochs=epochs)
    model.save_weights(f"shakes_lstm_weights_{i+1}.h5")
```

<h4>4. Predict the next n characters with temperature</h4>
```
import random
def sample(preds, temprature=1.0):
    preds     = np.asarray(preds).astype('float64')
    preds     = np.log(preds) / temprature
    exp_preds = np.exp(preds)
    preds     = exp_preds / np.sum(exp_preds)
    probas    = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)
    
import sys
start_index = random.randint(0, len(text)-maxlen-1)
for diversity in [.2, .5, 1.]:
    print()
    print(f"------------ Diversity: {diversity}")
    generated = ''
    sentence  = text[start_index: start_index+maxlen]
    generated += sentence
    print(f"---------- Generating with seed: {sentence}")
    sys.stdout.write(generated)
    
    for i in range(400):
        x = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            x[0, t, char_indices[char]] = 1.
        preds = model.predict(x, verbose=0)[0]
        next_index = sample(preds, diversity)
        next_char  = indices_char[next_index]
        generated += next_char
        sentence   = sentence[1:] + next_char
        sys.stdout.write(next_char)
        sys.stdout.flush()

    print()
```
</p></details>

<details><summary><b>Seq2Seq</b></summary><p>
<h4>1. Prepare the data</h4>
```
# !pip install nlpia
from nlpia.loaders import get_data
df = get_data("moviedialog")
input_texts, target_texts = [], []
input_vocab, output_vocab = set(), set()
start_token, stop_token   = '\t', '\n'
max_training_samples      = min(25_000, len(df)-1)


for input_text, target_text in zip(df.statement, df.reply):
    target_text = start_token + target_text + stop_token
    input_texts.append(input_text)
    target_texts.append(target_text)

    for char in input_text:
        if char not in input_vocab:
            input_vocab.add(char)

    for char in target_text:
        if char not in output_vocab:
            output_vocab.add(char)
```

```
input_vocab  = sorted(input_vocab)
output_vocab = sorted(output_vocab)

input_vocab_size  = len(input_vocab)
output_vocab_size = len(output_vocab)

max_encoder_seq_length = max([len(txt) for txt in input_texts])
max_decoder_seq_length = max([len(txt) for txt in target_texts])

input_token_index  = dict([(char, i) for i, char in enumerate(input_vocab)])
target_token_index = dict([(char, i) for i, char in enumerate(output_vocab)])

reverse_input_char_index  = dict((i, char) for char, i in input_token_index.items())
reverse_target_char_index = dict((i, char) for char, i in target_token_index.items())
```

```
encoder_input_data = np.zeros((len(input_texts), max_encoder_seq_length, input_vocab_size),
                              dtype='float32')
decoder_input_data = np.zeros((len(input_texts), max_decoder_seq_length, output_vocab_size),
                              dtype="float32")
decoder_target_data = np.zeros((len(input_texts), max_decoder_seq_length, output_vocab_size),
                               dtype="float32")

for i, (input_text, target_text) in enumerate(zip(input_texts, target_texts)):
    for t, char in enumerate(input_text):
        encoder_input_data[i, t, input_token_index[char]] = 1.
    
    for t, char in enumerate(target_text):
        decoder_input_data[i, t, target_token_index[char]] = 1.
        if t > 0:
            decoder_target_data[i, t-1, target_token_index[char]] = 1
```

<h4>2. Build the Model</h4>
```
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense

batch_size  = 64
epochs      = 100
num_neurons = 256

encoder_inputs = Input(shape=(None, input_vocab_size))
encoder        = LSTM(num_neurons, return_state=True)
encoder_outputs, state_h, state_c = encoder(encoder_inputs)
encoder_states = [state_h, state_c]

decoder_inputs  = Input(shape=(None, output_vocab_size))
decoder_lstm    = LSTM(num_neurons, return_sequences=True, return_state=True)
decoder_outputs = decoder_lstm(decoder_inputs, initial_state=encoder_states)[0]
decoder_dense   = Dense(output_vocab_size, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["acc"])

model.fit([encoder_input_data, decoder_input_data],
          decoder_target_data,
          batch_size=batch_size,
          epochs=epochs,
          validation_split=.1)
```
```
encoder_model = Model(encoder_inputs, encoder_states)
thought_input = [Input(shape=(num_neurons,)),
                 Input(shape=(num_neurons,))]
decoder_outputs, state_h, state_c = decoder_lstm(decoder_inputs,
                                                 initial_state=thought_input)
decoder_states  = [state_h, state_c]
decoder_outputs = decoder_dense(decoder_outputs)
decoder_model   = Model(
    inputs=[decoder_inputs] + thought_input,
    outputs=[decoder_outputs] + decoder_states
)
```

<h4>3. Response </h4>
```
def decode_sequence(input_seq):
    thought = encoder_model.predict(input_seq)

    target_seq = np.zeros((1, 1, output_vocab_size))
    target_seq[0, 0, target_token_index[stop_token]] = 1.

    stop_condition = False
    generated_sequence = ''

    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + thought)

        generated_token_idx = np.argmax(output_tokens[0, -1, :])
        generated_char      = reverse_target_char_index[generated_token_idx]
        generated_sequence += generated_char
        if (generated_char == stop_token or len(generated_sequence) > max_decoder_seq_length):
            stop_condition = True
            target_seq = np.zeros((1, 1, output_vocab_size))
            target_seq[0, 0, generated_token_idx] = 1.
            thought = [h, c]
    
    return generated_sequence
```
```
def response(input_text):
    input_seq = np.zeros((1, max_encoder_seq_length, input_vocab_size), dtype="float32")
    for t, char in enumerate(input_text):
        input_seq[0, t, input_token_index[char]] = 1.
    decoded_sentence = decode_sequence(input_seq)
    print(f"Bot Reply: {decoded_sentence}")
    
respone("what is the internet?")
```
</p></details>

<details><summary><b>Approximate Nearest Neighbors (ANN) Search</b> Libraries</summary><p><ul>
<li>Spotify's Annoy <a href="https://github.com/spotify/annoy">github</a></li>
<li>BallTree (using nmslib) <a href="https://github.com/searchivarius/nmslib">github</a></li>
<li>Brute Force using Basic Linear Algebra Subprograms library (BLAS) <a href="http://scikit-learn.org/stable/modules/neighbors.html#brute-force">github</a></li>
<li>Brute Force using Non-Metric Space Library (NMSlib) <a href="https://github.com/searchivarius/NMSLIB"> github</a></li>
<li>Dimension reductiOn and LookuPs on a Hypercube for effIcient Near Neigh-bor (DolphinnPy) <a href="https://github.com/ipsarros/DolphinnPy"> github</a></li>
<li>Random Projection Tree Forest (rpforest)<a href="https://github.com/lyst/rpforest"> github</a></li>
<li>Locality sensitive hashing (datasketch)<a href="https://github.com/ekzhu/datasketch"> github</a></li>
<li>Multi-indexing hashing (MIH)<a href="https://github.com/norouzi/mih"> github</a></li>
<li>Fast Lookup of Cosine and Other Nearest Neighbors (FALCONN)<a href="https://pypi.python.org/pypi/FALCONN"> github</a></li>
<li>Fast Lookup of Approximate Nearest Neighbors (FLANN)<a href="http://www.cs.ubc.ca/research/flann/"> github</a></li>
<li>Hierarchical Navigable Small World (HNSW) (in nmslib)<a href="https://github.com/searchivarius/
nmslib/blob/master/similarity_search/include/factory/method/hnsw.h"> github</a></li>
<li>K-Dimensional Trees (kdtree)<a href="https://github.com/stefankoegl/kdtree"> github</a></li>
<li>nearpy <a href="https://pypi.python.org/pypi/NearPy">github</a></li>
</ul>

<details><summary>Using <b>Annoy</b> on word-vectors</summary><p>
NOTE: Read Page 409 in nlp in action book.
<h4>1. Load WordVectors using gensim (wv), Annoy</h4>
```
!pip install annoy
from annoy import AnnoyIndex

n_words, n_dimensions = wv.vectors.shape
index                   = AnnoyIndex(n_dimensions)
```

<h4>2. Add each word vector to the AnnoyIndex</h4>
```
from tqdm import tqdm
for i, word in enumerate(tqdm(wv.index2word)):
    index.add_item(i, wv[word])
```
<h4>Build Euclidean/Cosine distance index with 15 trees</h4>
```
# Euclidean
from tqdm import tqdm
for i, word in enumerate(tqdm(wv.index2word)):
    index.add_item(i, wv[word])
    
index.build(n_trees)
index.save('Word2vec_euc_index.ann')
w2id = dict(zip(range(len(wv.vocab)), wv.vocab))

# Cosine
index_cos = AnnoyIndex(f=n_dimensions, metric='angular')

for i, word in enumerate(wv.index2word):
    if not i % 100_000:   # Another way to keep track of your progress.
        print(f"{i}: {word}")
    index_cos.add_item(i, wv[word])

# Increase the number of trees to get more accurate results.
index_cos.build(30)
index_cos.save('word2vec_cos_index.ann')
```


<h4>Find Harry_Potter neighbors with AnnoyIndex</h4>
```
# Find Harry_Potter neighbors with AnnoyIndex.
print(wv.vocab['Harry_Potter'].index)
print(wv.vocab['Harry_Potter'].count)

w2id = dict(zip(
    wv.vocab, range(len(wv.vocab))
))

print(w2id['Harry_Potter'])

# Get similar items to "Harry_Potter".
ids = index.get_nns_by_item(w2id['Harry_Potter'], 11)
print(ids)

print([wv.vocab[i] for i in ids])
print([wv.index2word[i] for i in ids])
```
</p></details>
</p></details>
</div>