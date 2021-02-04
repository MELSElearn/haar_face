import os
import cv2
import PIL
import io
import numpy as np

from base64 import b64decode, b64encode
from IPython.display import display, Javascript
#from google.colab.output import eval_js
from js2py import eval_js

from flask import Flask, render_template, Response

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@socketio.on('catch-frame')
def catch_frame(data):

    ## getting the data frames

    ## do some processing 

    ## send it back to client
    emit('response_back', data)  ## ??


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1')
