import os
import cv2
import PIL
import io

from base64 import b64decode, b64encode
from IPython.display import display, Javascript
from google.colab.output import eval_js

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return "Testing Correct"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)
