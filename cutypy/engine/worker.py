from os.path import join, abspath, isfile

from cutypy.engine.discovery import discover
from cutypy.engine.pipelines.check import check_pipeline
from cutypy.engine.pipelines.solve import solve_pipeline
from cutypy.models.args import Args
from cutypy.models.content import Content

from langex.core.functions import autosig

@autosig
def read(path: str) -> str:
  with open(path, "r") as f:
    return f.read()

@autosig
def write(path: str, content: str):
  with open(path, "w") as f:
    f.write(content)

@autosig
def resolve_path(base_path: str, path: str) -> str:
  return abspath(join(base_path, path))

@autosig
def run_workflow(
  initial_paths: list[str],
  iterated_set: set[str],
  pipeline_fn: callable
):
  paths = [*initial_paths]

  while paths:
    path = paths.pop(0)

    if path in iterated_set:
      continue

    iterated_set.add(path)

    if isfile(path):
      data = read(path)
      content = Content(data)
      result = pipeline_fn(content)

      if result.formatted():
        print(f"formatted: {path}")
        write(path, result.content)

      if result.issues:
        print(f"issues found in {path}:")

        for issue in result.issues:
          print(f"  - type: {issue['type']}")
          print(f"    info: {issue['info']}")

          if "line" in issue:
            print(f"    path: {path}:{issue['line']}")
    else:
      new_files = discover(path)
      paths.extend(new_files)

@autosig
def start_engine(args: Args):
  check_set = set()
  solve_set = set()
  run_workflow(
    args.check_paths,
    check_set,
    check_pipeline.run
  )

  run_workflow(
    args.solve_paths,
    solve_set,
    solve_pipeline.run
  )

