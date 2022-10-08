from base import Shape


class Rectangle(Shape):
    def __init__(self, heigth, width):
        if any((x <= 0 for x in (heigth, width))):
            raise ValueError('value muse be positive')
        super().__init__()
        self.heigth = heigth
        self.width = width

    def __add__(self, other):
            return Rectangle(self.heigth + other.heigth, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(self.heigth - other.heigth, self.width - other.width)

    def get_area(self):
        return int(self.width * self.heigth)


S_Rectangle_one = Rectangle(3, 5)
S_Rectangle_two = Rectangle(2, 4)
S_Rectangle_three = S_Rectangle_one + S_Rectangle_two
S_Rectangle_four = S_Rectangle_one - S_Rectangle_two

assert S_Rectangle_one.get_area() == 15
assert S_Rectangle_two.get_area() == 8
assert S_Rectangle_three.get_area() == 45
assert S_Rectangle_four.get_area() == 1

