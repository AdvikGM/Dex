from flask import Flask, render_template, request, jsonify
from chatbot import brain

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/debug', methods=['POST'])
def debug():
    data = request.get_json() or {}
    code = data.get('code', '').strip()
    filename = data.get('filename', 'main.py')
    
    if not code:
        return jsonify({'error': 'No code provided'}), 400
    
    result = brain.analyze_code(code, filename)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)