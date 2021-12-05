from random import random, triangular
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

    @classmethod
    def random(cls, max_magnitude):
        magnitude = triangular(0, max_magnitude, max_magnitude)
        angle = random() * 360
        v = Vector()
        v.from_polar((magnitude, angle))
        return v
