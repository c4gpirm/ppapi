import io
import json
from flask import Flask, request, jsonify
from PIL import Image

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

    bluriness = 3

    sampledata = [
        insects_and_probs,
        bluriness
    ]

    return json.dumps(sampledata)


@app.route("/predict", methods=["POST"])
def predict():
    # ensure an image was properly uploaded to our endpoint
    if request.files.get("image"):
        # read the image in PIL format
        image = request.files["image"].read()
        image = Image.open(io.BytesIO(image))
        return jsonify(image)
    else:
        return 'NOK'
