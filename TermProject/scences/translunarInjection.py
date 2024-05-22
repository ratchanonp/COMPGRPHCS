import pygame

from objects.earth import Earth
from objects.rocket import Rocket
from utils.config import Config
from utils.utils import Circle, Point, TextDrawer

class TranslunarInjection:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        
        self.earth_pos = pygame.Vector2(Config.WIDTH // 2, Config.HEIGHT // 2)
        self.earth = Earth(self.earth_pos, (200, 200))
        self.background = pygame.image.load("assets/space.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (Config.WIDTH, Config.HEIGHT))

        self.earth_parking_orbit = Circle(Point(self.earth_pos[0], self.earth_pos[1]), 200)
        
        self.orbit_angle = 180
        self.rocket = Rocket(pygame.Vector2(self.earth_parking_orbit.get_point(self.orbit_angle), pygame.sprite.Group()))
        self.rocket.rotate(180)

    def render(self):
        self.display.blit(self.background, (0, 0))
        self.earth.draw(self.display)

        # Draw circle dashed line for moon orbit
        self.earth_parking_orbit.draw_dashed_circle(self.display, (255, 255, 255), 5, 5)
        self.rocket.draw(self.display)
        TextDrawer("assets/nasalization-rg.ttf", 32, (255, 255, 255), self.display).draw("Trans Lunar Injection", Config.WIDTH // 2, Config.HEIGHT - 50)


    def update(self, delta_time):
        if self.orbit_angle > 80:
            # self.rocket.rotate(1)
            self.rocket.move(self.earth_parking_orbit.get_point(self.orbit_angle))
            self.orbit_angle -= 0.25
        else:
            if self.rocket.angle != 270:
                self.rocket.rotate(90)
            self.rocket.engine_on = True
            self.rocket.velocity = pygame.Vector2(1.5, -0.5)
            self.rocket.update(delta_time)

        if self.rocket.pos[0] > Config.WIDTH:
            self.gameStateManager.set_current_scence("S_IVB")
