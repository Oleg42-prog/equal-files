from options import CodeComparsionOptions
from utils import read_file


def compare_text_files(
    file_path_1: str,
    file_path_2: str,
    options: CodeComparsionOptions,
    encoding='utf-8',
    **kwargs
):
    text_1 = read_file(file_path_1, encoding=encoding, **kwargs)
    text_2 = read_file(file_path_2, encoding=encoding, **kwargs)
    return compare_text(text_1, text_2, options)


def compare_text(
    text_1: str,
    text_2: str,
    options: CodeComparsionOptions
):
    raise NotImplementedError
