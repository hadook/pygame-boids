import pygame
from random import triangular
from config import Canvas
from vector import Vector


# Represents a single boid object
class Boid(pygame.sprite.Sprite):

    max_force = 0.1
    max_speed = 4
    orientation = 300

    def __init__(self, color=pygame.Color('cornflowerblue')):
        super().__init__()

        self.position = Vector.random(max_x=Canvas.width, max_y=Canvas.height, margin=Canvas.margin)
        self.velocity = Vector.random(max_magnitude=self.max_speed)

        self.color = color
        self.art = self.load_art()
        self.image = pygame.transform.rotozoom(self.art, (-1) * self.velocity.angle, 1)
        self.rect = self.art.get_rect(center=self.position)

    def load_art(self):
        art = pygame.image.load('../art/boid.png')
        hue = pygame.Surface(art.get_size()).convert_alpha()
        hue.fill(self.color.correct_gamma(triangular(0.8, 1.2, 1)))
        art.blit(hue, (0, 0), special_flags=pygame.BLEND_MULT)
        return art

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
