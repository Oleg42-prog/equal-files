from utils import first


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
