# Word Embedding

<div style='width:1000px;margin:auto'>
<details><summary><b style='font-size:20px'>GloVe</b></summary><p>

<details><summary><b style='font-size:20px'>Read Glove</b></summary><p>
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
</p></details>

<details><summary><b style='font-size:20px'>Deep Learning for GloVe</b></summary><p>

```
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

MAX_LEN = 50
max_words = 10_000 # considers only the top10,000 words in the dataset.
tokensizer = Tokenizer(num_words=max_words)
tokensizer.fit_on_texts(corpus)
sequences  = tokensizer.texts_to_sequences(corpus)

tweet_pad = pad_sequences(sequences, maxlen=MAX_LEN, truncating='post', padding='post')

# Print number of words
word_index = tokensizer.word_index
print(f'~> Number of Unique words: {bg(len(word_index))}')
```

<h4>3. Create Embedding Matrix</h4>
```
# num_words should equal max_words if you define it first, if not, go with the following line.
num_words = len(word_index)+1
embedding_matrix = np.zeros((num_words, 100))

for word, i in tqdm(word_index.items()):
    if i < num_words:
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

<details><summary><b style='font-size:20px'>ML Models for GloVe</b></summary><p>

<h4>5. Make GloVe suitable for ML Models</h4>
```
# Convert each text in a row to a vector.
def sent2vec(s):
    words = str(s).lower()
    words = word_tokenize(words)
    words = [w for w in words if not w in stop and w.isalpha()]
    
    M = []
    for w in words:
        try:
            M.append(embedding_dict[w])
        except:
            continue
            
    M = np.array(M)
    v = M.sum(axis=0)
    if type(v) != np.ndarray: return np.zeros(100)
    return v / np.sqrt((v**2).sum())

# Apply the function
df['text'] = [sent2vec(x) for x in tqdm(df['text'], position=0)]
```
```
# Train Test Split the data
X_train, X_valid, y_train, y_valid = train_test_split(df[df.target.notnull()]['text'],
                                                      df[df.target.notnull()]['target'],
                                                      test_size=.2,
                                                      random_state=33)
```
```
# Convert the data into arrays
X_train, X_valid = X_train.apply(pd.Series), X_valid.apply(pd.Series)
```
</p></details>
</p></details>

<details><summary><b style='font-size:20px'>Universal Sentence Encoding</b></summary><p>
<h4>1. Load the embeddings</h4>
```
# Import the hubber
import tensorflow_hub as hub

# Load the embbedding
embed = hub.load('../../../Personal/Development/Courses Docs/Word Embeddings/Universal Sentence Encoder')
X_train_embedding = embed(train.text.values)
X_test_embedding  = embed(test.text.values)
```

<h4>2. Concatenate with other features</h4>
```
# Merge with TF-IDF
train_df    = np.concatenate([X_train_embedding['outputs'], tf_train], axis=1)
test_df     = np.concatenate([X_test_embedding['outputs'], tf_test], axis=1)
```
</p></details>

<details><summary><b style='font-size:20px'>Gensim [Word2Vec]</b></summary><p>
<h4>1. Load Word2Vec into Gensim</h4>
```
# NOTE: you can limit = 200_000, if you have limited memory.
# GoogleNews: https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit
from gensim.models import KeyedVectors

word_vectors = KeyedVectors.load_word2vec_format("https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz", binary=True, limit=200_000)
```

<h4>2. Most similar words "Synonems"</h4>
```
word_vectors.most_similar(positive=['cooking', 'potatoes'], topn=5)

#Result.
[('cook', 0.6973530650138855),
('oven_roasting', 0.6754530668258667),
('Slow_cooker', 0.6742032170295715),
('sweet_potatoes', 0.6600279808044434),
('stir_fry_vegetables', 0.6548759341239929)]
```

<h4>3. Adding & Subtracting words.</h4>
```
word_vectors.most_similar(positive=['king', 'women'], negative=['man'], topn=2)

#RESULT
[('queen', 0.7118192315101624), ('monarch', 0.6189674139022827)]
```

<h4>4. Detect unrelated terms</h4>
```
word_vectors.doesnt_match("potatoes milk cake computer".split())

#RESULT
'computer'
```

<h4>5. Cosine similarity b/w words.</h4>
```
word_vectors.similarity('princess', 'queen')

#RESULT
0.70705315983704509
```

<h4>6. Numerical Dimension of the word.</h4>
```
word_vectors['phone']

#RESULT
array([-0.01446533, -0.12792969, -0.11572266, -0.22167969, -0.07373047,
-0.05981445, -0.10009766, -0.06884766, 0.14941406, 0.10107422,
-0.03076172, -0.03271484, -0.03125
 , -0.10791016, 0.12158203,
0.16015625, 0.19335938, 0.0065918 , -0.15429688, 0.03710938,
...
```
</p></details>

<details><summary><b style='font-size:20px'>Build Custom Word2Vec</b></summary><p>
First you need to break your documents into sentences and the sentences into tokens. End up like this:
```
>>> token_list
[
['to', 'provide', 'early', 'intervention/early', 'childhood', 'special',
'education', 'services', 'to', 'eligible', 'children', 'and', 'their',
'families'],
['essential', 'job', 'functions'],
['participate', 'as', 'a', 'transdisciplinary', 'team', 'member', 'to',
'complete', 'educational', 'assessments', 'for']
...
]
```

<h4>Load the Model</h4>
```
from gensim.models.word2vec import Word2Vec

# Setup the parameters.
num_features = 300  # Number of vector elements to represent the word.
min_word_count = 3  # Min number of word count to be considered in the Word2vec model.
num_workers = 2   # Number of CPU cores used for the training.
window_size = 6  # Context window size.
subsampling = 1e-3		# Subsampling rate for frequent terms.
```

<h4>Build the Model</h4>
```
model = Word2Vec(
			token_list,
			workers=num_workers,
			size=num_features,
			min_count=min_word_count,
			window=window_size,
			sample=subsampling)

```

Word2vec models can consume quite a bit of memory. But remember that only the
weight matrix for the hidden layer is of interest. Once you’ve trained your word
model, you can reduce the memory footprint by about half if you freeze your model
and discard the unnecessary information. The following command will discard the
unneeded output weights of your neural network:
```
model.init_sims(replace=True)
```

<h4>Save the model</h4>
```
model_name = "my_domain_specific_word2vec_model"
model.save(model_name)
```

<h4>Use the newly trained model</h4>
```
from gensim.models.word2vec import Word2Vec
model_name = "my_domain_specific_word2vec_model"
model = Word2Vec.load(model_name)
model.most_similar('radiology')
```
</p></details>

<details><summary><b style='font-size:20px'>Build Custom Embedding Layer</b></summary><p>
<h4>Instantiating an Embedding layer</h4>
```
from tensorflow.keras.layers import Embedding

# The Embedding layer takes at least 2 arguments.
# the number of possible tokens (here, 1,000: 1+maximum word index)
# and the dimensionality of the embeddings (here, 64).
embedding_layer = Embedding(1000, 64)
```
<p>This Embedding layer takes as input a 2D tensor of integers, of shape (samples, sequence_length), and returns a 3D floating-point tensor of shape (samples, sequence_length, embedding_dimensionality), the this 3D can be processed by an RNN or 1D convolution layer.</p>

<h4>Loading Dataset</h4>
```
from tensorflow.keras.datasets import imdb
from tensorflow.keras import preprocessing

max_features = 10_000  # Number of words to consider as features
maxlen = 20  # cutds off the text after this number of words (among the max_features most common words).

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=max_features)

# Turn the lists of integers into a 2D integer tensor of shape (samples, maxlen).
X_train = preprocessing.sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = preprocessing.sequence.pad_sequences(X_test, maxlen=maxlen)
```

<h4>Using an Embedding layer and classifier on the dataset</h4>
```
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

# Specifies the maximum input lenght to the Embedding layer so you can later flatten the embedding inputs. After the Embedding layer the activations have shape (samples, maxlen, 8).
model = Sequential()
model.add(Embedding(10_000, 8, input_length=maxlen)
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer="rmsprop", loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

history = model.fit(X_train, y_train,
			      epochs=10,
			      batch_size=32,
			      validation_split=.2)
```
Then you can save the model, after traning!
</p></details>

<details><summary><b style='font-size:20px'>fastText</b></summary><p>
Head over to the fastText model repository and download the bin+text model for your language of choice.
After the download finishes, unzip the binary language file.27 With the following code, you can then load it into gensim:
```
# If using gensim version before 3.2.0, use the following code: gensim.models.wrappers.fasttext import FastText
from gensim.models.fasttext import FastText
ft_model = FastText.load_fasttext_format(\
		model_file=MODEL_PATH)
ft_model.most_similar('soccer')
```
</p></details>

<details><summary><b style='font-size:20px'>Similarity Measures</b></summary><p>
```
# Calculate "Eclidean distance"
np.linalg.norm(wv["Illinois"] - wv["Illini"])

# Calculate Cosine Similatiry == Normalized dot product.
cos_similarity = np.dot(wv["Illinois"], wv["Illini"]) / (
    np.linalg.norm(wv["Illinois"]) *\
    np.linalg.norm(wv["Illini"]))
print(cos_similarity)

# Calculate Cosine Distance.
# 0 = Similar
# 
print(1 - cos_similarity)
```
</p></details>

<details><summary><b style='font-size:20px'>Embeddings for Sentence</b></summary><p>
```
def sentence_to_vec(sent, embedding_dict):
	# initialize emtpy list to store embeddings.
	M = []
	for w in words:
		# for every word, fetch the embedding from
		# the dictionary, and append to list of embeddings.
		if w in embedding_dict:
			M.append(embedding_dict[w])
			
	# if we don't have any vectors, returns zeros.
	if len(M) == 0:
		return np.zeros(300)
		
	# Convert list of embeddings to array.
	M = np.array(M)
	
	# Calculate sum over axis=0
	v = M.sum(axis=0)
	
	# Return normalized vector
	return v / np.sqrt((v ** 2).sum())
```
</p></details>
</div>