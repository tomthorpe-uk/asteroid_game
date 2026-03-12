from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        asteroid_1_vector = self.velocity.rotate(split_angle)
        asteroid_2_vector = self.velocity.rotate(-split_angle)
        new_asteroid_size = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_size)
        asteroid_1.velocity = asteroid_1_vector

        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_size)
        asteroid_2.velocity = asteroid_2_vector

        
