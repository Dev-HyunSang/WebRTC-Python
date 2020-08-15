from simple_websocket_server import WebSocketServer, WebSocket
import base64
from cv2 import cv2
import numpy as np
import warnings
warnings.simplefilter('ignore', DeprecationWarning)

# OPENCV PYTHON RECORING / 개발 중...
capture = cv2.VideoCapture("/image/Recording.mpy");
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

class SimpleEcho(WebSocket):
    def handle(self):
        msg = self.data
        img = cv2.imdecode(np.fromstring(base64.b64decode(msg.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('image', img)
        cv2.waitKey(1)

    def connected(self):
        print(self.address, 'Connected')
    
    def handle_close(self):
        print(self.address, 'Closed')

server = WebSocketServer('localhost', 3000, SimpleEcho)
server.serve_forever()