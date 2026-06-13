# app/chatbot.py
# 🧠 DEX MULTI-SKILL ENGINE + DYNAMIC CHANNELS FOR TEXT & IMAGE PIPELINES

import random
import math
import base64
import json
import os       
import requests 
import urllib.parse 
from datetime import datetime
from zoneinfo import ZoneInfo
from google import genai
from google.genai import types

class AssistantBot:
    def __init__(self, name):
        self.name = name
        self.todo_list = []
        self.ai_client = genai.Client()
        
    def process_message(self, raw_input, history_context="No history.", model_target="gemini-2.5-flash", image_base64=None, permanent_facts=""):
        clean_input = raw_input.strip()
        
        if image_base64 and (image_base64.strip() == "" or ("base64," in image_base64 and len(image_base64.split(",")[1]) == 0)):
            image_base64 = None
        
        if not clean_input and image_base64:
            clean_input = "Describe this image in detail."
        elif not clean_input and not image_base64:
            return "Please type a message, upload a picture, or say 'draw [something]'!"
            
        user_input = clean_input[0].upper() + clean_input[1:] if len(clean_input) > 0 else clean_input

        # ⚡ LOCAL CORE ROUTING SKILLS
        if user_input == "Time" and not image_base64:
            india_tz = ZoneInfo("Asia/Kolkata")
            now = datetime.now(india_tz)
            return f"📅 Today is {now.strftime('%B %d, %Y (%A)')} | ⏰ India Time: {now.strftime('%I:%M %p')}"
            
        elif user_input == "System" and not image_base64:
            return f"🏷️ Name: {self.name} | 🐍 Environment: Python 3 | 🗄️ Database: SQLite3 (Dynamic Fact Extractor) | 🧠 AI Core: {model_target.upper()}"
            
        elif user_input == "Flip" and not image_base64:
            return f"Flipping a coin... It landed on: {random.choice(['🪙 HEADS!', '🪙 TAILS!'])}"
            
        elif user_input == "Roll" and not image_base64:
            return f"🎲 You rolled a: {random.randint(1, 6)}"
            
        elif user_input == "Tasks" and not image_base64:
            if not self.todo_list: return "📋 Your Todo List is completely empty!"
            reply = "📋 Current Tasks:<br>"
            for index, task in enumerate(self.todo_list, start=1): reply += f"{index}. [ ] {task}<br>"
            return reply
            
        elif clean_input.lower().startswith("add ") and not image_base64:
            task_content = clean_input[4:].strip()
            if task_content:
                self.todo_list.append(task_content)
                return f"✅ Added '{task_content}' to your todo list! Type 'Tasks' to view it."
            return "❌ Task description cannot be blank!"
            
        elif clean_input.lower().startswith("done ") and not image_base64:
            try:
                task_index = int(clean_input[5:].strip()) - 1
                if 0 <= task_index < len(self.todo_list):
                    removed_task = self.todo_list.pop(task_index)
                    return f"🔥 Task Scratch-Off! Marked **'{removed_task}'** as complete."
                else: return f"❌ System Error: Task position #{task_index + 1} does not exist!"
            except ValueError: return "❌ Input Error: Please provide a valid task number integer."
            
        elif user_input == "Clear tasks" and not image_base64:
            self.todo_list.clear()
            return "🧹 Todo list cleared out completely!"
            
        elif clean_input.lower().startswith("calc ") and not image_base64:
            try:
                expression = clean_input[5:].strip()
                safe_dictionary = {'sin': lambda x: math.sin(math.radians(x)), 'cos': lambda x: math.cos(math.radians(x)), 'tan': lambda x: math.tan(math.radians(x)), 'sqrt': math.sqrt, 'pi': math.pi}
                result = eval(expression, {"__builtins__": None}, safe_dictionary)
                return f"🧮 Math Result: `{expression}` = **{result}**"
            except Exception: return "❌ Calculation Error! Try simple expressions like `calc 12 * 12`."
            
        elif user_input == "Help" and not image_base64:
            return "--- 🛠️ Core Instructions ---<br>💡 <b>Time</b> // <b>System</b> // <b>Tasks</b><br>💡 <b>draw [art description]</b> - Generate AI photos!<br>🧠 <i>Dex is scanning your chats to learn permanent facts about you live!</i>"

        # 🎨 DUAL-ENGINE AI IMAGE PIPELINE WITH FRONT-END ERROR FLAG SIGNALING
        elif clean_input.lower().startswith("draw ") and not image_base64:
            art_prompt = clean_input[5:].strip()
            if not art_prompt: return "❌ Please specify what you want me to create!"
            
            encoded_prompt = urllib.parse.quote(art_prompt)
            current_seed = random.randint(1, 9999999)
            
            # --- 🚀 GENERATOR 1: PRIMARY ENGINE ---
            try:
                print(f"🚀 [Generator Primary] Accessing Turbo Realism Engine...")
                primary_url = f"https://image.pollinations.ai/p/{encoded_prompt}?width=512&height=512&model=turbo&seed={current_seed}"
                
                img_response = requests.get(primary_url, timeout=6)
                if img_response.status_code == 200 and len(img_response.content) > 5000:
                    base64_data = base64.b64encode(img_response.content).decode('utf-8')
                    return f"🔮 <b>Art Core (Primary Engine Active):</b> '{art_prompt}'<br><img src='data:image/jpeg;base64,{base64_data}' class='chat-img-render' style='border-radius: 8px; margin-top: 10px; max-width: 100%;'>"
                else:
                    raise RuntimeError()
                    
            # --- 🔄 GENERATOR 2: CLOUD BACKUP ENGINE ---
            except Exception:
                try:
                    print(f"🔄 [Generator Backup] Swapping traffic over to Aurora Engine...")
                    backup_url = f"https://image.pollinations.ai/p/{encoded_prompt}?width=512&height=512&model=aurora&seed={current_seed}"
                    
                    img_response = requests.get(backup_url, timeout=6)
                    if img_response.status_code == 200 and len(img_response.content) > 5000:
                        base64_data = base64.b64encode(img_response.content).decode('utf-8')
                        return f"🔮 <b>Art Core (Backup Engine Active):</b> '{art_prompt}'<br><img src='data:image/jpeg;base64,{base64_data}' class='chat-img-render' style='border-radius: 8px; margin-top: 10px; max-width: 100%;'>"
                    else:
                        raise RuntimeError()
                    
                # --- 🛑 TRIGGER POP-UP DETECTOR AT FRONT-END ---
                except Exception:
                    print(f"⚠️ [Detector Active] All generation sources exhausted. Sending pop-up flag...")
                    return "SYSTEM_GENERATION_FAILURE_404"

        # 🧠 COGNITIVE MULTI-MODAL CHAT INTERCEPTOR
        else:
            try:
                prompt_config = {
                    "system_instruction": (
                        f"You are Dex, an energetic personal assistant bot engineered by developer Advik. "
                        f"Keep responses concise, fun, and conversational with emojis.\n\n"
                        f"⚡ CRITICAL SYSTEM INFO: Here are permanent facts you have memorized about the user. "
                        f"Always remember these facts across all chat sessions:\n"
                        f"=== PERMANENT FACT SHEET VAULT ===\n{permanent_facts}\n===================================\n\n"
                        f"=== ACTIVE SESSION THREAD HISTORY ===\n{history_context}\n====================================="
                    )
                }
                
                contents_payload = []
                if image_base64:
                    if "," in image_base64: image_base64 = image_base64.split(",")[1]
                    raw_image_bytes = base64.b64decode(image_base64)
                    image_part = types.Part.from_bytes(data=raw_image_bytes, mime_type="image/jpeg")
                    contents_payload.append(image_part)
                
                contents_payload.append(clean_input)
                
                response = self.ai_client.models.generate_content(
                    model=model_target, contents=contents_payload, config=prompt_config
                )
                return response.text
            except Exception as e:
                print(f"⚠️ Neural Network Connection Glitch: {repr(e)}")
                return "I lost sync with my central AI grid matrix, but my local routing framework is up! Try typing 'Help'."

    # 🔬 THE FACT EXTRACTOR ENGINE
    def extract_new_facts(self, user_msg):
        try:
            extraction_prompt = (
                f"Analyze the following incoming user message: '{user_msg}'.\n"
                f"Determine if the user is sharing a definitive, permanent personal fact about themselves, "
                f"their hobbies, favorites, family, or equipment.\n\n"
                f"If they ARE sharing a permanent personal fact, extract it as a single concise bullet-point sentence "
                f"written from a third-person perspective (e.g., 'User's dog is named Bruno').\n"
                f"Return the response in strict JSON format like this: {{\"fact_found\": true, \"fact\": \"concise sentence\"}}.\n"
                f"If no meaningful permanent personal fact is found, return exactly: {{\"fact_found\": false, \"fact\": \"\"}}."
            )
            response = self.ai_client.models.generate_content(
                model='gemini-2.5-flash',
                contents=extraction_prompt,
                config={"response_mime_type": "application/json"}
            )
            data = json.loads(response.text)
            if data.get("fact_found") and data.get("fact"):
                return data["fact"].strip()
            return None
        except Exception as e:
            print(f"🔬 Fact Vault Synchronization Standby (Google Cloud high load): {e}")
            return None

dex_brain = AssistantBot("Dex")
