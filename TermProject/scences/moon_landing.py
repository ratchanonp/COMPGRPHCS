import pygame

from objects.csm import CSM
from objects.lem import LEM
from objects.moon import Moon
from utils.config import Config
from utils.utils import Circle, Point


class MoonLandingScene:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        self.background = pygame.image.load("assets/space.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (Config.WIDTH, Config.HEIGHT))

        self.moon = Moon(pygame.Vector2(Config.WIDTH // 2, Config.HEIGHT + 100), (600, 600))
        self.lem = LEM(pygame.Vector2(Config.WIDTH // 2, 200), pygame.sprite.Group())

        self.usaflag = pygame.image.load("assets/usa.png").convert_alpha()
        self.usaflag = pygame.transform.scale(self.usaflag, (100, 100))
        self.usaflag = pygame.transform.rotate(self.usaflag, -15)

        self.is_landed = False
        self.is_flag_raised = False

        self.counter = 0

    def render(self):
        self.display.blit(self.background, (0, 0))

        self.moon.draw(self.display)
        self.lem.draw(self.display)

        if self.is_flag_raised:
            self.display.blit(self.usaflag, (Config.WIDTH // 2 + 50, Config.HEIGHT // 2 + 50))


    def update(self, delta_time):
        self.counter += delta_time
        print(self.counter)
        if self.lem.pos.y < Config.HEIGHT - 200:
            self.lem.velocity = pygame.math.Vector2(0, 1)
            self.lem.engine_on = True
        else:
            self.lem.engine_on = False
            
            if self.is_landed == False:
                self.is_landed = True
                self.counter = 0

            self.lem.velocity = pygame.math.Vector2(0, 0)
        
        if self.is_landed and self.counter > 1:
            self.is_flag_raised = True
        if self.is_landed and self.counter > 3:
            self.lem.engine_on = True
            self.lem.velocity = pygame.math.Vector2(0, -1)

        if self.lem.pos.y < 0:
            self.gameStateManager.set_current_scence("MoonOrbitSceneBack")
            
        self.lem.update(delta_time)