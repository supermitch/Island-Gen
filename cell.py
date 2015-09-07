from __future__ import division

import collections
import itertools
import math


Spoke = collections.namedtuple('Spoke', 'start, end')


def get_neighbours(cell, include_self=False):
    """
    Get 8 neighbouring cell coords to a start cell.

    If `include_self` is True, returns the current (center) cell as well.
    """
    offsets = list(itertools.product([0, 1, -1], repeat=2))
    if not include_self:
        del offsets[offsets.index((0, 0))]  # Don't include start cell
    return [(cell[0] + dx, cell[1] + dy) for dx, dy in offsets]


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
    max_length = abs(end[1] - start[1]) + abs(end[0] - start[0])

    Line = collections.namedtuple('Line', 'start, end')
    line = Line(start, end)
    print(line)
    results = [start]
    seen = set()
    while start != end:
        neighbours = get_neighbours(start)
        print(neighbours)
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
            return None
        seen.add(next_cell)
        start = next_cell
    return results

