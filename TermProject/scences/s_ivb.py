import math
import pygame

from objects.csm import CSM
from objects.earth import Earth
from objects.lem import LEM
from objects.rocket import Rocket
from utils.config import Config
from utils.utils import Circle, Point, TextDrawer

class S_IVB:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        

        self.background = pygame.image.load("assets/space.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (Config.WIDTH, Config.HEIGHT))

        self.rocket = Rocket(pygame.Vector2(0, 500), pygame.sprite.Group())
        self.rocket.rotate(-90)
        self.csm = CSM(pygame.Vector2(0, 500), pygame.sprite.Group())
        self.lem = LEM(pygame.Vector2(0, 500), pygame.sprite.Group())
        self.lem.rotate(-90)

        self.is_sep = False
        self.is_csm_rotate = False

        self.counter = 0

    def render(self):
        self.display.blit(self.background, (0, 0))

        self.rocket.draw(self.display)

        if self.is_sep:
            self.csm.draw(self.display)
            self.lem.draw(self.display)
        
        TextDrawer("assets/nasalization-rg.ttf", 32, (255, 255, 255), self.display).draw("S-IVB Sep", Config.WIDTH // 2, Config.HEIGHT - 50)


    def update(self, delta_time):
        self.counter += delta_time

        if self.counter < 5:
            self.rocket.velocity = pygame.Vector2(0.5, -0.25)
            self.csm.velocity = pygame.Vector2(0.5, -0.25)
            self.lem.velocity = pygame.Vector2(0.5, -0.25)
        elif self.counter < 7:
            self.is_sep = True
            self.csm.engine_on = True
            self.csm.velocity = pygame.Vector2(2, -0.25)
        elif self.counter < 9:
            self.csm.engine_on = False
            self.csm.velocity = pygame.Vector2(0.5, -0.25)
        elif math.floor(self.counter) == 9 and not self.is_csm_rotate:
            self.csm.engine_on = False
            self.csm.rotate(180)
            self.is_csm_rotate = True
        elif self.counter < 11:
            self.csm.engine_on = True
            self.csm.velocity = pygame.Vector2(-0.75, -0.25)
        elif self.counter < 16:
            self.lem.engine_on = True
            self.csm.engine_on = False
            self.csm.velocity = pygame.Vector2(1, -0.25)
            self.lem.velocity = pygame.Vector2(1, -0.25)
            self.rocket.velocity = pygame.Vector2(0.5, -0.5)
        elif self.counter < 17:
            self.lem.engine_on = False
            self.csm.engine_on = False
            self.csm.velocity = pygame.Vector2(1, -0.25)
            self.lem.velocity = pygame.Vector2(1, -0.25)
        

        if self.csm.pos.x > Config.WIDTH:
            self.gameStateManager.set_current_scence("TranslunarCoast")
        
        self.rocket.update(delta_time)
        self.csm.update(delta_time)
        self.lem.update(delta_time)