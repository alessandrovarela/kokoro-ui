# 🚀 How to run the Kokoro TTS UI application

## Prerequisites
- Python 3.12 (automatically configured by UV)
- UV (dependency manager)
- Internet connection (for model download on first run)

## Installed dependencies
✅ All dependencies were successfully installed:
- streamlit==1.47.1
- kokoro==0.9.4
- soundfile==0.13.1
- numpy==2.3.2
- + 100+ auxiliary dependencies

## How to run

### Run the application
```bash
uv run streamlit run app.py --server.runOnSave true
```

**OR** (if virtual environment is active):
```bash
python -m streamlit run app.py --server.runOnSave true
```

**OR** using the run script:
```bash
uv run python run.py
```

### Access the application
- Open your browser at: http://localhost:8501
- The application will load automatically

## Common issues

### 1. "ModuleNotFoundError: No module named 'streamlit'"
**Solution:** Always use `uv run` before commands:
```bash
uv run streamlit run app.py
```

### 2. Reinstall dependencies (if needed)
```bash
uv sync
```

## Application features

### Left Column (Settings):
- **Input Text**: Text field for inserting up to 500 characters
- **Language**: Language selector (default: Brazilian Portuguese)
- **Voice**: Voice selector (filtered by selected language)
- **Speed**: Slider to adjust speed (0.1 to 2.0)
- **Generate**: Button to generate audio

### Right Column (Generated Audio):
- **Audio Player**: Player to play the generated audio
- **File Download**: Information and download button for WAV file

## Available voices by language

- 🇺🇸 **American English**: 20 voices (11F, 9M)
- 🇬🇧 **British English**: 8 voices (4F, 4M)  
- 🇯🇵 **Japanese**: 5 voices (4F, 1M)
- 🇨🇳 **Mandarin Chinese**: 8 voices (4F, 4M)
- 🇪🇸 **Spanish**: 3 voices (1F, 2M)
- 🇫🇷 **French**: 1 voice (1F)
- 🇮🇳 **Hindi**: 4 voices (2F, 2M)
- 🇮🇹 **Italian**: 2 voices (1F, 1M)
- 🇧🇷 **Brazilian Portuguese**: 3 voices (1F, 2M)
  - pf_dora (🚺)
  - pm_alex (🚹)
  - pm_santa (🚹)

## Session management
- Each user receives a unique session
- Previous audio files are automatically removed
- Automatic cleanup of temporary files

## Project files
- `app.py` - Main Streamlit application
- `pyproject.toml` - Configuration and dependencies
- `uv.lock` - Dependencies lock file
- `README.md` - Documentation
- `voices.md` - Voice documentation

---
🎤 **Application created successfully!** Ready to convert text to speech using Kokoro TTS.
