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
    """ Renders a 2D graph of a series of points. """
    point_list = [(x + 50, -y + 800) for x, y in points]  # Up is -ve
    pygame.draw.line(surf, CYAN, (50, 800), (410, 800), 1)  # x-axis
    pygame.draw.line(surf, CYAN, (50, 800), (50, 700), 1)  # y-axis

    for x, y in point_list:  # points
        surf.set_at((int(x), int(y)), RED)


def render_lines(surf, line_cells):
    """ Renders an aaline of a series of points. """
    for cell in line_cells:
        surf.set_at(cell.tuple('2D'), YELLOW)


def flood_fill(surf):
    print('Flood filling')
    WHITE = (255, 255, 255, 255)
    screen_size = surf.get_size()
    center_x, center_y = screen_size[0]/2, screen_size[1]/2
    start_color = surf.get_at((center_x, center_y))  # Black
    seen = set()
    start = (center_x, center_y)
    stack = [start]
    while True:
        adjacent = False  # Has no adjacent unvisited pixels
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Check 4 neighbours
            x, y = start.x + dx, start.y + dy
            if (x, y) in seen:
                continue
            else:
                if surf.get_at((x, y)) == start_color:
                    adjacent = True
                    stack.append((x, y))
                    surf.set_at((x, y), WHITE)  # Set color to white
                    seen.add((x, y))
        if not adjacent:
            stack.pop()
        if not stack:
            break
        else:
            start = stack[-1]

