def first(iterable):
    return next(iter(iterable))


def read_file(file_path: str, encoding='utf-8', **kwargs):
    with open(file_path, 'r', encoding=encoding, **kwargs) as file:
        return file.read()


def write_file(file_path: str, text: str, encoding='utf-8', **kwargs):
    with open(file_path, 'w', encoding=encoding, **kwargs) as file:
        file.write(text)
