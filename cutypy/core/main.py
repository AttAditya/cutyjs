from cutypy.cli.args_handler import get_cli_args
from cutypy.cli.version import version_interference
from cutypy.engine.worker import start_engine

from langex.core.pipeline import Pipeline

cli_pipeline = (
  Pipeline
  | get_cli_args
  | version_interference
  | start_engine
)

def cli_entry():
  cli_pipeline.run()

