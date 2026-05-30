from flask import Flask, request, jsonify, render_template
from datetime import datetime
import sqlite3
import random

# Initialize Flask (Looks for templates/index.html automatically)
app = Flask(__name__)

# =====================================================================
# 🏗️ THE CORE BOT LOGIC BLUEPRINT
# =====================================================================
class AssistantBot:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.chat_data = {
            "Hello": ["Hey there!", "Hi! Ready to chat?", "Hello!"],
            "Hi": ["Hey there!", "Hi! Ready to chat?", "Hello!"],
            "Good": ["That's awesome! I'm happy to hear that.", "Sweet! Good vibes only."],
            "Sad": ["I'm sorry to hear that. Sending a virtual hug! 🤗", "Cheer up! You got this!"],
            "Tired": ["Go get some rest! 😴", "Take a break, coding can wait."]
        }

    def process_message(self, raw_input):
        clean_input = raw_input.strip()
        if not clean_input:
            return "Please say something!"
            
        # Standardize phrasing format
        user_input = clean_input[0].upper() + clean_input[1:] if len(clean_input) > 0 else clean_input

        # Core Routing Commands
        if user_input == "Time":
            now = datetime.now()
            return f"📅 Today is {now.strftime('%B %d, %Y')} | ⏰ Time: {now.strftime('%I:%M %p')}"
            
        elif user_input == "System":
            return f"🏷️ Name: {self.name} | 🚀 Version: {self.version} | 🗄️ Database: SQLite3 (site.db)"
            
        elif user_input == "Flip":
            return f"Flipping a coin... It landed on: {random.choice(['🪙 HEADS!', '🪙 TAILS!'])}"
            
        elif user_input == "Roll":
            return f"🎲 You rolled a: {random.randint(1, 6)}"
            
        else:
            # Check dictionary matching
            for key in self.chat_data:
                if key.lower() in user_input.lower():
                    return random.choice(self.chat_data[key])
            
            return "I don't know that command yet. Try typing 'Time', 'System', 'Flip', or 'Roll'!"

# Create our active global bot brain instance
dex_brain = AssistantBot("Dex", "v2.8.5")


# =====================================================================
# 🗄️ SQLITE3 DATABASE LOGIC
# =====================================================================
def save_to_database(user_text, bot_text):
    # 1. Connect to our file (creates site.db automatically if missing)
    conn = sqlite3.connect("site.db")
    
    # 2. Open up our tool workspace cursor
    cursor = conn.cursor()
    
    # 3. Build our table structure columns if they don't exist yet
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_msg TEXT,
            bot_msg TEXT,
            timestamp TEXT
        )
    ''')
    
    # 4. Insert the string values securely into the matching columns
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO history (user_msg, bot_msg, timestamp) VALUES (?, ?, ?)", 
        (user_text, bot_text, current_time)
    )
    
    # 5. Hit the Save button and close the database connection cleanly
    conn.commit()
    conn.close()


# =====================================================================
# 🌐 FLASK WEB API ROUTE CONTROLLERS
# =====================================================================

# ROUTE 1: Opens your visual web layout interface inside your browser
@app.route('/')
def home():
    return render_template('index.html')

# ROUTE 2: API endpoint designed to catch and reply to data packets
@app.route('/ask', methods=['POST'])
def ask_dex():
    data = request.get_json() or {}
    user_message = data.get("message", "")

    # Run the message directly through our standard Bot Class logic
    bot_reply = dex_brain.process_message(user_message)

    # Save the conversation using our SQLite function
    if user_message.strip():
        save_to_database(user_message, bot_reply)

    return jsonify({"dex_says": bot_reply})
