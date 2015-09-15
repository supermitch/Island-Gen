#!/usr/bin/env python

from __future__ import division
import argparse
import collections
import itertools
import math
import random
import sys

import pygame
from pygame.locals import *
from noise import pnoise1, pnoise2, snoise2

import cell
import line
import render
from generator import IslandGenerator


def setup_args():
    parser = argparse.ArgumentParser('Island Generator')
    parser.add_argument('-p', '--pygame', action='store_true',
                        help='Render the Island using PyGame')
    parser.add_argument('-m', '--matplotlib', action='store_true',
                        help='Render the Island using Matplotlib')
    return parser.parse_args()


def setup_screen(screen_size=(900, 900)):
    surf = pygame.display.set_mode(screen_size, RESIZABLE)
    pygame.display.set_caption('Pyland Gen 1.0')
    return surf


def get_input():
    """ Wait for input. """
    for event in pygame.event.get():
        if event.type == QUIT:
            return 'quit', None
        elif event.type == KEYDOWN:
            shift = bool(pygame.key.get_mods() & pygame.KMOD_LSHIFT)
            if event.key == (K_s):
                return 'span', shift
            elif event.key == (K_o):
                return 'octaves', shift
            elif event.key == (K_c):
                return 'scale', shift
            elif event.key in (K_q, K_ESCAPE):
                return 'quit', None
            elif event.key == K_SPACE:
                return 'regen', None


def main():
    print('Pyland Gen 1.0')

    args = setup_args()

    generator = IslandGenerator(radius=200)

    if not args.pygame:
        island = generator.generate_island()
        print(island)
    else:
        pygame.init()
        clock = pygame.time.Clock()
        surface = setup_screen()

        result = 'regen'
        while True:
            clock.tick(10)

            if result == 'quit':
                pygame.quit()
                sys.exit()
            elif result == 'span':
                sign = +1 if shifted else -1
                generator.span += sign * 1
                result = 'regen'
            elif result == 'scale':
                sign = +1 if shifted else -1
                generator.scale += sign * 10
                result = 'regen'
            elif result == 'octaves':
                sign = +1 if shifted else -1
                generator.octaves += sign * 1
                result = 'regen'
            if result == 'regen':

                island = generator.generate_island()

                surface.fill(BLACK)
                render.render_island(surface, island)
                pygame.display.flip()

            result = get_input()
            if result and len(result) > 1:
                result, shifted = result


if __name__ == '__main__':
    main()

