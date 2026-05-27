from cutypy.models.content import Content

from langex.core.functions import autosig

@autosig
def remove_blanks(content: Content) -> Content:
  lines = content.content.split("\n")
  lines = [line for line in lines if line.strip()]
  content.content = "\n".join(lines)

  return content

