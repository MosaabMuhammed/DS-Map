#  Data Cleaning

<div style='width:1000px;margin:auto'>
<details><summary><b style='font-size:20px'>1. Remove URL</b></summary><p>
<h4>1. Find text contains URL</h4>
```
df.loc[df['text'].str.contains('http')]
```
<h4>2. Remove text contains URL</h4>
```
# First code
import re

def remove_URL(text):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'',text)
    
# Second Code
pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

def remove_html(text):
    no_html= pattern.sub('',text)
    return no_html
```
</p></details>

<details><summary><b style='font-size:20px'>2. Remove HTML</b></summary><p>
~~~python
def remove_HTML(text):
    html = re.compile(r'<.*?>')
    return html.sub(r'', text)
~~~
</p></details>

<details><summary><b style='font-size:20px'>3. Remove emoji</b></summary><p>
~~~python
# Reference : https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)
~~~
</p></details>

<details><summary><b style='font-size:20px'>4. Remove Punctuations</b></summary><p>
~~~python
import string

def remove_punct(text):
    table = str.maketrans('', '', string.punctuation)
    return text.translate(table)
~~~
~~~
puncts = [',', '.', '"', ':', ')', '(', '-', '!', '?', '|', ';', "'", '$', '&', '/', '[', ']', '>', '%', '=', '#', '*', '+', '\\', '•',  '~', '@', '£', 
 '·', '_', '{', '}', '©', '^', '®', '`',  '<', '→', '°', '€', '™', '›',  '♥', '←', '×', '§', '″', '′', 'Â', '█', '½', 'à', '…', 
 '“', '★', '”', '–', '●', 'â', '►', '−', '¢', '²', '¬', '░', '¶', '↑', '±', '¿', '▾', '═', '¦', '║', '―', '¥', '▓', '—', '‹', '─', 
 '▒', '：', '¼', '⊕', '▼', '▪', '†', '■', '’', '▀', '¨', '▄', '♫', '☆', 'é', '¯', '♦', '¤', '▲', 'è', '¸', '¾', 'Ã', '⋅', '‘', '∞', 
 '∙', '）', '↓', '、', '│', '（', '»', '，', '♪', '╩', '╚', '³', '・', '╦', '╣', '╔', '╗', '▬', '❤', 'ï', 'Ø', '¹', '≤', '‡', '√', ]

def clean_text(x):
    x = str(x)
    for punct in puncts:
        if punct in x:
            x = x.replace(punct, f' {punct} ')
    return x
~~~
~~~
def clean_text(x):
    pattern = r'[^a-zA-z0-9\s]'
    text = re.sub(pattern, '', x)
    return x
~~~
</p></details>

<details><summary><b style='font-size:20px'>5. Spell Checker</b></summary><p>
~~~python
!pip install pyspellchecker

from spellchecker import SpellChecker

spell = SpellChecker()
def correct_spellings(text):
    corrected_text = []
    misspelled_words = spell.unknown(text.split())
    
    for word in text.split():
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)
~~~
</p></details>

<details><summary><b style='font-size:20px'>6. Find Hashtags</b></summary><p>
```
import re
from tqdm import tqdm
tqdm.pandas(tqdm())

# Extracting hastags using simple regex
train['hastags'] = train['text'].progress_apply(lambda x: re.findall('#\w*', x))
```

```
#Finding the hashtags in a tweet
def hashtag(tweet):
    with_hashtag = " ".join([word for word in tweet.split() if word.startswith('#')])
    with_hashtag = with_hashtag.lower().split()
    return with_hashtag
```
</p></details>

<details><summary><b style='font-size:20px'>7. Clean Numbers</b></summary><p>
~~~
## Why do we want to replace numbers with #s? Because most embeddings have preprocessed their text like this.
def clean_numbers(x):
    if bool(re.search(r'\d', x)):
        x = re.sub('[0-9]{5,}', '#####', x)
        x = re.sub('[0-9]{4}', '####', x)
        x = re.sub('[0-9]{3}', '###', x)
        x = re.sub('[0-9]{2}', '##', x)
    return x
~~~
</p></details>

<details><summary><b style='font-size:20px'>8. Remove Contractions</b></summary><p>
~~~
contraction_dict = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not", "didn't": "did not",  "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not", "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",  "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would", "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would", "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam", "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock", "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is", "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as", "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would", "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have", "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have", "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are", "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",  "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is", "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have", "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have", "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have","you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have", "you're": "you are", "you've": "you have"}

def _get_contractions(contraction_dict):
    contraction_re = re.compile('(%s)' % '|'.join(contraction_dict.keys()))
    return contraction_dict, contraction_re

contractions, contractions_re = _get_contractions(contraction_dict)

def replace_contractions(text):
    def replace(match):
        return contractions[match.group(0)]
    return contractions_re.sub(replace, text)

# Usage
replace_contractions("this's a text with contraction")
~~~
</p></details>

<details><summary><b style='font-size:20px'>9. Stemming</b></summary><p>
~~~
from nltk.stem import  SnowballStemmer
from nltk.tokenize.toktok import ToktokTokenizer
def stem_text(text):
    tokenizer = ToktokTokenizer()
    stemmer = SnowballStemmer('english')
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    tokens = [stemmer.stem(token.lower()) for token in tokens]
    return ' '.join(tokens)
~~~
</p></details>

<details><summary><b style='font-size:20px'>10. Lemmatization</b></summary><p>
~~~
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.toktok import ToktokTokenizer
nltk.download('wordnet')


def lemma_text(text):
    lemmatizer = WordNetLemmatizer()
    tokenizer  = ToktokTokenizer()
    tokens     = tokenizer.tokenize(text)
    tokens     = [token.strip() for token in tokens]
    tokens     = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return ' '.join(tokens)
~~~
</p></details>

<details><summary><b style='font-size:20px'>12. Remove Stopwords</b></summary><p>
```
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop = stopwords.words('english')

def remove_stopwords(text):
    return ' '.join([word.lower() for word in text.split() if word not in stop])
    
#### Usage 
tweet['text'] = tweet.text.progress_apply(remove_stopwords)
```
</p></details>
</div>