from cutypy.models.content import Content

from langex.core.functions import autosig

@autosig
def fix_indentation(content: Content) -> Content:
  content_lines = content.content.split("\n")
  level = 0
  lines = []
  last = [0]

  for line in content_lines:
    if not line.strip():
      lines.append((level, ""))
      continue

    count = 0

    for char in line:
      if char == " ":
        count += 1
      else:
        break

    if last[-1] < count:
      level += 1
      last.append(count)
    elif last[-1] > count:
      while last and last[-1] > count:
        level -= 1
        last.pop()

    lines.append((level, line[count:]))

  result = ""

  for level, line in lines:
    result += ("  " * level) + line + "\n"

  content.content = result

  return content

