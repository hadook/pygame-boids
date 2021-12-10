import pygame
from config import Canvas
from vector import Vector


# Represents a single boid object
class Boid(pygame.sprite.Sprite):

    max_force = 0.1
    max_speed = 4
    orientation = 300
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
        if (target - self.position).magnitude() < self.orientation:
            desired_velocity = (target - self.position).normalize() * self.max_speed
            steering = (desired_velocity - self.velocity).truncate(self.max_force)
            self.velocity = (self.velocity + steering).truncate(self.max_speed)
