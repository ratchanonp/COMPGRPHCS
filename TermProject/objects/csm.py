# Class Rocket inherits from DynamicObject
import pygame


class CSM(pygame.sprite.Sprite):
    def __init__(self, pos, *grps):
        super().__init__(*grps)
        self.image = pygame.image.load("assets/csm.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.flame = pygame.image.load("assets/flame.png").convert_alpha()
        self.flame = pygame.transform.scale(self.flame, (20, 20))
        self.flame = pygame.transform.rotate(self.flame, 90)

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
        
    def scale(self, scale):
        original_size = self.image.get_size()[0]
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(center=self.pos)

        self.flame = pygame.transform.scale_by(self.flame, original_size / scale[0])

    def rotate(self, angle):
        self.flame = pygame.transform.rotate(self.flame, angle)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.pos)
        self.angle += angle

        


    def draw(self, display):
        if self.engine_on:
            # Calculate flame position based on angle
            flame_pos = self.pos + pygame.math.Vector2(-(self.rect.width / 2), 0).rotate(-self.angle)
            display.blit(self.flame, self.flame.get_rect(center=flame_pos))
        display.blit(self.image, self.rect)