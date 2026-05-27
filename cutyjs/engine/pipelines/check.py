from cutyjs.checker.check_line_length import check_line_length
from cutyjs.common.reset import reset

from langex.core.pipeline import Pipeline

check_pipeline = (
  Pipeline
  | check_line_length
  | reset
)

