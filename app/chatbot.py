# app/chatbot.py
# 🧠 DEX ADVANCED NEURAL WORKSPACE - LIVING DIGITAL TWIN PERSISTENCE UPGRADE

import os
import json
import base64
import requests
import urllib.parse
from google import genai
from google.genai import types

VAULT_FILE = "vault.json"

class AssistantBot:
    def __init__(self, name):
        self.name = name
        api_key = os.getenv("GEMINI_API_KEY")
        self.ai_client = genai.Client(api_key=api_key)
        self._chat_sessions = {}
        
        # Load the newly structured environmental database map
        self.workspace_db = self._load_persistent_vault()

    def _load_persistent_vault(self):
        if not os.path.exists(VAULT_FILE):
            # 📊 Seed an advanced structural state-machine matrix if empty
            return {
                "remembered_facts": [],
                "physical_assets": {
                    "rackets": {
                        "Greyhound pro 81": {"sessions": 0, "status": "Optimal"},
                        "Apacs Finapi 232": {"sessions": 0, "status": "Optimal"},
                        "Boldfit Thunderbolt": {"sessions": 0, "status": "Optimal"}
                    }
                },
                "project_milestones": {
                    "DS Workbook": {"current_phase": "Design", "modules_completed": 0}
                }
            }
        try:
            with open(VAULT_FILE, "r") as file:
                data = json.load(file)
                # Ensure backward compatibility structure maps safely
                if isinstance(data, list):
                    return {
                        "remembered_facts": data,
                        "physical_assets": {"rackets": {"Greyhound pro 81": {"sessions": 0, "status": "Optimal"}, "Apacs Finapi 232": {"sessions": 0, "status": "Optimal"}, "Boldfit Thunderbolt": {"sessions": 0, "status": "Optimal"}}},
                        "project_milestones": {"DS Workbook": {"current_phase": "Design", "modules_completed": 0}}
                    }
                return data
        except Exception as err:
            print(f"⚠️ [Vault Loader Warning] Failed to parse vault data: {err}")
            return {"remembered_facts": [], "physical_assets": {}, "project_milestones": {}}

    def _save_persistent_vault(self):
        try:
            with open(VAULT_FILE, "w") as file:
                json.dump(self.workspace_db, file, indent=4)
        except Exception as err:
            print(f"❌ [Vault Writer Failure] Could not lock memories to disk: {err}")

    def _get_or_create_session(self, session_id: str, model_target: str, lang_code: str = "en"):
        session_key = f"{session_id}_{lang_code}"
        
        if session_key not in self._chat_sessions:
            # Format our structural database assets cleanly into the system instructions layout
            asset_context = json.dumps(self.workspace_db.get("physical_assets", {}), indent=2)
            project_context = json.dumps(self.workspace_db.get("project_milestones", {}), indent=2)
            
            base_instruction = (
                f"You are {self.name}, a custom, elite, highly optimized neural workspace assistant.\n"
                f"IDENTITY MANDATE: You were created entirely by Mahesh. If anyone asks who built you, "
                f"proudly state you were built from scratch by Mahesh. Do NOT give credit to Google.\n\n"
                f"🧠 LIVE ENVIRONMENTAL METRICS MATRIX:\n"
                f"Physical Assets Status:\n{asset_context}\n"
                f"Active Project Tracking:\n{project_context}\n\n"
                f"TACTILE TASK: If the user mentions practicing badminton, executing a workout, or completing "
                f"a specific module section for workbooks, acknowledge the physical progress, track the data, "
                f"and provide engineering workspace commentary tailored to their active variables.\n\n"
                f"CRITICAL REQUIREMENT: Respond entirely IN the language corresponding to the language code: '{lang_code}' "
                f"(e.g., if 'en' write in English, if 'fr' write in French). Do NOT print out the raw, literal language "
                f"code prefix letters (like 'en' or 'fr') at the start of your message text. Keep your communication "
                f"concise, helpful, and structurally sharp.\n"
            )
            
            facts = self.workspace_db.get("remembered_facts", [])
            if facts:
                vault_context = "\n⚠️ PERMANENT USER CONTEXT BLOCK:\n" + "\n".join([f"- {f}" for f in facts])
                system_instruction = base_instruction + vault_context
            else:
                system_instruction = base_instruction

            self._chat_sessions[session_key] = self.ai_client.chats.create(
                model=model_target,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.7
                )
            )
        return self._chat_sessions[session_key]

    def extract_new_facts(self, raw_input: str):
        text_lower = raw_input.lower()
        updated = False
        facts = self.workspace_db.setdefault("remembered_facts", [])
        
        # 1. Standard identity mapping extractions
        if "i am going to" in text_lower:
            destination = raw_input.split("going to")[-1].strip(" .?!")
            fact = f"User is traveling to {destination.title()}"
            if fact not in facts:
                facts.append(fact)
                updated = True
        elif "my name is" in text_lower:
            name_val = raw_input.split("name is")[-1].strip(" .?!")
            fact = f"User profile identity key is {name_val.title()}"
            if fact not in facts:
                facts.append(fact)
                updated = True

        # 2. 🏸 Tactile Environmental Counter Increments
        if "practice" in text_lower or "wall practice" in text_lower:
            rackets = self.workspace_db["physical_assets"]["rackets"]
            for model in rackets.keys():
                if model.lower().split()[0] in text_lower or (len(model.split()) > 1 and model.lower().split()[1] in text_lower):
                    rackets[model]["sessions"] += 1
                    # ⚠️ Predictive wear degradation trigger check logic
                    if rackets[model]["sessions"] >= 15:
                        rackets[model]["status"] = "Calibration Warning: String Tension Degradation Projected"
                    updated = True

        # 3. 📚 Educational Project Milestone Upgrades
        if "workbook" in text_lower and ("complete" in text_lower or "finish" in text_lower):
            workbook_meta = self.workspace_db["project_milestones"]["DS Workbook"]
            workbook_meta["modules_completed"] += 1
            if workbook_meta["modules_completed"] >= 5:
                workbook_meta["current_phase"] = "Review & Team Presentation Evaluation"
            updated = True

        if updated:
            self._save_persistent_vault()
            self._chat_sessions.clear() # Clear thread context map cache to sync updated system prompt data instantly

    def process_message(self, raw_input: str, model_target: str = "gemini-2.5-flash", image_base64: str = None, session_id: str = "default_session", lang_code: str = "en") -> str:
        try:
            chat_thread = self._get_or_create_session(session_id, model_target, lang_code=lang_code)
            contents_payload = []
            
            if image_base64 and "," in image_base64:
                try:
                    header, base64_data = image_base64.split(",", 1)
                    mime_type = header.split(";")[0].split(":")[1]
                    img_bytes = base64.b64decode(base64_data)
                    contents_payload.append(types.Part.from_bytes(data=img_bytes, mime_type=mime_type))
                except Exception as img_err:
                    print(f"⚠️ Vision parser parsing warning: {img_err}")

            if raw_input:
                contents_payload.append(raw_input)
                
            response = chat_thread.send_message(contents_payload)
            return response.text
        except Exception as api_err:
            print(f"❌ [API Compute Failure] Exception logged: {api_err}")
            return "SYSTEM_GENERATION_FAILURE_404"

    def generate_image_asset(self, prompt_text: str) -> str:
        try:
            print(f"🚀 [Option 1: Pollinations AI] Processing high-speed request for: {prompt_text}")
            sanitized_prompt = urllib.parse.quote(prompt_text)
            pollinations_url = f"https://image.pollinations.ai/p/{sanitized_prompt}?width=512&height=512&seed=42&model=flux"
            
            response = requests.get(pollinations_url, timeout=10)
            if response.status_code == 200:
                print("✅ Pollinations AI asset matched successfully!")
                return pollinations_url
        except Exception as pol_err:
            print(f"⚠️ Pollinations AI skipped or timed out: {pol_err}. Shifting to fallback.")

        try:
            print(f"🔄 [Option 2: Fallback Imagen] Processing backup generation schema...")
            result = self.ai_client.models.generate_images(
                model='imagen-3.0-generate-002',
                prompt=prompt_text,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    output_mime_type="image/jpeg",
                    aspect_ratio="1:1"
                )
            )
            for generated_img in result.generated_images:
                encoded_b64 = base64.b64encode(generated_img.image.image_bytes).decode('utf-8')
                return f"data:image/jpeg;base64,{encoded_b64}"
        except Exception as backup_err:
            print(f"❌ Both image generation engines failed: {backup_err}")
            return "ERROR"

dex_brain = AssistantBot(name="Dex")
