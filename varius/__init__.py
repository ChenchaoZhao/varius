from typing import Any, Dict

VARIABLE_STORAGE: Dict[str, Dict[str, float]] = {"default": dict()}
EXPRESSION_STORAGE: Dict[str, Dict[str, float]] = {"default": dict()}


class MagicGlobals:
    latex: bool = True  # use latex
    cv: str = "default"  # current version
    repr_indent: int = 2


def set_latex(use: bool = True):
    MagicGlobals.latex = use


from .scope import Scope as note
from .variable import Expression, Variable, eval_expr

vr = Variable
ev = eval_expr
ex = Expression

__all__ = ["note", "vr", "ev", "ex"]

__version__ = "0.1.0"
