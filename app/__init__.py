# app/__init__.py
# 🚀 SYSTEM ENGINE CORE ROOT PACKAGE INITIALIZATION

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# 🔐 Load secure API environment configuration keys from your root .env file
load_dotenv()

# Initialize Flask Framework Engine
# We add template_folder='../templates' so Flask can find your HTML files from inside this new folder!
app = Flask(__name__, template_folder='../templates')

# 🗄️ Configure SQLite Relational Database path to save securely in your root folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy Database instance controller
db = SQLAlchemy(app)

# 🌐 Register our web traffic controller systems
# CRITICAL: We import this at the absolute bottom to prevent circular import loops!
from app.routes import configure_routes
configure_routes(app)
