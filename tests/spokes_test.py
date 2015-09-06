import spokes


def test_get_neighbours_with_self():
    cell = (5, 5)
    expected = [
        (5, 5), (5, 6), (5, 4),
        (6, 5), (6, 6), (6, 4),
        (4, 5), (4, 6), (4, 4),
    ]
    results = spokes.get_neighbours(cell, include_self=True)
    assert expected == results


def test_get_neighbours_no_self():
    cell = (5, 5)
    expected = [
        (5, 6), (5, 4),
        (6, 5), (6, 6), (6, 4),
        (4, 5), (4, 6), (4, 4),
    ]
    results = spokes.get_neighbours(cell)
    assert expected == results


def test_right_intersection():
    # Middle of a "box"
    line = spokes.Spoke((0, 0), (2, 2))
    point = (2, 0)
    result = spokes.right_intersection(point, line)  # Fails
    assert result == (1, 1)


def test_right_intersection_horizontal_line():
    line = spokes.Spoke((0, 0), (9, 0))
    point = (3, 2)
    result = spokes.right_intersection(point, line)  # Fails
    assert result == (3, 0)


def test_right_intersection_vertical_line():
    line = spokes.Spoke((1, 0), (1, 7))
    point = (3, 2)
    result = spokes.right_intersection(point, line)  # Fails
    assert result == (1, 2)


def test_point_distance_direct():
    start = (3, 3)
    end = (6, 3)
    result = spokes.point_distance(start, end)
    assert result == 3.0

    result = spokes.point_distance(start, end, squared=True)
    assert result == 9.0

def test_point_distance_angle():
    start = (0, 0)
    end = (3, 4)
    result = spokes.point_distance(start, end)
    assert result == 5.0  # 3-4-5 triangle

