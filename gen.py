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

def main():
    print('Pyland Gen 1.0')
    map = gen_map()
    render(map)

if __name__ == '__main__':
    main()

