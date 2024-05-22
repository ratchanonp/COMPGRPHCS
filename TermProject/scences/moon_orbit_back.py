import pygame

from objects.csm import CSM
from objects.lem import LEM
from objects.moon import Moon
from utils.config import Config
from utils.utils import Circle, Point


class MoonOrbitBackScene:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        self.background = pygame.image.load("assets/space.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (Config.WIDTH, Config.HEIGHT))

        self.moon = Moon(pygame.Vector2(Config.WIDTH // 2, Config.HEIGHT // 2), (100, 100))

        self.csm = CSM(pygame.Vector2(Config.WIDTH // 2, Config.HEIGHT // 2 - 225), pygame.sprite.Group())
        self.lem = LEM(pygame.Vector2(Config.WIDTH // 2, Config.HEIGHT // 2 - 50), pygame.sprite.Group())
        self.csm.rotate(-90)

        self.lunar_parking_orbit = Circle(Point(Config.WIDTH // 2, Config.HEIGHT // 2), 200)

        self.orbit_angel = 180
        self.orbit_count = 0

        self.meetup = False
   
    def render(self):
        self.display.blit(self.background, (0, 0))

        self.moon.draw(self.display)
        self.csm.draw(self.display)
        self.lem.draw(self.display)
        self.lunar_parking_orbit.draw_dashed_circle(self.display, (0, 102, 204), 5, 5)


    def update(self, delta_time):
        new_pos = self.lunar_parking_orbit.get_point(self.orbit_angel)
        self.orbit_angel += 0.5
        self.orbit_angel %= 360


        if not self.meetup:
            self.csm.move(pygame.Vector2(new_pos.x, new_pos.y - 25))
            self.lem.velocity = pygame.math.Vector2(0, -0.75)
       
        else:
            if self.orbit_count == 0:
                self.lem.velocity = pygame.math.Vector2(0, 0)
                self.csm.engine_on = True

                self.csm.move(pygame.Vector2(new_pos.x, new_pos.y - 25))
                self.lem.move(pygame.Vector2(new_pos.x, new_pos.y + 25))


        if not self.meetup:
            if self.lem.rect.colliderect(self.csm.rect):
                self.meetup = True

        if self.orbit_angel == 90:
            self.orbit_count += 1
            
            self.csm.rotate(-90)
            # self.lem.rotate(-90)

            self.csm.velocity = pygame.math.Vector2(-1.5, -0.75)
            self.lem.velocity = pygame.math.Vector2(-1.5, 0.75)

        if self.csm.pos.x < 0:
            self.gameStateManager.set_current_scence('TransEarthScene')

        self.csm.update(delta_time)
        self.lem.update(delta_time)