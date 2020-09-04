<!doctype HTML><html><head><meta charset="utf-8"><title>Made with Remarkable!</title><link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.1/styles/github.min.css"><style type='text/css'>body,table tr{background-color:#fff}table tr td,table tr th{border:1px solid #ccc;text-align:left;padding:6px 13px;margin:0}pre code,table,table tr{padding:0}hr,pre code{background:0 0}body{font:16px Helvetica,Arial,sans-serif;line-height:1.4;color:#333;word-wrap:break-word;padding:10px 15px}strong,table tr th{font-weight:700}h1{font-size:2em;margin:.67em 0;text-align:center}h2{font-size:1.75em}h3{font-size:1.5em}h4{font-size:1.25em}h1,h2,h3,h4,h5,h6{font-weight:700;position:relative;margin-top:15px;margin-bottom:15px;line-height:1.1}h1,h2{border-bottom:1px solid #eee}hr{height:0;margin:15px 0;overflow:hidden;border:0;border-bottom:1px solid #ddd}a{color:#4183C4}a.absent{color:#c00}ol,ul{padding-left:15px;margin-left:5px}ol{list-style-type:lower-roman}table tr{border-top:1px solid #ccc;margin:0}table tr:nth-child(2n){background-color:#aaa}table tr td :first-child,table tr th :first-child{margin-top:0}table tr td:last-child,table tr th :last-child{margin-bottom:0}img{max-width:100%}blockquote{padding:0 15px;border-left:4px solid #ccc}code,tt{margin:0 2px;padding:0 5px;white-space:nowrap;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px}pre code{margin:0;white-space:pre;border:none}.highlight pre,pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px}</style></head><body><h1>Nerual Networks</h1>
<div style="width:1000px;margin:auto">
<details><summary><strong>1. Linear Model</strong> (Digit Recoginzer)</summary>

<p>

<h4 id="1importrequiredlibraries">1. Import required libraries.</h4>

<pre><code class="python">from keras.models import Sequential
from keras.layers.core import Lambda, Dense, Flatten, Dropout
</code></pre>


<h4 id="2desingthearchitectureofthemodel">2. Desing the architecture of the model.</h4>


<pre><code class="python">def standardize(x):
    return (x - mean_px)/std_px
</code></pre>


<pre><code class="python">model = Sequential()
model.add(Lambda(standardize, input_shape=(28, 28, 1)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

print('~&gt; Input Shape:', model.input_shape)
print('~&gt; Output Shape:', model.output_shape)
</code></pre>


<h4 id="3setoptimizermetricandlossfunction">3. Set Optimizer, Metric, and loss function.</h4>

<pre><code class="Python">from keras.optimizers import RMSprop

model.compile(optimizer=RMSprop(lr=.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])
</code></pre>


<h4 id="4dataagumentation">4. Data Agumentation.</h4>

<pre><code class="python">from keras.preprocessing import image

gen = image.ImageDataGenerator()

from sklearn.model_selection import train_test_split

X = X_train
y = y_train

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=.1, random_state=42)
train_batches = gen.flow(X_train, y_train, batch_size=64)
val_batches   = gen.flow(X_val, y_val, batch_size=64)
</code></pre>


<h4 id="5fitthemodel">5. Fit the model.</h4>

<pre><code class="python">history = model.fit_generator(generator=train_batches, 
                              steps_per_epoch=train_batches.n, 
                              epochs=5,
                              validation_data=val_batches,
                              validation_steps=val_batches.n)
</code></pre>

</p></details>


<details><summary><strong>2. Fully Connected Model</strong> (Digit Recoginzer)</summary><p>
<h4 id="desingthearchitectureofthemodel">Desing the architecture of the model.</h4>

<pre><code class="python">def get_fc_model():
    model = Sequential([
        Lambda(standardize, input_shape=(28, 28, 1)),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='Adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model
</code></pre>


<h4 id="callandhypertune">Call and hypertune.</h4>

<pre><code class="python">fc = get_fc_model()
fc.optimizer.lr=0.01
</code></pre>


#### Run

<pre><code class="python">history=fc.fit_generator(generator=batches, steps_per_epoch=batches.n, epochs=1, 
                    validation_data=val_batches, validation_steps=val_batches.n)
</code></pre>

</p></details>

<details><summary><strong>3. Functional API</strong></summary><p>
<h4>Strucuture of the model</h4>

<pre><code>import tensorflow as tf

input_A = tf.keras.layers.Input(shape=[5], name=&quot;Input_A&quot;)
input_B = tf.keras.layers.Input(shape=[6], name=&quot;Input_B&quot;)

hidden1 = tf.keras.layers.Dense(30, activation=&quot;relu&quot;, name=&quot;Hidden_1&quot;)(input_B)
hidden2 = tf.keras.layers.Dense(30, activation=&quot;relu&quot;, name=&quot;Hidden_2&quot;)(hidden1)
concat  = tf.keras.layers.concatenate([input_A, hidden2])
output  = tf.keras.layers.Dense(1, activation=&quot;linear&quot;, name=&quot;Output&quot;)(concat)
aux_out = tf.keras.layers.Dense(1, activation=&quot;linear&quot;, name=&quot;Aux_Output&quot;)(hidden2)

model = tf.keras.models.Model(inputs=[input_A, input_B], outputs=[output, aux_out])

# Visualize the structure of the model.
tf.keras.utils.plot_model(model)
</code></pre>


<h4>Reset the dataset to be fed</h4>

<pre><code>X_train_A, X_train_B = X_train_scaled[:, :5], X_train_scaled[:, 2:]
X_valid_A, X_valid_B = X_valid_scaled[:, :5], X_valid_scaled[:, 2:]
X_test_A, X_test_B   = X_test_scaled[:, :5],  X_test_scaled[:, 2:]

# Fit and Compile.
# you can use a dictionary to feed the losses like this:
# {&quot;output1&quot;: &quot;mse&quot;, &quot;output2&quot;: &quot;cross_entropy&quot;}, but you have to name those output layers.
# Secondly, try to figure out the loss_weights for each loss.
model.compile(loss=[&quot;mse&quot;, &quot;mse&quot;],
              loss_weights=[.9, .1],
              optimizer=&quot;sgd&quot;)

history = model.fit([X_train_A, X_train_B],
                    [y_train, y_train],
                    epochs=20,
                    validation_data=([X_valid_A, X_valid_B], [y_valid, y_valid]))
</code></pre>

</p></details>

<details><summary><strong>4. SubClass API</strong></summary><p>

<pre><code># In call(), you can use if statements, for loops, whatever you want!
class WideAndDeepModel(tf.keras.models.Model):
    def __init__(self, units=30, activation=&quot;relu&quot;, **kwargs):
        super().__init__(**kwargs)  # Handles standard args (e.g., name)
        self.hidden1     = tf.keras.layers.Dense(units, activation=activation)
        self.hidden2     = tf.keras.layers.Dense(units, activation=activation)
        self.main_output = tf.keras.layers.Dense(1)
        self.aux_output  = tf.keras.layers.Dense(1)

    def call(self, inputs):
        input_A, input_B = inputs

        hidden1 = self.hidden1(input_B)
        hidden2 = self.hidden2(hidden1)
        concat  = tf.keras.layers.concatenate([input_A, hidden2])
        min_out = self.main_output(concat)
        aux_out = self.aux_output(hidden2)

        return main_output, aux_output

model = WideAndDeepModel()
</code></pre>

</p></details>

<a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/5%20Gradient%20Descent.html#Logistic-Regression-Model">Manual Hyperparameter Tunning</a>

</div><script src="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.1/highlight.min.js"></script><script>hljs.initHighlightingOnLoad();</script><script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script><script type="text/javascript">MathJax.Hub.Config({"showProcessingMessages" : false,"messageStyle" : "none","tex2jax": { inlineMath: [ [ "$", "$" ] ] }});</script></body></html>