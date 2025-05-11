from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # Cho phép tất cả origin, hoặc bạn có thể giới hạn domain

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
