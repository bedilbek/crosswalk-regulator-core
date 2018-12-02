from analyzer.classes.analyze import analyze
from analyzer.classes.objects import Person, Car
from utils.figures import Region, Point

region = Region()
region.add_corner(Point(2, 1))
region.add_corner(Point(10, 1))
region.add_corner(Point(2, 10))
region.add_corner(Point(10, 10))
region.sort()
objects = list()


def testing_left_right():
    """
    testing from left to right with 2 persons and 1 car
    :return:
    """
    p1 = Person(Point(1, 5), Point(2, 5))
    objects.append(p1)
    objects.append(Car(Point(5, 20), Point(7, 10), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(1, 5), Point(2, 5))
    objects.append(p1)
    p2 = Person(Point(3, 5), Point(4, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(4, 5), Point(5, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(5, 5), Point(6, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(6, 5), Point(7, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(7, 5), Point(8, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(8, 5), Point(9, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(10, 5), Point(11, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(11, 5), Point(12, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 7), 'tb'))
    result = analyze(objects, region)
    assert result != []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(11, 5), Point(12, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 15), Point(7, 4), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()


def testing_right_left():
    """
    testing from left to right with 2 persons and 1 car
    :return:
    """
    p1 = Person(Point(10, 5), Point(11, 5))
    objects.append(p1)
    objects.append(Car(Point(5, 20), Point(7, 10), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(9, 5), Point(10, 5))
    objects.append(p1)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(8, 5), Point(9, 5))
    objects.append(p1)
    p2 = Person(Point(10, 5), Point(11, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(7, 5), Point(8, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(6, 5), Point(7, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(5, 5), Point(6, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(4, 5), Point(5, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(3, 5), Point(4, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(2, 5), Point(3, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(1, 5), Point(2, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 9), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()

    p1 = Person(Point(0, 5), Point(1, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 20), Point(7, 7), 'tb'))
    result = analyze(objects, region)
    assert result != []
    objects.clear()

    p1 = Person(Point(0, 5), Point(1, 5))
    objects.append(p1)
    p2 = Person(Point(9, 5), Point(10, 5))
    objects.append(p2)
    objects.append(Car(Point(5, 15), Point(7, 4), 'tb'))
    result = analyze(objects, region)
    assert result == []
    objects.clear()


testing_left_right()
testing_right_left()
