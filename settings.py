import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VIDEO_PREVIEW = True  # show the video being processed

VIDEO_IN_FPS = 20  # change based on GPU power

VIDEO_OUT_FULL = True

VIDEO_OUT_FPS = 20  # number of frames per second
VIDEO_OUT_INTERVAL = 100  # number of frames
VIDEO_OUT_CODEC = 'XVID'
VIDEO_OUT_EXTENSION = ".avi"
VIDEO_OUT_FRAME_SIZE = (640, 480)
VIDEO_OUT_PATH = "out/"
PROCESSED_VIDEO_FRAME_COUNTER_PREVIEW = True


IMAGE_SAMPLES_PATH = "image_samples/"
VIDEO_SAMPLES_PATH = 'video_samples/'
TESSERACT_CONFIG_PATH = 'cfg/tesseract/'

sys.path.append(BASE_DIR)
