<h1 id="huggingface">HuggingFace</h1>

<div style='width:1000px;margin:auto'>

<details><summary> <b style="font-size:20px">Transformers</b></summary><ul>

<details><summary>How to use <b>transformers</b> library</summary>
<a href="./0_notebooks/02_transformers.html">notebook</a>
</details>

<details><summary>Using <b>BERT</b>/<b>DistilBERT</b> as Embeddings [Arabic/English]</summary>
Use BERT for embedding and sklearn model after it.
<a href="./0_notebooks/A_Visual_Notebook_to_Using_BERT_for_the_First_Time.html"><b >notebook</b></a><br>
<a href="./0_notebooks/3.03. Generating BERT embedding .html"><b >Another Detailed Notebook</b></a>
<br>
<a href="./0_notebooks/3.04. Extracting embeddings from all encoder layers of BERT.html"><b >Extract Embedding from any encoder in Bert</b></a>
</details>

</ul></details>

<details><summary> <b style="font-size:20px">Tokenizers</b></summary><ul>
 <b>BERT</b>/<b>DistilBERT</b>/<b>Electra</b> uses <i>WordPiece</i>.<br>
 <b>XLNet</b> uses <i>SentencePiece</i>.<br>
 <b>GPT-2</b>/<b>Roberta</b> uses <i>Byte-level BPE</i>.<br><br>
<li><details><summary><b>WordPiece</b></summary><pre><code>from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
tokenizer.tokenize("I have a new GPU!")
# ['i', 'have', 'a', 'new', 'gp', '##u', '!']
</code></pre>
</details></li>
<li><details><summary><b>SentencePiece</b></summary><pre><code>import transformers as ppb
tokenizer = ppb.XLNetTokenizer.from_pretrained('xlnet-base-cased')
tokenizer.tokenize("Don't you love transformers? We pretty sure you do.")
# ['▁Don',
# "'",
# 't',
# '▁you',
# '▁love',
# '▁transform',
# 'ers',
# '?',
# '▁We',
# '▁pretty',
# '▁sure',
# '▁you',
# '▁do',
# '.']
</code></pre>
</details></li>
<li><details><summary><b>Byte-level BPE</b></summary><pre><code>import transformers as ppb
tokenizer = ppb.GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.tokenize("This is a simple to be tokenized.")
# ['This', 'Ġis', 'Ġa', 'Ġsimple', 'Ġto', 'Ġbe', 'Ġtoken', 'ized', '.']
</code></pre>
</details></li>

<li><details><summary>Any <b>other unlist model</b></summary><pre><code>import transformers as ppb

tokenizer = ppb.AutoTokenizer.from_pretrained("asafaya/bert-mini-arabic")
tokenizer.tokenize("كيف حالك اليوم؟ و حال أولادك يا عمر")
# ['كيف', 'حال', '##ك', 'اليوم', '؟', 'و', 'حال', 'اولاد', '##ك', 'يا', 'عمر']
</code></pre>
</details></li>

<li><details><summary>Build <b>Custom Tokenizer</b></summary>
<a href="https://huggingface.co/docs/tokenizers/python/latest/quicktour.html">Quicktour [huggingface's docs]</a><br>
<a href="https://huggingface.co/docs/tokenizers/python/latest/pipeline.html"><b>Normalization</b>, <b>Pre-Tokenization</b>, The <b>Model</b>, and <b>Post-Processing</b></a><br>
<a href="./0_notebooks/01_training_tokenizers.html">Custom Tokenizer</a>

</details></li>
</ul></details>

<details><summary> <b style="font-size:20px">Pipeline</b></summary><ul>

<details><summary>How to use <b>pipelines</b> [ner, sent_ana, text_extraction, ...]</summary>
<a href="./0_notebooks/03_pipelines.html">notebook</a>
</details>


</ul></details>

</div>