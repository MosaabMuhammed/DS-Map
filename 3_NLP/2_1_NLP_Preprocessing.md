#  Corpus Preprocessing & Wrangling

<div style='width:1000px;margin:auto'>

<details><summary><b style="font-size:20px">Segmentation</b></summary>
```
# Note: Check PunktSentenceTokenizer for European languages by NLTK.
from nltk import sent_tokenize

sents = []
for sentence in sent_tokenize(paragraph):
	sents.append(sentence)
```
</details>

<details><summary><b style="font-size:20px">Tokenization</b></summary>
```
#  do we want to remove punctuation from tokens, and if so, should we make punctuation marks tokens themselves? Should we preserve hyphenated words as compound elements or break them apart? Should we approach contractions as one token or two, and if they are two tokens, where should they be split?

from nltk import wordpunct_tokenize

tokens = []
for token in wordpunct_tokenize(sentence):
	tokens.append(token)
```
</details>

<details><summary><b style="font-size:20px">Part-of-Speech Tagging</b></summary>
```
from nltk import pos_tag

tags = []
for paragraph in paragraphs:
	for sentence in sent_tokenize(paragraph):
		tags.append(pos_tag(wordpunct_tokenize(sentence)))
```
</details>

<details><summary><b style="font-size:20px">Stats. of Corpus</b></summary>
```
# Helps to monitor the changes into your corpus
import nltk, time

def describe():
	started = time.time()

	# Structures to perform counting.
	counts = nltk.FreqDist()
	tokens = nltk.FreqDist()

	# Perform single pass over paragraphs, tokenize and count.
	for para in paragraphs:
		counts["para"] += 1
	
		for sent in para:
			counts["sents"] += 1
		
			for word, tag in sent:
				counts["words"] +=1 
				tokens[word]      += 1
			
	# Count the number of files and categories in the corpus.
	n_fileids = ...
	n_topics = ...

	# Return data structure with information
	return {
		'files': n_fileids,
		'topics': n_topics,
		'paras': counts["para"],
		'sents': counts["sents"],
		'words': counts["words"],
		'vocab': len(tokens),
		'lexdiv': float(counts["words"]) / float(len(tokens)),
		'ppdoc': float(counts["paras"]) / float(n_fileids),
		'sppar': float(counts["sents"]) / float(counts["paras"]),
		'secs': time.time() - started
	}
```
</details>

</div>