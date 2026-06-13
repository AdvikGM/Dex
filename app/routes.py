# app/routes.py
# 🌐 HIGHWAY CONTROLLER WITH SECURITY ENFORCEMENT & USAGE AUDITING

from flask import request, jsonify, render_template, session
from app import db
from app.models import ChatHistory, UserFact, User, PromptCounter
from app.chatbot import dex_brain
import hashlib

def configure_routes(app):
    # Set a secure secret key for session cookies tracking
    app.secret_key = "dex_system_core_secret_matrix_key"

    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        return response

    @app.route('/')
    def home():
        # Assign a generic tracking key to guests if they don't have one
        if "guest_token" not in session:
            import uuid
            session["guest_token"] = str(uuid.uuid4())
        return render_template('index.html')

    @app.route('/register', methods=['POST'])
    def register_user():
        data = request.get_json() or {}
        username = data.get("username", "").strip().lower()
        password = data.get("password", "").strip()

        if not username or not password:
            return jsonify({"status": "error", "message": "Username and password required!"}), 400

        existing = User.query.filter_by(username=username).first()
        if existing:
            return jsonify({"status": "error", "message": "Username already exists!"}), 400

        hashed_pass = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(username=username, password_hash=hashed_pass)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"status": "success", "message": "Account created! You can now log in."})

    @app.route('/login', methods=['POST'])
    def login_user():
        data = request.get_json() or {}
        username = data.get("username", "").strip().lower()
        password = data.get("password", "").strip()

        hashed_pass = hashlib.sha256(password.encode()).hexdigest()
        user = User.query.filter_by(username=username, password_hash=hashed_pass).first()

        if user:
            session["logged_in"] = True
            session["username"] = username
            return jsonify({"status": "success", "username": username})
        return jsonify({"status": "error", "message": "Invalid credentials matched."}), 401

    @app.route('/logout', methods=['POST'])
    def logout_user():
        session.pop("logged_in", None)
        session.pop("username", None)
        return jsonify({"status": "success"})

    @app.route('/ask', methods=['POST', 'OPTIONS'])
    def ask_dex():
        if request.method == 'OPTIONS': return jsonify({"status": "ok"}), 200
            
        data = request.get_json() or {}
        user_message = data.get("message", "").strip()
        selected_model = data.get("model", "gemini-2.5-flash")
        uploaded_image = data.get("image_data", None)
        active_session = data.get("session_id", "default_session")

        # 🔐 SECURITY AUDIT STAGE
        is_logged_in = session.get("logged_in", False)
        guest_token = session.get("guest_token", "unknown_guest")
        
        current_usage = 0
        if not is_logged_in:
            tracker = PromptCounter.query.filter_by(visitor_token=guest_token).first()
            if not tracker:
                tracker = PromptCounter(visitor_token=guest_token, count=0)
                db.session.add(tracker)
                db.session.commit()
            
            current_usage = tracker.count
            # Trigger enforcement barrier if prompt count matches or exceeds 10 limits
            if current_usage >= 10:
                return jsonify({
                    "dex_says": "⚠️ <b>System Access Blocked:</b> Free guest tier allotment (10 Prompts Max) has been completely exhausted. Please log in or register an administrative account to open infinite compute loops! ⚡"
                }), 403

        if not user_message and not uploaded_image:
            return jsonify({"dex_says": "System Ready. Standing by for instructions... ⚡"})

        # Increment anonymous consumption counter metrics if user isn't logged in
        if not is_logged_in:
            tracker = PromptCounter.query.filter_by(visitor_token=guest_token).first()
            tracker.count += 1
            db.session.commit()
            current_usage = tracker.count

        # Compile profiles as normal
        fact_matrix_string = ""
        try:
            all_facts = UserFact.query.order_by(UserFact.id.asc()).all()
            for f in all_facts: fact_matrix_string += f"• {f.fact_text}\n"
        except Exception: pass

        memory_string = ""
        try:
            past_logs = ChatHistory.query.filter_by(session_id=active_session).order_by(ChatHistory.id.desc()).limit(5).all()
            for log in reversed(past_logs): memory_string += f"User: {log.user_msg}\nDex: {log.bot_msg}\n"
        except Exception: pass

        bot_reply = dex_brain.process_message(
            user_message, 
            history_context=memory_string, 
            model_target=selected_model,
            image_base64=uploaded_image,
            permanent_facts=fact_matrix_string
        )

        if user_message or uploaded_image:
            try:
                display_msg = user_message if user_message else "🖼️ Sent an Image Attachment"
                new_log = ChatHistory(session_id=active_session, user_msg=display_msg, bot_msg=bot_reply)
                db.session.add(new_log)
                db.session.commit()
            except Exception: pass

        return jsonify({"dex_says": bot_reply, "usage_count": current_usage})

    @app.route('/history', methods=['GET'])
    def get_history_feed():
        active_session = request.args.get("session_id", "default_session")
        try:
            records = ChatHistory.query.filter_by(session_id=active_session).order_by(ChatHistory.id.desc()).limit(4).all()
            feed_list = [{"user": item.user_msg[:25] + "..." if len(item.user_msg) > 25 else item.user_msg, "time": item.timestamp.split(" ")[1][:5]} for item in records]
            
            fact_records = UserFact.query.order_by(UserFact.id.desc()).all()
            fact_list = [f.fact_text for f in fact_records]

            # Return login credentials status flags to client loops
            return jsonify({
                "history_feed": feed_list, 
                "facts_vault": fact_list,
                "authenticated": session.get("logged_in", False),
                "username": session.get("username", "Guest Node")
            }), 200
        except Exception as e: return jsonify({"status": "error", "message": str(e)}), 500
            
