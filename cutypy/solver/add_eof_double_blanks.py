from cutypy.models.content import Content

from langex.core.functions import autosig

@autosig
def add_eof_double_blanks(content: Content) -> Content:
  end_idx = len(content.content)

  while end_idx > 0 and content.content[end_idx - 1] == "\n":
    end_idx -= 1

  content.content = content.content[:end_idx] + "\n\n"

  return content

