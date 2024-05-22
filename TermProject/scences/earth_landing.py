import pygame

from objects.csm import CSM
from objects.earth import Earth
from objects.lem import LEM
from objects.moon import Moon
from utils.config import Config
from utils.utils import Circle, Point, TextDrawer


class EarthLandingScene:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        self.background = pygame.image.load("assets/space.jpg").convert_alpha()
        self.background = pygame.transform.scale(
            self.background, (Config.WIDTH, Config.HEIGHT))

        self.earth = Earth(pygame.Vector2(Config.WIDTH // 2,
                           Config.HEIGHT + 100), (600, 600))
        self.csm = CSM(pygame.Vector2(Config.WIDTH // 2, 200),
                       pygame.sprite.Group())
        self.csm.rotate(90)

        self.is_landed = False

        self.counter = 0

    def render(self):
        self.display.blit(self.background, (0, 0))

        

        self.earth.draw(self.display)
        self.csm.draw(self.display)

        if self.is_landed:
            TextDrawer("assets/nasalization-rg.ttf", 32, (255, 255, 255), self.display).draw("End", Config.WIDTH // 2, Config.HEIGHT - 50)

    def update(self, delta_time):
        self.csm.velocity = pygame.math.Vector2(0, 1)

        if self.csm.pos.y > Config.HEIGHT // 2 + 100:
            self.is_landed = True
            self.csm.velocity = pygame.math.Vector2(0, 0)

        self.csm.update(delta_time)
