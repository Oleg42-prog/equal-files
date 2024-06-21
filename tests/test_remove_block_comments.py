import pytest
from comments.block_comments import remove_block_comments
from utils import read_file


@pytest.mark.parametrize('input_file_path, block_comment_start_char, block_comment_end_char, expected_file_path', [
    (
        'tests/mock_files/input/block_comments_file.txt',
        '/*',
        '*/',
        'tests/mock_files/expected/block_comments_file.txt'
    )
])
def test_remove_line_comments(
    input_file_path: str,
    block_comment_start_char: str,
    block_comment_end_char: str,
    expected_file_path: str
):
    input_text = read_file(input_file_path)
    expected_text = read_file(expected_file_path)
    actual_text = remove_block_comments(input_text, block_comment_start_char, block_comment_end_char)
    assert actual_text == expected_text
