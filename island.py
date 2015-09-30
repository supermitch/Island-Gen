from __future__ import division
import random

import matrix
from tile import Tile


class Island(object):

    def __init__(self, width=300, height=300):
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

    def flood_fill(self, start=None):
        """
        Sets all None tiles to Tile(x, y, -1) within the island shore.
        """
        if self.peak:
            center_x, center_y = self.peak.x, self.peak.y
        elif start:
            center_x, center_y = start.x, start.y
        else:
            raise ValueError('Must define peak or start cell for flood fill.')
        print('Flood filling')
        seen = set()
        start = (center_x, center_y)
        stack = [start]
        while True:
            adjacent = False  # Has no adjacent unvisited pixels
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Check 4 neighbours
                x, y = start[0] + dx, start[1] + dy
                if (x, y) in seen:
                    continue
                else:
                    if self.tiles[x][y] is None:
                        adjacent = True
                        stack.append((x, y))
                        self.tiles[x][y] = Tile(x, y, -1)  # Set height -1
                        seen.add((x, y))
            if not adjacent:
                stack.pop()
            if not stack:
                break
            else:
                start = stack[-1]

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
                    if tile.height > 0:  # Ignore negative tiles
                        tile.height = float(tile.height) / max_height
                    elif tile.height < 0:
                        tile.height = -1

    def height_fill(self):
        attempt = 0
        last_empty_count = 0
        while self.has_empty:
            empties = self.empties()
            empty_count = len(empties)
            print('Island has {} empty tiles'.format(empty_count))
            if empty_count == last_empty_count:
                attempt += 1
            last_empty_count = empty_count
            if attempt > 10: break;

            random.shuffle(empties)
            while empties:
                i, j = empties.pop()
                tile = self.tiles[i][j]
                if tile and tile.height == -1:
                    averages = []
                    for span in range(1, 5):
                        ring_total = 0
                        neighbour_count = 0
                        ring_avg = 0
                        for x, y in matrix.find_neighbours_2D(self.tiles, (i, j), span):
                            try:
                                value = self.tiles[x][y].height
                                # print('value: {}'.format(value))
                            except (IndexError, AttributeError):
                                continue
                            if value in [-1,]:
                                continue
                            ring_total += value
                            neighbour_count += 1
                        if ring_total:
                            ring_avg = ring_total/neighbour_count
                            # averages.append(ring_avg * 9 / span ** 0.9)  # Further away == less impact
                            averages.append(ring_avg)  # Further away == less impact
                    if averages:
                        # print(averages)
                        overall = sum(averages)/len(averages)
                        # print('overall: {}'.format(overall))
                        tile.height = overall

    @property
    def has_empty(self):
        return any(True if tile.height == -1 else False
                   for row in self.tiles for tile in row if tile is not None)

    def empties(self):
        empty_cells = []
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] is not None and self.tiles[i][j].height == -1:
                    empty_cells.append((i, j))
        return empty_cells

