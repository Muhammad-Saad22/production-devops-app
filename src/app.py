from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Production DevOps App")
APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Production DevOps App",
        "app": APP_NAME,
        "environment": APP_ENV
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/ready")
def ready():
    return jsonify({
        "status": "ready"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
