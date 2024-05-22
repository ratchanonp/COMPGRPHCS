import pygame

from utils.utils import Point


class Object:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        
    def draw(self, screen):
        # Draw at the position x, y centered 
        screen.blit(self.image, (self.x - self.rect.width // 2, self.y - self.rect.height // 2))
    
    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def scale(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=self.rect.center)

# Dynamic object inherits from Object add velocity and acceleration
class DynamicObject(Object):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)

        
    def update(self, delta_time):
        self.velocity += self.acceleration * delta_time
        self.x += self.velocity.x * delta_time
        self.y += self.velocity.y * delta_time
        self.rect = self.image.get_rect(center=(self.x, self.y))