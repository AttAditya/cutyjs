from cutyjs.models.content import Content

from langex.core.functions import autosig

def _is_import_start_line(line: str) -> bool:
  return line.startswith("import ")

def _is_import_end_line(line: str) -> bool:
  if "{" in line and "}" not in line:
    return False
  return True

def _segregate_code(content: str) -> dict:
  lines = content.split("\n")
  import_type = []
  normal_type = []
  is_import = False
  current = []

  for line in lines:
    if _is_import_start_line(line) and not is_import:
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

def _extract_module_name(import_statement: str) -> str:
  # Simple extraction of module name for sorting
  # import { a } from 'module-name'
  # import a from 'module-name'
  # import 'module-name'
  import_statement = import_statement.strip()
  if "from" in import_statement:
    parts = import_statement.split("from")
    module_part = parts[1].strip().strip("'\"")
    return module_part
  else:
    # import 'module-name'
    return import_statement.replace("import ", "").strip().strip("'\"")

def _import_grouping(import_statements: list[str]) -> list[str]:
  if not import_statements:
    return []
  
  # Sort import statements based on extracted module name
  sorted_imports = sorted(import_statements, key=_extract_module_name)
  return sorted_imports

def _generate_import_code(import_lines: list[str]) -> str:
  sorted_lines = _import_grouping(import_lines)
  
  compaction_key = "::~cmpx::"
  compaction_key += "import_blank"
  
  return f"\n{compaction_key}\n".join(sorted_lines) + f"\n{compaction_key}\n"

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
