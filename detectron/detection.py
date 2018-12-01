import cv2

from analyzer.analyze_image import analyze_image
from settings import *
from darkflow.net.build import TFNet
import numpy as np

from utils.figures import Point
from utils.make_objects import make_objects


class Detect(object):
    option = {
        'model': os.path.join(BASE_DIR, 'cfg/yolo.cfg'),
        'load': os.path.join(BASE_DIR, 'weights/yolo.weights'),
        'threshold': 0.15,
        'gpu': 1.0
    }

    colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

    def __init__(self, source):
        self.tfnet = TFNet(self.option)
        self.cap = cv2.VideoCapture(source)
        self.cap.set(cv2.CAP_PROP_FPS, 2)

    def detect(self):
        while True:
            _, frame = self.cap.read()
            results = self.tfnet.return_predict(frame)
            data = list()
            for color, result in zip(self.colors, results):
                tl = (result['topleft']['x'], result['topleft']['y'])
                br = (result['bottomright']['x'], result['bottomright']['y'])
                label = result['label']
                datum = (label, Point(**result['topleft']), Point(**result['bottomright']))
                data.append(datum)
                frame = cv2.rectangle(frame, tl, br, color, 7)
                frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            #  checking for violation
            violated = analyze_image(make_objects(data=data))  # Fixme: pass region
            # TODO should be completed for the case of detected violation
            cv2.imshow('frame', frame)
            # print('FPS {:.1f}'.format(1 / (time.time() - stime)))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def start(self):
        while True:
            self.detect()
