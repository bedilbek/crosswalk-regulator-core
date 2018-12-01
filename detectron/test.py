from analyzer.classes.objects import Person, Car
from detectron.region_detection import RegionDetection
from utils.figures import Point
from utils.make_objects import make_objects

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

region_detection = RegionDetection(0)
region = region_detection.detect_region()


print("Test successfully finished")
