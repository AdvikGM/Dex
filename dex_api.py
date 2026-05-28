from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Our simple memory database
chat_data = {
    "Hello": ["Hey there!", "Hi! Ready to chat?", "Hello!"],
    "Sad": ["I'm sorry to hear that. Sending a virtual hug! 🤗", "Cheer up!"],
}

# The main API endpoint (The drive-thru window)
@app.route('/ask', methods=['POST'])
def ask_dex():
    # 1. Take the incoming data from the user
    user_data = request.get_json()
    user_message = user_data.get("message")

    # 2. Check our memory database for an answer
    if user_message in chat_data:
        reply = random.choice(chat_data[user_message])
    else:
        reply = "I don't know that word yet, but I am learning!"

    # 3. Send the answer back to the user
    return jsonify({"dex_says": reply})

if __name__ == '__main__':
    app.run(debug=True)
