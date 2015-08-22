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
    base = random.randint(0, 500)
    border = []
    for i in range(points):
        x = float(i) * span / points
        y = pnoise1(x + base, octaves) * 1.5
        y += pnoise1(x + base, octaves + 4) * 5
        border.append((i, y))
    return border


def gen_shore(border, radius=200, scale=40):
    """ Apply our border to our island. """
    radii = (radius + y * scale for _, y in border)  # Adjust radii
    angles = (x * math.pi / 180.0 for x, _ in border)  # Convert to radians
    return [(r * math.cos(theta) + 450, r * math.sin(theta) + 450) \
            for r, theta in zip(radii, angles)]  # To rectangular coords


def render_island(surf, points, radius):
    """ Renders an aaline of a series of points. """
    surf.fill(BLACK)
    pygame.draw.circle(surf, RED, (450, 450), radius, 1)  # Original centre

    pygame.draw.aalines(surf, BEIGE, True, points, False)  # Island shore
    for point in points:  # Data points
        pygame.draw.circle(surf, GREEN, (int(point[0]), int(point[1])), 1)

    pygame.display.flip()


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
            border = gen_border()
            point_list = gen_shore(border, radius=radius)
            render_island(surface, point_list, radius)
            flood_fill(surface)
        result = get_input()


if __name__ == '__main__':
    main()

