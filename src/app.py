import sys
import pygame
from config import Canvas
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

    for i in range(20):
        boid = Boid(pygame.Color('darkmagenta'))
        boids.append(boid)
        flock.add(boid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # # seek mouse cursor
        # if pygame.mouse.get_focused():
        #     target = Vector(pygame.mouse.get_pos())
        #     for b in boids:
        #         b.seek(target)

        # separation
        for b in boids:
            b.separation(boids)

        screen.fill((30, 30, 30))
        flock.update()
        flock.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        # print(clock.get_fps())


if __name__ == "__main__":
    main()
