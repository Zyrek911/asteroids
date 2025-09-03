import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            split_angle = random.uniform(20,50)
            first_vector = self.velocity.rotate(split_angle)
            second_vector = self.velocity.rotate(-split_angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            first = Asteroid(self.position[0], self.position[1], split_radius)
            first.velocity = first_vector * 1.2
            second = Asteroid(self.position[0], self.position[1], split_radius)
            second.velocity = second_vector * 1.2