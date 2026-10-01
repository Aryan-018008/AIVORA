from flask import Flask, request, jsonify , render_template
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("Groq_API_Key")
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json
    user_input = data.get("message")

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages
    )

    assistant_reply = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return jsonify({
        "reply": assistant_reply
    })


if __name__ == "__main__":
    app.run(debug=True)