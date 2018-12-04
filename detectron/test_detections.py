import numpy as np

from analyzer.classes.objects import Person, Car
from detectron.region_detection import RegionDetection
from utils.figures import Point
from utils.make_objects import make_objects
from settings import *
from os import path
from pytesseract import image_to_string, Output
import cv2


def test_make_objects_for_analysis():
    data = (
        ('person', Point(**{'x': 1, 'y': 3}), Point(**{'x': 3, 'y': 23})),
        ('car', Point(**{'x': 22, 'y': 42}), Point(**{'x': 12, 'y': 36})),
        ('person', Point(**{'x': 11, 'y': 37}), Point(**{'x': 16, 'y': 41})),
        ('dummy', Point(**{'x': 13, 'y': 43}), Point(**{'x': 51, 'y': 17})),
        ('car', Point(**{'x': 15, 'y': 32}), Point(**{'x': 81, 'y': 99}))
    )

    object_list = make_objects(data)

    assert len(object_list) == 4

    assert isinstance(object_list[0], Person)
    assert isinstance(object_list[3], Car)


def test_region_detection():
    region_detection = RegionDetection(0)
    region = region_detection.detect_region()


def tes_object_detection():
    pass


def test_text_detection():
    image_file = path.join(BASE_DIR, IMAGE_SAMPLES_PATH, "license_plate.png")
    image = cv2.imread(image_file, 0)
    assert image is not None, '{} imaga file should exist in that given path to run test'.format(image_file)
    # rescale image for 300dpi
    image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    # remove some noise
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    text = image_to_string(image=image, config=path.join(BASE_DIR, TESSERACT_CONFIG_PATH, 'bazaar'),
                           output_type=Output.DICT)
    assert text is not None


# test_make_objects_for_analysis()
# tes_object_detection()
# test_region_detection()
test_text_detection()

print("Test successfully finished")
