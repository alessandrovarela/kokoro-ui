---
title: Kokoro TTS UI
sdk: docker
app_port: 8501
license: mit
---

title: Kokoro TTS UI
emoji: 🎤
## 🔧 Technologies

- **Streamlit** - Web interface
- **Kokoro TTS** - Voice synthesis system
- **PyTorch** - Machine learning backend
- **NumPy** - Audio processing
- **SoundFile** - Audio file manipulation
- **Docker** - Containerization for deployment

## 🚀 Deployment

This application is designed to run on **Hugging Face Spaces** using Docker.

### Docker Configuration:
- **Base Image**: Python 3.12-slim
- **Port**: 8501
- **System Dependencies**: espeak-ng, ffmpeg, libsndfile1
- **User**: Non-root user (UID 1000)

### Local Development:
```bash
# Using UV (recommended)
uv run streamlit run app.py

# Using Docker
docker build -t kokoro-tts-ui .
docker run -p 8501:8501 kokoro-tts-ui
```

## 📝 License

MIT License - see LICENSE file for details.


# 🎤 Kokoro TTS Generator

An elegant web interface for voice synthesis using the Kokoro AI system, built with Streamlit.

## ✨ Features

- **Two-column interface** optimized for desktop and mobile
- **Support for 9 languages**: English (US/UK), Japanese, Mandarin Chinese, Spanish, French, Hindi, Italian, Brazilian Portuguese
- **Multiple voices** male and female for each language
- **Adjustable speed control** (0.1x to 2.0x)
- **Integrated audio player** for immediate playback
- **Direct download** of generated WAV files
- **Intelligent session management** for multiple users
- **Custom filenames** with timestamp

## 🎯 How to use

1. **Type your text** (up to 500 characters)
2. **Select the desired language**
3. **Choose an available voice** for the language
4. **Adjust speed** if needed
5. **Click Generate** to create audio
6. **Play** the generated audio and **download** if desired

## 🔧 Technologies

- **Streamlit** - Web interface
- **Kokoro TTS** - Voice synthesis system
- **PyTorch** - Machine learning backend
- **NumPy** - Audio processing
- **SoundFile** - Audio file manipulation

## 📝 License

MIT License - see LICENSE file for details.

---

Powered by [Kokoro TTS](https://github.com/hexgrad/kokoro)
   ```

2. **Access the interface:**
   - Open your browser at `http://localhost:8501`


## 🌍 Supported Languages and Voices

- **🇺🇸 American English**: 11 female voices, 9 male voices
- **🇬🇧 British English**: 4 female voices, 4 male voices  
- **🇯🇵 Japanese**: 4 female voices, 1 male voice
- **🇨🇳 Mandarin Chinese**: 4 female voices, 4 male voices
- **🇪🇸 Spanish**: 1 female voice, 2 male voices
- **🇫🇷 French**: 1 female voice
- **🇮🇳 Hindi**: 2 female voices, 2 male voices
- **🇮🇹 Italian**: 1 female voice, 1 male voice
- **🇧🇷 Brazilian Portuguese**: 1 female voice, 2 male voices


## 🔧 Configuration

The application uses the following default settings:
- **Port**: 8501
- **Audio quality**: 24kHz WAV
- **Character limit**: 500 per generation


## 🤝 Based on

This project is based on [kokoro-sample](https://github.com/alessandrovarela/kokoro-sample) and uses the [Kokoro TTS](https://github.com/hexgrad/kokoro) system for voice synthesis.

## 📄 License

This project follows the same license as the original Kokoro project.