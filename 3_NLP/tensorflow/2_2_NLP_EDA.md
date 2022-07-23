<h1 id="eda">EDA</h1>

<div style='width:1000px;margin:auto'>

<details><summary><b>n-gram Viewer with Time</b></summary>
<pre><code>fig, ax = plt.subplots(figsize=(9,6))

for term in terms:
    data[term].plot(ax=ax)

ax.set_title("Token Frequency over Time")
ax.set_ylabel("word count")
ax.set_xlabel("publication date")
ax.set_xlim(("2016-02-29","2016-05-25"))
ax.legend()
plt.show()

# NOTE: If you don't have time column, you can display it with index, but convert it to bag-of-words first.
</code></pre>
<p><img src="imgs/20200606-153159.png" alt="" /></p>
</details>

<details><summary><b>Network Visualization</b></summary>

Visualize the relationship between each pair of words.
<h4>1. Create the corpus</h4><pre><code>import itertools

corpus = []
for sentence in df['sample'].values:
    corpus.extend(sentence.split())

def cooccurrence(corpus):
    possible_pairs = list(itertools.combinations(corpus, 2))
    cooccurring    = dict.fromkeys(possible_pairs, 0)
    for idx, current_token in enumerate(corpus):
        if (idx+1 &lt; len(corpus)) and (tuple((current_token, corpus[idx+1])) in possible_pairs):
            cooccurring[(current_token, corpus[idx+1])] += 1
    return cooccurring

pairs = cooccurrence(corpus)
</code></pre>
<h4>2. Create the network</h4><pre><code>import networkx as nx

G = nx.Graph()
G.name = "The Social Network of tokens"

# pairs = cooccurrence(corpus)
for pair, wgt in pairs.items():
    if wgt &gt; 0:
        G.add_edge(pair[0], pair[1], weight=wgt)

# Make some the center!
# TODO: WRITE YOUR WORD OF INTEREST HERE!!
D = nx.ego_graph(G, "corona")
edges, weights = zip(*nx.get_edge_attributes(D, "weight").items())

# Push nodes away that are less related to that specific word.
pos = nx.spring_layout(D, k=.5, iterations=40)
nx.draw(D, pos, node_color="gold", node_size=50, edgelist=edges,
        width=.5, edge_color="orange", with_labels=True, font_size=12)
plt.show()
</code></pre>
</details>

<details><summary><b>Heatmap</b> b/w <b style="font-size:20px">Tokens</b></summary>

<h4>1. Create the Matrix</h4><pre><code>specific_tokens = ['kill', 'corona', 'viris', 'hi', 'symptoms', 'the', 'treatment']

corpus = []
for sentence in df['sample'].values:
    corpus.append(sentence.split())

def cooccurrence_mtx(corpus, specific_tokens=None, sort_alpha=False):
    if sort_alpha: specific_tokens = sorted(specific_tokens)
    possible_pairs = list(itertools.permutations(specific_tokens, 2))
    cooccurring    = dict.fromkeys(possible_pairs, 0)

    for idx, current_sample in enumerate(corpus):
        for pair in possible_pairs:
            if pair[0] in current_sample and pair[1] in current_sample:
                cooccurring[pair] += 1

    pairs = cooccurring.copy()
    mtx = pd.DataFrame(columns=["p1", "p2", "count"])
    for pair, weight in pairs.items():
        mtx = mtx.append({"p1":    pair[0],
                        "p2":    pair[1],
                        "count": float(weight)}, ignore_index=True)

    mtx = pd.pivot(mtx, index='p1', columns='p2', values='count')
    mtx.fillna(.0, inplace=True)
    return mtx

mtx = cooccurrence_mtx(corpus, specific_tokens, True)


mtx.sample(5)
</code></pre>

<h4>2. Show Heatmap</h4><pre><code>import matplotlib

fig, ax = plt.subplots()
fig.suptitle("Co-occurrence of Tokens", fontsize=12)
fig.subplots_adjust(wspace=.75)

n = len(specific_tokens)
x_tick_marks = np.arange(n)
y_tick_marks = np.arange(n)

ax1 = plt.subplot(121)
ax1.set_xticks(x_tick_marks)
ax1.set_yticks(y_tick_marks)
ax1.set_xticklabels(specific_tokens, fontsize=8, rotation=90)
ax1.set_yticklabels(specific_tokens, fontsize=8)
ax1.xaxis.tick_top()
ax1.set_xlabel("By Frequency")
sns.heatmap(mtx, cmap="viridis")

# And alphabetically
alpha_cast = sorted(specific_tokens)
alpha_mtx  = 
</code></pre>
</details>

<details><summary><b>POS Tagging Coloring</b></summary><pre><code># Import required libraries.
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize
from yellowbrick.text.postag import PosTagVisualizer
</code></pre>
<pre><code>pie = """
In a small saucepan, combine sugar and eggs
until well blended. Cook over low heat, stirring
constantly, until mixture reaches 160° and coats
the back of a metal spoon. Remove from the heat.
Stir in chocolate and vanilla until smooth. Cool
to lukewarm (90°), stirring occasionally. In a small
bowl, cream butter until light and fluffy. Add cooled
chocolate mixture; beat on high speed for 5 minutes
or until light and fluffy. In another large bowl,
beat cream until it begins to thicken. Add
confectioners' sugar; beat until stiff peaks form.
Fold into chocolate mixture. Pour into crust. Chill
for at least 6 hours before serving. Garnish with
whipped cream and chocolate curls if desired.
"""

tokens = word_tokenize(pie)
tagged = pos_tag(tokens)

visualizer = PosTagVisualizer()
visualizer.transform(tagged)

print(" ".join((visualizer.colorize(token, color)
                for color, token in visualizer.tagged)))
print("\n")
</code></pre>
</details>

<details><summary><b>Frequency Distribution</b></summary><pre><code>from yellowbrick.text.freqdist import FreqDistVisualizer
from sklearn.feature_extraction.text import CountVectorizer

# "stop_words" parameter removes stopwords.
# Remove the parameter, if you prefer another thing.
vectorizer = CountVectorizer(stop_words="english")
docs       = vectorizer.fit_transform(df["sample"].values)
features   = vectorizer.get_feature_names()

plt.figure(figsize=(15, 8))
visualizer = FreqDistVisualizer(features=features)
visualizer.fit(docs)
visualizer.poof()
</code></pre>
</details>

<details><summary><b>t-SNE Visualizer</b></summary>
<p><b>yellowbrick</b> applies a decomosition first (SVD with 50 components by defaults), then performs the t-SNE embedding</p><pre><code>from yellowbrick.text import TSNEVisualizer
from sklearn.feature_extraction.text import TfidfVectorizer

# We could use any vectorization technique and not specifically TF-IDF.
tfidf = TfidfVectorizer()
docs  = tfidf.fit_transform(df["sample"].values)

# We could try PCA instead of SVD, by passing "decompose="pca"" into TSNEVisualizer().
tsne = TSNEVisualizer()
tsne.fit(docs, y=df["intent"].values)
tsne.poof()
</code></pre>
<pre><code># Apply clustering instead of class names.
from sklearn.cluster import KMeans
clusters = KMeans(n_clusters=5)
clusters.fit(docs)

tsne = TSNEVisualizer()
tsne.fit(docs, ["c{}".format(c) for c in clusters.labels_])
tsne.poof()
</code></pre>
</details>

<details><summary><b>Classification Report - Visualizer</b></summary>
<pre><code>from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from yellowbrick.classifier import ClassificationReport
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

docs   = TfidfVectorizer().fit_transform(df["sample"].values)
labels = LabelEncoder().fit_transform(df["intent"].values)


X_train, X_test, y_train, y_test = train_test_split(
    docs.toarray(), labels, test_size=.2
)

plt.figure(figsize=(15, 8))
visualizer = ClassificationReport(GaussianNB(), classes=df["intent"].unique())
visualizer.fit(X_train, y_train)
visualizer.score(docs.toarray(), labels)
visualizer.poof()
</code></pre>
</details>

<details><summary><b>Confusion Matrix - Visualizer</b></summary><pre><code>from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from yellowbrick.classifier import ConfusionMatrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

samples = TfidfVectorizer().fit_transform(df["sample"].values)
# intents = LabelEncoder().fit_transform(df["intent"].values)

X_train, X_test, y_train, y_test = train_test_split(
    samples.toarray(), df["intent"].values, test_size=.2
)

visualizer = ConfusionMatrix(GaussianNB(), classes=df["intent"].unique())
visualizer.fit(X_train, y_train)
visualizer.score(X_test, y_test)
visualizer.poof()
</code></pre>
</details>

<details><summary><b>Get Frequency of Top n-grams</b></summary>
<pre><code>def get_top_ngram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(n, n),stop_words=stop).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:20]
    
    
fig,ax=plt.subplots(1,2,figsize=(15,10))
for i in range(2):
    new=df[df['sentiment']==sent[i+1]]['selected_text']
    top_n_bigrams=get_top_ngram(new,2)[:20]
    x,y=map(list,zip(*top_n_bigrams))
    sns.barplot(x=y,y=x,ax=ax[i],color=colors[i+1])
    ax[i].set_title(sent[i+1])
    
fig.suptitle("Common bigrams in selected text")
</code></pre>
</details>

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

def plot_jaccard(sentiment,ax):
    jacc=[]
    text=train[train['sentiment']==sentiment].dropna()['text'].values.tolist()
    selected=train[train['sentiment']==sentiment].dropna()['selected_text'].values.tolist()
    for i,k in zip(text,selected):
        jacc.append(jaccard(i,k))
    ax.hist(jacc,bins=10,color='blue',alpha=0.4)
    ax.set_title(sentiment)

fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(15,5))
plot_jaccard('positive',ax=ax1)
plot_jaccard('negative',ax2)
plot_jaccard('neutral',ax3)
fig.suptitle('jaccard similarity of text and selected text')
</code></pre>
</details>

<details><summary><b>Polarity</b></summary>
<pre><code>from textblob import TextBlob

def get_sent(text):
    testimonial = TextBlob(str(text))
    return testimonial.sentiment.polarity
    
plt.figure(figsize=(10,7))
train['polarity']=train['selected_text'].apply(lambda x : get_sent(x))
sns.boxplot(x='sentiment', y='polarity', data=train)
plt.gca().set_title('Sentiment vs Polarity of selected text')
plt.show()
</code></pre>
</details>

