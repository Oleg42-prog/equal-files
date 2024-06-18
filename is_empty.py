from utils import first


def is_empty_file(
    file_path: str,
    ignore_whitespaces=False,
    ignore_line_comments=False,
    ignore_block_comments=False,
    line_comment_char='//',
    block_comment_start_char='/*',
    block_comment_end_char='*/',
    encoding='utf-8',
    **kwargs
):
    with open(file_path, 'r', encoding=encoding, **kwargs) as file:
        return is_empty_text(
            text=file.read(),
            ignore_whitespaces=ignore_whitespaces,
            ignore_line_comments=ignore_line_comments,
            ignore_block_comments=ignore_block_comments,
            line_comment_char=line_comment_char,
            block_comment_start_char=block_comment_start_char,
            block_comment_end_char=block_comment_end_char
        )


def is_empty_text(
    text: str,
    ignore_whitespaces=False,
    ignore_line_comments=False,
    ignore_block_comments=False,
    line_comment_char='//',
    block_comment_start_char='/*',
    block_comment_end_char='*/'
):
    if ignore_line_comments:
        text = remove_line_comments(text, line_comment_char)

    if ignore_block_comments:
        text = remove_block_comments(text, block_comment_start_char, block_comment_end_char)

    if ignore_whitespaces:
        return text.isspace()

    return text == ''


def remove_line_comments(
    text: str,
    line_comment_char: str
):
    new_text = []

    for line in text.split('\n'):
        new_line = remove_line_comment(line, line_comment_char)
        new_text.append(new_line)

    return '\n'.join(new_text)


def remove_line_comment(
    line: str,
    line_comment_char: str
):
    return first(line.split(line_comment_char))


def remove_block_comments(
    text: str,
    block_comment_start_char: str,
    block_comment_end_char: str
):
    raise NotImplementedError
