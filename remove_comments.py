from comments import remove_line_comments
from comments import remove_block_comments
from utils import read_file, write_file


def remove_comments_from_file(
    file_path: str,
    line_comments: bool = True,
    block_comments: bool = True,
    remove_empty_lines: bool = False,
    remove_whitespace_lines: bool = False,
    line_comment_char: str = '//',
    block_comment_start_char: str = '/*',
    block_comment_end_char: str = '*/',
    encoding='utf-8',
    **kwargs
):
    text = read_file(file_path, encoding='utf-8', **kwargs)

    if line_comments:
        text = remove_line_comments(text, line_comment_char)

    if block_comments:
        text = remove_block_comments(text, block_comment_start_char, block_comment_end_char)

    if remove_whitespace_lines:
        text = '\n'.join([line for line in text.split('\n') if not line.isspace()])

    if remove_empty_lines:
        text = '\n'.join([line for line in text.split('\n') if not line == ''])

    write_file(file_path, text, encoding=encoding, **kwargs)
