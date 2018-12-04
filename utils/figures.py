import operator

import cv2


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return self.x, self.y

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

    def __repr__(self):
        return '{}, {}'.format(self.x, self.y)

    def get_coordinates(self):
        return self.x, self.y


class Region(object):
    corners = list()

    @property
    def is_ready(self):
        return len(self.corners) == 4

    def add_corner(self, point):
        if self.is_ready:
            return
        self.corners.append(point)

    def sort(self):
        """
        sort corners as bottom-right, bottom-left, top-left, top-right
        :return:
        """
        self.corners.sort(key=operator.attrgetter('x'))
        left_side = self.corners[:2]
        left_side.sort(key=operator.attrgetter('y'))
        right_side = self.corners[2:]
        right_side.sort(key=operator.attrgetter('y'))
        self.corners[0] = left_side[0]
        self.corners[1] = right_side[0]
        self.corners[2] = right_side[1]
        self.corners[3] = left_side[1]

    def draw_region(self, image):
        for i, point in enumerate(self.corners):
            beginning = point
            ending = self.corners[0] if len(self.corners) == i + 1 else self.corners[i + 1]
            if beginning and ending:
                cv2.line(image, beginning(), ending(), (100, 50, 200), 2)
        return image

    @staticmethod
    def get_line_equation(beginning_point, ending_point):
        """
        Y = Slope*X + b
        get_slope -> Slope
        get_b -> b
        """

        def get_slope():
            return (beginning_point.y - ending_point.y) / (beginning_point.x - ending_point.x)

        def get_b(s):
            return beginning_point.y - beginning_point.x * s

        slope = get_slope()
        b = get_b(slope)
        return slope, b

    @property
    def left_line(self):
        return self.corners[0], self.corners[1]

    @property
    def right_line(self):
        return self.corners[1], self.corners[2]

    @property
    def top_line(self):
        return self.corners[0], self.corners[1]

    @property
    def bottom_line(self):
        return self.corners[2], self.corners[3]

    def __str__(self):
        return ("left-line: {self.left_line} \n"
                "top-line, {self.top_line}\n"
                "right-line, {self.right_line}\n"
                "bottom-line, {self.bottom_line}\n")


class Line(object):

    def __init__(self, p1: Point, p2: Point, accessible=False):
        self.p1 = p1
        self.p2 = p2
        self.accessible = accessible

    def get_color(self):
        if self.accessible:
            return 133, 184, 79
        return 100, 50, 200

    def draw_line(self, image):
        cv2.line(image, self.p1.get_coordinates(), self.p2.get_coordinates(), self.get_color(), 2)
        return image

    def get_x_points(self):
        x_points = [self.p1.x, self.p2.x]
        sorted(x_points)
        return x_points


def on_click(event, x, y, flags, params):
    global region
    if flags == cv2.EVENT_FLAG_SHIFTKEY:
        region.corners.clear()
        return

    if len(region.corners) < 4 and event == cv2.EVENT_LBUTTONDBLCLK:
        region.corners.append(Point(x, y))
