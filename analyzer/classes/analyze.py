import operator

from analyzer.classes.objects import Car
from utils.figures import Region

# TODO: crossable line
crossable_lines = list()
global_person_list = list()


def analyze(object_list: list, region: Region):
    top_line_points = region.top_line
    top_line_points = (top_line_points[0].x, top_line_points[1].x)

    def get_barrier():
        for i in range(len(object_list) - 1):
            if object_list[i].obj_type != object_list[i + 1].obj_type:
                return i
        return len(object_list)

    def filter_persons(persons: list):
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

    def filter_cars(cars: list, persons: list):
        # TODO:think filtering
        def find_boundary():
            """
            find person whose y is below respect to and close to top line and return y for him
            """
            max_boundary = region.top_line[0].y
            min_boundary = 0
            for person in persons:
                if person.point_r_b.y <= max_boundary:
                    min_boundary = max(min_boundary, person.point_r_b.y)
            return max_boundary, min_boundary

        max_b, min_b = find_boundary()
        index = 0
        size = len(cars)
        for _ in range(size):
            if not (max_b - Car.bound_pixel > cars[index].point_r_b.y > min_b):
                cars.pop(index)
            else:
                index += 1

    def find_crossable_line(persons):
        """
        :return position of not crossable line
        """
        # TODO:check line, is done

        not_crossable_line = [top_line_points[1], top_line_points[1], top_line_points[0], top_line_points[0]]
        for person in persons:
            l_boundary, r_boundary = person.get_x_boundaries()
            if person.direction == 'lr':
                not_crossable_line[0] = min(l_boundary, not_crossable_line[0])
            else:
                not_crossable_line[3] = max(r_boundary, not_crossable_line[3])
        if not_crossable_line[0] > not_crossable_line[3]:
            return not_crossable_line[0], not_crossable_line[3]
        return 0, 0

    def detect_cars(cars, c_line):
        """
        detect cars whether between green line
        :param cars:
        :param c_line:
        :return:
        """
        index = 0
        size = len(cars)
        for _ in range(size):
            x_left, x_right = cars[index].x_points()
            if x_left < c_line[0] or x_right > c_line[1]:
                index += 1
            else:
                cars.pop(index)

    object_list.sort(key=operator.attrgetter('obj_type'))  # Sort to cars and persons
    barrier = get_barrier()  # Find barrier of person and car
    if barrier != len(object_list):
        car_list = object_list[:barrier + 1]  # get cars from list
        person_list = object_list[barrier + 1:]  # get persons from list
    else:
        if object_list[0].object_type == 'car':
            car_list = object_list
            person_list = []
        else:
            car_list = []
            person_list = object_list
    from analyzer.classes.objects import Person
    for person in person_list:
        Person.update_or_add(global_person_list, person, region)
    persons_history = list(global_person_list)
    filter_persons(persons_history)  # filter persons who is in region respect to left and right lines
    crossable_line = find_crossable_line(persons_history)  # find crossable line using filtered persons
    if car_list:
        filter_cars(car_list, persons_history)  # filter cars respect to filtered users
    detect_cars(car_list, crossable_line)  # detect cars respect to crossable line
    return car_list
