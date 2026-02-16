from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

MODEL_BASE = "https://painful-brit-university24-63a5a91e.koyeb.app"
MODEL_PATH = "/chat"  # Change if needed

@app.route("/api/chat", methods=["POST"])
def proxy_chat():
    payload = request.json or {}

    url = MODEL_BASE.rstrip("/") + MODEL_PATH

    headers = {
        "Content-Type": "application/json"
    }

    # If your model requires auth:
    # headers["Authorization"] = "Bearer YOUR_SECRET_KEY"

    response = requests.post(url, json=payload, headers=headers, timeout=60)

    return Response(
        response.content,
        status=response.status_code,
        content_type=response.headers.get("Content-Type")
    )

if __name__ == "__main__":
    app.run(port=8000)
