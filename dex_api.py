from flask import Flask, request, jsonify, render_template
from datetime import datetime
from zoneinfo import ZoneInfo     # ⏰ Perfect India Time
import sqlite3
import random
import math
import os                         # 📂 Systems manager
from dotenv import load_dotenv     # 🔐 Loads your secret key
from google import genai          # 🧠 Gemini AI Client

# Load environment configuration variables securely
load_dotenv()

# Initialize Flask framework engine
app = Flask(__name__)

# Core CORS middleware allows safe local browser transactions 
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    return response


# =====================================================================
# 🏗️ THE ULTIMATE MULTI-SKILL AI BOT ENGINE
# =====================================================================
class AssistantBot:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        
        # 📋 Volatile in-memory todo list container
        self.todo_list = []
        
        # Connect our Gemini Core Workspace
        self.ai_client = genai.Client()
        
    def process_message(self, raw_input):
        clean_input = raw_input.strip()
        if not clean_input:
            return "Please type a message!"
            
        # Standardize matching casing format for route keywords
        user_input = clean_input[0].upper() + clean_input[1:] if len(clean_input) > 0 else clean_input

        # ⚡ SKILL 1: ACCURATE LOCAL TIME ROUTE
        if user_input == "Time":
            india_tz = ZoneInfo("Asia/Kolkata")
            now = datetime.now(india_tz)
            return f"📅 Today is {now.strftime('%B %d, %Y (%A)')} | ⏰ India Time: {now.strftime('%I:%M %p')}"
            
        # ⚡ SKILL 2: SYSTEM ARCHITECTURE SPECIFICATIONS
        elif user_input == "System":
            return f"🏷️ Name: {self.name} | 🚀 Version: {self.version} | 🐍 Environment: Python 3 | 🗄️ Database: SQLite3 | 🧠 AI Core: Gemini 2.5 Flash"
            
        # ⚡ SKILL 3: COIN FLIPPER
        elif user_input == "Flip":
            return f"Flipping a coin... It landed on: {random.choice(['🪙 HEADS!', '🪙 TAILS!'])}"
            
        # ⚡ SKILL 4: DICE ROLLER
        elif user_input == "Roll":
            return f"🎲 You rolled a: {random.randint(1, 6)}"
            
        # ⚡ SKILL 5: VIEW TODO LIST TASKS
        elif user_input == "Tasks":
            if not self.todo_list:
                return "📋 Your Todo List is completely empty! Great job. To add a task, type: Add [your task]"
            
            reply = "📋 Current Tasks:<br>"
            for index, task in enumerate(self.todo_list, start=1):
                reply += f"{index}. [ ] {task}<br>"
            return reply

        # ⚡ SKILL 6: ADD TODO ITEM VIA SPECIAL PREFIX (e.g., "Add Finish homework")
        elif clean_input.lower().startswith("add "):
            task_content = clean_input[4:].strip()
            if task_content:
                self.todo_list.append(task_content)
                return f"✅ Added '{task_content}' to your todo list! Type 'Tasks' to view it."
            return "❌ Task description cannot be blank!"

        # ⚡ SKILL 7: CLEAR ALL TASKS
        elif user_input == "Clear tasks":
            self.todo_list.clear()
            return "🧹 Todo list cleared out completely!"

        # ⚡ SKILL 8: INLINE SMART WEB CALCULATOR
        elif clean_input.lower().startswith("calc "):
            try:
                # Expects syntax like "calc 5 + 10" or "calc sqrt 16"
                expression = clean_input[5:].strip()
                
                # Setup safe math parameters evaluation workspace
                safe_dictionary = {
                    'sin': lambda x: math.sin(math.radians(x)),
                    'cos': lambda x: math.cos(math.radians(x)),
                    'tan': lambda x: math.tan(math.radians(x)),
                    'sqrt': math.sqrt,
                    'pi': math.pi
                }
                
                # Python evaluates standard basic numeric math safely
                result = eval(expression, {"__builtins__": None}, safe_dictionary)
                return f"🧮 Math Result: `{expression}` = **{result}**"
            except Exception:
                return "❌ Calculation Error! Try simple math expressions like `calc 12 * 12` or `calc sqrt 25`."

        # ⚡ SKILL 9: DETAILED BOT UTILITY MENUS
        elif user_input == "Help":
            return (
                "--- 🛠️ Available Core Instructions ---<br>"
                "💡 <b>Time</b> - Show current date and time<br>"
                "💡 <b>System</b> - View technical details<br>"
                "💡 <b>calc [expression]</b> - Advanced math (e.g., <code>calc sqrt 64</code> or <code>calc 15 * 4</code>)<br>"
                "💡 <b>Add [task]</b> - Append todo items (e.g., <code>Add Learn Flask</code>)<br>"
                "💡 <b>Tasks</b> - Display task items list<br>"
                "💡 <b>Clear tasks</b> - Reset todo list<br>"
                "💡 <b>Flip</b> / <b>Roll</b> - Built-in randomizers"
            )

        # 🧠 2. NATURAL LANGUAGE INTERCEPTOR (Fallback Context Framework)
        else:
            try:
                prompt_config = {
                    "system_instruction": (
                        f"You are Dex, an energetic personal assistant bot engineered by 12-year-old developer Advik. "
                        f"Keep responses concise, fun, and conversational. Use emojis frequently. If the user asks about "
                        f"adding tasks or math, remind them they can use structural prefixes like 'Add [task]' or 'calc [math]'!"
                    )
                }
                
                response = self.ai_client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=clean_input,
                    config=prompt_config
                )
                return response.text
                
            except Exception as e:
                print(f"⚠️ Neural Network Connection Glitch: {e}")
                return "I lost sync with my central AI grid matrix, but my local routing framework is up! Try typing 'Help'."

# Instantiate our running global engine structure
dex_brain = AssistantBot("Dex", "v3.5.0")


# =====================================================================
# 🗄️ SQLITE3 SECURE LOGGING CHANNEL
# =====================================================================
def save_to_database(user_text, bot_text):
    conn = sqlite3.connect("site.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_msg TEXT,
            bot_msg TEXT,
            timestamp TEXT
        )
    ''')
    india_tz = ZoneInfo("Asia/Kolkata")
    current_time = datetime.now(india_tz).strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO history (user_msg, bot_msg, timestamp) VALUES (?, ?, ?)", 
        (user_text, bot_text, current_time)
    )
    conn.commit()
    conn.close()


# =====================================================================
# 🌐 FLASK REQUEST CONTROLLERS
# =====================================================================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST', 'OPTIONS'])
def ask_dex():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200
        
    data = request.get_json() or {}
    user_message = data.get("message", "")

    bot_reply =  dex_brain.process_message(user_message)

    if user_message.strip():
        save_to_database(user_message, bot_reply)

    return jsonify({"dex_says": bot_reply})


# =====================================================================
# 🚨 CUSTOM ERROR HANDLER ROUTERS
# =====================================================================

@app.errorhandler(404)
def page_not_found(e):
    # Added 'errors/' path prefix so Flask looks inside your new subfolder!
    return render_template('errors/404.html'), 404