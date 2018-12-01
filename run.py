from detectron.object_detection import ObjectDetection
from detectron.region_detection import RegionDetection

url = 0
region_detection = RegionDetection(url)
region = region_detection.detect_region()

object_detection = ObjectDetection(source=url, region=region)

object_detection.start()
