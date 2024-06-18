def is_empty_file(
    file_path: str,
    ignore_whitespaces=False,
    ignore_comments=False,
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
            ignore_comments=ignore_comments,
            line_comment_char=line_comment_char,
            block_comment_start_char=block_comment_start_char,
            block_comment_end_char=block_comment_end_char
        )


def is_empty_text(
    text: str,
    ignore_whitespaces=False,
    ignore_comments=False,
    line_comment_char='//',
    block_comment_start_char='/*',
    block_comment_end_char='*/'
):
    raise NotImplementedError
