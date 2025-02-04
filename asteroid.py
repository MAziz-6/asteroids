import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(self.x, self.y, self.radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            surface= screen,
            color= "white",
            center= (self.x, self.y),
            radius= self.radius,
            width= 2
        )

    def update(self, dt):
        self.position += (self.velocity * dt)