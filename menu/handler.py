# menu/handler.py
import os
import json
from menu.config import DEFAULT_SETTINGS

SETTINGS_FILE = "user_config.json"

def load_user_settings():
    if not os.path.exists(SETTINGS_FILE):
        return DEFAULT_SETTINGS
    try:
        with open(SETTINGS_FILE, "r") as file:
            saved_data = json.load(file)
            return {**DEFAULT_SETTINGS, **saved_data}
    except Exception as err:
        print(f"⚠️ Preferences parser error: {err}")
        return DEFAULT_SETTINGS

def save_user_settings(new_updates: dict):
    try:
        current_config = load_user_settings()
        updated_config = {**current_config, **new_updates}
        with open(SETTINGS_FILE, "w") as file:
            json.dump(updated_config, file, indent=4)
        return {"status": "success", "message": "System configurations updated successfully!"}
    except Exception as err:
        return {"status": "error", "message": f"Settings write failure: {str(err)}"}
