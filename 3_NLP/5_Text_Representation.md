# Text Representation

<div style='width:1000px;margin:auto'>
<details><summary><b style='font-size:20px'>1. Bag of Words</b></summary><p>
~~~
cnt_vectorizer = CountVectorizer(dtype=np.float32,
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),min_df=3)


# we fit count vectorizer to get ngrams from both train and test data.
cnt_vectorizer.fit(list(train_df.cleaned_text.values) + list(test_df.cleaned_text.values))

xtrain_cntv =  cnt_vectorizer.transform(train_df.cleaned_text.values) 
xtest_cntv = cnt_vectorizer.transform(test_df.cleaned_text.values)
~~~
</p></details>

<details><summary><b style='font-size:20px'>2. TF-IDF</b></summary><p>
<p><b>NOTE:</b> You can build TF-IDF followed by search engine instead of ML models, and calculate cosine similarity between the quest and your documents using inverted index O(1) using Whoosh python library.</p>
~~~
# Always start with these features. They work (almost) everytime!
tfv = TfidfVectorizer(dtype=np.float32, min_df=3,  max_features=None, 
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3), use_idf=1,smooth_idf=1,sublinear_tf=1,
            stop_words = 'english')

# Fitting TF-IDF to both training and test sets (semi-supervised learning)
tfv.fit(list(train_df.cleaned_text.values) + list(test_df.cleaned_text.values))
xtrain_tfv =  tfv.transform(train_df.cleaned_text.values) 
xvalid_tfv = tfv.transform(test_df.cleaned_text.values)
~~~
</p></details>

<details><summary><b style='font-size:20px'>3. Hashing Features</b></summary><p>
~~~
# Always start with these features. They work (almost) everytime!
hv = HashingVectorizer(dtype=np.float32,
            strip_accents='unicode', analyzer='word',
            ngram_range=(1, 4),n_features=2**12,non_negative=True)
# Fitting Hash Vectorizer to both training and test sets (semi-supervised learning)
hv.fit(list(train_df.cleaned_text.values) + list(test_df.cleaned_text.values))
xtrain_hv =  hv.transform(train_df.cleaned_text.values) 
xvalid_hv = hv.transform(test_df.cleaned_text.values)
y_train = train_df.target.values
~~~
</p></details>

<details><summary><b style='font-size:20px'>4. Other Schemes</b></summary><p>
<p><img src="imgs/20200621-174111.png" alt="" /></p>
</p></details>
</div>