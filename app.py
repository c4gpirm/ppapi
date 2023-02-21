from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def hello_api_consumer():
    return "<p>Hello, Api consumer!</p>"

@app.route('/getsampledata', methods=['GET'])
def get_sample_data():
    insects_and_probs = [
        {"type": "WMV", "prob": 89},
        {"type": "WMV", "prob": 89},
        {"type": "WMV", "prob": 89},
        {"type": "WMV", "prob": 89},
        {"type": "WMV", "prob": 89}
    ]

    bluriness = 2

    sampledata = [
        insects_and_probs,
        bluriness
    ]

    return json.dumps(sampledata)