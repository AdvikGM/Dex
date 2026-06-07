# app/routes.py
# 🌐 WEB FRAMEWORK NETWORK HIGHWAY CONTROLLER

from flask import request, jsonify, render_template
from app import db
from app.models import ChatHistory
from app.chatbot import dex_brain

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
        user_message = data.get("message", "").strip()

        # 🛡️ THE STARTUP SHIELD: If the incoming message is totally blank, stop immediately!
        if not user_message:
            return jsonify({"dex_says": "System Ready. Standing by for instructions... ⚡"})

        # 💾 FEATURE 1: COMPILE LONG-TERM AI DATABASE CONTEXT
        memory_string = ""
        try:
            past_logs = ChatHistory.query.order_by(ChatHistory.id.desc()).limit(5).all()
            for log in reversed(past_logs):
                memory_string += f"User: {log.user_msg}\nDex: {log.bot_msg}\n"
        except Exception as db_err:
            print(f"⚠️ Memory Fetch Warning: {db_err}")
            memory_string = "No previous history logs accessible."

        # Pass context to engine
        bot_reply = dex_brain.process_message(user_message, history_context=memory_string)

        # Securely log transactions into database
        try:
            new_log = ChatHistory(user_msg=user_message, bot_msg=bot_reply)
            db.session.add(new_log)
            db.session.commit()
        except Exception as e:
            print(f"🗄️ Database Write Error: {e}")

        return jsonify({"dex_says": bot_reply})

    # 💾 FEATURE 2: NEW API ENDPOINT FOR DYNAMIC SIDEBAR HISTORY FEED
    @app.route('/history', methods=['GET'])
    def get_history_feed():
        try:
            records = ChatHistory.query.order_by(ChatHistory.id.desc()).limit(4).all()
            feed_list = []
            for item in records:
                feed_list.append({
                    "user": item.user_msg[:25] + "..." if len(item.user_msg) > 25 else item.user_msg,
                    "time": item.timestamp.split(" ")[1][:5]
                })
            return jsonify({"history_feed": feed_list}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404
