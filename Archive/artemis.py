import pygame
import sys
import RPGtext

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
EARTH_POS = (200, 300)
MOON_POS = (600, 300)
WHITE = (255, 255, 255)

EARTH_FILE = "TermProject/assets/earth.png"
MOON_FILE = "TermProject/assets/moon.png"
BACKGROUND_FILE = "TermProject/assets/space.jpg"
earth_image = pygame.image.load(EARTH_FILE)
moon_image = pygame.image.load(MOON_FILE)

TEXTBOX = "TermProject/assets/TextFrame.png"
textbox = pygame.image.load(TEXTBOX)


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))



def draw_text(text, font_size, color, x, y, centered=True):

    font = pygame.font.Font("TermProject/assets/nasalization-rg.ttf", font_size)
    text = font.render(text, True, color)

    if centered:
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    else:
        screen.blit(text, (x, y))

def draw_spline(screen, color, control_points):
    # Draw Cubic Bezier Curve
    for i in range(0, 1000):
        t = i / 1000
        x = (1-t)**3 * control_points[0][0] + 3*t*(1-t)**2 * control_points[1][0] + 3*t**2*(1-t) * control_points[2][0] + t**3 * control_points[3][0]
        y = (1-t)**3 * control_points[0][1] + 3*t*(1-t)**2 * control_points[1][1] + 3*t**2*(1-t) * control_points[2][1] + t**3 * control_points[3][1]
        pygame.draw.circle(screen, color, (int(x), int(y)), 1)


def scence_1():
    

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with background image
    background = pygame.image.load(BACKGROUND_FILE)
    # zoom the background image to fit the screen
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))

    # # Set size
    earth_image = pygame.transform.scale(earth_image, (80, 80))
    moon_image = pygame.transform.scale(moon_image, (30, 30))

    # # Set image center as the position
    earth_rect = earth_image.get_rect(center=EARTH_POS)
    moon_rect = moon_image.get_rect(center=MOON_POS)

    # # Draw the Earth and Moon
    screen.blit(earth_image, earth_rect)
    screen.blit(moon_image, moon_rect)

    draw_text("Earth", 36, WHITE, EARTH_POS[0]-30, EARTH_POS[1]-50)

    # # Draw the Bezier Curve starting from Earth to Moon
    # controls_points = [(EARTH_POS[0], EARTH_POS[1]), (EARTH_POS[0]+100, EARTH_POS[1]-100), (MOON_POS[0]-100, MOON_POS[1]+100), (MOON_POS[0], MOON_POS[1])]
    # draw_spline(screen, WHITE, controls_points)

    
    # Draw text
    draw_text("NASA", 36, WHITE, WIDTH//2, HEIGHT//2)

    # Flip the display
    pygame.display.flip()

    # Move text up
    if EARTH_POS[1] > 100:
        EARTH_POS = (EARTH_POS[0], EARTH_POS[1]-1)
        MOON_POS = (MOON_POS[0], MOON_POS[1]-1)
    
    pygame.time.wait(10)  # 10ms delay
