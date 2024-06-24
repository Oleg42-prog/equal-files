import os
from typing import Iterable


def first(iterable: Iterable):
    return next(iter(iterable))


def read_file(file_path: str, encoding='utf-8', **kwargs):
    with open(file_path, 'r', encoding=encoding, **kwargs) as file:
        return file.read()


def write_file(file_path: str, text: str, encoding='utf-8', **kwargs):
    with open(file_path, 'w', encoding=encoding, **kwargs) as file:
        file.write(text)


def walk_file_paths(folder_path: str):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            yield os.path.join(root, file_name)


def filter_by_extensions(file_names: Iterable, extensions: Iterable):
    tuple_extensions = tuple(extensions)
    for file_name in file_names:
        if file_name.endswith(tuple_extensions):
            yield file_name


def upper_triangular_matrix(
    rows: Iterable,
    columns: Iterable,
    diagonal: bool = True
):
    rows = list(rows)
    columns = list(columns)

    n = len(rows)
    m = len(columns)

    for i in range(n):
        for j in range(m):
            if i < j or (i == j and diagonal):
                yield rows[i], columns[j]


def triangular_matrix(
    iterable_1: Iterable,
    iterable_2: Iterable,
    diagonal: bool = True
):
    list_1 = list(iterable_1)
    list_2 = list(iterable_2)

    n = len(list_1)
    m = len(list_2)

    if n > m:
        for item_1, item_2 in upper_triangular_matrix(list_2, list_1, diagonal):
            yield item_2, item_1
    else:
        yield from upper_triangular_matrix(list_1, list_2, diagonal)
