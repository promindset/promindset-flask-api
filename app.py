import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    return json.dumps({"message": "Hello World!!!"})
