from cutypy.models.content import Content
from cutypy.solver.fix_double_blanks import fix_double_blanks

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = fix_double_blanks(Content(original))

@discover_test
def test_fix_double_blanks():
  (lambda: received.content) @expects (expected)

