# Class Rocket inherits from DynamicObject
from types import UnionType
from typing import Any
import pygame


class Rocket(pygame.sprite.Sprite):
    def __init__(self, pos, *grps):
        super().__init__(*grps)
        self.image = pygame.image.load("assets/spaceship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.flame = pygame.image.load("assets/flame.png").convert_alpha()
        self.flame = pygame.transform.scale(self.flame, (20, 20))
        self.flame = pygame.transform.rotate(self.flame, 180)

        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(pos)
        self.velocity = pygame.math.Vector2(0, 0)

        self.angle = 0
        self.engine_on = False

    def move(self, pos):
        self.pos = pos
        self.rect.center = self.pos

    def update(self, delta_time):
        if self.velocity.length() > 0:
            self.pos += self.velocity
            self.rect.center = self.pos
        

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.pos)
        self.angle += angle

        self.flame = pygame.transform.rotate(self.flame, angle)
        


    def draw(self, display):
        display.blit(self.image, self.rect)
        if self.engine_on:
            # Calculate flame position based on angle
            flame_pos = self.pos + pygame.math.Vector2(0, 25).rotate(-self.angle)
            display.blit(self.flame, self.flame.get_rect(center=flame_pos))