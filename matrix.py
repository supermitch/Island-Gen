from __future__ import division

import itertools


def get_offsets(span):
    """
    Get matrix offsets for a square of distance `span`.
    """
    if span < 0:
        raise ValueError('Cannot return neighbours for negative distance')

    all_offsets = set(itertools.product([x for x in range(-span, span + 1)], repeat=2))
    if span >= 1:
        inner_offsets = set(itertools.product([x for x in range(-(span - 1), span)], repeat=2))
    else:
        inner_offsets = set()
    return all_offsets - inner_offsets


def find_neighbours_2D(array, start, span):
    """
    Return neighbours in a 2D array, given a start point and range.
    """
    x, y = start  # Start coords
    rows = len(array)  # How many rows
    cols = len(array[0])  # Assume square matrix
    return


def new(size, value=None):
    """ Initialize a new square matrix. """
    return [[value] * size for _ in range(size)]

