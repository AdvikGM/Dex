# run.py
# 🚀 CORE ENTRY POINT LAUNCHER FOR THE DEX NEURAL SYSTEM WORKSPACE

import os
from dotenv import load_dotenv

# 🎯 CRITICAL FIX: Force environment variables to load BEFORE importing app blueprints
load_dotenv()

from flask import Flask
from app.routes import main_blueprint

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("FLASK_SECRET_KEY", "dex_core_neural_matrix_secret_9981")
    app.register_blueprint(main_blueprint)
    return app

app = create_app()

if __name__ == '__main__':
    print("⚡ [Dex Launch Subsystem] Initializing server...")
    print("🌐 Gateway running at: http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
