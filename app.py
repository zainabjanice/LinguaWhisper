import streamlit as st
import numpy as np
import librosa
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
import os
import whisper
from googletrans import Translator

# --- Configuration ---
LANGUAGES = ['francais', 'italien', 'allemande', 'russe']
MODEL_DIR = r"C:\Users\jamil\Downloads\models_gmm"
TEMPDIR = r"C:\Users\jamil\Desktop\tempdir"
N_COMPONENTS = 512

# --- Extraction des caractéristiques ---
def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    y_trimmed, _ = librosa.effects.trim(y, top_db=20)

    mfcc = librosa.feature.mfcc(y=y_trimmed, sr=sr, n_mfcc=13)
    delta = librosa.feature.delta(mfcc)
    delta2 = librosa.feature.delta(mfcc, order=2)

    features = np.vstack([mfcc, delta, delta2]).T

    scaler = StandardScaler()
    return scaler.fit_transform(features)

# --- Chargement des modèles GMM ---
@st.cache_resource
def load_gmm_models(model_dir=MODEL_DIR, n_components=N_COMPONENTS):
    models = {}
    for lang in LANGUAGES:
        means = np.load(os.path.join(model_dir, f"{lang}_means.npy"))
        covariances = np.load(os.path.join(model_dir, f"{lang}_covariances.npy"))
        weights = np.load(os.path.join(model_dir, f"{lang}_weights.npy"))
        precisions_cholesky = np.load(os.path.join(model_dir, f"{lang}_precisions_cholesky.npy"))

        gmm = GaussianMixture(n_components=n_components, covariance_type='diag')
        gmm.means_ = means
        gmm.covariances_ = covariances
        gmm.weights_ = weights
        gmm.precisions_cholesky_ = precisions_cholesky
        models[lang] = gmm
    return models

# --- Prédiction ---
def predict(models, features):
    scores = {lang: model.score(features) for lang, model in models.items()}
    best_lang = max(scores, key=scores.get)
    return best_lang, scores

# --- Interface Streamlit ---
st.set_page_config(page_title="Détection & Transcription Audio", page_icon="🎙️", layout="centered")
st.title("🎙️ Language Detection, Transcription and Translation")
st.write("Upload an audio file, detect the language, transcribe with Whisper, and translate.")

# Upload & Save
uploaded_file = st.file_uploader("📂 Choose an audio file (WAV, MP3, M4A...)", type=["wav", "mp3", "m4a"])
if uploaded_file:
    file_path = os.path.join(TEMPDIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.audio(file_path, format="audio/wav")
    #st.success(f"Fichier enregistré dans {TEMPDIR}")

    # Load models once
    with st.spinner("Chargement des modèles GMM..."):
        models = load_gmm_models()

    # Language detection
    if st.button("🔍 Detect the language"):
        with st.spinner("Audio Analysis..."):
            features = extract_features(file_path)
            best_lang, scores = predict(models, features)
        st.success(f"Detected language : **{best_lang}**")
        st.write("Scores :", {k: round(v, 2) for k, v in scores.items()})

    # Transcription
    if st.button("📝 Transcribe with Whisper"):
        with st.spinner("Loading the Whisper model..."):
            model = whisper.load_model("tiny")
        with st.spinner("Transcription in progress..."):
            result = model.transcribe(file_path)
        st.subheader("Transcription")
        st.write(result["text"])
        st.session_state["last_transcription"] = result["text"]

    # Translation
    if "last_transcription" in st.session_state and st.button("🌍 Translate into English"):
        with st.spinner("Translation in progress..."):
            translator = Translator()
            translation = translator.translate(st.session_state["last_transcription"], dest="en")
        st.subheader("Translation in english")
        st.write(translation.text)
