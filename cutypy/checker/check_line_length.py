from cutypy.models.content import Content

from langex.core.functions import autosig

@autosig
def check_line_length(content: Content) -> Content:
  lines = content.content.split("\n")
  line_cap = 70

  for i, line in enumerate(lines):
    if len(line) > line_cap:
      content.issues.append({
        "line": i + 1,
        "type": "line-length",
        "info": f"Line {i + 1} exceeds {line_cap}"
          f" characters ({len(line)} characters)",
      })

  return content

