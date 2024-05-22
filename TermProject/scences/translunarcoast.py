import pygame
import pygame.gfxdraw

from objects.csm import CSM
from objects.earth import Earth
from objects.lem import LEM
from objects.moon import Moon
from objects.rocket import Rocket
from utils.config import Config
from utils.utils import Circle, Point, TextDrawer

class TranslunarCoast:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
        self.background = pygame.image.load("assets/space.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (Config.WIDTH, Config.HEIGHT))


        self.earth = Earth(pygame.Vector2(150, Config.HEIGHT // 2), pygame.Vector2(100, 100))
        self.moon = Moon(pygame.Vector2(650, Config.HEIGHT // 2), pygame.Vector2(50, 50))

        self.csm = CSM(pygame.Vector2(175, Config.HEIGHT // 2 + 75), pygame.sprite.Group())
        self.csm.scale(pygame.Vector2(35, 35))

        self.lem = LEM(pygame.Vector2(210, Config.HEIGHT // 2 + 75), pygame.sprite.Group())
        self.lem.image = pygame.transform.scale(self.lem.image, (35, 35))
        self.lem.rotate(90)

        self.csm.engine_on = True

    def render(self):
        self.display.blit(self.background, (0, 0))
        TextDrawer("assets/nasalization-rg.ttf", 32, (255, 255, 255), self.display).draw("Translunar Coast Phase", Config.WIDTH // 2, Config.HEIGHT - 50)

        self.earth.draw(self.display)
        self.moon.draw(self.display)

        b_points = [
            (150 + 50,  Config.HEIGHT // 2), 
            (150 + 75,  Config.HEIGHT // 2), 
            (150 + 75,  Config.HEIGHT // 2 - 75), 
            (150,       Config.HEIGHT // 2 - 75), 
            ]
        
        pygame.gfxdraw.bezier(self.display, b_points, 10, (255,0,0))

        b_points = [
            (150,       Config.HEIGHT // 2 - 75), 
            (150 - 75,  Config.HEIGHT // 2 - 75),
            (150 - 75,  Config.HEIGHT // 2),
        ]
        pygame.gfxdraw.bezier(self.display, b_points, 10, (255,0,0))

        b_points= [
            (150 - 75,  Config.HEIGHT // 2),
            (150 - 75,  Config.HEIGHT // 2 + 75),
            (150,       Config.HEIGHT // 2 + 75),
        ]
        pygame.gfxdraw.bezier(self.display, b_points, 10, (255,0,0))

        b_points = [
            (150,       Config.HEIGHT // 2 + 75),
            (150 + 75,  Config.HEIGHT // 2 + 75),
            (Config.WIDTH // 2,  Config.HEIGHT // 2 - 50),
            (650,  Config.HEIGHT // 2 - 50)
        ]
        pygame.gfxdraw.bezier(self.display, b_points, 10, (255,0,0))
        
        b_points = [
            (650,  Config.HEIGHT // 2 - 50),
            (650 + 50,  Config.HEIGHT // 2 - 50),
            (650 + 50,  Config.HEIGHT // 2),
        ]
        pygame.gfxdraw.bezier(self.display, b_points, 10, (255,255,0))

        b_points = [
            (650 + 50,  Config.HEIGHT // 2),
            (650 + 50,  Config.HEIGHT // 2 + 50),
            (650 + 25,  Config.HEIGHT // 2 + 50),
            (650,  Config.HEIGHT // 2 + 25),
            (650,  Config.HEIGHT // 2 + 25),
        ]
        pygame.gfxdraw.bezier(self.display, b_points, 10, (255,255,0))

        pygame.gfxdraw.circle(self.display, 650, Config.HEIGHT // 2, 50, (0,102,204))

        self.csm.draw(self.display)
        self.lem.draw(self.display)

    def update(self, delta_time):
        self.csm.velocity = pygame.Vector2(0.5, -0.175)
        self.lem.velocity = pygame.Vector2(0.5, -0.175)

        if self.csm.pos.y < Config.HEIGHT // 2 - 50:
            self.csm.velocity = pygame.Vector2(0.5, 0)
            self.lem.velocity = pygame.Vector2(0.5, 0)

        if self.csm.pos.x > 650:
            self.gameStateManager.set_current_scence('MoonOrbitScene')

        self.csm.update(delta_time)
        self.lem.update(delta_time)