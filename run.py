from detectron.object_detection import ObjectDetection
from detectron.region_detection import RegionDetection
from os import path
from settings import *

url = path.join(BASE_DIR, VIDEO_SAMPLES_PATH, 'out_next.mp4')
region_detection = RegionDetection(url)
region = region_detection.detect_region()

object_detection = ObjectDetection(source=url, region=region)

object_detection.start()
