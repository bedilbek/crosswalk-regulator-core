import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VIDEO_PREVIEW = False  # show the video being processed

VIDEO_IN_FPS = 30  # change based on GPU power

VIDEO_OUT_FULL = False
VIDEO_OUT_FPS = 30  # number of frames per second
VIDEO_OUT_INTERVAL = 179      # number of frames
VIDEO_OUT_CODEC = 'XVID'
VIDEO_OUT_EXTENSION = ".avi"
VIDEO_OUT_FRAME_SIZE = (1920, 1080)
VIDEO_OUT_PATH = "out/"
PROCESSED_VIDEO_FRAME_COUNTER_PREVIEW = True


IMAGE_SAMPLES_PATH = "image_samples/"
VIDEO_SAMPLES_PATH = 'video_samples/'
TESSERACT_CONFIG_PATH = 'cfg/tesseract/'

sys.path.append(BASE_DIR)
