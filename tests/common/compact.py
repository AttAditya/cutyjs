from cutypy.common.compact import compact
from cutypy.models.content import Content

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = compact(Content(original))

@discover_test
def test_compact():
  (lambda: received.content) @expects (expected)

