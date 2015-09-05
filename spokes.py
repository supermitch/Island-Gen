from __future__ import division

import collections


def gen_spokes():
    data = [
        ((650, 450), (458, 439)),
        ((550, 624), (458, 439)),
        ((351, 621), (458, 439)),
        ((250, 450), (458, 439)),
        ((338, 257), (458, 439)),
        ((549, 276), (458, 439))
    ]
    Spoke = collections.namedtuple('Spoke', 'start, end')
    return [(Spoke(points[0], points[1])) for points in data]


def collect_cells(spoke):
    print(spoke)
    left = min(spoke.start[0], spoke.end[0])
    right = max(spoke.start[0], spoke.end[0])
    top  = min(spoke.start[1], spoke.end[1])
    bottom = max(spoke.start[1], spoke.end[1])
    print('Span: ({}, {}) ({}, {})'.format(left, right, top, bottom))
    return [(x, y) for x in range(left, right + 1) for y in range(top, bottom + 1)]


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


def main():
    spokes = gen_spokes()
    for spoke in spokes:
        cells = collect_cells(spoke)
        for cell in cells:
            point = right_intersection(cell, spoke)


if __name__ == '__main__':
    main()

