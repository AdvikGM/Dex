# app/chatbot.py
# 🧠 DEX MULTI-SKILL AI COGNITIVE CORE ENGINE

import random
import math
from datetime import datetime
from zoneinfo import ZoneInfo
from google import genai

class AssistantBot:
    def __init__(self, name):
        self.name = name
        self.todo_list = []
        # Automatically connects using the GEMINI_API_KEY from your root .env file
        self.ai_client = genai.Client()
        
    def process_message(self, raw_input, history_context="No previous history available."):
        clean_input = raw_input.strip()
        if not clean_input:
            return "Please type a message!"
            
        # Standardize phrasing format for main structural keyword routing
        user_input = clean_input[0].upper() + clean_input[1:] if len(clean_input) > 0 else clean_input

        # ⚡ SKILL 1: LOCAL TIME ROUTE
        if user_input == "Time":
            india_tz = ZoneInfo("Asia/Kolkata")
            now = datetime.now(india_tz)
            return f"📅 Today is {now.strftime('%B %d, %Y (%A)')} | ⏰ India Time: {now.strftime('%I:%M %p')}"
            
        # ⚡ SKILL 2: SYSTEM ARCHITECTURE SPECIFICATIONS
        elif user_input == "System":
            return f"🏷️ Name: {self.name} | 🐍 Environment: Python 3 | 🗄️ Database: SQLite3 (SQLAlchemy) | 🧠 AI Core: Gemini 2.0 Flash (Traffic Bypass Mode)"
            
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

        # ⚡ SKILL 6: ADD TODO ITEM VIA SPECIAL PREFIX
        elif clean_input.lower().startswith("add "):
            task_content = clean_input[4:].strip()
            if task_content:
                self.todo_list.append(task_content)
                return f"✅ Added '{task_content}' to your todo list! Type 'Tasks' to view it."
            return "❌ Task description cannot be blank!"

        # ⚡ SKILL 7: SMART TASK ERASER (Done Command)
        elif clean_input.lower().startswith("done "):
            try:
                task_index = int(clean_input[5:].strip()) - 1
                if 0 <= task_index < len(self.todo_list):
                    removed_task = self.todo_list.pop(task_index)
                    return f"🔥 Task Scratch-Off! Marked **'{removed_task}'** as complete. Type 'Tasks' to view remaining chores."
                else:
                    return f"❌ System Error: Task position #{task_index + 1} does not exist in your active matrix!"
            except ValueError:
                return "❌ Input Error: Please provide a valid task number integer. Example: `Done 1`."

        # ⚡ SKILL 8: CLEAR ALL TASKS
        elif user_input == "Clear tasks":
            self.todo_list.clear()
            return "🧹 Todo list cleared out completely!"

        # ⚡ SKILL 9: INLINE SMART WEB CALCULATOR
        elif clean_input.lower().startswith("calc "):
            try:
                expression = clean_input[5:].strip()
                safe_dictionary = {
                    'sin': lambda x: math.sin(math.radians(x)),
                    'cos': lambda x: math.cos(math.radians(x)),
                    'tan': lambda x: math.tan(math.radians(x)),
                    'sqrt': math.sqrt,
                    'pi': math.pi
                }
                result = eval(expression, {"__builtins__": None}, safe_dictionary)
                return f"🧮 Math Result: `{expression}` = **{result}**"
            except Exception:
                return "❌ Calculation Error! Try simple expressions like `calc 12 * 12`."

        # ⚡ SKILL 10: DETAILED BOT UTILITY MENUS
        elif user_input == "Help":
            return (
                "--- 🛠️ Available Core Instructions ---<br>"
                "💡 <b>Time</b> - Show current date and time<br>"
                "💡 <b>System</b> - View technical details<br>"
                "💡 <b>calc [expression]</b> - Advanced math (e.g., <code>calc sqrt 64</code>)<br>"
                "💡 <b>Add [task]</b> - Append todo items<br>"
                "💡 <b>Tasks</b> - Display task items list<br>"
                "💡 <b>Done [number]</b> - Clear a single task (e.g., <code>Done 1</code>)<br>"
                "💡 <b>Clear tasks</b> - Reset todo list<br>"
                "💡 <b>Flip</b> / <b>Roll</b> - Built-in randomizers"
            )

        # 🧠 NATURAL LANGUAGE INTERCEPTOR VIA GEMINI 2.0 FLASH
        else:
            try:
                prompt_config = {
                    "system_instruction": (
                        f"You are Dex, an energetic personal assistant bot engineered by 12-year-old developer Advik. "
                        f"Keep responses concise, fun, and conversational. Use emojis frequently. If the user asks about "
                        f"adding tasks or math, remind them they can use structural prefixes like 'Add [task]' or 'calc [math]'!"
                    )
                }
                
                # 🎯 Routed to the 2.0 network tier to bypass the global 503 traffic spikes
                response = self.ai_client.models.generate_content(
                    model='gemini-2.0-flash', 
                    contents=clean_input,
                    config=prompt_config
                )
                return response.text
                
            except Exception as e:
                print(f"⚠️ Neural Network Connection Glitch: {e}")
                return "I lost sync with my central AI grid matrix, but my local routing framework is up! Try typing 'Help'."

# Expose the master class instance to your routes
dex_brain = AssistantBot("Dex")
