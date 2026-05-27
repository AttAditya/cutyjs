from os import listdir
from os.path import join, isdir

from langex.core.functions import autosig

@autosig
def should_ignore(path: str) -> bool:
  if path.endswith("__pycache__"):
    return True

  if path.split("/")[-1].startswith("."):
    return True

  return False

@autosig
def discover(base_path: str) -> list[str]:
  files = []
  dir_queue = [base_path]

  while dir_queue:
    current_path = dir_queue.pop(0)

    for entry in listdir(current_path):
      entry_path = join(current_path, entry)

      if should_ignore(entry_path):
        continue

      if isdir(entry_path):
        dir_queue.append(entry_path)
      elif entry_path.endswith(".py"):
        files.append(entry_path)

  return files

