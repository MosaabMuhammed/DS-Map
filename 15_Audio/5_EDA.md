<h1 id="4exploratorydataanalysiseda">4. Exploratory Data Analysis (EDA)</h1>

<div style='width:1000px;margin:auto'>
<details><summary>Show <b> the audio</b></summary>
<pre><code># Using librosa
import librosa
import librosa.display

data, rate = librosa.load(audio_file)
print("Sampling (frame) rate = ", rate)
print("Total samples (frames) = ", data.shape)
print(data)

librosa.display.waveplot(data)
</code></pre>
<pre><code># Using scipy
from scipy.io import wavfile
rate, data = wavfile.read(fname)
print("Sampling (frame) rate = ", rate)
print("Total samples (frames) = ", data.shape)
print(data)

plt.plot(data, '-', );

### Zoom in
plt.figure(figsize=(16, 4))
plt.plot(data[:500], '.'); plt.plot(data[:500], '-');
</code></pre>
</details>

<details><summary>Show <b> Spectogram</b></summary>
<a href="./0_notebooks/Extracting Spectrograms from Audio with Python.html">Notebook</a>
</details>
</div>