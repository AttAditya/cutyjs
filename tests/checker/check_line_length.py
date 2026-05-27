from cutypy.checker.check_line_length import check_line_length
from cutypy.models.content import Content

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = check_line_length(Content(original))

@discover_test
def test_check_line_length():
  (lambda: received.content) @expects (expected)

