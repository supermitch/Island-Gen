#!/usr/bin/env python

from __future__ import division
import collections
import itertools
import math
import random
import sys

import pygame
from pygame.locals import *
from noise import pnoise1, pnoise2, snoise2

import cell

BEIGE = (200, 200, 100)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)


def setup_screen(screen_size=(900, 900)):
    surf = pygame.display.set_mode(screen_size, RESIZABLE)
    pygame.display.set_caption('Pyland Gen 1.0')
    return surf


class IslandGenerator():
    """ Generates a random graph of noise. (Not really an Island) """
    def __init__(self):
        """ Initialize some pnoise generator defaults. """
        self.span = 8.0
        self.octaves = 8
        self.scale = 40

    def gen_border(self, points):
        """
        Generate a border to apply to our island to build shoreline.

        Returns a list of (x, y) points of generated pnoise.

        - Points is the number of points in the returned list.
        """
        base = random.randint(0, 5000)
        border = []
        for i in range(points):
            x = float(i) * self.span / points
            y = pnoise1(x + base, self.octaves) * 1
            y += pnoise1(x + base, self.octaves + 4) * 2
            y *= self.scale
            border.append((i, y))
        return border

    def define_peak(self, polar_shore, scale=20):
        while True:
            alpha = 4.0
            theta = 1.0
            beta = 1.0 / theta
            var = random.gammavariate(alpha, beta)
            radius = var * scale
            angle = random.randint(0, 360)  # Random orientation
            for r, _ in polar_shore:
                if r < radius:  # Check that peak is within shoreline
                    break  # Repeat generation
            else:
                break  # Exit loop
        height = random.randint(20, 200)
        print(height)
        x, y = polar_to_rectangular((radius, angle))
        return (x, y, height)

    def gen_spokes(self, rect_shore, peak):
        """
        Generate a list of lines (spokes) from start to end positions.
        """
        Spoke = collections.namedtuple('Spoke', 'start, end')
        return [Spoke(point, peak) for point in rect_shore[::60]]



def apply_noise_to_base(border, radius=200):
    """ Apply our noisy 'border' to our base circle. """
    radii = (radius + y for _, y in border)  # Adjust radii
    angles = (x * math.pi / 180.0 for x, _ in border)  # Convert to radians
    return zip(radii, angles)


def polar_to_rectangular(polar_coords, offset_x=450, offset_y=450):
    r, theta = polar_coords
    return int(r * math.cos(theta) + offset_x), int(r * math.sin(theta) + offset_y)


def apply_peak_height(spoke_noise, peak):
    output_noise = []
    for i, (x, y) in enumerate(spoke_noise):
        dy = i / len(spoke_noise) * peak[2]
        y += dy
        output_noise.append((x, y))
    print(dy)
    return output_noise


def render_island(surf, coords, radius):
    """ Renders an aaline of a series of points. """
    pygame.draw.circle(surf, RED, (450, 450), radius, 1)  # Original centre
    # pygame.draw.aalines(surf, BEIGE, True, coords, False)  # Island shore
    for point in coords:  # Data points
        x, y = int(point[0]), int(point[1])
        surf.set_at((x, y), GREEN)  # Color pixel


def render_peak(surf, pos):
    pygame.draw.circle(surf, WHITE, (pos[0], pos[1]), 3, 1)  # Peak centre


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
        surf.set_at(cell, YELLOW)


def flood_fill(surf):
    print('Flood filling')
    WHITE = (255, 255, 255, 255)
    screen_size = surf.get_size()
    center_x, center_y = screen_size[0]/2, screen_size[1]/2
    start_color = surf.get_at((center_x, center_y))  # Black
    seen = set()
    start = (center_x, center_y)
    stack = [start]
    neighbours = list(itertools.product([0, 1, -1], repeat=2))
    while True:
        adjacent = False  # Has no adjacent unvisited pixels
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Check 4 neighbours
            x, y = start[0] + dx, start[1] + dy
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
    pygame.init()
    clock = pygame.time.Clock()
    surface = setup_screen()

    generator = IslandGenerator()
    radius = 200
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
            surface.fill(BLACK)
            shore_noise = generator.gen_border(points=360)  # Generate random noise
            render_shore_noise(surface, shore_noise)  # Draw it

            polar_shore = apply_noise_to_base(shore_noise, radius=radius)  # Wrap it around a circle
            rect_shore = [polar_to_rectangular(x) for x in polar_shore]  # Conver to (x, y)
            peak = generator.define_peak(polar_shore)
            lines = generator.gen_spokes(rect_shore, peak)
            spokes = [cell.discretize_line(x.start, x.end) for x in lines]
            for spoke in spokes:
                render_lines(surface, spoke)
                spoke_noise = generator.gen_border(points=len(spoke))
                spoke_noise = apply_peak_height(spoke_noise, peak)
                spoke_cells = [(x, y, z) for (x, y), (_, z) in zip(spoke, spoke_noise)]

            render_island(surface, rect_shore, radius)  # Graph island
            render_peak(surface, peak)

            # flood_fill(surface)  # Fill Island w/ color
            pygame.display.flip()

        result = get_input()
        if result and len(result) > 1:
            result, shifted = result


if __name__ == '__main__':
    main()

