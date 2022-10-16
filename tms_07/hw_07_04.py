from hw_07_03 import Circle
from hw_07_02 import Rectangle
from base import Shape


class Box:

    def __init__(self):
        self.shapes = []

    def add_shape(self, sh):
        if isinstance(sh, Shape):
            return self.shapes.append(sh)

    def remove_shape(self):
        self.shapes.pop()

    def get_common_area(self):
        return int(sum(sh.get_area() for sh in self.shapes))


box = Box()
box.add_shape(Rectangle(2, 4))
box.add_shape(Circle(3))
assert box.get_common_area() == 36
box.add_shape(Circle(4))
assert box.get_common_area() == 86
box.remove_shape()
assert box.get_common_area() == 36
