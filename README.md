---
title: Kokoro TTS UI
emoji: 🎤
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.47.1
app_file: app.py
pinned: false
license: mit
---

# 🎤 Kokoro TTS Generator

Uma interface web elegante para síntese de voz usando o sistema Kokoro AI, construída com Streamlit.

## ✨ Características

- **Interface em duas colunas** otimizada para desktop e mobile
- **Suporte a 9 idiomas**: Inglês (US/UK), Japonês, Chinês Mandarim, Espanhol, Francês, Hindi, Italiano, Português Brasileiro
- **Múltiplas vozes** masculinas e femininas para cada idioma
- **Controle de velocidade** ajustável (0.1x a 2.0x)
- **Player de áudio integrado** para reprodução imediata
- **Download direto** dos arquivos WAV gerados
- **Gerenciamento inteligente de sessões** para múltiplos usuários
- **Nomes de arquivo personalizados** com timestamp

## 🎯 Como usar

1. **Digite seu texto** (até 500 caracteres)
2. **Selecione o idioma** desejado
3. **Escolha uma voz** disponível para o idioma
4. **Ajuste a velocidade** se necessário
5. **Clique em Generate** para criar o áudio
6. **Reproduza** o áudio gerado e **faça o download** se desejar

## 🔧 Tecnologias

- **Streamlit** - Interface web
- **Kokoro TTS** - Sistema de síntese de voz
- **PyTorch** - Backend de machine learning
- **NumPy** - Processamento de áudio
- **SoundFile** - Manipulação de arquivos de áudio

## 📝 Licença

MIT License - veja o arquivo LICENSE para detalhes.

---

Powered by [Kokoro TTS](https://github.com/hexgrad/kokoro)
   ```

2. **Acessar a interface:**
   - Abra seu navegador em `http://localhost:8501`


## 🌍 Idiomas e Vozes Suportados

- **🇺🇸 Inglês Americano**: 11 vozes femininas, 9 masculinas
- **🇬🇧 Inglês Britânico**: 4 vozes femininas, 4 masculinas  
- **🇯🇵 Japonês**: 4 vozes femininas, 1 masculina
- **🇨🇳 Chinês Mandarim**: 4 vozes femininas, 4 masculinas
- **🇪🇸 Espanhol**: 1 voz feminina, 2 masculinas
- **🇫🇷 Francês**: 1 voz feminina
- **🇮🇳 Hindi**: 2 vozes femininas, 2 masculinas
- **🇮🇹 Italiano**: 1 voz feminina, 1 masculina
- **🇧🇷 Português Brasileiro**: 1 voz feminina, 2 masculinas


## 🔧 Configuração

A aplicação usa as seguintes configurações padrão:
- **Porta**: 8501
- **Qualidade de áudio**: 24kHz WAV
- **Limite de caracteres**: 500 por geração


## 🤝 Baseado em

Este projeto é baseado no [kokoro-sample](https://github.com/alessandrovarela/kokoro-sample) e utiliza o sistema [Kokoro TTS](https://github.com/hexgrad/kokoro) para síntese de voz.

## 📄 Licença

Este projeto segue a mesma licença do projeto Kokoro original.