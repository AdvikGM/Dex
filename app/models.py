# app/models.py
# 🗄️ DATABASE SYSTEM Blueprints WITH USER SECURITY & PROMPT TRACKING

from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False) # Stores securely encrypted passwords
    timestamp = db.Column(db.String(50), default=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class PromptCounter(db.Model):
    __tablename__ = 'prompt_counters'
    id = db.Column(db.Integer, primary_key=True)
    visitor_token = db.Column(db.String(100), unique=True, nullable=False)
    count = db.Column(db.Integer, default=0)
    last_update = db.Column(db.String(50), default=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class ChatHistory(db.Model):
    __tablename__ = 'chat_history'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), nullable=False, default="default_session")
    user_msg = db.Column(db.Text, nullable=False)
    bot_msg = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.String(50), default=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class UserFact(db.Model):
    __tablename__ = 'user_facts'
    id = db.Column(db.Integer, primary_key=True)
    fact_text = db.Column(db.String(500), nullable=False, unique=True)
    timestamp = db.Column(db.String(50), default=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
