import sys

import pygame
from pygame.locals import *

def gen_map(width=500, height=500):
    """ Returns a map of width x height tiles. """
    map = [[None for x in range(width)] for y in range(height)]
    return map

def render(map):
    BG_COLOR = (00, 00, 00)
    screen_size = len(map), len(map[0])
    surf = pygame.display.set_mode(screen_size, RESIZABLE)
    pygame.display.set_caption('Pyland Gen 1.0')
    surf.fill(BG_COLOR)
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

