from base import Shape

class Circle(Shape):
    def __init__(self, radius=int, pi=3.14):
        if any((x <= 0 for x in (radius, pi))):
            raise ValueError('value muse be positive')
        super().__init__()
        self.radius = radius
        self.pi = pi

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def get_area(self):
        return int(self.pi * self.radius ** 2)


S_circle_one = Circle(4)
S_circle_two = Circle(3)
S_circle_three = S_circle_one + S_circle_two
S_circle_four = S_circle_one - S_circle_two

assert S_circle_one.get_area() == 50
assert S_circle_two.get_area() == 28
assert S_circle_three.get_area() == 153
assert S_circle_four.get_area() == 3