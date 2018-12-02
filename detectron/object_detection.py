from os import path

import cv2
from uuid import uuid4

from analyzer.analyze_image import analyze_image
from settings import *
from darkflow.net.build import TFNet
import numpy as np

from utils.figures import Point
from utils.make_objects import make_objects


class ObjectDetection(object):
    option = {
        'model': os.path.join(BASE_DIR, 'cfg/yolo.cfg'),
        'load': os.path.join(BASE_DIR, 'weights/yolo.weights'),
        'threshold': 0.15,
        'gpu': 1.0
    }

    colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

    def __init__(self, source, region):
        self.tfnet = TFNet(self.option)
        self.region = region
        self.cap = cv2.VideoCapture(source)
        self.cap.set(cv2.CAP_PROP_FPS, 2)

    def detect(self):
        processed_frame_counter = 0
        fourcc = cv2.VideoWriter_fourcc(*VIDEO_OUT_CODEC)
        video_out_settings = [path.join(BASE_DIR, VIDEO_OUT_PATH, str(uuid4()), VIDEO_OUT_EXTENSION), fourcc, VIDEO_OUT_FPS, VIDEO_OUT_FRAME_SIZE]
        out = cv2.VideoWriter(*video_out_settings)
        frame_counter = 0
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
            # Writing object detected frame to disk
            if frame_counter == VIDEO_OUT_INTERVAL:
                out.release()
                frame_counter = 0
                video_out_settings[0] = '{}{}{}'.format(VIDEO_OUT_PATH, uuid4(), VIDEO_OUT_EXTENSION)
                out = cv2.VideoWriter(*video_out_settings)
                out.write(frame)
            else:
                out.write(frame)
            frame_counter += 1
            if PROCESSED_VIDEO_FRAME_COUNTER_PREVIEW:
                processed_frame_counter += 1
                print("{} frames completed".format(processed_frame_counter))
            #  checking for violation
            violated = analyze_image(make_objects(data=data), region=self.region)
            # TODO should be completed for the case of detected violation
            if VIDEO_PREVIEW:
                cv2.imshow('frame', frame)
                # print('FPS {:.1f}'.format(1 / (time.time() - stime)))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    def start(self):
        while True:
            self.detect()
