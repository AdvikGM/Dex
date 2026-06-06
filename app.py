from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Initialize Flask
app = Flask(__name__)

# Configure SQLite Database path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy Database instance
db = SQLAlchemy(app)

# Import and register routes AFTER initializing db to avoid circular imports
from routes import configure_routes
configure_routes(app)