import argparse
from options import CodeComparsionOptions
from comments import remove_line_comments, remove_block_comments
from utils import read_file, walk_file_paths


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


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--basis_folder', type=str, required=True)
    parser.add_argument('--relative_folder', type=str, required=True)
    parser.add_argument('--compare_by_name', action='store_true')
    parser.add_argument('--extensions', nargs='+', default=['.c', '.cpp'], type=str)
    parser.add_argument('--ignore_whitespaces', action='store_true')
    parser.add_argument('--ignore_line_comments', action='store_true')
    parser.add_argument('--ignore_block_comments', action='store_true')
    parser.add_argument('--line_comment_char', type=str, default='//')
    parser.add_argument('--block_comment_start_char', type=str, default='/*')
    parser.add_argument('--block_comment_end_char', type=str, default='*/')
    parser.add_argument('--encoding', type=str, default='utf-8')
    parser.add_argument('--errors', type=str, default='strict')
    parser.add_argument('--show_diff', action='store_true')
    args = parser.parse_args()

    if args.errors not in ['replace', 'ignore', 'strict']:
        raise ValueError('The --errors parameter can only be replace, ignore or strict')

    problem_files: list[str] = []
    extensions = tuple(args.extensions)
    code_options = CodeComparsionOptions(
        ignore_whitespaces=args.ignore_whitespaces,
        ignore_line_comments=args.ignore_line_comments,
        line_comment_char=args.line_comment_char,
        ignore_block_comments=args.ignore_block_comments,
        block_comment_start_char=args.block_comment_start_char,
        block_comment_end_char=args.block_comment_end_char
    )

    basis_file_paths = list(walk_file_paths(args.basis_folder))
    relative_file_paths = list(walk_file_paths(args.relative_folder))
