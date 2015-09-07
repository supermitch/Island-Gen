import cell


def test_get_neighbours_with_self():
    start = (5, 5)
    expected = [
        (5, 5), (5, 6), (5, 4),
        (6, 5), (6, 6), (6, 4),
        (4, 5), (4, 6), (4, 4),
    ]
    results = cell.get_neighbours(start, include_self=True)
    assert expected == results


def test_get_neighbours_no_self():
    start = (5, 5)
    expected = [
        (5, 6), (5, 4),
        (6, 5), (6, 6), (6, 4),
        (4, 5), (4, 6), (4, 4),
    ]
    results = cell.get_neighbours(start)
    assert expected == results


def test_right_intersection():
    # Middle of a "box"
    line = cell.Spoke((0, 0), (2, 2))
    point = (2, 0)
    result = cell.right_intersection(point, line)  # Fails
    assert result == (1, 1)


def test_right_intersection_horizontal_line():
    line = cell.Spoke((0, 0), (9, 0))
    point = (3, 2)
    result = cell.right_intersection(point, line)  # Fails
    assert result == (3, 0)


def test_right_intersection_vertical_line():
    line = cell.Spoke((1, 0), (1, 7))
    point = (3, 2)
    result = cell.right_intersection(point, line)  # Fails
    assert result == (1, 2)


def test_point_distance_direct():
    start = (3, 3)
    end = (6, 3)
    result = cell.point_distance(start, end)
    assert result == 3.0

    result = cell.point_distance(start, end, squared=True)
    assert result == 9.0

def test_point_distance_angle():
    start = (0, 0)
    end = (3, 4)
    result = cell.point_distance(start, end)
    assert result == 5.0  # 3-4-5 triangle

def test_discretize_line_simple():
    start = (0, 0)
    end = (2, 0)
    expected = [(0, 0), (1, 0), (2, 0)]
    result = cell.discretize_line(start, end)
    assert result == expected

def test_discretize_line_45():
    start = (0, 0)
    end = (-3, -3)
    expected = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    result = cell.discretize_line(start, end)
    assert result == expected

