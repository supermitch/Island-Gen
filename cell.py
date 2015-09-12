from __future__ import division

import collections
import itertools
import math


class Cell(object):
    """
    Representation of a 2D or 3D point in space.
    """

    def __init__(self, x=0, y=0, z=0):
        """
        Initialize with any of x, y or z coordinates.
        """
        if isinstance(x, tuple):
            self.x, self.y, self.z = 0, 0, 0  # init
            if len(x) > 0:
                self.x = x[0]
            if len(x) > 1:
                self.y = x[1]
            if len(x) > 2:
                self.z = x[2]
        else:
            self.x = x
            self.y = y
            self.z = z

    def neighbours(self, ndims=2):
        """
        Get 8 neighbouring cell coords to a start cell.
        """
        offsets = list(itertools.product([0, 1, -1], repeat=2))
        del offsets[offsets.index((0, 0))]  # Don't include self
        return [Cell(self.x + dx, self.y + dy, self.z) for dx, dy in offsets]

    def distance(self, point, squared=False, ndims=2):
        """
        Calculate distance between two points using Pythagorean theorem.
        """
        d_squared = (point.x - self.x) ** 2 + (point.y - self.y) ** 2
        if squared:
            return d_squared
        else:
            return math.sqrt(d_squared)

    def to_tuple(self, ndims=3):
        if ndims == 2:
            return (self.x, self.y)
        else:
            return (self.x, self.y, self.z)

    def __eq__(self, other):
        return all([self.x == other.x, self.y == other.y, self.z == other.z])

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    def __repr__(self):
        return 'cell.Cell({}, {}, {})'.format(self.x, self.y, self.z)



def restrict_quadrants(neighbours, start, end):
    cells = neighbours[:]
    if end.x > start.x:
        cells = [x for x in cells if x.x >= start.x]
    elif end.x < start.x:
        cells = [x for x in cells if x.x <= start.x]
    if end.y > start.y:
        cells = [x for x in cells if x.y >= start.y]
    elif end.y < start.y:
        cells = [x for x in cells if x.y <= start.y]
    return cells


def right_intersection(point, line):
    """
    Determine the point at which a point is closest to a line

    A line through that point would intersect at a right angle.
    """
    if line.start.y == line.end.y:  # line is horizontal (same y values)
        x, y = point.x, line.start.y
    elif line.start.x == line.end.x:  # line is vertical (same x values)
        x, y = line.start.x, point.y
    else:
        m = (line.end.y - line.start.y) / (line.end.x - line.start.x)  # slope
        b = line.start.y - m * line.start.x  # y-intercept
        c = point.y + point.x / m  # y-intercept of intersecting line
        x = m * (c - b) / (m ** 2 + 1)  # x-coord of intersection
        y = m * x + b  # y-coord of intersection
    return Cell(x, y)


def discretize_line(start, end):
    """
    Turn start and end points (which are integer (x, y) tuples) into
    a list of integer (x, y) points forming a line.
    """
    max_length = abs(end.y - start.y) + abs(end.x - start.x) + 1  # Plus start

    Line = collections.namedtuple('Line', 'start, end')
    line = Line(start, end)
    results = [start]
    seen = set()
    while start != (end.x, end.y):  # Check in 2D only
        neighbours = start.neighbours()
        neighbours = restrict_quadrants(neighbours, start, end)

        next_cell = None
        min_distance = float('inf')
        for cell in neighbours:
            if cell in seen:  # Don't go backwards
                continue
            intersection = right_intersection(cell, line)
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

