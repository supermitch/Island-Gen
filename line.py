import math


class Line(object):
    """
    Representation of a line joining two points.
    """
    def __init__(self, start, end):
        """
        Initialize with start and end Cell objects.
        """
        self.start = start
        self.end = end

    def length(self, squared=False):
        """
        Calculate distance between start & end using Pythagorean theorem.
        """
        d_squared = (self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2
        if squared:
            return d_squared
        else:
            return math.sqrt(d_squared)

    def discretize(self):
        """
        Turn a line into a list of integer (x, y) Cells forming a line.
        """
        max_length = abs(self.end.y - self.start.y) + abs(self.end.x - self.start.x) + 1  # Plus start

        start = self.start
        results = [start]
        seen = set()
        while start != (self.end.x, self.end.y):  # Check in 2D only
            neighbours = start.neighbours()
            neighbours = cell.restrict_quadrants(neighbours, start, self.end)

            next_cell = None
            min_distance = float('inf')
            for cell in neighbours:
                if cell in seen:  # Don't go backwards
                    continue
                intersection = geometry.right_intersection(cell, self)
                distance = cell.distance(intersection)
                if distance < min_distance:
                    min_distance = distance
                    next_cell = cell
            results.append(next_cell)
            if len(results) > max_length:  # Failed!
                print('Found too many cells. Aborting.')
                return None
            seen.add(next_cell)
            start = next_cell
        return results


    def __str__(self):
        return '({}, {})'.format(self.start, self.end)

    def __repr__(self):
        return 'line.Line({}, {})'.format(self.start, self.end)

