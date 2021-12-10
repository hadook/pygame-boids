import sys
import pygame
from config import Canvas
from vector import Vector
from boid import Boid


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Canvas.width, Canvas.height))

    flock = pygame.sprite.Group()
    boids = []

    for i in range(50):
        boid = Boid()
        boids.append(boid)
        flock.add(boid)

    for i in range(10):
        boid = Boid(pygame.Color('indianred'))
        boids.append(boid)
        flock.add(boid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if pygame.mouse.get_focused():
            target = Vector(pygame.mouse.get_pos())
            for b in boids:
                b.seek(target)

        screen.fill((30, 30, 30))
        flock.update()
        flock.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
