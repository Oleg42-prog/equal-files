import os
import argparse
from send2trash import send2trash
from comments import remove_line_comments
from comments import remove_block_comments


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


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_folder', type=str, required=True)
    parser.add_argument('--extensions', nargs='+', default=['.c', '.cpp'], type=str)
    parser.add_argument('--ignore_whitespaces', action='store_true')
    parser.add_argument('--ignore_line_comments', action='store_true')
    parser.add_argument('--ignore_block_comments', action='store_true')
    parser.add_argument('--line_comment_char', type=str, default='//')
    parser.add_argument('--block_comment_start_char', type=str, default='/*')
    parser.add_argument('--block_comment_end_char', type=str, default='*/')
    parser.add_argument('--encoding', type=str, default='utf-8')
    parser.add_argument('--remove', action='store_true')
    parser.add_argument('--trash', action='store_true')
    parser.add_argument('--errors', type=str, default='strict')
    args = parser.parse_args()

    if args.errors not in ['replace', 'ignore', 'strict']:
        raise ValueError('The --errors parameter can only be replace, ignore or strict')

    if args.remove and args.trash:
        raise ValueError('The --remove and --trash parameters can not be used together')

    print('The empty files:')

    problem_files: list[str] = []
    extensions = tuple(args.extensions)

    for root, _, files in os.walk(args.input_folder):

        for file_name in files:

            if not file_name.endswith(extensions):
                continue

            full_file_path = os.path.join(root, file_name)
            output_user_file_path = full_file_path.replace(args.input_folder, '')

            try:
                if is_empty_file(
                    file_path=full_file_path,
                    ignore_whitespaces=args.ignore_whitespaces,
                    ignore_line_comments=args.ignore_line_comments,
                    ignore_block_comments=args.ignore_block_comments,
                    line_comment_char=args.line_comment_char,
                    block_comment_start_char=args.block_comment_start_char,
                    block_comment_end_char=args.block_comment_end_char,
                    encoding=args.encoding,
                    errors=args.errors
                ):

                    if args.trash:
                        send2trash(full_file_path)

                    if args.remove:
                        os.remove(full_file_path)

                    print(output_user_file_path)

            except UnicodeDecodeError as e:
                print(f'UnicodeDecodeError: {full_file_path}', e)
