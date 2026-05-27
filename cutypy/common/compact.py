from cutypy.models.content import Content

from langex.core.functions import autosig
from langex.core.pipeline import Pipeline

def _compact_code(
  content: Content,
  type_char: str,
  compaction_type: str,
) -> Content:
  txt_key = hash(content.content)
  escaped = False
  working = False
  current = ""

  def create_compaction_key(text: str) -> str:
    text_id = hash(text)
    merged_id = hash((text_id, txt_key))

    return f"::~cmpx::{merged_id}"

  for char in content.content:
    if char == "\\":
      escaped = not escaped
      current += char
      continue

    if char == type_char and not escaped:
      if working:
        key = create_compaction_key(current)
        content.compactions[key] = {
          "expansion": current,
          "type_char": type_char,
          "type": compaction_type,
        }

      working = not working
      current = ""
      continue

    escaped = False

    if working:
      current += char

  for value in content.compactions:
    compaction = content.compactions[value]
    expansion = compaction["expansion"]
    type_char = compaction["type_char"]
    key = f"{type_char}{expansion}{type_char}"
    content.content = content.content.replace(key, value)

  return content

def _create_char_compaction(type_char: str, compaction_type: str):
  def char_compaction(content: Content) -> Content:
    return _compact_code(content, type_char, compaction_type)

  return char_compaction

_compact_pipeline = (
  Pipeline
  | _create_char_compaction("\'", "single-quoted-string")
  | _create_char_compaction("\"", "double-quoted-string")
  | _create_char_compaction("\'", "single-quoted-string")
  | _create_char_compaction("\"", "double-quoted-string")
  | _create_char_compaction("\'", "single-quoted-string")
  | _create_char_compaction("\"", "double-quoted-string")
)

@autosig
def compact(content: Content) -> Content:
  return _compact_pipeline.run(content)

