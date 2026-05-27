from cutypy.models.content import Content
from cutypy.solver.fix_line_ends import fix_line_ends

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = fix_line_ends(Content(original))

@discover_test
def test_fix_line_ends():
  (lambda: received.content) @expects (expected)

