import pygame
from vector import Vector


# Represents a single boid object
class Boid(pygame.sprite.Sprite):

    max_force = 1
    max_speed = 1
    art = pygame.image.load('../art/boid.png')

    def __init__(self):
        super().__init__()

        self.position = Vector()
        self.velocity = Vector()

        # self.image = pygame.transform.rotozoom(self.art)




    #     self.art = pygame.image.load("../art/boid.png")
    #
    #     self.vel = 4
    #     self.turn = 3
    #     self.pos = Vector()
    #     self.dir = Vector()
    #     self.reset()
    #
    #     self.image = pygame.transform.rotozoom(self.art, (-1) * self.dir.as_polar()[1], 1)
    #     self.rect = self.art.get_rect(center=self.pos)
    #
    # def update(self):
    #     self.image = pygame.transform.rotozoom(self.art, (-1) * self.dir.as_polar()[1], 1)
    #     self.pos += self.vel * self.dir
    #     self.rect.center = self.pos.int()
    #
    # def reset(self):
    #     self.pos = Vector(800, 450)
    #     self.dir = Vector()
    #     self.dir.randomize()
    #     print("theta =", self.dir.as_polar()[1])
    #
    # def turn_left(self):
    #     self.dir.rotate_ip(self.turn * -1)
    #
    # def turn_right(self):
    #     self.dir.rotate_ip(self.turn * 1)

