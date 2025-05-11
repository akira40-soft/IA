import subprocess
import os
import sys
from flask import Flask
from src.api.api import api_bp
import asyncio

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')

def start_venom_bot():
    """Inicia o venom_bot.js em um processo separado."""
    bot_path = os.path.join(os.path.dirname(__file__), 'src', 'bot', 'venom_bot.js')
    if os.path.exists(bot_path):
        print("Iniciando venom_bot.js...")
        subprocess.Popen(['node', bot_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        print("Erro: venom_bot.js não encontrado em src/bot/")

def run_api():
    """Inicia a API Flask."""
    print("Iniciando API Flask...")
    app.run(host= "0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    # Iniciar o bot em uma thread separada
    import threading
    bot_thread = threading.Thread(target=start_venom_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # Iniciar a API
    run_api()
