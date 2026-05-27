from cutypy.models.content import Content
from cutypy.solver.add_keyword_blanks import add_keyword_blanks

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = add_keyword_blanks(Content(original))

@discover_test
def test_add_keyword_blanks():
  (lambda: received.content) @expects (expected)

