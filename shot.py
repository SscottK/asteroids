import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        
        
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            (255, 255, 255), 
            self.position, 
            self.radius, 2
        )
    
    def update(self, dt):
        self.position += self.velocity * dt