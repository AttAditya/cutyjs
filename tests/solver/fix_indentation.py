from cutyjs.models.content import Content
from cutyjs.solver.fix_indentation import fix_indentation

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = fix_indentation(Content(original))

@discover_test
def test_fix_indentation():
  (lambda: received.content) @expects (expected)

