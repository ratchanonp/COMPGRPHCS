import pygame
import sys

from scences.earth_landing import EarthLandingScene
from scences.moon_landing import MoonLandingScene
from scences.moon_orbit import MoonOrbitScene
from scences.moon_orbit_back import MoonOrbitBackScene
from scences.transearth import TransEarthScene
from scences.translunarInjection import TranslunarInjection
from scences.overview import Overview
from scences.translunarcoast import TranslunarCoast
from scences.welcome import Welcome
from scences.s_ivb import S_IVB
from utils.config import Config

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('welcome')

        self.welcome = Welcome(self.screen, self.gameStateManager)
        self.TranslunarInjection = TranslunarInjection(self.screen, self.gameStateManager)
        self.S_IVB = S_IVB(self.screen, self.gameStateManager)
        self.TranslunarCoast = TranslunarCoast(self.screen, self.gameStateManager)
        self.MoonOrbitScene = MoonOrbitScene(self.screen, self.gameStateManager)
        self.MoonLandingScene = MoonLandingScene(self.screen, self.gameStateManager)
        self.MoonOrbitBackScene = MoonOrbitBackScene(self.screen, self.gameStateManager)
        self.TransEarthScene = TransEarthScene(self.screen, self.gameStateManager)
        self.EarthLandingScene = EarthLandingScene(self.screen, self.gameStateManager)

        self.scence = {
            'welcome': self.welcome,
            'TranslunarInjection': self.TranslunarInjection,
            'S_IVB': self.S_IVB,
            'TranslunarCoast': self.TranslunarCoast,
            'MoonOrbitScene': self.MoonOrbitScene,
            'MoonLandingScene': self.MoonLandingScene,
            'MoonOrbitSceneBack': self.MoonOrbitBackScene,
            'TransEarthScene': self.TransEarthScene,
            'EarthLandingScene': self.EarthLandingScene,
        }

    def render(self):
        self.scence[self.gameStateManager.get_current_scence()].render()
        pygame.display.update()

    def update(self, delta_time):
        self.scence[self.gameStateManager.get_current_scence()].update(delta_time)


    def run(self):
        delta_time = 0
        self.clock.tick(Config.FPS)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update(delta_time)
            self.render()
            delta_time = self.clock.tick(Config.FPS) / 1000.0
            print(delta_time)

class GameStateManager:
    def __init__(self, currentScence):
        self.currentScence = currentScence

    def get_current_scence(self):
        return self.currentScence

    def set_current_scence(self, currentScence):
        self.currentScence = currentScence

if __name__ == "__main__":
    game = Game()
    game.run()
