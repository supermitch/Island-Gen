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

