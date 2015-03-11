import math
import random
import sys

import pygame
from noise import pnoise1, pnoise2, snoise2
from pygame.locals import *


def gen_border():
    """ Generate a border to apply to our island to build shoreline. """
    points = 360
    span = 5.0
    octaves = 1
    base = 0
    border = []
    for i in range(points):
        x = float(i) * span / points
        y = pnoise1(x + base, octaves)
        border.append((i, y))
    print(len(border))
    return border

def gen_shore(border, radius=300, scale=75):
    """ Apply our border to our island. """
    radii = (radius + y * scale for _, y in border)
    angles = (x * math.pi / 180.0 for x, _ in border)
    points = [(radius * math.cos(theta), radius * math.sin(theta)) \
             for radius, theta in zip(radii, angles)]
    return points

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

def render(map):
    screen_size = len(map), len(map[0])
    surf = pygame.display.set_mode(screen_size, RESIZABLE)

    pygame.display.set_caption('Pyland Gen 1.0')

    BG_COLOR = (00, 00, 00)
    surf.fill(BG_COLOR)

    # Draw tiles
    for i in range(screen_size[0]):
        for j in range(screen_size[1]):
            size = (3, 3)
            px = pygame.Surface(size)
            color = map[i][j]
            px.fill(color)
            pos = (i * size[0], j * size[1])
            surf.blit(px, pos)

    pygame.display.flip()

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
    map = gen_random_map()
    render(map)
    while True:
        get_input()


if __name__ == '__main__':
    main()

