from cutyjs.cli.args_handler import get_cli_args
from cutyjs.cli.version import version_interference
from cutyjs.engine.worker import start_engine

from langex.core.pipeline import Pipeline

cli_pipeline = (
  Pipeline
  | get_cli_args
  | version_interference
  | start_engine
)

def cli_entry():
  cli_pipeline.run()

