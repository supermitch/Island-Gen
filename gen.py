import random
import sys

import pygame
from pygame.locals import *

def gen_map(width=500, height=500):
    """ Returns a map of width x height tiles. """
    map = [[None for x in range(width)] for y in range(height)]
    for row in range(height):
        for col in range(width):
            # Choose a random color, for now
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
    map = gen_map()
    render(map)
    while True:
        get_input()


if __name__ == '__main__':
    main()

