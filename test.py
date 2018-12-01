from analyzer.classes.analyze import analyze
from analyzer.classes.objects import Person, Car
from analyzer.classes.select_region import Region, Point

region = Region()
region.add_corner(Point(2, 1))
region.add_corner(Point(10, 1))
region.add_corner(Point(2, 10))
region.add_corner(Point(10, 10))
region.sort()
# for p in region.corners:
#     print(p)

objects = list()
p1 = Person(Point(1, 5), Point(2, 5))
objects.append(p1)

# objects.append(Person(1, Point(1, 5), Point(1.3, 5), 'lr'))
# objects.append(Person(2, Point(9.7, 4), Point(10, 5), 'rl'))
p2 = Person(Point(6, 5), Point(6.3, 5), 'lr')
objects.append(p2)

p3 = Person(Point(4, 4), Point(5, 4), 'rl')
objects.append(p3)

p4 = Person(Point(2, 4), Point(2.3, 5), 'rl')
objects.append(p4)


analyze(objects, region)

objects.clear()
p5 = Person(Point(5, 4), Point(6, 4))
objects.append(p5)
objects.append(Car(1, Point(5, 20), Point(7, 10), 'tb'))
analyze(objects, region)
