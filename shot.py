from circleshape import *
from constants import *


class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE_COLOR, self.position, self.radius, SHOT_POLYGON_THICKNESS)

    def update(self, dt):
        self.position += (self.velocity * dt)
