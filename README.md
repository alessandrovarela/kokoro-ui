# 🎤 Kokoro TTS UI

Uma interface web simples e elegante para o sistema de síntese de voz Kokoro, construída com Streamlit.

## ✨ Características

- **Interface em duas colunas** para uma experiência otimizada
- **Suporte a múltiplos idiomas**
- **Múltiplas vozes** para cada idioma (masculinas e femininas)
- **Controle de velocidade** ajustável (0.1x a 2.0x)
- **Player de áudio integrado** para reprodução imediata
- **Download direto** dos arquivos WAV gerados
- **Gerenciamento de sessões** para múltiplos usuários

## 🚀 Instalação

### Pré-requisitos
- Python 3.12 ou superior
- UV (gerenciador de dependências)

### Instalação das dependências
```bash
uv sync
```

## 🎯 Como usar

1. **Iniciar a aplicação:**
   ```bash
   uv run streamlit run app.py
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