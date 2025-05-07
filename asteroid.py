import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = self.velocity.rotate(random.uniform(20, 50))
        random_angle_2 = self.velocity.rotate(360 - random.uniform(20, 50))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = random_angle * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = random_angle_2 * 1.2