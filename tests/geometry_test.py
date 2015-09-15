import math

import cell
import geometry
import line


def test_polar_to_rectangular():
    assert geometry.polar_to_rectangular((20, 0), 0, 0) == (20, 0)
    assert geometry.polar_to_rectangular((5, math.pi), 0, 0) == (-5, 0)
    assert geometry.polar_to_rectangular((5, math.pi / 2), 0, 0) == (0, 5)
    assert geometry.polar_to_rectangular((5, 0), 20, 20) == (25, 20)


def test_right_intersection():
    # Middle of a "box"
    _line = line.Line(cell.Cell(0, 0), cell.Cell(2, 2))
    point = cell.Cell(2, 0)
    result = geometry.right_intersection(point, _line)  # Fails
    assert result == cell.Cell(1, 1)


def test_right_intersection_horizontal_line():
    _line = line.Line(cell.Cell(0, 0), cell.Cell(9, 0))
    point = cell.Cell(3, 2)
    result = geometry.right_intersection(point, _line)  # Fails
    assert result == cell.Cell(3, 0)


def test_right_intersection_vertical_line():
    _line = line.Line(cell.Cell(1, 0), cell.Cell(1, 7))
    point = cell.Cell(3, 2)
    result = geometry.right_intersection(point, _line)  # Fails
    assert result == cell.Cell(1, 2)

