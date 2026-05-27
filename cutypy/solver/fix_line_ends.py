from cutypy.models.content import Content

from langex.core.functions import autosig

@autosig
def fix_line_ends(content: Content) -> Content:
  lines = content.content.split("\n")

  for i in range(len(lines)):
    lines[i] = lines[i].rstrip(" \r")

  content.content = "\n".join(lines)

  return content

