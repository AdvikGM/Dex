# app/routes.py
# 🌐 FLASK ROUTE MANAGEMENT - LINKING REAL-TIME AI LANGUAGE SELECTION & WORKSPACE PERSISTENCE

import os
import json
from flask import Blueprint, render_template, request, jsonify, redirect, session
from app.chatbot import dex_brain
from app.models import UserProfile

from menu.handler import load_user_settings, save_user_settings
from menu.config import THEMES, LANGUAGES

main_blueprint = Blueprint('main', __name__)

AUTH_FOLDER = "authentication"
FILE_NAME = os.path.join(AUTH_FOLDER, "users.json")

def load_users():
    if not os.path.exists(AUTH_FOLDER):
        os.makedirs(AUTH_FOLDER)
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_users(users):
    if not os.path.exists(AUTH_FOLDER):
        os.makedirs(AUTH_FOLDER)
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)

@main_blueprint.route('/')
def home_index():
    return render_template('index.html')

@main_blueprint.route('/settings/get', methods=['GET'])
def fetch_runtime_settings():
    return jsonify({
        "current_config": load_user_settings(),
        "available_themes": THEMES,
        "available_languages": LANGUAGES
    })

@main_blueprint.route('/settings/update', methods=['POST'])
def sync_runtime_settings():
    incoming_data = request.get_json() or {}
    result = save_user_settings(incoming_data)
    return jsonify(result)

@main_blueprint.route('/ask', methods=['POST'])
def process_ask_request():
    payload = request.get_json() or {}
    user_msg = payload.get("message", "")
    img_data = payload.get("image_data", None)
    selected_model = payload.get("model", "gemini-2.5-flash")
    
    # Read the user's preferred language directly out of config backend data storage
    current_settings = load_user_settings()
    target_lang_code = current_settings.get("selected_language", "en")

    if user_msg.lower().startswith("generate image:"):
        image_prompt = user_msg[15:].strip()
        rendered_src = dex_brain.generate_image_asset(image_prompt)
        if rendered_src == "ERROR":
            return jsonify({"dex_says": "❌ Critical Visual Generation Pipeline Failure."})
        return jsonify({"dex_says": f"🎨 **Generated Image Grid:**\n\n<img src='{rendered_src}' class='chat-img-render'/>"})

    dex_brain.extract_new_facts(user_msg)
    
    # Pass the language code directly into the chatbot processing loop
    bot_reply = dex_brain.process_message(
        raw_input=user_msg,
        model_target=selected_model,
        image_base64=img_data,
        lang_code=target_lang_code
    )
    return jsonify({"dex_says": bot_reply})

@main_blueprint.route('/register', methods=['POST'])
def web_register_user():
    payload = request.get_json() or {}
    username = payload.get("username", "").strip()
    password = payload.get("password", "").strip()
    email = payload.get("email", "").strip()

    if not username or not password or not email:
        return jsonify({"status": "error", "message": "All fields required!"}), 400

    users = load_users()
    if username in users:
        return jsonify({"status": "error", "message": "Username already exists!"}), 400

    new_user_instance = UserProfile(username=username, password_raw=password, email=email)
    users[username] = new_user_instance.to_dict()
    save_users(users)
    return jsonify({"status": "success", "message": "Registration complete!"})

@main_blueprint.route('/login', methods=['POST'])
def web_login_user():
    payload = request.get_json() or {}
    username = payload.get("username", "").strip()
    password = payload.get("password", "").strip()

    users = load_users()
    if username not in users:
        return jsonify({"status": "error", "message": "Profile identity keys not found."}), 400

    hashed_entry = UserProfile.hash_string_data(password)
    if users[username]["password"] == hashed_entry:
        session["logged_in_user"] = username
        save_user_settings({"account_display_name": username, "auth_type": "local_account"})
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Incorrect parameters entry."}), 400

@main_blueprint.route('/logout', methods=['POST'])
def web_logout_user():
    session.clear()
    save_user_settings({"account_display_name": "Guest Operator", "auth_type": "guest"})
    return jsonify({"status": "success"})

@main_blueprint.route('/history', methods=['GET'])
def fetch_session_history():
    is_authed = "logged_in_user" in session
    current_user = session.get("logged_in_user", "Guest Operator")
    
    # 🎯 FIX: Pull facts directly out of the upgraded workspace dictionary structure
    active_facts = dex_brain.workspace_db.get("remembered_facts", [])
    
    return jsonify({
        "authenticated": is_authed, 
        "username": current_user, 
        "facts_vault": active_facts
    })
