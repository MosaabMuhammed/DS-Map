<h1 id="improvingperformance">Improving Performance</h1>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Learning-curves"><b style='color:#333'>1. Learning Curves</b></a> </p>

<details><summary><b>Batch Normalization</b></summary><p>
<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Batch-Normalization"><b style='color:#333'>2. Batch Normalization</b></a> </p>

<h4>You can try both of the following, and see which one works best for you</h4>
```
# Adding BatchNormalization after activation.
input1      = tf.keras.layers.Input(shape=[2])
batch_norm1 = tf.keras.layers.BatchNormalization()(input1)
hidden1     = tf.keras.layers.Dense(50, activation="elu", kernel_initializer="he_normal")(batch_norm1)
batch_norm2 = tf.keras.layers.BatchNormalization()(hidden1)
hidden2     = tf.keras.layers.Dense(30, activation="elu", kernel_initializer="he_normal")(batch_norm2)
batch_norm3 = tf.keras.layers.BatchNormalization()(hidden2)
output1     = tf.keras.layers.Dense(1, activation="sigmoid")
```

```
# Adding BatchNormalization BEFORE activation.
input1      = tf.keras.layers.Input(shape=[2])
batch_norm1 = tf.keras.layers.BatchNormalization()(input1)
hidden1     = tf.keras.layers.Dense(50, kernel_initializer="he_normal")(batch_norm1)
batch_norm2 = tf.keras.layers.BatchNormalization()(hidden1)
elu1        = tf.keras.layers.Activation("elu")(batch_norm2)

hidden2     = tf.keras.layers.Dense(30, kernel_initializer="he_normal")(elu1)
batch_norm3 = tf.keras.layers.BatchNormalization()(hidden2)
elu2        = tf.keras.layers.Activation("elu")(batch_norm3)
output1     = tf.keras.layers.Dense(1, activation="sigmoid")
```
</p></details>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Weight-Regularization-&amp;-Dropout"><b style='color:#333'>3. Dropout</b></a> </p>

<details><summary><b>4. Weight Regularization</b></summary>
<p>
<li><a href="https://keras.io/initializers/"><b style='color:#333'>1. Available initializers in Keras</b></a> </li>

<li><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/Deep%20Learning%20Nanodegree/0_Data/deep-learning-master/weight-initialization/weight_initialization.html#Weight-Initialization"><b style='color:#333'>2. Which one is better (Experiment)</b></a> </p>

</p>
</details>

<details><summary><b>4. Data Augmentation</b></summary>
<p>

<p><a href="file:///media/mosaab/Volume/Courses/Computer%20Science/Advanced/Machine%20Learning/Udacity/Udacity%20-%20Deep%20Learning%20Nanodegree%20Program/Part%2003-Module%2001-Lesson%2002_Convolutional%20Neural%20Networks/20.%20Image%20Augmentation%20in%20Keras.html"><b style='color:#333'>1. Concept (Udacity)</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Data-augmentation"><b style='color:#333'>2. Code Example</b></a> </p>


</p>
</details>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Embeddings"><b style='color:#333'>5. Embedding</b></a> </p>

<p><a href="file:///media/mosaab/Volume/Personal/Development/Courses%20Docs/zero_to_deep_learning_video/course/9%20Improving%20performance.html#Sentiment-prediction-on-movie-Reviews"><b style='color:#333'>Ex: Sentiment Analysis on Movie Review</b></a> </p>
 