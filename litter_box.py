"""Litter box service"""
from flask import Flask, jsonify

# App
app = Flask(__name__)

@app.route("/healthz")
def healthz():
    """Healthz API"""
    return jsonify({'status': 'success', 'message': 'OK'}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
