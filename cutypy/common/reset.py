from cutypy.models.content import Content

from langex.core.functions import autosig

@autosig
def reset(content: Content) -> Content:
  content.content = content.original

  return content

