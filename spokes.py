from __future__ import division

import collections
import itertools
import math


Spoke = collections.namedtuple('Spoke', 'start, end')


def gen_spokes():
    data = [
        ((650, 450), (458, 439)),
        ((550, 624), (458, 439)),
        ((351, 621), (458, 439)),
        ((250, 450), (458, 439)),
        ((338, 257), (458, 439)),
        ((549, 276), (458, 439))
    ]
    return [(Spoke(points[0], points[1])) for points in data]


def get_neighbours(cell, include_self=False):
    """ Get 8 neighbouring cell coords to a start cell. """
    offsets = list(itertools.product([0, 1, -1], repeat=2))
    if not include_self:
        del offsets[offsets.index((0, 0))]  # Don't include start cell
    return [(cell[0] + dx, cell[1] + dy) for dx, dy in offsets]


def discretize_line(start, end):
    spoke = Spoke(start, end)
    print(spoke)
    line = [start]
    seen = set()
    while start != end:
        neighbours = get_neighbours(start)
        print(neighbours)
        next_cell = None
        min_distance = float('inf')
        for cell in neighbours:
            if cell in seen:  # Don't go backwards
                continue
            intersection = right_intersection(cell, spoke)
            distance = point_distance(cell, intersection)
            if distance < min_distance:
                min_distance = distance
                next_cell = cell
            print(intersection, cell, distance)
        line.append(next_cell)
        seen.add(next_cell)
        start = next_cell
    return line


def right_intersection(point, line):
    """
    Determine the point at which a point is closest to a line

    A line through that point would intersect at a right angle.
    """
    m = (line.end[1] - line.start[1]) / (line.end[0] - line.end[1])  # slope
    b = line.start[1] - m * line.start[0]  # y-intercept
    c = 1 / m * point[0] - point[1]  # y-intercept of intersecting line
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


def main():
    spokes = gen_spokes()
    lines = []
    for spoke in spokes:
        line_cells = discretize_line(spoke.start, spoke.end)
        lines.append(line_cells)
    print(line_cells)


if __name__ == '__main__':
    main()

