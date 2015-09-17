from __future__ import division

from tile import Tile


class Island(object):

    def __init__(self, width=900, height=900):
        self.radius = None
        self.shore_noise = None
        self.rect_shore = None
        self.shore_lines = None
        self.peak = None
        self.spokes = None
        self.tiles = [[None] * width for _ in range(height)]

    def cells_to_tiles(self, *cells):
        """
        Apply a Cell(x, y, z) into an Island tile height.
        """
        for x, y, z in cells:
            self.tiles[x][y] = Tile(x, y, z)

    def normalize(self):
        max_height = 1
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    if tile.height > max_height:
                        max_height = tile.height
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    tile.height = float(tile.height) / max_height

