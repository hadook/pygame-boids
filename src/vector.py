import pygame


# class to represent a 2d vector in-game
class Vector(pygame.math.Vector2):

    # returns a vector with coordinates rounded to the nearest integers
    def int(self):
        return Vector(round(self.x), round(self.y))
