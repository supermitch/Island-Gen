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
        self.x = x
        self.y = y
        self.z = z

    def neighbours(self, ndims=2):
        """
        Get 8 neighbouring cell coords to a start cell.
        """
        offsets = list(itertools.product([0, 1, -1], repeat=2))
        del offsets[offsets.index((0, 0))]  # Don't include self
        return [(self.x + dx, self.y + dy) for dx, dy in offsets]

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

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    def __repr__(self):
        return 'cell.Cell({}, {}, {})'.format(self.x, self.y, self.z)



def restrict_quadrants(neighbours, start, end):
    cells = neighbours[:]
    if end[0] > start[0]:
        cells = [x for x in cells if x[0] >= start[0]]
    elif end[0] < start[0]:
        cells = [x for x in cells if x[0] <= start[0]]
    if end[1] > start[1]:
        cells = [x for x in cells if x[1] >= start[1]]
    elif end[1] < start[1]:
        cells = [x for x in cells if x[1] <= start[1]]

    return cells


def right_intersection(point, line):
    """
    Determine the point at which a point is closest to a line

    A line through that point would intersect at a right angle.
    """
    if line.start[1] == line.end[1]:  # line is horizontal (same y values)
        return (point[0], line.start[1])
    elif line.start[0] == line.end[0]:  # line is vertical (same x values)
        return (line.start[0], point[1])

    m = (line.end[1] - line.start[1]) / (line.end[0] - line.start[0])  # slope
    b = line.start[1] - m * line.start[0]  # y-intercept
    c = point[1] + point[0] / m  # y-intercept of intersecting line
    x = m * (c - b) / (m ** 2 + 1)  # x-coord of intersection
    y = m * x + b  # y-coord of intersection
    return (x, y)


def point_distance(start, end, squared=False):
    """
    Calculate distance between two points using Pythagorean theorem.
    """
    d_squared = (end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2
    if squared:
        return d_squared
    else:
        return math.sqrt(d_squared)


def discretize_line(start, end):
    """
    Turn start and end points (which are integer (x, y) tuples) into
    a list of integer (x, y) points forming a line.
    """
    max_length = abs(end[1] - start[1]) + abs(end[0] - start[0]) + 1  # Plus start

    Line = collections.namedtuple('Line', 'start, end')
    line = Line(start, end)
    results = [start]
    seen = set()
    while start != (end[0], end[1]):
        neighbours = get_neighbours(start)
        neighbours = restrict_quadrants(neighbours, start, end)

        next_cell = None
        min_distance = float('inf')
        for cell in neighbours:
            if cell in seen:  # Don't go backwards
                continue
            intersection = right_intersection(cell, line)
            distance = point_distance(cell, intersection)
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

