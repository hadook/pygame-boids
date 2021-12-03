import math


class Vector:
    """Class to represent a 2D vector in pygame."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def len(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    @property
    def int(self):
        return Vector(int(self.x), int(self.y))

    @property
    def normalized(self):
        if self.len > 0:
            return Vector(self.x / self.len, self.y / self.len)
        else:
            return Vector(0, 0)
