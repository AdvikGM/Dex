import sys
import subprocess

REQUIRED = {"flask": "flask", "requests": "requests", "dotenv": "python-dotenv"}

def install_deps():
    for mod, pkg in REQUIRED.items():
        try:
            __import__(mod)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

if __name__ == '__main__':
    install_deps()
    from app import app
    print("\n🚀 Code Debugger is running at http://127.0.0.1:5000\n")
    app.run(host='0.0.0.0', port=5000, debug=True)