import pygame
from constants import *
from player import *

def main():
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    fps_counter = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        pygame.Surface.fill(screen, BLACK_COLOR)

        player.draw(screen)
        player.update(dt)

        pygame.display.flip()

        fps_counter.tick(60)
        dt = fps_counter.tick(60) / 1000

if __name__ == "__main__":
    main()
