import cell
import geometry
import line


def test_right_intersection():
    # Middle of a "box"
    line = line.Line(cell.Cell(0, 0), cell.Cell(2, 2))
    point = cell.Cell(2, 0)
    result = geometry.right_intersection(point, line)  # Fails
    assert result == cell.Cell(1, 1)


def test_right_intersection_horizontal_line():
    line = line.Line(cell.Cell(0, 0), cell.Cell(9, 0))
    point = cell.Cell(3, 2)
    result = geometry.right_intersection(point, line)  # Fails
    assert result == cell.Cell(3, 0)


def test_right_intersection_vertical_line():
    line = line.Line(cell.Cell(1, 0), cell.Cell(1, 7))
    point = cell.Cell(3, 2)
    result = geometry.right_intersection(point, line)  # Fails
    assert result == cell.Cell(1, 2)

