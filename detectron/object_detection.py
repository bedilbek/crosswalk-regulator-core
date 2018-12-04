from os import path

import cv2
from uuid import uuid4

from PIL import Image
from pytesseract import image_to_string, Output

from analyzer.analyze_image import analyze_image
from settings import *
from lib.keras_yolo3.yolo import YOLO
import numpy as np

from utils.figures import Point
from utils.make_objects import make_objects


class ObjectDetection(object):

    colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

    def __init__(self, source, region):
        self.yolo = YOLO()
        self.region = region
        self.cap = cv2.VideoCapture(source)
        self.cap.set(cv2.CAP_PROP_FPS, VIDEO_IN_FPS)

    def detect(self):
        processed_frame_counter = 0
        fourcc = cv2.VideoWriter_fourcc(*VIDEO_OUT_CODEC)
        interval_counter = 1
        video_out_settings = [
            '{}{}{}'.format(VIDEO_OUT_PATH, str(interval_counter), VIDEO_OUT_EXTENSION),
            fourcc,
            VIDEO_OUT_FPS,
            VIDEO_OUT_FRAME_SIZE
        ]
        # video_fcc = self.cap.get(cv2.CAP_PROP_FOURCC)
        # video_out_settings[1] = int(video_fcc)
        out = cv2.VideoWriter(*video_out_settings)
        frame_counter = 1
        while True:
            _, frame = self.cap.read()
            if not _:
                if out:
                    out.release()
                    video_out_settings[0] = '{}{}{}'.format(VIDEO_OUT_PATH, str(interval_counter + 1), VIDEO_OUT_EXTENSION)
                    out = cv2.VideoWriter(*video_out_settings)
                break
            image = Image.fromarray(frame)
            # text_image = frame.copy()
            results = self.yolo.detect_image(image)
            data = list()
            for cat, score, tl, br in results:
                top_left_x = tl[0]
                top_left_y = tl[1]
                bottom_right_x = br[0]
                bottom_right_y = br[1]
                label = cat
                datum = (
                label, Point(**{'x': top_left_x, 'y': top_left_y}), Point(**{'x': bottom_right_x, 'y': bottom_right_y}))
                data.append(datum)
                frame = cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), 7)
                frame = cv2.putText(frame, label, (top_left_x, top_left_y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            # Writing object detected frame to disk
            if frame_counter == VIDEO_OUT_INTERVAL:
                if not VIDEO_OUT_FULL:
                    out.release()
                    frame_counter = 0
                    interval_counter += 1
                    video_out_settings[0] = '{}{}{}'.format(VIDEO_OUT_PATH, str(interval_counter), VIDEO_OUT_EXTENSION)
                    out = cv2.VideoWriter(*video_out_settings)
            validation = analyze_image(make_objects(data), self.region)
            if validation:
                # text_image = cv2.resize(text_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
                # text = image_to_string(image=text_image, config=path.join(BASE_DIR, TESSERACT_CONFIG_PATH, 'bazaar'),
                #                      output_type=Output.STRING)
                cv2.putText(frame, "violation: ", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 232, 0), 2)
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
        self.detect()
