import pygame
import datetime

from constants import *

def main():
    pygame.init()
    pygame.time.Clock()
    delta_time = 0

    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        time_passed = pygame.time.Clock().tick(60)
        delta_time += time_passed / 1000.0
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == "__main__":
    main()
