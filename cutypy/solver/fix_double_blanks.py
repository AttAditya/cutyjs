from cutypy.models.content import Content

from langex.core.functions import autosig

@autosig
def fix_double_blanks(content: Content) -> Content:
  content.content = content.content.replace("\n\n\n", "\n\n")
  content.content = content.content.replace("\n\n\n", "\n\n")
  content.content = content.content.replace("\n\n\n", "\n\n")

  return content

