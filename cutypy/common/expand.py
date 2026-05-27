from cutypy.models.content import Content

from langex.core.functions import autosig
from langex.core.pipeline import Pipeline

def _expand_code(content: Content) -> Content:
  for key in content.compactions:
    compaction = content.compactions[key]
    expansion = compaction["expansion"]
    type_char = compaction["type_char"]
    value = f"{type_char}{expansion}{type_char}"
    content.content = content.content.replace(key, value)

  return content

_expand_pipeline = (
  Pipeline
  | _expand_code
  | _expand_code
  | _expand_code
  | _expand_code
  | _expand_code
  | _expand_code
)

@autosig
def expand(content: Content) -> Content:
  return _expand_pipeline.run(content)

