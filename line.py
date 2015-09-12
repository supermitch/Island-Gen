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

    def __str__(self):
        return '({}, {})'.format(self.start, self.end)

    def __repr__(self):
        return 'line.Line({}, {})'.format(self.start, self.end)

