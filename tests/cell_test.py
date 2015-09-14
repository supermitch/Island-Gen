import cell


def test_tuple_init():
    assert cell.Cell(1, 0, 0) == cell.Cell((1,))
    assert cell.Cell(1, 2, 0) == cell.Cell((1, 2))
    assert cell.Cell(1, 2, 3) == cell.Cell((1, 2, 3))
    assert cell.Cell(1, 2, 3) == cell.Cell((1, 2, 3, 4))  # 4D tuple

def test_equality():
    assert cell.Cell(1, 2, 3) == cell.Cell(1, 2, 3)

def test_str():
    assert str(cell.Cell(3, 5, 7)) == '(3, 5, 7)'

def test_iter():
    assert [x for x in cell.Cell(1, 2, 3)] == [1, 2, 3]

def test_get_neighbours():
    start = cell.Cell(5, 5)
    coords = [
        (5, 6), (5, 4),
        (6, 5), (6, 6), (6, 4),
        (4, 5), (4, 6), (4, 4),
    ]
    expected = [cell.Cell(x) for x in coords]
    assert start.neighbours() == expected

def test_distance():
    start = cell.Cell(3, 3)
    end = cell.Cell(6, 3)
    assert start.distance(end) == 3.0
    assert start.distance(end, squared=True) == 9.0

def test_point_distance_angle():
    start = cell.Cell(0, 0)
    end = cell.Cell(3, 4)
    assert start.distance(end) == 5.0  # 3-4-5 triangle
    assert start.distance(end, squared=True) == 25.0

def test_restrict_quadrants():
    coords = [
        (5, 6), (5, 4),
        (6, 5), (6, 6), (6, 4),
        (4, 5), (4, 6), (4, 4),
    ]
    neighbours = [cell.Cell(x) for x in coords]
    start = cell.Cell(5, 5)
    end = cell.Cell(10, 10)
    coords = [(5, 6),  (6, 5), (6, 6)]
    expected = [cell.Cell(x) for x in coords]
    results = cell.restrict_quadrants(neighbours, start, end)
    assert results == expected

