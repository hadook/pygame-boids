import pygame
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30, 30, 30))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
