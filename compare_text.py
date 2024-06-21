from options import CodeComparsionOptions
from comments import remove_line_comments
from comments import remove_block_comments
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
    if options.ignore_line_comments:
        text_1 = remove_line_comments(text_1, options.line_comment_char)
        text_2 = remove_line_comments(text_2, options.line_comment_char)

    if options.ignore_block_comments:
        text_1 = remove_block_comments(text_1, options.block_comment_start_char, options.block_comment_end_char)
        text_2 = remove_block_comments(text_2, options.block_comment_start_char, options.block_comment_end_char)

    if options.ignore_whitespaces:
        text_1 = ''.join([char for char in text_1 if not char.isspace()])
        text_2 = ''.join([char for char in text_2 if not char.isspace()])

    return text_1 == text_2
