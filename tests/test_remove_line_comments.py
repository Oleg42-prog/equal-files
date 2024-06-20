import pytest
from comments.line_comments import remove_line_comments
from utils import read_file


@pytest.mark.parametrize('input_file_path, line_comment_char, expected_file_path', [
    (
        'tests/mock_files/input/comments_file.txt',
        '#',
        'tests/mock_files/expected/comments_file_hash_sign.txt'
    ),

    (
        'tests/mock_files/input/comments_file.txt',
        '//',
        'tests/mock_files/expected/comments_file_two_slashes.txt'
    ),

    (
        'tests/mock_files/input/comments_file.txt',
        ';',
        'tests/mock_files/expected/comments_file_semicolon.txt'
    )
])
def test_remove_line_comments(
    input_file_path: str,
    line_comment_char: str,
    expected_file_path: str
):
    input_text = read_file(input_file_path)
    expected_text = read_file(expected_file_path)
    actual_text = remove_line_comments(input_text, line_comment_char)
    assert actual_text == expected_text
