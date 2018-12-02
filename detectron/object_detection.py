from os import path

import cv2
from uuid import uuid4

from analyzer.analyze_image import analyze_image
from settings import *
from pydarknet import Detector, Image
import numpy as np

from utils.figures import Point
from utils.make_objects import make_objects


class ObjectDetection(object):

    colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

    def __init__(self, source, region):
        self.net = Detector(bytes("cfg/yolov3.cfg", encoding="utf-8"), bytes("weights/yolov3.weights", encoding="utf-8"), 0,
                   bytes("cfg/coco.data", encoding="utf-8"))
        # self.net = load_net(1, "weights/yolov3.weights", 0)
        # self.meta = load_meta("cfg/coco.data".encode('ascii'))
        self.region = region
        self.cap = cv2.VideoCapture(source)
        self.cap.set(cv2.CAP_PROP_FPS, VIDEO_IN_FPS)

    def detect(self):
        processed_frame_counter = 0
        fourcc = cv2.VideoWriter_fourcc(*VIDEO_OUT_CODEC)
        video_out_settings = [path.join(BASE_DIR, VIDEO_OUT_PATH, str(uuid4()), VIDEO_OUT_EXTENSION), fourcc, VIDEO_OUT_FPS, VIDEO_OUT_FRAME_SIZE]
        out = cv2.VideoWriter(*video_out_settings)
        frame_counter = 0
        while True:
            _, frame = self.cap.read()
            dark_frame = Image(frame)
            results = self.net.detect(dark_frame)
            del dark_frame
            data = list()
            for cat, score, bounds in results:
                x, y, w, h = bounds
                top_left_x = x-w/2
                top_left_y = y-h/2
                bottom_right_x = x+w/2
                bottom_right_y = y+h/2
                label = str(cat.decode("utf-8"))
                datum = (label, Point(**{'x': top_left_x, 'y': top_left_y}), Point(**{'x': bottom_right_x, 'y': bottom_right_y}))
                data.append(datum)
                frame = cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255,0,0), 7)
                frame = cv2.putText(frame, label, (top_left_x, top_left_y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
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
            # violated = analyze_image(make_objects(data=data), region=self.region)
            # TODO should be completed for the case of detected violation
            if VIDEO_PREVIEW:
                cv2.imshow('frame', frame)
                # print('FPS {:.1f}'.format(1 / (time.time() - stime)))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    def start(self):
        while True:
            self.detect()
