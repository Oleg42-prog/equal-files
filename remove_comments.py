import os
import argparse
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


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str, required=True)
    parser.add_argument('--extensions', nargs='+', default=['.c', '.cpp'], type=str)
    parser.add_argument('--remove_line_comments', action='store_true')
    parser.add_argument('--remove_block_comments', action='store_true')
    parser.add_argument('--remove_empty_lines', action='store_true')
    parser.add_argument('--remove_whitespace_lines', action='store_true')
    parser.add_argument('--line_comment_char', type=str, default='//')
    parser.add_argument('--block_comment_start_char', type=str, default='/*')
    parser.add_argument('--block_comment_end_char', type=str, default='*/')
    parser.add_argument('--encoding', type=str, default='utf-8')
    parser.add_argument('--errors', type=str, default='strict')
    args = parser.parse_args()

    extensions = tuple(args.extensions)

    for root, dirs, files in os.walk(args.input_folder):

        for file_name in files:

            if not file_name.endswith(extensions):
                continue

            remove_comments_from_file(
                file_path=os.path.join(root, file_name),
                line_comments=args.remove_line_comments,
                block_comments=args.remove_block_comments,
                remove_empty_lines=args.remove_empty_lines,
                remove_whitespace_lines=args.remove_whitespace_lines,
                line_comment_char=args.line_comment_char,
                block_comment_start_char=args.block_comment_start_char,
                block_comment_end_char=args.block_comment_end_char,
                encoding=args.encoding,
                errors=args.errors
            )
