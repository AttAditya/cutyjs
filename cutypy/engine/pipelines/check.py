from cutypy.checker.check_line_length import check_line_length
from cutypy.common.reset import reset

from langex.core.pipeline import Pipeline

check_pipeline = (
  Pipeline
  | check_line_length
  | reset
)

