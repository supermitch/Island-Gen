import math
import random
import sys

import pygame
from pygame.locals import *
from noise import pnoise1, pnoise2, snoise2


def gen_border():
    """ Generate a border to apply to our island to build shoreline. """
    points = 360
    span = 8.0
    octaves = 3
    base = random.randint(0, 500)
    border = []
    for i in range(points):
        x = float(i) * span / points
        y = pnoise1(x + base, octaves) * 1.5
        y += pnoise1(x + base, octaves + 4) * 5
        border.append((i, y))
    print(len(border))
    return border


def gen_shore(border, radius=300, scale=75):
    """ Apply our border to our island. """
    radii = (radius + y * scale for _, y in border)
    angles = (x * math.pi / 180.0 for x, _ in border)
    return [(radius * math.cos(theta) + 400, radius * math.sin(theta) + 400) \
            for radius, theta in zip(radii, angles)]


def gen_random_map(width=500, height=500):
    """ Returns a map of width x height tiles. """
    # Initialize map to matrix of None
    map = [[None for x in range(width)] for y in range(height)]
    for row in range(height):
        for col in range(width):
            # Random R, G & B
            map[row][col] = (random.randint(0, 255), random.randint(0, 255),
                             random.randint(0, 255))
    return map


def setup_screen(screen_size=(900, 900)):
    surf = pygame.display.set_mode(screen_size, RESIZABLE)

    pygame.display.set_caption('Pyland Gen 1.0')

    BG_COLOR = (00, 00, 00)
    surf.fill(BG_COLOR)

    return surf


def render_island(surf, points):
    """ Renders and aaline of a series of points. """
    color = (200, 200, 100)
    pygame.draw.aalines(surf, color, True, points, False)
    pygame.display.flip()


def render():
    # Draw tiles
    for i in range(screen_size[0]):
        for j in range(screen_size[1]):
            size = (3, 3)
            px = pygame.Surface(size)
            color = map[i][j]
            px.fill(color)
            pos = (i * size[0], j * size[1])
            surf.blit(px, pos)


def flood_fill(surf):
    screen_size = surf.get_size()
    center_x, center_y = screen_size[0]/2, screen_size[1]/2

    start_color = surf.get_at((center_x, center_y))
    print(start_color)
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
            terminate()
        elif event.type == KEYDOWN:
            if event.key in (K_q, K_ESCAPE):
                terminate()
            elif event.key == K_SPACE:
                # TODO: regenerate planet
                pass


def terminate():
    pygame.quit()
    sys.exit()


def main():
    print('Pyland Gen 1.0')
    pygame.init()
    border = gen_border()
    point_list = gen_shore(border)
    surface = setup_screen()

    render_island(surface, point_list)
    flood_fill(surface)

    print('Waiting for input')
    while True:
        get_input()


if __name__ == '__main__':
    main()

