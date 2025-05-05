from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE_COLOR, self.position, self.radius, ASTEROID_POLYGON_THICKNESS)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            pos_new_rand_vec = self.velocity.rotate(rand_angle)
            neg_new_rand_vec = self.velocity.rotate(-rand_angle)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            splitted_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            splitted_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            splitted_asteroid_one.velocity = pos_new_rand_vec * 1.2
            splitted_asteroid_two.velocity = neg_new_rand_vec * 1.2
