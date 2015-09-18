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

    def height_fill(self):
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    print(tile.height)
        return

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i, row in enumerate(self.tiles):
            for j, tile in enumerate(row):
                if tile and tile.height == -1:
                    averages = []
                    for r in range(1, 5):
                        ring_total = 0
                        neighbour_count = 0
                        ring_avg = 0
                        for dx, dy in deltas:  # Check 8 neighbours
                            dx, dy = dx * r, dy * r
                            x, y = i + dx, j + dy
                            print('x, y: {}, {}'.format(x, y))
                            try:
                                value = self.tiles[x][y].height
                                print('value: {}'.format(value))
                            except (IndexError, AttributeError):
                                continue
                            if value == -1:
                                continue
                            ring_total += value
                            neighbour_count += 1
                        if ring_total:
                            ring_avg = ring_total/neighbour_count
                            averages.append(ring_avg * 9 / r ** 0.9)  # Further away == less impact
                    if averages:
                        tile.height = sum(averages)/len(averages)










