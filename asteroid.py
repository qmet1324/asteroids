from circleshape import * 
from constants import *

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE_COLOR, self.position, self.radius, ASTEROID_POLYGON_THICKNESS)

    def update(self, dt):
        self.position += (self.velocity * dt)
