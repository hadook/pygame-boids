import pygame
from config import Canvas
from vector import Vector


# Represents a single boid object
class Boid(pygame.sprite.Sprite):

    max_force = 0.5
    max_speed = 4
    art = pygame.image.load('../art/boid.png')

    def __init__(self):
        super().__init__()

        self.position = Vector.random(max_x=Canvas.width, max_y=Canvas.height, margin=Canvas.margin)
        self.velocity = Vector.random(max_magnitude=self.max_speed)

        self.image = pygame.transform.rotozoom(self.art, (-1) * self.velocity.angle, 1)
        self.rect = self.art.get_rect(center=self.position)

    def update(self):
        self.position += self.velocity
        self.wrap_edge()
        self.image = pygame.transform.rotozoom(self.art, (-1) * self.velocity.angle, 1)
        self.rect.center = self.position.int

    def wrap_edge(self):
        if self.position.x < 0 - Canvas.margin:
            self.position.x = Canvas.width + Canvas.margin
        if self.position.x > Canvas.width + Canvas.margin:
            self.position.x = 0 - Canvas.margin
        if self.position.y < 0 - Canvas.margin:
            self.position.y = Canvas.height + Canvas.margin
        if self.position.y > Canvas.height + Canvas.margin:
            self.position.y = 0 - Canvas.margin

    def seek(self, target: Vector):



        desired_velocity = Vector(self.position - target)
        desired_velocity.normalize_ip()
        desired_velocity.scale_to_length(self.max_speed)
        steering = Vector(desired_velocity - self.velocity)
        steering.scale_to_length(self.max_force)
        self.velocity = Vector(self.velocity + steering)
        self.velocity.scale_to_length(self.max_speed)


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

