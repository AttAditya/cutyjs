from sys import stdlib_module_names

from cutypy.models.content import Content

from langex.core.functions import autosig

def _is_import_start_line(line: str) -> bool:
  if line.startswith("import "):
    return True

  if line.startswith("from "):
    return True

  return False

def _is_import_end_line(line: str) -> bool:
  if line.startswith("import "):
    return True

  if ")" in line:
    return True

  if line.startswith("from ") and "(" not in line:
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

def _classify(line: str) -> str:
  if not line.strip():
    return "garbage"

  if line.startswith("import "):
    if "," in line:
      return "import_multi"

    if " as " in line:
      return "import_alias"

    return "import_plain"

  if "(" in line:
    return "from_paren"

  if " as " in line:
    return "from_alias"

  return "from_plain"

def _import_grouping(lines: list[str]) -> list[str]:
  if not lines:
    return []

  return ["\n".join(lines)]

def _from_grouping(lines: list[str]) -> list[str]:
  buckets = {}
  bucket_keys = []

  for line in lines:
    initial = line.split(" import")[0].strip()
    module = initial.split("from")[1].strip()
    bucket = module.split(".")[0]
    priority1 = 1
    priority2 = tuple(module.split("."))
    priority3 = line

    if bucket in stdlib_module_names:
      priority1 = 0

    if not bucket:
      priority1 = 2

    if bucket not in buckets:
      buckets[bucket] = []
      bucket_keys.append((priority1, bucket))

    buckets[bucket].append((
      priority2,
      priority3,
    ))

  grouped = []
  bucket_keys.sort()

  for _, bucket in bucket_keys:
    bucket_lines = buckets[bucket]
    bucket_lines.sort()
    bucket_lines = [line for _, line in bucket_lines]
    grouped.append("\n".join(bucket_lines))

  return grouped

def _generate_import_code(import_lines: list[str]) -> str:
  classifications = {
    "import_plain": [],
    "import_alias": [],
    "import_multi": [],
    "from_plain": [],
    "from_alias": [],
    "from_paren": [],
    "garbage": [],
  }

  for line in import_lines:
    classification = _classify(line)
    classifications[classification].append(line)

  import_order = [
    "import_plain",
    "import_alias",
    "import_multi",
    "from_plain",
    "from_alias",
    "from_paren",
  ]

  grouping_functions = {
    "import_plain": _import_grouping,
    "import_alias": _import_grouping,
    "import_multi": _import_grouping,
    "from_plain": _from_grouping,
    "from_alias": _from_grouping,
    "from_paren": lambda lines: lines,
  }

  generated = ""
  compaction_key = "::~cmpx::"
  compaction_key += "import_blank"

  for import_type in import_order:
    raw_lines = classifications[import_type]
    grouping_fn = grouping_functions[import_type]
    lines = grouping_fn(raw_lines)

    if not lines:
      continue

    generated += f"\n{compaction_key}\n".join(lines)
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

