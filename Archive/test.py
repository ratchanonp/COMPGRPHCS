import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Bonanza")

# Colors
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

# --- Ball Class ---
class Ball:
    def __init__(self, color, radius, x, y, x_speed, y_speed, rotation_speed=2):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotation_angle = 0
        self.rotation_speed = rotation_speed
        self.scale = 1

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

        # Bounce off edges of screen
        if self.x + self.radius > width or self.x - self.radius < 0:
            self.x_speed *= -1
        if self.y + self.radius > height or self.y - self.radius < 0:
            self.y_speed *= -1

        self.rotation_angle += self.rotation_speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        # Optional: Draw a feature on the ball to show rotation
        feature_x = self.x + self.radius * math.cos(math.radians(self.rotation_angle))
        feature_y = self.y + self.radius * math.sin(math.radians(self.rotation_angle))
        pygame.draw.circle(screen, white, (feature_x, feature_y), self.radius // 5)

# --- Create Balls ---
main_ball = Ball(red, 30, 50, 50, 5, 3)
small_balls = [
    Ball(blue, 15, width // 2, height // 2, 4, -2, 5),
    Ball(green, 15, width // 2 + 50, height // 2, -3, 4),
    Ball(yellow, 15, width // 2 - 50, height // 2, 2, 3, 8)
]

# --- Game Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update ---
    main_ball.update()

    # Smaller balls appear after a delay and follow the main ball
    if pygame.time.get_ticks() > 3000:  # 3 seconds in milliseconds
        for ball in small_balls:
            ball.update()

    # --- Draw ---
    screen.fill((0, 0, 0))  # Clear the screen

    main_ball.draw()

    if pygame.time.get_ticks() > 3000:  # 3 seconds in milliseconds
        for ball in small_balls:
            ball.draw()

    pygame.display.flip()

    pygame.time.Clock().tick(60)  # Limit frame rate to 60 FPS

pygame.quit()