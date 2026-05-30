# Import the 'app' server instance directly from your dex_api file
from dex_api import app

if __name__ == '__main__':
    # Fire up the live web server thread execution loop
    print("🚀 Booting up the Dex Web Application Server via run.py...")
    app.run(debug=True)