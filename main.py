import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps_counter = pygame.time.Clock()
    dt = 0

    updatable_objs = pygame.sprite.Group()
    drawable_objs = pygame.sprite.Group()
    asteroid_objs = pygame.sprite.Group()

    Player.containers = (updatable_objs, drawable_objs)
    Asteroid.containers = (asteroid_objs, updatable_objs, drawable_objs)
    AsteroidField.containers = (updatable_objs)

    asteroid = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

        updatable_objs.update(dt)

        for obj in asteroid_objs:
            if obj.check_collision(player):
                sys.exit("Game over!")

        for obj in drawable_objs:
            obj.draw(screen)

        pygame.display.flip()

        fps_counter.tick(60)
        dt = fps_counter.tick(60) / 1000

if __name__ == "__main__":
    main()
