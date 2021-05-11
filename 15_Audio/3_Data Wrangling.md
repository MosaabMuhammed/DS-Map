<h1 id="3datawrangling">3. Data Wrangling</h1>

<div style='width:1000px;margin:auto'>

<details><summary><b>Display Audio</b> in notebook</summary><pre><code>import IPython.display as ipd
fname = '../input/freesound-audio-tagging/audio_train/' + '00043347.wav'   # Hi-hat
ipd.Audio(fname)
</code></pre></details>

<details><summary>Get <b>Sampling Rate / Total Samples</b></summary>
<pre><code># Using wave library
import wave
fname = '../input/freesound-audio-tagging/audio_train/' + '00044347.wav'   # Hi-hat
wav = wave.open(fname)
print("Sampling (frame) rate = ", wav.getframerate())
print("Total samples (frames) = ", wav.getnframes())
print("Duration = ", wav.getnframes()/wav.getframerate())
</code></pre>
<pre><code># Using wave library
# Using scipy
from scipy.io import wavfile
rate, data = wavfile.read(fname)
print("Sampling (frame) rate = ", rate)
print("Total samples (frames) = ", data.shape)
print(data)
</code></pre>
<pre><code># Using librosa package
audio_path = '../input/birdsong-recognition/train_audio/aldfly/XC181484.mp3'

y, sr = librosa.load(audio_path, sr=22050)

print("Audio Intially")
ipd.Audio(y,rate=sr)
</code></pre>
</details>

<details><summary><b>Data Augmentation<b> using <b>Albumentations</b></summary>

<a href="./0_notebooks/audio-albumentations-transform-your-audio.html">Notebook</a>
</details>
 </div>