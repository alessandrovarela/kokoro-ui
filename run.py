#!/usr/bin/env python3
"""
Script para executar a aplicação Kokoro TTS UI
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Execute a aplicação Streamlit"""
    app_path = Path(__file__).parent / "app.py"
    
    if not app_path.exists():
        print("❌ Erro: app.py não encontrado!")
        sys.exit(1)
    
    print("🎤 Iniciando Kokoro TTS UI...")
    print("📱 A aplicação será aberta em: http://localhost:8501")
    print("⏹️  Para parar a aplicação, pressione Ctrl+C")
    print()
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            str(app_path),
            "--server.headless", "true",
            "--server.port", "8501",
            "--browser.gatherUsageStats", "false",
            "--server.runOnSave", "true"
        ])
    except KeyboardInterrupt:
        print("\n👋 Aplicação finalizada!")
    except Exception as e:
        print(f"❌ Erro ao executar a aplicação: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
