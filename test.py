from analyzer.classes.analyze import analyze, global_person_list
from analyzer.classes.objects import Person, Car
from utils.figures import Region, Point
from utils.make_objects import make_objects

region = Region()
region.add_corner(Point(2, 1))
region.add_corner(Point(10, 1))
region.add_corner(Point(2, 10))
region.add_corner(Point(10, 10))
region.sort()


def testing_left_right():
    from analyzer.classes.analyze import global_person_list
    global_person_list.clear()
    """
    testing from left to right with 2 persons and 1 car
    :return:
    """
    objects = list()
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
    from analyzer.classes.analyze import global_person_list
    global_person_list.clear()
    """
    testing from left to right with 2 persons and 1 car
    :return:
    """
    objects = list()
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


def testing_right_and_left():
    from analyzer.classes.analyze import global_person_list
    global_person_list.clear()
    """
    testing from left to right with 2 persons and 1 car
    :return:
    """
    data = [
        ['person', Point(1, 4), Point(2, 4)],
        ['car', Point(5, 15), Point(7, 11)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(2, 4), Point(3, 4)],
        ['car', Point(5, 14), Point(7, 10)],
        ['person', Point(11, 5), Point(12, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(2, 4), Point(3, 4)],
        ['car', Point(5, 13), Point(7, 9)],
        ['person', Point(10, 5), Point(11, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(2, 4), Point(3, 4)],
        ['car', Point(5, 12), Point(7, 8)],
        ['person', Point(10, 5), Point(11, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(3, 4), Point(4, 4)],
        ['car', Point(5, 12), Point(7, 8)],
        ['person', Point(9, 5), Point(10, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(5, 4), Point(6, 4)],
        ['car', Point(5, 12), Point(7, 8)],
        ['person', Point(8, 5), Point(9, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(6, 4), Point(7, 4)],
        ['car', Point(5, 12), Point(7, 8)],
        ['car', Point(3, 15), Point(5, 11)],
        ['person', Point(7, 5), Point(8, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(7, 4), Point(8, 4)],
        ['car', Point(5, 12), Point(7, 8)],
        ['car', Point(3, 15), Point(5, 11)],
        ['person', Point(6, 5), Point(7, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(8, 4), Point(9, 4)],
        ['car', Point(5, 12), Point(7, 8)],
        ['car', Point(3, 15), Point(5, 11)],
        ['person', Point(5, 5), Point(6, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(8, 4), Point(9, 4)],
        ['car', Point(5, 12), Point(7, 8)],
        ['car', Point(3, 15), Point(5, 11)],
        ['person', Point(4, 5), Point(5, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(8, 4), Point(9, 4)],
        ['car', Point(5, 12), Point(7, 8)],
        ['car', Point(3, 15), Point(5, 11)],
        ['person', Point(3, 5), Point(4, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result != []

    data = [
        ['person', Point(8, 4), Point(9, 4)],
        ['car', Point(5, 11), Point(7, 7)],
        ['car', Point(3, 14), Point(5, 10)],
        ['person', Point(3, 5), Point(4, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(8, 4), Point(9, 4)],
        ['car', Point(5, 10), Point(7, 6)],
        ['car', Point(3, 13), Point(5, 10)],
        ['person', Point(3, 5), Point(4, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(8, 4), Point(9, 4)],
        ['car', Point(5, 9), Point(7, 5)],
        ['car', Point(3, 12), Point(5, 9)],
        ['person', Point(3, 5), Point(4, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(8, 4), Point(9, 4)],
        ['car', Point(5, 8), Point(7, 4)],
        ['car', Point(3, 11), Point(5, 8)],
        ['person', Point(3, 5), Point(4, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(8, 4), Point(9, 4)],
        ['car', Point(5, 7), Point(7, 3)],
        ['car', Point(3, 10), Point(5, 7)],
        ['person', Point(3, 5), Point(4, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []

    data = [
        ['person', Point(8, 4), Point(9, 4)],
        ['car', Point(5, 6), Point(7, 2)],
        ['car', Point(3, 9), Point(5, 6)],
        ['person', Point(3, 5), Point(4, 5)],
    ]
    objects = make_objects(data)
    result = analyze(objects, region)
    assert result == []


testing_left_right()
testing_right_left()
testing_right_and_left()
