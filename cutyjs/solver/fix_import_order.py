from cutyjs.models.content import Content

from langex.core.functions import autosig

NODE_BUILTINS = {
  "fs", "path", "os", "http", "https", "crypto",
  "stream", "util", "events", "url", "zlib", "buffer",
  "child_process", "timers", "net", "tls",
}

def _is_import_start_line(line: str) -> bool:
  if line.startswith("import "):
    return True

  return False

def _is_import_end_line(line: str) -> bool:
  if line.endswith((";", "\'", "\"", "`")):
    return True

  return False

def _segregate_code(content: str) -> list:
  lines = content.split("\n")
  import_type = []
  normal_type = []
  is_import = False
  current = []

  for line in lines:
    if _is_import_start_line(line):
      current = []
      is_import = True

    if is_import:
      current.append(line)

      if _is_import_end_line(line):
        is_import = False
        import_type.append("\n".join(current))
        current = []
    else:
      normal_type.append(line)

  return {
    "import": import_type,
    "normal": normal_type,
  }

def _import_grouping(lines: list[str]) -> list[str]:
  module = lambda line: line.split(" ")[-1].strip('"').strip("'")
  key_fn = lambda line: tuple(module(line).split("/"))

  return sorted(lines, key=key_fn)

def _bucket_priority(bucket: str) -> int:
  if bucket in NODE_BUILTINS:
    return 0

  if bucket.endswith((".css", ".scss", ".less")):
    return 5

  if bucket.startswith("@"):
    return 2

  if bucket.startswith(".."):
    return 3

  if bucket.startswith("."):
    return 4

  return 1

def _generate_import_code(import_lines: list[str]) -> str:
  classifications = {}

  for line in import_lines:
    module = line.split(" ")[-1].strip('"').strip("'")
    classification = _bucket_priority(module)

    if classification not in classifications:
      classifications[classification] = []

    classifications[classification].append(line)

  generated = ""
  compaction_key = "::~cmpx::"
  compaction_key += "import_blank"

  for import_type in sorted(classifications.keys()):
    raw_lines = classifications[import_type]
    lines = _import_grouping(raw_lines)

    if not lines:
      continue

    generated += f"\n".join(lines)
    generated += f"\n{compaction_key}\n"

  return generated

def _generate_normal_code(normal_lines: list[str]) -> str:
  return "\n".join(normal_lines)

@autosig
def fix_import_order(content: Content) -> Content:
  segregated = _segregate_code(content.content)
  generated = ""
  generated += _generate_import_code(segregated["import"])
  generated += _generate_normal_code(segregated["normal"])
  compaction_key = "::~cmpx::"
  compaction_key += "import_blank"
  content.content = generated
  content.compactions[compaction_key] = {
    "expansion": "",
    "type_char": "",
    "type": "import-blank",
  }

  return content

