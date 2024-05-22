import math
import pygame
import numpy as np


class TextDrawer:
    def __init__(self, font_path, font_size, color, display):
        self.font = pygame.font.Font(font_path, font_size)
        self.color = color
        self.display = display

    def draw(self, text, x, y):
        text = self.font.render(text, True, self.color)
        text_rect = text.get_rect(center=(x, y))
        self.display.blit(text, text_rect)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, display, color, width):
        pygame.draw.line(display, color, (self.start.x,
                         self.start.y), (self.end.x, self.end.y), width)

    def draw_dashed_line(self, display, color, width, dash_length):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        distance = max(abs(dx), abs(dy))
        dx = dx / distance
        dy = dy / distance
        x = self.start.x
        y = self.start.y
        for i in range(int(distance // dash_length)):
            pygame.draw.line(display, color, (x, y), (x + dx *
                             dash_length, y + dy * dash_length), width)
            x += 2 * dx * dash_length
            y += 2 * dy * dash_length


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self, display, color, width):
        pygame.draw.circle(display, color, (self.center.x,
                           self.center.y), self.radius, width)

    def draw_dashed_circle(self, display, color, width, dash_length):
        for i in range(0, 360, 2 * dash_length):
            x = self.center.x + self.radius * math.cos(math.radians(i))
            y = self.center.y + self.radius * math.sin(math.radians(i))
            x2 = self.center.x + self.radius * \
                math.cos(math.radians(i + dash_length))
            y2 = self.center.y + self.radius * \
                math.sin(math.radians(i + dash_length))
            pygame.draw.line(display, color, (x, y), (x2, y2), width)

    def get_point(self, angle):
        x = self.center.x + self.radius * math.cos(math.radians(angle))
        y = self.center.y + self.radius * math.sin(math.radians(angle))
        return pygame.Vector2(x, y)


class Spline:
    def __init__(self):
        self.points: list[Point] = []
        self.line_duration: float = 5
        self.M_BEZ = np.array(
            [[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]])
        self.counter = 0

    def add_control_point(self, point: Point):
        self.points.append(point)

    def draw(self, display):
        pass

    def update(self, delta_time):
        self.counter += delta_time
        if self.counter > self.line_duration:
            self.counter = 0

    def get_point(self, t):
        PX = np.array([p.x for p in self.points])
        PY = np.array([p.y for p in self.points])

        u_vector = np.array([t ** 3, t ** 2, t, 1])
        x = np.dot(u_vector, np.dot(self.M_BEZ, PX))
        y = np.dot(u_vector, np.dot(self.M_BEZ, PY))

        return Point(x, y)
