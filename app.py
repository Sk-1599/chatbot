# app.py
from flask import Flask, request, jsonify
import chatbot

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('query')
    response = chatbot.chatbot(query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
