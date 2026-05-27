from cutypy.models.content import Content
from cutypy.solver.fix_import_order import fix_import_order

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = fix_import_order(Content(original))

@discover_test
def test_fix_import_order():
  (lambda: received.content) @expects (expected)

