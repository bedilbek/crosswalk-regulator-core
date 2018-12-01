import numpy as np

from .select_region import Point, Region


class Object(object):
    def __init__(self, obj_type, point_l_t, point_r_b, direction=None, pk=None):
        self.obj_type = obj_type
        self.pk = pk
        self.point_l_t: Point = point_l_t
        self.point_r_b: Point = point_r_b
        self.direction = direction


class Person(Object):
    index = 0
    bound_pixel = 2

    def __init__(self, point_l_t, point_r_b, direction=None, pk=None):
        super(Person, self).__init__(obj_type='person', point_l_t=point_l_t, point_r_b=point_r_b,
                                     direction=direction, pk=pk)
        self.center = round((self.point_l_t.x + self.point_r_b.x) / 2), round((self.point_l_t.y + self.point_r_b.y) / 2)

    @property
    def x_cross_point(self):
        return (self.point_l_t.x + self.point_r_b.x) / 2, self.point_r_b.y

    def get_side_c(self, p_1: Point, p_2: Point):
        mid_x, bottom_y = self.x_cross_point
        c = (mid_x - p_1.x) * (p_2.y - p_1.y) - (bottom_y - p_1.y) * (p_2.x - p_1.x)
        return c

    def decide_side(self, p_1, p_2):
        c = (p_1.x - p_1.x) - 1 * (p_2.y - p_1.y) - (p_1.y - p_1.y + 1) * (p_2.x - p_1.x)
        return c

    def is_in_region(self, region: Region):
        assert self.direction
        if self.direction == 'lr':
            decision = self.decide_side(*region.left_line)
            side_coef = self.get_side_c(*region.left_line)
            return side_coef * decision < 0
        else:
            decision = self.decide_side(*region.right_line)
            side_coef = self.get_side_c(*region.right_line)
            return side_coef * decision > 0

    def get_x_boundaries(self):
        return self.point_l_t.x, self.point_r_b.x

    def find_direction(self, region: Region):
        if self.direction:
            return

        def from_left():
            decision = self.decide_side(*region.left_line)
            side_coeff = self.get_side_c(*region.left_line)
            return side_coeff / abs(side_coeff) == decision / abs(decision)

        def from_right():
            decision = self.decide_side(*region.right_line)
            side_coeff = self.get_side_c(*region.right_line)
            return side_coeff / abs(side_coeff) != decision / abs(decision)

        if from_left() and not from_right():
            self.direction = 'lr'
        else:
            self.direction = 'rl'

    @classmethod
    def update_or_add(cls, persons: list, person, region):
        direction = dict(
            lr=1,
            rl=2,
        )
        array = [[*p.center, p.pk, direction[p.direction]] for p in persons]
        array = np.array(array)
        if len(array) > 0:
            array = array - [*person.center, 0, 0]
            array.view('i8,i8,i8,i8').sort(order=['f0', 'f1'], axis=0)
        for i, data in enumerate(array):
            if 0 > person.center[0] - data[0] > -cls.bound_pixel and data[3] == 1:
                # going left
                target: Person = filter(lambda p: p.pk == data[2], persons)
                target.point_l_t = person.point_l_t
                target.point_r_b = person.point_r_b
                return
            elif 0 < person.center[0] - data[0] < cls.bound_pixel and data[3] == 2:
                # going right
                target = filter(lambda p: p.pk == data[2], persons)
                target.point_l_t = person.point_l_t
                target.point_r_b = person.point_r_b
                return
        person.pk = cls.index
        person.find_direction(region)
        cls.index += 1
        persons.append(person)
        return


class Car(Object):
    def __init__(self, point_l_t, point_r_b, direction=None, pk=None):
        super(Car, self).__init__(obj_type='car', point_l_t=point_l_t, point_r_b=point_r_b,
                                  direction=direction, pk=pk)

    def y_points(self):
        return self.point_r_b.y, self.point_l_t.y

    def x_points(self):
        return self.point_l_t.x, self.point_r_b.x