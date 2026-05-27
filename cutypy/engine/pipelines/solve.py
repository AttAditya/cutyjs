from cutypy.common.compact import compact
from cutypy.common.expand import expand
from cutypy.solver.add_eof_double_blanks import add_eof_double_blanks
from cutypy.solver.add_keyword_blanks import add_keyword_blanks
from cutypy.solver.fix_double_blanks import fix_double_blanks
from cutypy.solver.fix_import_order import fix_import_order
from cutypy.solver.fix_indentation import fix_indentation
from cutypy.solver.fix_line_ends import fix_line_ends
from cutypy.solver.remove_blanks import remove_blanks

from langex.core.pipeline import Pipeline

solve_pipeline = (
  Pipeline
  | compact
  | fix_indentation
  | fix_line_ends
  | fix_import_order
  | remove_blanks
  | add_keyword_blanks
  | fix_double_blanks
  | add_eof_double_blanks
  | expand
)

