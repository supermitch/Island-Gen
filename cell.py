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

    def __eq__(self, other):
        return all([self.x == other.x, self.y == other.y, self.z == other.z])

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __hash__(self):
        return hash(repr(self))

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    def __repr__(self):
        return 'cell.Cell({}, {}, {})'.format(self.x, self.y, self.z)


def restrict_quadrants(neighbours, start, end):
    """
    Only return the quadrants of a set of neighbours that are
    oriented in the direction of 'end' Cell.
    """
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

