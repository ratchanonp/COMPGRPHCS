import pygame
from utils.config import Config
from utils.utils import TextDrawer


class Welcome:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.textDrawer = TextDrawer("assets/nasalization-rg.ttf", 32, (255, 255, 255), display)
        self.counter = 0

    def render(self):
        self.textDrawer.draw("Welcome to the Artemis Program", Config.WIDTH // 2, Config.HEIGHT // 2 - 50)
        self.textDrawer.draw("How we go to the moon", Config.WIDTH // 2, Config.HEIGHT // 2)

    def update(self, delta_time):
        self.counter += delta_time
        if self.counter > 3:
            self.gameStateManager.set_current_scence('TranslunarInjection')