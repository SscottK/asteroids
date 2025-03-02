import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            (255, 255, 255), 
            ((int(self.position.x), int(self.position.y))), 
            self.radius, 2
        )
    
    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            rand_angle = random.uniform(20, 50)
            new_vel1 = self.velocity.rotate(rand_angle)
            new_vel2 = self.velocity.rotate(-rand_angle)
            new_vel1 *= 1.2
            new_vel2 *= 1.2
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid_1.velocity = new_vel1
            asteroid_2.velocity = new_vel2
            self.kill()


            
