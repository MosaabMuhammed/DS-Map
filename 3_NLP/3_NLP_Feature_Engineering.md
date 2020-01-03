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
</div>