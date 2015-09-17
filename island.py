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
        print('Flood filling')
        if self.peak:
            center_x, center_y = self.peak.x, self.peak.y
        elif start:
            center_x, center_y = start.x, start.y
        else:
            raise ValueError('Must define peak or start cell for flood fill.')
        start_color = self.surface.get_at((center_x, center_y))  # Black
        seen = set()
        start = (center_x, center_y)
        stack = [start]
        while True:
            adjacent = False  # Has no adjacent unvisited pixels
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Check 4 neighbours
                x, y = start.x + dx, start.y + dy
                if (x, y) in seen:
                    continue
                else:
                    if self.surface.get_at((x, y)) == start_color:
                        adjacent = True
                        stack.append((x, y))
                        self.surface.set_at((x, y), WHITE)  # Set color to white
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
                    tile.height = float(tile.height) / max_height

