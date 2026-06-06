from flask import request, jsonify, render_template
from app import db
from models import ChatHistory
from chatbot import dex_brain

def configure_routes(app):

    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        return response

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/ask', methods=['POST', 'OPTIONS'])
    def ask_dex():
        if request.method == 'OPTIONS':
            return jsonify({"status": "ok"}), 200
            
        data = request.get_json() or {}
        user_message = data.get("message", "")

        # Process the message through the chatbot brain module
        bot_reply = dex_brain.process_message(user_message)

        # Securely log into the database using our Model
        if user_message.strip():
            try:
                new_log = ChatHistory(user_msg=user_message, bot_msg=bot_reply)
                db.session.add(new_log)
                db.session.commit()
            except Exception as e:
                print(f"🗄️ Database Error: {e}")

        return jsonify({"dex_says": bot_reply})

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404
