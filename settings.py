import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VIDEO_PREVIEW = False  # show the video being processed
VIDEO_OUT_FPS = 20  # number of frames per second
VIDEO_OUT_INTERVAL = 40  # number of frames
VIDEO_OUT_CODEC = 'XVID'
VIDEO_OUT_EXTENSION = ".avi"
VIDEO_OUT_FRAME_SIZE = (640, 480)
VIDEO_OUT_PATH = "out/"
PROCESSED_VIDEO_FRAME_COUNTER_PREVIEW = True


IMAGE_SAMPLES_PATH = "image_samples/"
TESSERACT_CONFIG_PATH = 'cfg/tesseract/'

sys.path.append(BASE_DIR)
