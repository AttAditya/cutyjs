from pathlib import Path

from tomllib import load

from cutypy.models.args import Args

from langex.core.functions import autosig

from importlib.metadata import version

@autosig
def version_interference(args: Args) -> Args:
  if not args.version_check:
    return args

  try:
    installed_version = version("cutypy")
  except Exception:
    ROOT = Path(__file__).resolve().parents[2]
    pyproject = ROOT / "pyproject.toml"

    with pyproject.open("rb") as f:
      data = load(f)

    installed_version = data["project"]["version"]

  print(f"CutyPy {installed_version}")

  return Args()

