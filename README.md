# 🚀 LinguaWhisper: Multilingual Audio Detection, Transcription & Translation 🎙️🌐

![Streamlit](https://img.shields.io/badge/Streamlit-App-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🔥 What is LinguaWhisper?

LinguaWhisper is a **cutting-edge Streamlit app** that empowers users to:

- Upload audio files (`wav`, `mp3`, `m4a`)  
- Automatically detect the spoken language using GMM models  
- Transcribe speech to text using OpenAI's Whisper tiny model  
- Instantly translate the transcription into French (or other languages)  

Ideal for **journalists, researchers, language learners, and AI enthusiasts** working with multilingual audio data.

---

## ⚡ Features at a Glance

| Feature                        | Description                                     |
|-------------------------------|------------------------------------------------|
| 🎵 Multi-format Audio Upload   | WAV, MP3, M4A, and more                        |
| 🌍 Language Detection          | French, Italian, German, Russian via GMM       |
| 📝 Accurate Transcription      | Powered by OpenAI Whisper tiny                  |
| 🌐 Instant Translation         | Translate transcriptions seamlessly              |
| 🚀 Interactive UI              | Fast & user-friendly Streamlit interface        |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher  
- [Streamlit](https://streamlit.io/)  
- FFmpeg is installed and added to your system PATH  

### Installation

```bash
git clone https://github.com/YourUsername/LinguaWhisper.git
cd LinguaWhisper

# Optional: create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat # Windows

pip install -r requirements.txt
```
###  Run the App 
```bash
streamlit run app.py
```
<p align="center">
  <img src="https://github.com/zainabjanice/LinguaWhisper/blob/f24650967446ede82e7894f9dbe835f726318c83/cap1.png?raw=true" alt="Screenshot" width="620"/>
</p>

### 🛠️ How to Use
1. Upload your audio file via the uploader widget.

2. Click **Detect the language** to detect the language.

3. Click **Transcribe with Whisper** to transcribe the audio.

4. Optionally, translate the text by clicking **Translate into English**.

### 📄 License
This project is licensed under the MIT License. See LICENSE for details.

### 📞 Contact
Created with ❤️ by Zainab Jamil

Gmail: jamilzainab91@gmail.com

LinkedIn: https://www.linkedin.com/in/zainab-jamil-50223a247/
