from typing import Iterable
import pytest
from utils import upper_triangular_matrix


@pytest.mark.parametrize('rows, columns, expected_pairs, diagonal', [
    (
        ['A', 'B', 'C', 'D'],
        ['A', 'B', 'C', 'D'],
        [
            ('A', 'B'), ('A', 'C'), ('A', 'D'),
            ('B', 'C'), ('B', 'D'),
            ('C', 'D')
        ],
        False
    ),

    (
        ['A', 'B', 'C', 'D'],
        ['A', 'B', 'C', 'D'],
        [
            ('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'),
            ('B', 'B'), ('B', 'C'), ('B', 'D'),
            ('C', 'C'), ('C', 'D'),
            ('D', 'D')
        ],
        True
    ),

    (
        ['A', 'B', 'C', 'D'],
        [1, 2, 3, 4],
        [
            ('A', 2), ('A', 3), ('A', 4),
            ('B', 3), ('B', 4),
            ('C', 4)
        ],
        False
    ),

    (
        [1, 2, 3, 4],
        ['A', 'B', 'C', 'D'],
        [
            (1, 'B'), (1, 'C'), (1, 'D'),
            (2, 'C'), (2, 'D'),
            (3, 'D')
        ],
        False
    ),

    (
        ['A', 'B', 'C', 'D'],
        [1, 2, 3, 4],
        [
            ('A', 1), ('A', 2), ('A', 3), ('A', 4),
            ('B', 2), ('B', 3), ('B', 4),
            ('C', 3), ('C', 4),
            ('D', 4)
        ],
        True
    ),

    (
        [1, 2, 3, 4],
        ['A', 'B', 'C', 'D'],
        [
            (1, 'A'), (1, 'B'), (1, 'C'), (1, 'D'),
            (2, 'B'), (2, 'C'), (2, 'D'),
            (3, 'C'), (3, 'D'),
            (4, 'D')
        ],
        True
    ),

    (
        ['A', 'B', 'C', 'D'],
        ['A', 'B'],
        [
            ('A', 'B')
        ],
        False
    ),

    (
        ['A', 'B'],
        ['A', 'B', 'C', 'D'],
        [
            ('A', 'B'), ('A', 'C'), ('A', 'D'),
            ('B', 'C'), ('B', 'D')
        ],
        False
    ),

    (
        ['A', 'B'],
        ['A', 'B', 'C', 'D'],
        [
            ('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'),
            ('B', 'B'), ('B', 'C'), ('B', 'D')
        ],
        True
    ),

    (
        ['A', 'B', 'C', 'D'],
        ['A', 'B'],
        [
            ('A', 'A'), ('A', 'B'),
            ('B', 'B')
        ],
        True
    ),

    (
        ['A', 'B'],
        [1, 2, 3, 4],
        [
            ('A', 2), ('A', 3), ('A', 4),
            ('B', 3), ('B', 4)
        ],
        False
    ),

    (
        ['A', 'B', 'C', 'D'],
        [1, 2],
        [
            ('A', 2)
        ],
        False
    ),

    (
        [1, 2],
        ['A', 'B', 'C', 'D'],
        [
            (1, 'B'), (1, 'C'), (1, 'D'),
            (2, 'C'), (2, 'D')
        ],
        False
    ),

    (
        [1, 2, 3, 4],
        ['A', 'B'],
        [
            (1, 'B')
        ],
        False
    ),

    (
        ['A', 'B'],
        [1, 2, 3, 4],
        [
            ('A', 1), ('A', 2), ('A', 3), ('A', 4),
            ('B', 2), ('B', 3), ('B', 4)
        ],
        True
    ),

    (
        ['A', 'B', 'C', 'D'],
        [1, 2],
        [
            ('A', 1), ('A', 2),
            ('B', 2)
        ],
        True
    ),

    (
        [1, 2],
        ['A', 'B', 'C', 'D'],
        [
            (1, 'A'), (1, 'B'), (1, 'C'), (1, 'D'),
            (2, 'B'), (2, 'C'), (2, 'D')
        ],
        True
    ),

    (
        [1, 2, 3, 4],
        ['A', 'B'],
        [
            (1, 'A'), (1, 'B'),
            (2, 'B')
        ],
        True
    ),
])
def test_upper_triangular_matrix(
    rows: Iterable,
    columns: Iterable,
    expected_pairs: Iterable,
    diagonal: bool
):
    assert list(upper_triangular_matrix(rows, columns, diagonal)) == expected_pairs
