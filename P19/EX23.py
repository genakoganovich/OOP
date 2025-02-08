from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return circle * 2 + side

    def __init__(self, diameter, high):
        self.dia = diameter
        self.h = high
        self.area = self.make_area(diameter, high)


a = Cylinder(1, 2)
print(a.area)
print(a.make_area(2, 2))
