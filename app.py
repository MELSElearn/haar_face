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
from flask_socketio import SocketIO, emit

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

@socketio.on('image')
def image(data_image):
    sbuf = StringIO()
    sbuf.write(data_image)

    # decode and convert into image
    b = io.BytesIO(base64.b64decode(data_image))
    pimg = Image.open(b)

    ## converting RGB to BGR, as opencv standards
    frame = cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

    # Process the image frame
    frame = imutils.resize(frame, width=700)
    frame = cv2.flip(frame, 1)
    imgencode = cv2.imencode('.jpg', frame)[1]

    # base64 encode
    stringData = base64.b64encode(imgencode).decode('utf-8')
    b64_src = 'data:image/jpg;base64,'
    stringData = b64_src + stringData

    # emit the frame back
    emit('response_back', stringData)
    
if __name__ == '__main__':
    socketio.run(app)
