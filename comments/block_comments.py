def remove_block_comments(
    text: str,
    block_comment_start_char: str,
    block_comment_end_char: str
):
    depth = 0
    new_text = []

    n = len(block_comment_start_char)
    m = len(block_comment_end_char)

    for index, char in enumerate(text):

        if text[index:index + n] == block_comment_start_char:
            depth += 1

        if text[index - m:index] == block_comment_end_char:
            if depth > 0:
                depth -= 1

        if depth == 0:
            new_text.append(char)

    return ''.join(new_text)
