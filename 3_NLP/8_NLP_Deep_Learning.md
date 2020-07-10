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
</div>