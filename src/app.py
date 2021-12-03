import pygame
import sys


def rotate(surface, angle):
    rotated_surface = pygame.transform.rotate(surface, angle)
    rotated_rect = rotated_surface.get_rect(center=(400, 300))
    return rotated_surface, rotated_rect


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    boid = pygame.image.load("../art/boid.png")
    boid_rect = boid.get_rect(center=(400, 300))
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                angle = (angle + 15) % 360
                print("Current angle:", angle)
                boid = pygame.transform.rotate(boid, angle)
                boid_rect = boid.get_rect(center=(400, 300))

        screen.fill((30, 30, 30))
        screen.blit(boid, boid_rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
