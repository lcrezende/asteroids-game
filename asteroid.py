import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    new_radius = (self.radius - ASTEROID_MIN_RADIUS)
    random_angle = random.uniform(20, 50)
    pos_angle = self.velocity.rotate(random_angle)
    neg_angle = self.velocity.rotate(-random_angle)

    new1 = Asteroid(self.position.x, self.position.y, new_radius)
    new1.velocity = pos_angle * 1.2
    
    new2 = Asteroid(self.position.x, self.position.y, new_radius)
    new2.velocity = neg_angle * 1.2
  
  def update(self, dt):
    self.position += self.velocity * dt