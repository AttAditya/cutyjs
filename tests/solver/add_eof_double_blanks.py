from cutypy.models.content import Content
from cutypy.solver.add_eof_double_blanks import add_eof_double_blanks

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = add_eof_double_blanks(Content(original))

@discover_test
def test_add_eof_double_blanks():
  (lambda: received.content) @expects (expected)

