# Feature Engineering

<div style='width:1000px;margin:auto'>
<details><summary><b style='font-size:20px'>1. Text Length</b></summary><p>
```
from tqdm import tqdm
tqdm.pandas()

df['total_length'] = df['text'].progress_apply(len)
```
</p></details>

<details><summary><b style='font-size:20px'>2. Words Length</b></summary><p>
```
# Count the number of words.
from tqdm import tqdm
tqdm.pandas()

df['num_words'] = df.text.str.count('\S+')
```
</p></details>

<details><summary><b style='font-size:20px'>3. Capitals Length</b></summary><p>
```
# Count the number of capital characters.
from tqdm import tqdm
tqdm.pandas()

df['capitals'] = df['text'].progress_apply(lambda comment: sum(1 for c in comment if c.isupper()))
```
</p></details>

<details><summary><b style='font-size:20px'>4. Unique Words Length</b></summary><p>
```
# Count the number of unique words.
from tqdm import tqdm
tqdm.pandas()

df['num_unique_words'] = df['text'].progress_apply(lambda comment: len(set(w for w in comment.split())))
```
</p></details>

<details><summary><b style='font-size:20px'>5. Unique vs. Words</b></summary><p>
```
df['words_vs_unique'] = df['num_unique_words'] / df['num_words']
```
</p></details>

<details><summary><b style='font-size:20px'>6. Caps vs. Length</b></summary><p>
```
# Count the number of unique words.
from tqdm import tqdm
tqdm.pandas()

df['caps_vs_length'] = df.progress_apply(lambda row: float(row['capitals'])/float(row['total_length']), axis=1)
```
</p></details>

<details><summary><b>Flesch reading-ease score (FRES) test</b></summary>
Readability is the ease with which a reader can understand a written text. In natural language processing, the readability of text depends on its content. It focuses on the words we choose, and how we put them into sentences and paragraphs for the readers to comprehend. 9.1 The Flesch Reading Ease formula<br>

In the Flesch reading-ease test, higher scores indicate material that is easier to read; lower numbers mark passages that are more difficult to read. The formula for the Flesch reading-ease score (FRES) test is<br>
<img src="./imgs/readability.png"><br>
90-100 - Very Easy<br>
80-89 - Easy<br>
70-79 - Fairly Easy<br>
60-69 - Standard<br>
50-59 - Fairly Difficult<br>
30-49 - Difficult<br>
0-29 - Very Confusing<br>
<pre><code>#utility functions:
def plot_readability(a,b,c,title,bins=0.4,colors=colors):
    trace1 = ff.create_distplot([a,b,c],sent, bin_size=bins, colors=colors, show_rug=False)
    trace1['layout'].update(title=title)
    py.iplot(trace1, filename='Distplot')
    table_data= [["Statistical Measures","neu",'pos','neg'],
                ["Mean",mean(a),mean(b),mean(c)],
                ["Standard Deviation",pstdev(a),pstdev(b),pstdev(c)],
                ["Variance",pvariance(a),pvariance(b),pvariance(c)],
                ["Median",median(a),median(b),median(c)],
                ["Maximum value",max(a),max(b),max(c)],
                ["Minimum value",min(a),min(b),min(c)]]
    trace2 = ff.create_table(table_data)
    py.iplot(trace2, filename='Table')

</code></pre>
<pre><code>!pip install textstat
import textstat
from tqdm import tqdm

tqdm.pandas()
fre_neu = np.array(df["text"][df["sentiment"] == sent[0]].progress_apply(textstat.flesch_reading_ease))
fre_pos = np.array(df["text"][df["sentiment"] == sent[1]].progress_apply(textstat.flesch_reading_ease))
fre_neg = np.array(df["text"][df["sentiment"] == sent[2]].progress_apply(textstat.flesch_reading_ease))

plot_readability(fre_neu,fre_pos,fre_neg,"Flesch Reading Ease",20)

</code></pre>
</details>

<details><summary><b>Jaccard Score</b></summary>
<pre><code>def jaccard(str1, str2): 
    a = set(str(str1).lower().split()) 
    b = set(str(str2).lower().split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))
</code></pre>
</details>

<details><summary><b>Polarity</b></summary>
<pre><code>from textblob import TextBlob

def get_sent(text):
    testimonial = TextBlob(str(text))
    return testimonial.sentiment.polarity
</code></pre>
</details>


- Gender Feature [detect if sentence is male, female, or none].<br>
- Grammer Feature [detect if sentence is in past, present, or future].
</div>