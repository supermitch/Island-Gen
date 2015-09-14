from __future__ import division

import cell


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
    return cell.Cell(x, y)

