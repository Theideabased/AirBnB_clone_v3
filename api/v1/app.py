#!/usr/bin/python3
"""script that starts Flask web application"""
from flask import Flask, jsonify, json
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(exception):
    """closes the database"""
    storage.close()


@app.errorhandler(404)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST')
    port = os.environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        host = '5000'
    app.run(host, port, threaded=True)
