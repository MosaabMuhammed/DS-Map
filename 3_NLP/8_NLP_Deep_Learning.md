# Modeling

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

</div>