import operator

from analyzer.classes.objects import Car
from utils.figures import Region, Line, Point

crossable_lines = list()
global_person_list = list()


def analyze(object_list, region):
    top_line_points = region.top_line
    top_line_points = (top_line_points[0].x, top_line_points[1].x)

    def separate_objects():
        p = list()
        c = list()
        classification = dict(
            car=c,
            person=p,
        )
        for object_ in object_list:
            classification[object_.obj_type].append(object_)

        return c, p

    def filter_persons(persons):
        """
        Remove persons who do not enter to cross region
        """
        index = 0
        size = len(persons)
        for _ in range(size):
            if not persons[index].is_in_region(region):
                persons.pop(index)
            else:
                index += 1

    def filter_cars(cars, persons):
        # TODO:think filtering
        def find_boundary():
            """
            find person whose y is below respect to and close to top line and return y for him
            """
            max_boundary = (region.top_line[0].y + region.top_line[1].y) / 2
            min_boundary = 0
            for person in persons:
                if person.point_r_b.y >= max_boundary:
                    min_boundary = max(min_boundary, person.point_r_b.y)
            return max_boundary, min_boundary

        max_b, min_b = find_boundary()
        index = 0
        size = len(cars)
        for _ in range(size):
            if max_b + Car.bound_pixel < cars[index].point_r_b.y < min_b:
                index += 1
            else:
                cars.pop(index)

    def find_crossable_line(persons):
        """
        :return position of not crossable line
        """
        # TODO:check line, is done
        s, b = Region.get_line_equation(*region.top_line)
        not_crossable_line = [top_line_points[1], top_line_points[1], top_line_points[0], top_line_points[0]]
        lines = list()
        for person in persons:
            l_boundary, r_boundary = person.get_x_boundaries()
            if person.direction == 'lr':
                not_crossable_line[0] = min(l_boundary, not_crossable_line[0])
            else:
                not_crossable_line[3] = max(r_boundary, not_crossable_line[3])

        if not_crossable_line[0] != not_crossable_line[1]:
            lines.append(
                Line(
                    Point(not_crossable_line[0], int(s * not_crossable_line[0] + b)),
                    Point(not_crossable_line[1], int(s * not_crossable_line[1] + b)),
                    False
                )
            )

        if not_crossable_line[2] != not_crossable_line[3]:
            lines.append(
                Line(
                    Point(not_crossable_line[2], int(s * not_crossable_line[2] + b)),
                    Point(not_crossable_line[3], int(s * not_crossable_line[3] + b)),
                    False
                )
            )
        if not_crossable_line[0] > not_crossable_line[3]:
            lines.append(
                Line(
                    Point(not_crossable_line[3], int(s * not_crossable_line[3] + b)),
                    Point(not_crossable_line[0], int(s * not_crossable_line[0] + b)),
                    True
                )
            )
        return lines

    def detect_cars(cars, regulation_line):
        """
        detect cars whether between green line
        :param cars:
        :param c_line:
        :return:
        """
        index = 0
        cars_size = len(cars)

        for _ in range(cars_size):
            x_left, x_right = cars[index].x_points()
            counter = 0
            for line in regulation_line:
                x_left_bound, x_right_bound = line.get_x_points()
                if not line.accessible and x_left_bound < x_left and x_right_bound > x_right:
                    counter += 1
            if counter == 0:
                cars.pop(index)
            else:
                index += 1

    car_list, person_list = separate_objects()  # Dis
    from analyzer.classes.objects import Person
    for person in person_list:
        Person.update_or_add(global_person_list, person, region)
    persons_history = list(global_person_list)
    filter_persons(persons_history)  # filter persons who is in region respect to left and right lines
    initialized_lines = find_crossable_line(persons_history)  # find crossable line using filtered persons
    if car_list:
        filter_cars(car_list, persons_history)  # filter cars respect to filtered users
    detect_cars(car_list, initialized_lines)  # detect cars respect to crossable line
    return car_list, initialized_lines
