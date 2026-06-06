"""Hello Flask - Minimal Web Service"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    """Welcome endpoint - returns a friendly JSON message."""
    return jsonify({"message": "Welcome to Hello Flask!"})


@app.route("/health")
def health():
    """Health check endpoint - returns service status."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
