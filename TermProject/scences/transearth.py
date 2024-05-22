import pygame
import pygame.gfxdraw

from objects.csm import CSM
from objects.earth import Earth
from objects.lem import LEM
from objects.moon import Moon
from objects.rocket import Rocket
from utils.config import Config
from utils.utils import Circle, Point, TextDrawer

class TransEarthScene:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
        self.background = pygame.image.load("assets/space.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (Config.WIDTH, Config.HEIGHT))


        self.earth = Earth(pygame.Vector2(150, Config.HEIGHT // 2), pygame.Vector2(100, 100))
        self.moon = Moon(pygame.Vector2(650, Config.HEIGHT // 2), pygame.Vector2(50, 50))

        self.csm = CSM(pygame.Vector2(650, Config.HEIGHT // 2 + 75), pygame.sprite.Group())
        self.csm.scale(pygame.Vector2(35, 35))

        self.csm.rotate(180)

        self.csm.engine_on = True
        self.is_rotated = False

    def render(self):
        self.display.blit(self.background, (0, 0))
        TextDrawer("assets/nasalization-rg.ttf", 32, (255, 255, 255), self.display).draw("Trans Earth Coast Phase", Config.WIDTH // 2, Config.HEIGHT - 50)

        self.earth.draw(self.display)
        self.moon.draw(self.display)

        b_points = [
            (650 + 25,  Config.HEIGHT // 2), 
            (650 + 50,  Config.HEIGHT // 2), 
            (650 + 50,  Config.HEIGHT // 2 + 50),
            (650,       Config.HEIGHT // 2 + 50),
            
        ]
        
        pygame.gfxdraw.bezier(self.display, b_points, 10, (255, 255, 0))
        
        b_points = [
            (650,  Config.HEIGHT // 2 + 50),
            (500,       Config.HEIGHT // 2 + 100), 
            (300, Config.HEIGHT // 2 - 100),
            (150, Config.HEIGHT // 2 - 75),
        ]
        
        pygame.gfxdraw.bezier(self.display, b_points, 10, (51, 153, 255))
        
        b_points = [
            (150, Config.HEIGHT // 2 - 75),
            (100, Config.HEIGHT // 2 - 50),
            (125, Config.HEIGHT // 2 - 25),
        ]
        
        pygame.gfxdraw.bezier(self.display, b_points, 10, (255, 255, 255))


        self.csm.draw(self.display)

    def update(self, delta_time):
        self.csm.velocity = pygame.Vector2(-1.5, -0.5)

        if self.csm.pos.x < 150:
            if not self.is_rotated:
                self.csm.rotate(-90)
                self.is_rotated = True
            self.csm.engine_on = False
            self.csm.velocity = pygame.Vector2(-0.5, 0.5)

        if self.csm.pos.x < 125:
            self.gameStateManager.set_current_scence("EarthLandingScene")
        self.csm.update(delta_time)