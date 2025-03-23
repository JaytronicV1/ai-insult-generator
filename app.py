from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/generate_insult', methods=['POST'])
def generate_insult():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a witty insult bot."},
                {"role": "user", "content": "Give me a funny and spicy insult."}
            ],
            temperature=0.95,
            max_tokens=60
        )
        insult = response.choices[0].message['content'].strip()
        return jsonify({'insult': insult})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
