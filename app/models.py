from app import db
from datetime import datetime
from zoneinfo import ZoneInfo

class ChatHistory(db.Model):
    __tablename__ = 'history'
    
    id = db.Column(db.Integer, primary_key=True)
    user_msg = db.Column(db.Text, nullable=False)
    bot_msg = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.String(50), nullable=False)

    def __init__(self, user_msg, bot_msg):
        self.user_msg = user_msg
        self.bot_msg = bot_msg
        # Grab accurate India Standard Time automatically
        india_tz = ZoneInfo("Asia/Kolkata")
        self.timestamp = datetime.now(india_tz).strftime("%Y-%m-%d %H:%M:%S")
