---
title: Kokoro TTS UI
sdk: docker
app_port: 8501
license: mit
---

# 🎤 Kokoro TTS UI

Elegant web interface for voice synthesis using the **Kokoro** model, built with **Streamlit** and packaged for **Hugging Face Spaces (Docker)**.

## ✨ Features
- **Two‑column interface** optimized for desktop and mobile
- **9 languages**: EN‑US/EN‑UK, JA, ZH, ES, FR, HI, IT, PT‑BR
- **Multiple voices** per language (female/male)
- **Speed control** (0.1×–2.0×)
- **Integrated audio player** + **WAV download**
- **Session management** for concurrent users
- **Custom filenames** with timestamp

## 🚀 Deploy on Hugging Face Spaces (Docker)
1. Crie um Space do tipo **Docker**.
2. Este README já declara `sdk: docker` e `app_port: 8501` no front‑matter.
3. O container expõe e escuta em **0.0.0.0:8501** (veja `Dockerfile`).
4. Configure **Settings → Secrets/Variables** no Space se precisar de tokens/segredos.

### Docker configuration (summary)
- **Base image**: Python 3.12‑slim
- **Port**: 8501
- **System packages**: `espeak-ng`, `libsndfile1`, `ffmpeg`, `curl` (para healthcheck)
- **User**: non‑root (UID 1000)

## 🧪 Run locally
**Using UV (recommended)**
```bash
uv run streamlit run app.py
```

**Using Docker**
```bash
docker build -t kokoro-tts-ui .
docker run -p 8501:8501 kokoro-tts-ui
```

## 🎯 How to use
1. **Type your text** (up to 500 characters)
2. **Select language**
3. **Choose a voice**
4. **Adjust speed** (optional)
5. **Click Generate**
6. **Play** and/or **Download** the WAV

## 🔧 Technologies
- **Streamlit** – web UI
- **Kokoro TTS** – synthesis
- **PyTorch** – ML backend
- **NumPy** – audio processing helpers
- **SoundFile** – WAV I/O
- **Docker** – packaging/deploy

## 🌍 Supported languages and voices
- **🇺🇸 American English**: 11 female, 9 male
- **🇬🇧 British English**: 4 female, 4 male
- **🇯🇵 Japanese**: 4 female, 1 male
- **🇨🇳 Mandarin Chinese**: 4 female, 4 male
- **🇪🇸 Spanish**: 1 female, 2 male
- **🇫🇷 French**: 1 female
- **🇮🇳 Hindi**: 2 female, 2 male
- **🇮🇹 Italian**: 1 female, 1 male
- **🇧🇷 Brazilian Portuguese**: 1 female, 2 male

## 🔧 Configuration
Defaults:
- **Port**: 8501
- **Audio**: 24 kHz WAV
- **Character limit**: 500 per generation

## 🤝 Based on
- [kokoro-sample](https://github.com/alessandrovarela/kokoro-sample)
- [Kokoro TTS](https://github.com/hexgrad/kokoro)

## 📝 License
MIT — see `LICENSE`.