from __future__ import division

import matrix


def test_get_offsets():
    assert matrix.get_offsets(0) == set([(0, 0)])
    assert matrix.get_offsets(2) == set([(1, 2), (-2, 1), (-2, 0), (-2, 2),
                                         (-1, 2), (2, -2), (2, 1), (2, -1),
                                         (2, 0), (-2, -1), (-1, -2), (-2, -2),
                                         (2, 2), (0, -2), (1, -2), (0, 2)])

def test_new():
    m = matrix.new(3, 'a')
    assert len(m) == 3  # 3 rows
    assert len(m[0]) == 3  # 3 cols
    assert m[0][0] == 'a'
    assert m[2][2] == 'a'

    # Ensure each element of matrix is unique
    m[1][0] == 'c'
    assert m[1][1] == 'a'
    assert m[2][0] == 'a'

def test_find_neighbours_2D():
    m = matrix.new(4)
    results = matrix.find_neighbours_2D(m, (2, 2), 1)
    assert results == set([(1, 2), (3, 2), (1, 3), (3, 3),
                           (3, 1), (2, 1), (2, 3), (1, 1)])

