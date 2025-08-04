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

## 🚀 Demo on Hugging Face Spaces
https://huggingface.co/spaces/alessandrovarela/kokoro-ui


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