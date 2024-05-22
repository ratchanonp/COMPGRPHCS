import pygame


class Earth:
    def __init__(self, pos, size):
        self.pos = pygame.Vector2(pos)
        self.size = size
        self.image = pygame.image.load("assets/earth.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

    def draw(self, display):
        rect = self.image.get_rect(center=self.pos)
        display.blit(self.image, rect)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)