from cutyjs.common.compact import compact
from cutyjs.common.expand import expand
from cutyjs.solver.add_eof_double_blanks import add_eof_double_blanks
from cutyjs.solver.add_keyword_blanks import add_keyword_blanks
from cutyjs.solver.fix_double_blanks import fix_double_blanks
from cutyjs.solver.fix_import_order import fix_import_order
from cutyjs.solver.fix_indentation import fix_indentation
from cutyjs.solver.fix_line_ends import fix_line_ends
from cutyjs.solver.remove_blanks import remove_blanks

from langex.core.pipeline import Pipeline

solve_pipeline = (
  Pipeline
  | fix_import_order
  | compact
  | fix_indentation
  | fix_line_ends
  | remove_blanks
  | add_keyword_blanks
  | fix_double_blanks
  | add_eof_double_blanks
  | expand
)

