import math
import random
import sys

import pygame
from pygame.locals import *
from noise import pnoise1, pnoise2, snoise2


BEIGE = (200, 200, 100)
BLACK = (  0,   0,   0)
BLUE  = (  0,   0, 200)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
WHITE = (255, 255, 255)


def setup_screen(screen_size=(900, 900)):
    surf = pygame.display.set_mode(screen_size, RESIZABLE)
    pygame.display.set_caption('Pyland Gen 1.0')
    return surf


def gen_border():
    """
    Generate a border to apply to our island to build shoreline.

    Returns a list of (x, y) points of generated pnoise.
    """
    points = 360
    span = 8.0
    octaves = 8
    scale = 40
    base = random.randint(0, 500)
    border = []
    for i in range(points):
        x = float(i) * span / points
        y = pnoise1(x + base, octaves) * 1.5
        y += pnoise1(x + base, octaves + 4) * 5
        y *= scale
        border.append((i, y))
    return border


def scale_to_polar(border, radius=200):
    """ Apply our border to our island. """
    radii = (radius + y for _, y in border)  # Adjust radii
    angles = (x * math.pi / 180.0 for x, _ in border)  # Convert to radians
    return zip(radii, angles)


def polar_to_rectangular(polar_coords):
    return [(r * math.cos(theta) + 450, r * math.sin(theta) + 450) \
            for r, theta in polar_coords]  # To rectangular coords


def render_island(surf, coords, radius):
    """ Renders an aaline of a series of points. """
    pygame.draw.circle(surf, RED, (450, 450), radius, 1)  # Original centre
    pygame.draw.aalines(surf, BEIGE, True, coords, False)  # Island shore
    for point in coords:  # Data points
        pygame.draw.circle(surf, GREEN, (int(point[0]), int(point[1])), 1)


def render_border(surf, points):
    """ Renders an aaline of a series of points. """
    point_list = [(x + 50, y + 800) for x, y in points]
    pygame.draw.line(surf, BLUE, (50, 800), (410, 800), 1)  # x-axis
    pygame.draw.line(surf, BLUE, (50, 800), (50, 700), 1)  # y-axis

    pygame.draw.lines(surf, WHITE, False, point_list, 1)
    for x, y in point_list:  # points
        pygame.draw.circle(surf, RED, (int(x), int(y)), 1)


def flood_fill(surf):
    screen_size = surf.get_size()
    center_x, center_y = screen_size[0]/2, screen_size[1]/2
    start_color = surf.get_at((center_x, center_y))
    seen = []
    WHITE = (255, 255, 255, 255)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = center_x + dx, center_y + dy
        surf.set_at((x, y), WHITE)
        if surf.get_at((x, y)) == start_color:
            pass


def get_input():
    """ Wait for input. """
    for event in pygame.event.get():
        if event.type == QUIT:
            return 'quit'
        elif event.type == KEYDOWN:
            if event.key in (K_q, K_ESCAPE):
                return 'quit'
            elif event.key == K_SPACE:
                return 'regen'


def main():
    print('Pyland Gen 1.0')
    pygame.init()
    clock = pygame.time.Clock()
    surface = setup_screen()

    radius = 200
    result = 'regen'
    while True:
        clock.tick(10)

        if result == 'quit':
            pygame.quit()
            sys.exit()
        elif result == 'regen':
            surface.fill(BLACK)
            border = gen_border()  # Generate random noise
            render_border(surface, border)  # Draw it

            polar_coords = scale_to_polar(border, radius=radius)  # Wrap it around a circle
            rect_coords = polar_to_rectangular(polar_coords)  # Conver to (x, y)
            render_island(surface, rect_coords, radius)  # Graph island

            flood_fill(surface)  # Fill Island w/ color
            pygame.display.flip()

        result = get_input()


if __name__ == '__main__':
    main()

