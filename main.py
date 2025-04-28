import pygame
from constants import *

def main():
    pygame.init()
    fps_counter = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        pygame.Surface.fill(screen, BLACK_COLOR)
        pygame.display.flip()
        fps_counter.tick(60)
        dt = fps_counter.tick(60) / 1000

if __name__ == "__main__":
    main()
