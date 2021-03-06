import cell
import line


def test_str():
    _line = line.Line(cell.Cell(3, 3), cell.Cell(6, 3))
    assert str(_line) == '((3, 3, 0), (6, 3, 0))'

def test_repr():
    _line = line.Line(cell.Cell(3, 3), cell.Cell(6, 3))
    assert repr(_line) == 'line.Line((3, 3, 0), (6, 3, 0))'

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

def test_discretize_line_x5():
    start = cell.Cell(645, 463)
    end = cell.Cell(651, 467)
    _line = line.Line(start, end)
    expected = [cell.Cell(x) for x in ((645, 463), (646, 464), (647, 464),
                                       (648, 465), (649, 466), (650, 466),
                                       (651, 467))]
    result = list(_line.discretize())
    assert result == expected

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

