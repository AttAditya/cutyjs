from cutypy.common.expand import expand
from cutypy.models.content import Content

from langex.core.testing import discover_test, expects

original = ''
expected = ''
received = expand(Content(original))

@discover_test
def test_expand():
  (lambda: received.content) @expects (expected)

