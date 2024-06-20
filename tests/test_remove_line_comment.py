import pytest
from comments.line_comments import remove_line_comment


@pytest.mark.parametrize('line, line_comment_char, expected', [
    ('', '#', ''),
    ('#', '#', ''),
    ('#comment', '#', ''),
    ('text', '#', 'text'),
    ('text#', '#', 'text'),
    ('text#comment', '#', 'text'),
    ('text#comment#', '#', 'text'),
    ('text#comment1#comment2', '#', 'text'),
    ('text#comment1#comment2#comment3', '#', 'text'),

    ('some say ', '#', 'some say '),
    ('some say #', '#', 'some say '),
    ('some say #comment', '#', 'some say '),
    ('some say #comment#', '#', 'some say '),
    ('some say #comment1#comment2', '#', 'some say '),
    ('some say #comment1#comment2#comment3', '#', 'some say '),

    ('', ';', ''),
    (';', ';', ''),
    (';my ultra comment ', ';', ''),
    ('some say ', ';', 'some say '),
    ('some say ;', ';', 'some say '),
    ('some say ;my ultra comment ', ';', 'some say '),
    ('some say ;my ultra comment ;', ';', 'some say '),
    ('some say ;my ultra comment 1;my ultra comment 2', ';', 'some say '),
    ('some say ;my ultra comment 1;my ultra comment 2;my ultra comment 3', ';', 'some say '),

    ('', '//', ''),
    ('//', '//', ''),
    ('// my super !@#$% /\ \/ 24 comment ', '//', ''),
    ('some say ', '//', 'some say '),
    ('some say //', '//', 'some say '),
    (r'some say // my super !@#$%; /\ \/ 24 com ', '//', 'some say '),
    (r'some say // my super !@#$%; /\ \/ 24 com //', '//', 'some say '),
    (r'some say // my super !@#$%; /\ \/ 24 com 1// my super !@#$% /\ \/ 24 comm 2', '//', 'some say '),
    (r'some say // my super !@#$%; /\ \/ 24 com 1// my super !@#$% /\ \/ 24 comm 2// !@#$% /\ \/ 24 comm 3', '//', 'some say '),

    ('abc#def;hij//klm', '#', 'abc'),
    ('abc#def;hij//klm', ';', 'abc#def'),
    ('abc#def;hij//klm', '//', 'abc#def;hij'),
])
def test_remove_line_comment(
    line: str,
    line_comment_char: str,
    expected: str
):
    assert remove_line_comment(line, line_comment_char) == expected
