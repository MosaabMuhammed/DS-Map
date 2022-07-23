<h1 id="huggingface">HuggingFace</h1>

<div style='width:1000px;margin:auto'>

<details><summary> <b style="font-size:20px">Transformers</b></summary><ul>

<details><summary><b>Topic Modeling</b> </summary>

<a href="./0_notebooks/CH07d_Text_clustering_with_Sentence-BERT.html#Text-Clustering-with-Sentence-BERT">Text Clustering with Sentence-BERT</a><br>

<a href="./0_notebooks/CH07d_Text_clustering_with_Sentence-BERT.html#Topic-Modeling-with-BERT">Topic Modeling with BERT</a><br><br>
</details>

<details><summary><b>Embeddings</b> </summary>

<details><summary>Using <b>BERT</b>/<b>DistilBERT</b> as Embeddings [Arabic/English]</summary>
Use BERT for embedding and sklearn model after it.<br>
<a href="./0_notebooks/A_Visual_Notebook_to_Using_BERT_for_the_First_Time.html"><b >notebook</b></a><br>
<a href="./0_notebooks/3.03. Generating BERT embedding .html"><b >Another Detailed Notebook</b></a>
<br>
<a href="./0_notebooks/3.04. Extracting embeddings from all encoder layers of BERT.html"><b >Extract Embedding from any encoder in Bert</b></a><br><br>
</details>

<a href="./0_notebooks/4.03. Extracting embeddings with ALBERT.html">Extract Embeddings from <b>Albert</b></a><br>
<a href="./0_notebooks/4.05. Exploring the RoBERTa tokenizer .html">Extract Embeddings from <b>RoBERTa</b></a><br>

<a href="./0_notebooks/8.03. Exploring sentence-transformers library .html"><b >Get Embedding of Sentence with <b>SentenceBERT</b></b></a><br>

<a href="./0_notebooks/Semantic_Similarity_with_Flair.html">Semantic Similarity Experiment with <b>Flair</b></a><br>

<a href="./0_notebooks/CH07a_Benchmarking_sentence_similarity_models.html">Benchmarking sentence similarity models</a><br><br>

<a href="./0_notebooks/8.05. Computing sentence similarity .html">Cosine Similarity for <b>SentenceBERT</b></a><br>
<br></details>

<details><summary>Machine Translation with <b>Simple Transformers</b></summary>
<a href="./0_notebooks/CH04c_machine_translation_fine_tuning_using_simpletransformers.html">notebook</a>
</details>

<details><summary><b>Question-Answering</b> </summary>
<a href="./0_notebooks/CH06b_Thinking_of_the_question_answering_problem_as_a_start_stop_token_classification.html">notebook</a><br>
<a href="./0_notebooks/3.09. Q&A with finetuned BERT .html">BERT for Question-Answering</a><br>
</details>


<details><summary><b>NER/POS/Token Classification</b> with BERT</summary>
<a href="./0_notebooks/CH06a_Fine_tuning_language_models_for_NER.html">notebook</a>
</details>

<details><summary>Visualize the weights of any layer of any transformer [<b>BertVis</b>]
</summary>
<a href="./0_notebooks/head_view_bert.html">notebook</a>
</details>

<details><summary>How to use <b>transformers</b> library</summary>
<a href="./0_notebooks/02_transformers.html">notebook</a>
</details>

<details><summary>Pretraining <b>RoBERTa</b>  from Scratch</summary>
<a href="./0_notebooks/KantaiBERT.html">notebook</a>
</details>

<details><summary><b>Fine-tune</b> BERT for Text Classification</summary>
<a href="./0_notebooks/3.06. Text classification.html"><b >notebook 1</b></a><br>
<a href="./0_notebooks/BERT_Fine_Tuning_Sentence_Classification_DR.html"><b >notebook 2</b></a><br>
<a href="./0_notebooks/CH05a_BERT_fine-tuning.html"><b >Trainer</b></a><br>
<a href="./0_notebooks/CH05b_Training_with_Naitve_PyTorch.html"><b >Fine-Tune with Native PyTorch</b></a><br>
<a href="./0_notebooks/CH05c_Multi-class_Classification.html"><b >FineTuning BERT for Multi-Class Classification with custom datasets
</b></a>
</details>

<details><summary><b>Zero-Shot Learning</b></summary>
<a href="./0_notebooks/CH07b_Using_BART_for_zero_shot_learning.html">BART with/without pipeline</a>
</details>

<details><summary><b>Cross-Lingual Models</b></summary>

<a href="./0_notebooks/7.01. Understanding multilingual BERT .html"><b>How to use mBERT</b></a><br>

<a href="./0_notebooks/CH09a_XLM_and_multilingual_BERT.html"><b>XLM and multilingual BERT</b></a><br>

<a href="./0_notebooks/CH09b_Cross_lingual_text_similarity.html"><b>Cross lingual text similarity</b></a><br>

<a href="./0_notebooks/CH09c_Visualizing_cross-lingual_textual_similarity.html"><b>Visualizing cross-lingual textual Similarity</b></a><br>

<a href="./0_notebooks/CH09d_Cross_lingual_classification.html"><b>Cross lingual classification</b></a><br>

<a href="./0_notebooks/CH09e_Cross_lingual_zero_shot_learning.html"><b>Cross lingual zero shot learning.html</b></a><br>

<a href="./0_notebooks/CH09f_Fine-tuning_performance_of_multilingual_models.html"><b>Fine-tuning performance of multilingual models</b></a><br>

<br></details>



<details><summary>Sentence Pair Regression</summary>
<a href="./0_notebooks/CH05d_Sentence_Pair_Regression.html"><b >notebook</b></a><br><br></details>

<details><summary>Text Summarization with BART</summary>
<a href="./0_notebooks/9.05. Performing text summarization with BART .html"><b >notebook</b></a><br><br></details>

<a href="./0_notebooks/transformer_on_text_classification.html"><b>Different Arch. for text classification problem</b></a>
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
<a href="./0_notebooks/01_training_tokenizers.html">Custom Tokenizer</a><br>
<a href="./0_notebooks/CH03a_BERT_As_one_of_Autoencoding_Language_Models.html"> Auto-Encoding  Language Model</a><br>
<a href="./0_notebooks/CH04b_Autoregressive_language_model_training.html"> Auto-Regressive Language Model</a>

</details></li>
</ul></details>

<details><summary> <b style="font-size:20px">Pipeline</b></summary><ul>

<details><summary>How to use <b>pipelines</b> [ner, sent_ana, text_extraction, ...]</summary>
<a href="./0_notebooks/03_pipelines.html">notebook</a>
</details>
</ul></details>

<details><summary> <b style="font-size:20px">Dataset</b></summary><ul>

<a href="./0_notebooks/CH02b_Working_with_Datasets_Libary.html">notebook</a>
</ul></details>

<details><summary> <b style="font-size:20px">Bencmarking</b></summary><ul>

<a href="./0_notebooks/CH02c_Speed_and_Memory_Benchmarking.html">notebook</a>
</ul></details>


<details><summary> <b style="font-size:20px">Fixes for production</b></summary><ul>

<details><summary><b>Reduce Model Size </b>[Distillation, Quantization, Pruning] </summary>

<a href="./0_notebooks/CH08a_Pruning_Quantization.html">Pruning, Quantization</a><br>

</details>
<details><summary><b> Efficient Self-Attention</b></summary>

<a href="./0_notebooks/CH08b_Working_with_Efficient_Self-attention.html">Efficient Self-Attention</a><br><br>
</details>

</ul></details>

<details><summary> <b style="font-size:20px">Serving</b></summary><ul>

<details><summary><b>Docker</b></summary>
<pre><code type="docker">FROM python:3.7

RUN pip install torch

RUN pip install fastapi uvicorn transformers

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005"]
</code></pre>
<pre><code>docker build -t qaapi .
docker run -p 8000:8000 qaapi
</code></pre>
</details>

<details><summary><b>TFX</b></summary>
TFX provides a faster and more efficient way to serve deep learning-based models. But it
has some important key points you must understand before you use it. The model must
be a saved model type from TensorFlow so that it can be used by TFX Docker or the CLI.
<pre><code type="python"># You can perform TFX model serving by using a saved model format from
# TensorFlow. For more information about TensorFlow saved models, you can read
# the official documentation at https://www.tensorflow.org/guide/
# saved_model . To make a saved model from Transformers, you can simply use the
# following code:
from transformers import TFBertForSequenceClassification

model = TFBertForSequenceClassification.from_pretrained("nateraw/bert-base-uncased-imdb", from_pt=True)

model.save_pretrained("tfx_model", saved_model=True)
</code></pre>
<pre><code type="python"># Before we understand how to use it to serve Transformers, it is required to pull the
# Docker image for TFX:

$ docker pull tensorflow/serving
</code></pre>
<pre><code type="python"># This will pull the Docker container of the TFX being served. The next step is to run the Docker container and copy the saved model into it:
$ docker run -d --name serving_base tensorflow/serving

# You can copy the saved file into the Docker container using the following code:
$ docker cp tfx_model/saved_model tfx:/models/bert
</code></pre>
<pre><code type="python"># This will copy the saved model files into the container. However, you must commit the changes:
$ docker commit --change "ENV MODEL_NAME bert" tfx my_bert_model

# Now that everything is ready, you can kill the Docker container: following code:
$ docker kill tfx

# This will stop the container from running.
# Now that the model is ready and can be served by the TFX Docker, you can simply
# use it with another service. The reason we need another service to call TFX is that
# the Transformer-based models have a special input format provided by tokenizers.
</code></pre>
<pre><code type="python"># To do so, you must make a fastAPI service that will model the API that was served
# by the TensorFlow serving container. Before you code your service, you should start
# the Docker container by giving it parameters to run the BERT-based model. This
# will help you fix bugs in case there are any errors:
$ docker run -p 8501:8501 -p 8500:8500 --name bert my_bert_model
</code></pre>
<h3>The following content will be in main.py</h3>
<pre><code>import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import BertTokenizerFast, BertConfig
import requests
import json
import numpy as np

tokenizer = BertTokenizerFast.from_pretrained("nateraw/bert-base-uncased-imdb")
config = BertConfig.from_pretrained("nateraw/bert-base-uncased-imdb")


class DataModel(BaseModel):
    text: str

app = FastAPI()

@app.post("/sentiment")
async def sentiment_analysis(input_data: DataModel):
    print(input_data.text)
    tokenized_sentence = [dict(tokenizer(input_data.text))]
    data_send = {"instances": tokenized_sentence}
    response = requests.post("http://localhost:8501/v1/models/bert:predict", data=json.dumps(data_send))
    result = np.abs(json.loads(response.text)["predictions"][0])
    return {"sentiment": config.id2label[np.argmax(result)]}


if __name__ == '__main__': 
     uvicorn.run('main:app', workers=1) 
</code></pre>
We have loaded the config file because the labels are stored in it, and we need
them to return it in the result. You can simply run this file using python :
<pre><code>$ python main.py</code></pre>
</details>

<details><summary><b>Locust</b></summary>
<pre><code>$ pip install locust</code></pre>
<pre><code># Create a file called "locust_file.py"

from locust import HttpUser, task
from random import choice
from string import ascii_uppercase

class User(HttpUser):
    @task
    def predict(self):
        payload = {"text": ''.join(choice(ascii_uppercase) for i in range(20))}
        self.client.post("/sentiment", json=payload)
        
        
### From main.py FASTAPI
@app.post("/sentiment")
async def predict(input_data: DataModel):
    result = model(input_data.text)[0]
    return result
</code></pre>
By using HttpUser and creating the User class that's inherited from it, we can
define an HttpUser class. <br>The @task decorator is essential for defining the task
that the user must perform after spawning. <br>The predict function is the actual
task that the user will perform repeatedly after spawning. <br>It will generate a random
string that's 20 in length and send it to your API.

<pre><code># To start the test, you must start your service. Once you've started your service, run the following code to start the Locust load test:
$ locust -f locust_file.py
</code></pre>
</details>

</ul></details>

</div>








