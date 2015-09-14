import cell
import line


def test_length_distance_direct():
    start = cell.Cell(3, 3)
    end = cell.Cell(6, 3)
    _line = line.Line(start, end)
    assert _line.length() == 3.0

    assert _line.length(squared=True) == 9.0

def test_length_angle():
    start = cell.Cell(0, 0)
    end = cell.Cell(3, 4)
    _line = line.Line(start, end)
    assert _line.length() == 5.0  # 3-4-5 triangle

def test_discretize_line_simple():
    start = cell.Cell(0, 0)
    end = cell.Cell(2, 0)
    _line = line.Line(start, end)
    coords = [(0, 0), (1, 0), (2, 0)]
    expected = [cell.Cell(x) for x in coords]
    assert _line.discretize() == expected

def test_discretize_line_45():
    start = cell.Cell(0, 0)
    end = cell.Cell(-3, -3)
    _line = line.Line(start, end)
    expected = [cell.Cell(x) for x in ((0, 0), (-1, -1), (-2, -2), (-3, -3))]
    assert _line.discretize() == expected

def test_discretize_line_27():
    start = cell.Cell(0, 0)
    end = cell.Cell(2, 6)
    _line = line.Line(start, end)
    coords = [(0, 0), (0, 1), (1, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    expected = [cell.Cell(x) for x in coords]
    assert _line.discretize() == expected

