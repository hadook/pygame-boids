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

    for i in range(44):
        boid = Boid()
        boids.append(boid)
        flock.add(boid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # # seek
        # if pygame.mouse.get_pressed()[0] == True:
        #     target = Vector(pygame.mouse.get_pos())
        #     for boid in boids:
        #         boid.seek(target)

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         boid.reset()

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT]:
        #     boid.turn_left()
        # if keys[pygame.K_RIGHT]:
        #     boid.turn_right()

        screen.fill((30, 30, 30))
        flock.update()
        flock.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
