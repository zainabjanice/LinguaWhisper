# LinguaWhisper: Multilingual Audio Detection, Transcription & Translation 

![Streamlit](https://img.shields.io/badge/Streamlit-App-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

##  Project Story

Imagine a conversation where someone speaks in German, another responds in Italian, and a third joins in French. How can a machine instantly recognize each language just by listening, without being told beforehand?

That’s the challenge I set out to solve in **LinguaWhisper**, a multilingual language recognition system powered by **Gaussian Mixture Models (GMMs)** and advanced audio processing techniques.

---

## How the System Thinks
### 1. Listening Like a Musician MFCC Extraction 

Every sound has a unique **fingerprint**.

I used **Mel-Frequency Cepstral Coefficients (MFCCs)** to capture the essence of each language’s sound patterns, just like how musicians recognize a song in a few notes.
  
Let's go into details :

Humans don’t process sound linearly; we perceive frequencies differently at low vs. high ranges.
MFCCs are features that mimic human hearing, focusing on how we perceive pitch and tone.

**What It Does**
- Takes a raw audio waveform
- Splits it into short frames (e.g., 25 ms)
- Applies the Fourier Transform to get the frequency spectrum
- Scales it to the Mel scale to match human perception
- Applies the Discrete Cosine Transform (DCT) to decorrelate features
  
**Formula**

Given the power spectrum 
$$𝑃(𝑓)$$ the MFCC coefficients are:

$$\text{MFCC}[n] = \sum_{m=1}^M \log(S_m) \cos\left[\frac{\pi n}{M}(m-\frac12)\right]$$

Where:
- $S m$ = Mel-scaled filter bank energy for filter $𝑚$
- $M$ = Number of filters
- $𝑛$ = Coefficient index

  
**Role in this project:**  

Transforms each `.wav` file into a compact representation that captures the “shape” of speech sounds in a language-specific way.

---

### 2. Building Language Profiles: Gaussian Mixture Models
Each language has its own acoustic **accent**.**GMMs** represent these signatures as a combination of multiple Gaussian distributions.
Using GMMs, I built statistical models that learn the distribution of speech features for German, French, Italian, and Russian.

**What it does**
- Each Gaussian model has one cluster of feature vectors (MFCCs)
- The mixture models the entire distribution of speech features for a language

**Formula**

The probability of a feature vector $𝑥$ under a GMM with $𝐾$ components is:  

$$p(x) = \sum_{k=1}^{K} w_k \cdot \mathcal{N}(x \mid \mu_k, \Sigma_k)$$

Where:
- $w k$ = weight of the $𝑘-th$ Gaussian (sum to 1)
- $μ k$ = mean vector
- $Σ k$ = covariance matrix
- $N(x∣μ k,Σ k)$ = multivariate normal distribution

The **Expectation-Maximization (EM) algorithm** estimates the parameters $𝑤𝑘$, $𝜇𝑘$, $Σ𝑘$ from training data.

**Role in this project:**

Learns the probability distribution of features for each language and scores how likely a new audio sample belongs to it.

---

### 3. Decision Making: Scoring & Classification

When a new audio clip is received, the system calculates likelihood scores across all language models and selects the highest-scoring one. It assigns the audio to the language with the most similar acoustic pattern.

---

### 4. Keeping the System Honest: Evaluation Metrics
Accuracy isn’t enough.

I measured:
- **Precision** → How often the predicted language was correct.
- **Recall** → How many clips of a language were correctly identified?
- **F1-score** → Balance between precision and recall.


---

## Results
<div align="center">

| Dataset    | Accuracy | Macro Precision | Macro Recall | Macro F1 |
|------------|----------|-----------------|--------------|----------|
| Validation | 86.5%    | 0.874            | 0.865        | 0.866    |
| Test       | 85.4%    | 0.866            | 0.854        | 0.855    |

</div>

With 512-component GMMs, the system achieved:
- Validation accuracy: 86.5%
- Test accuracy: 85.4%
  
Strong performance in detecting German and Italian; improvement needed for French recall.

---

## Installation

```bash
git clone https://github.com/YourUsername/LinguaWhisper.git
cd LinguaWhisper

# Optional: create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat # Windows

pip install -r requirements.txt
```
---
###  Run the App 
```bash
streamlit run app.py
```
---
### Installing FFmpeg

FFmpeg is required to handle various audio formats (MP3, M4A, WAV, etc.). Make sure it’s installed and added to your system’s PATH.

#### Windows

- 1. Download FFmpeg from https://www.gyan.dev/ffmpeg/builds/.
- 2. Extract the ZIP file to a folder (e.g., C:\ffmpeg).
- 3. Add the `bin` folder `(e.g., C:\ffmpeg\bin)` to **your Environment Variables → PATH**.
- 4. Verify the installation:
     
```bash
ffmpeg -version
```
#### macOS
```bash
brew install ffmpeg
```
#### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install ffmpeg
```
#### Linux (Fedora)
```bash
sudo dnf install ffmpeg
```
⚡Tip: Without FFmpeg, the app will only read .wav files, and MP3/M4A uploads will fail.

---

###  Contact
Created with ❤️ by Zainab Jamil

Gmail: jamilzainab91@gmail.com

LinkedIn: https://www.linkedin.com/in/zainab-jamil-50223a247/

Thank you for exploring LinguaWhisper! 🎧✨


