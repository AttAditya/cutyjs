from cutypy.models.content import Content

from langex.core.functions import autosig

from langex.core.classes import (
  abstract,
  extends,
  interface,
  implements,
)

def _get_indent(line: str | None) -> int:
  if line is None:
    return 0

  return len(line) - len(line.lstrip())

def _check_keyword_line(line: str | None) -> bool:
  if line is None:
    return True

  stripped = line.strip()
  keywords = [
    "def ", "class ", "@", "if ", "raise ",
    "try:", "for ", "while ", "with ", "async ",
    "return ", "continue ", "break ", "yield ",
  ]

  return any(stripped.startswith(keyword) for keyword in keywords)

def _check_ignoring_keyword_line(line: str | None) -> bool:
  if line is None:
    return False

  stripped = line.strip()
  keywords = [
    "elif ", "else:", "except ", "finally:",
  ]

  return any(stripped.startswith(keyword) for keyword in keywords)

def _check_marker_line(line: str | None) -> bool:
  if line is None:
    return False

  return line.startswith("::~cmpx::")

def _check_closing_line(line: str | None) -> bool:
  if line is None:
    return False

  stripped = line.strip()
  closings = [
    "]", ")", "}",
  ]

  return any(stripped.startswith(closing) for closing in closings)

def _check_indent_token_line(line: str):
  stripped = line.strip()
  indent_tokens = [
    ":", ",",
  ]

  return any(stripped.endswith(token) for token in indent_tokens)

def _should_add_prev_blank(line: str, prev: str | None) -> bool:
  is_curr_keyword = _check_keyword_line(line)
  is_prev_keyword = _check_keyword_line(prev)
  is_ignoring_keyword = _check_ignoring_keyword_line(line)
  is_indent_down = _get_indent(line) < _get_indent(prev)
  is_indent_up = _get_indent(line) > _get_indent(prev)
  is_closing = _check_closing_line(line)
  is_prev_marker = _check_marker_line(prev)

  if is_closing or is_indent_up or is_ignoring_keyword:
    return False

  if is_indent_down:
    return True

  if is_prev_keyword or is_prev_marker:
    return False

  return is_curr_keyword

def _should_add_post_blank(line: str, post: str | None) -> bool:
  is_curr_closing = _check_closing_line(line)
  is_next_closing = _check_closing_line(post)
  is_next_indent_up = _get_indent(post) > _get_indent(line)
  is_next_marker = _check_marker_line(post)
  has_indent_token = _check_indent_token_line(line)

  if is_next_closing or is_next_indent_up or has_indent_token:
    return False

  return is_curr_closing and not is_next_marker

@autosig
def add_keyword_blanks(content: Content) -> Content:
  lines = content.content.split("\n")
  new_lines = []

  for line_idx, line in enumerate(lines):
    prev = None
    post = None

    if line_idx > 0:
      prev = lines[line_idx - 1]

    if line_idx < len(lines) - 1:
      post = lines[line_idx + 1]

    if _should_add_prev_blank(line, prev):
      new_lines.append("")

    new_lines.append(line)

    if _should_add_post_blank(line, post):
      new_lines.append("")

  content.content = "\n".join(new_lines)

  return content

