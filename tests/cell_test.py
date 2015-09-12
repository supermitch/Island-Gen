import cell


def test_tuple_init():
    assert cell.Cell(1, 0, 0) == cell.Cell((1,))
    assert cell.Cell(1, 2, 0) == cell.Cell((1, 2))
    assert cell.Cell(1, 2, 3) == cell.Cell((1, 2, 3))
    assert cell.Cell(1, 2, 3) == cell.Cell((1, 2, 3, 4))  # 4D tuple

def test_equality():
    assert cell.Cell(1, 2, 3) == cell.Cell(1, 2, 3)

def test_get_neighbours():
    start = cell.Cell(5, 5)
    data = [
        (5, 6), (5, 4),
        (6, 5), (6, 6), (6, 4),
        (4, 5), (4, 6), (4, 4),
    ]
    expected = [cell.Cell(*coords) for coords in data]
    assert start.neighbours() == expected

