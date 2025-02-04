import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        
    
    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=(self.position.x, self.position.y), 
            radius=self.radius,
            width=2
        )

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            parent_velocity = self.velocity
            sp1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            sp1.velocity = parent_velocity
            sp1.velocity = sp1.velocity.rotate(angle)
            sp1.velocity *= 1.2
            sp2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            sp2.velocity = parent_velocity
            sp2.velocity = sp2.velocity.rotate(- angle)
            sp2.velocity *= 1.2
            for group in self.groups():
                group.add(sp1)
                group.add(sp2)
        