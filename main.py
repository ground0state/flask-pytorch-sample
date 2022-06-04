import base64
import json
from io import BytesIO


from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image


from model import Predictor

app = Flask(__name__)
CORS(app)

predictor = Predictor('imagenet_class_index.json')


@app.route("/", methods=["POST"])
def predict():
    data = request.data.decode('utf-8')
    data = json.loads(data)

    img_stream = base64.b64decode(data['image'])
    img_pil = Image.open(BytesIO(img_stream))
    idx, label = predictor.predict(img_pil)

    response = {'result': label}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
