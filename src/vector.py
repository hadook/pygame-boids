from random import random, uniform, triangular
import pygame


# class to represent a 2d vector in-game, inherits from pygame's built-int Vector2 class
class Vector(pygame.math.Vector2):

    def __init__(self, *args):
        super().__init__(*args)

    @property
    def int(self):
        return Vector(round(self.x), round(self.y))

    @property
    def angle(self):
        return self.as_polar()[1]

    def truncate(self, max_magnitude):
        v = Vector(self)
        if v.magnitude() > max_magnitude:
            v.scale_to_length(max_magnitude)
        return v

    def truncate_ip(self, max_magnitude):
        if self.magnitude() > max_magnitude:
            self.scale_to_length(max_magnitude)

    @classmethod
    def random(cls, **kwargs):
        max_magnitude = kwargs.get("max_magnitude")
        max_x = kwargs.get("max_x")
        max_y = kwargs.get("max_y")
        margin = kwargs.get("margin")

        if max_magnitude is not None:
            magnitude = triangular(0, max_magnitude, max_magnitude)
            angle = random() * 360
            v = Vector()
            v.from_polar((magnitude, angle))
            return v
        else:
            if margin is None:
                margin = 0
            x = uniform(0 - margin, max_x + margin)
            y = uniform(0 - margin, max_y + margin)
            return Vector(x, y)
