import sys
import pygame
from boid import Boid


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen_width, screen_height = 1600, 900
    screen = pygame.display.set_mode((screen_width, screen_height))

    flock = pygame.sprite.Group()

    for i in range(20):
        boid = Boid()
        flock.add(boid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
