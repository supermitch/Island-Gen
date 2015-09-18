from __future__ import division

import pygame
from pygame.locals import *


BEIGE = (200, 200, 100)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)


class Renderer(object):

    def __init__(self, screen_size=(900, 900)):
        self.screen_size = screen_size
        self.surface = pygame.display.set_mode(screen_size, RESIZABLE)
        pygame.display.set_caption('Pyland Gen 1.0')

    def render_shore(self, coords, radius):
        """ Renders an aaline of a series of points. """
        pygame.draw.circle(self.surface, RED, (450, 450), int(radius), 1)  # Original centre
        # pygame.draw.aalines(self.surface, BEIGE, True, coords, False)  # Island shore
        for point in coords:  # Data points
            x, y = int(point.x), int(point.y)
            self.surface.set_at((x, y), GREEN)  # Color pixel

    def render_peak(self, point):
        pygame.draw.circle(self.surface, WHITE, (point.x, point.y), 3, 1)  # Peak centre

    def render_shore_noise(self, points):
        """ Renders a 2D graph of a series of points. """
        point_list = [(x + 50, -y + 800) for x, y in points]  # Up is -ve
        pygame.draw.line(self.surface, CYAN, (50, 800), (410, 800), 1)  # x-axis
        pygame.draw.line(self.surface, CYAN, (50, 800), (50, 700), 1)  # y-axis

        for x, y in point_list:  # points
            self.surface.set_at((int(x), int(y)), RED)

    def render_lines(self, line_cells):
        """ Renders series of cells as pixels. """
        for cell in line_cells:
            self.surface.set_at(cell.tuple('2D'), YELLOW)

    def render_tiles(self, tiles):
        """ Renders tiles with varying shades of grey depending on height. """
        for row in tiles:
            for tile in row:
                if tile is not None:
                    if tile.height < 0:
                        color = (0, 100, 0)
                    else:
                        z = max(0, tile.height)
                        color = tuple([z * 255] * 3)
                    self.surface.set_at((tile.x, tile.y), color)

    def render_island(self, island):
        self.surface.fill(MAGENTA)
        # self.render_shore_noise(island.shore_noise)  # Draw it
        # self.render_shore(island.rect_shore, island.radius)  # Graph island
        # self.render_peak(island.peak)
        # for spoke in island.spokes:
        #     self.render_lines(spoke)
        # for _line in island.shore_lines:
        #     self.render_lines(_line)
        # render.flood_fill(self.surface, island)  # Fill Island w/ color
        self.render_tiles(island.tiles)
        pygame.display.flip()

