from dataclasses import dataclass


@dataclass
class CodeComparsionOptions:

    ignore_whitespaces: bool = False

    ignore_line_comments: bool = False
    line_comment_char: str = '//'

    ignore_block_comments: bool = False
    block_comment_start_char: str = '/*'
    block_comment_end_char: str = '*/'
