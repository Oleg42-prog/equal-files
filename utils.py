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
