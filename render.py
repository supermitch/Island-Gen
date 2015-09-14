import pygame
from pygame.locals import *


BEIGE = (200, 200, 100)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)


def render_island(surf, coords, radius):
    """ Renders an aaline of a series of points. """
    pygame.draw.circle(surf, RED, (450, 450), radius, 1)  # Original centre
    # pygame.draw.aalines(surf, BEIGE, True, coords, False)  # Island shore
    for point in coords:  # Data points
        x, y = int(point.x), int(point.y)
        surf.set_at((x, y), GREEN)  # Color pixel


def render_peak(surf, point):
    pygame.draw.circle(surf, WHITE, (point.x, point.y), 3, 1)  # Peak centre


def render_shore_noise(surf, points):
    """ Renders an aaline of a series of points. """
    point_list = [(x + 50, -y + 800) for x, y in points]  # Up is -ve
    pygame.draw.line(surf, CYAN, (50, 800), (410, 800), 1)  # x-axis
    pygame.draw.line(surf, CYAN, (50, 800), (50, 700), 1)  # y-axis

    for x, y in point_list:  # points
        surf.set_at((int(x), int(y)), RED)


def render_lines(surf, line_cells):
    """ Renders an aaline of a series of points. """
    for cell in line_cells:
        surf.set_at(cell.tuple('2D'), YELLOW)

