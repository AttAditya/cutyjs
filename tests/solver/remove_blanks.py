from cutypy.models.content import Content
from cutypy.solver.remove_blanks import remove_blanks

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = remove_blanks(Content(original))

@discover_test
def test_remove_blanks():
  (lambda: received.content) @expects (expected)

