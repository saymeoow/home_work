from hw_07_03 import Circle
from hw_07_02 import Rectangle
from base import Shape


class Box:

    def __init__(self):
        self.shapes = 0

    def add_shape(self, inst):
        if isinstance(inst, Shape):
            self.shapes += inst.get_area()

    def remove_shape(self):
        self.shapes.pop()

    def get_common_area(self):
        return sum((x.get_area for x in self.shapes))

def main():
    box = Box()
    box.add_shape(Circle(3))
    box.add_shape(Rectangle(2, 4))
    assert box.get_common_area() == 36

main()
