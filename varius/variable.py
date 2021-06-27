from typing import *

import sympy
from IPython.display import Math

from . import EXPRESSION_STORAGE as ES
from . import VARIABLE_STORAGE as VS
from . import MagicGlobals as G

__all__ = ["Variable", "Expression"]


class Variable(sympy.Symbol):
    """An abstract variable that represents a numerical quantity."""

    def __new__(
        cls, name: str, value: Optional[Union[float, int]] = None, is_text: bool = True
    ):
        if is_text:
            name = "\\text{" + name + "}"
        instance = super(Variable, cls).__new__(cls, name)
        instance.is_text = is_text

        if G.cv is not None and value is not None:
            VS[G.cv][instance] = value

        return instance

    @property
    def value(self) -> Union[float, int]:
        if G.cv is not None:
            return self.__getitem__(G.cv)
        else:
            raise RuntimeError("Current version is `None`.")

    @value.setter
    def value(self, value: Union[float, int]):

        if G.cv is not None:
            self.__setitem__(G.cv, value)
        else:
            raise RuntimeError("Current version is `None`.")

    def __call__(self, value: Union[float, int]):
        self.value = value

    def __getitem__(self, version: str) -> Union[float, int]:
        if version in VS:
            if self in VS[version]:
                return VS[version][self]
            else:
                raise KeyError(
                    f"Variable `{self._name}` was not assigned a value in version `{version}`."
                )
        else:
            raise KeyError(f"Version `{version}` does not exist.")

    def __setitem__(self, version: str, value: Union[float, int]):
        if not isinstance(value, (float, int)):
            raise TypeError(
                f"Assigned value should be float or int but get {type(value)}"
            )
        if version not in VS:
            VS[version] = dict()
            ES[version] = dict()

        VS[version][self] = value

    def __repr__(self) -> str:
        if self.is_text:
            return self.name[len("\\text{") : -1]
        return self.name

    __str__ = __repr__

    def display(self):
        return Math(sympy.latex(self))


def eval_expr(expr, version: str = G.cv):
    val = VS[version]
    return expr.subs(val)


class Expression:
    def __init__(self, name: str, expr):
        self.name = name
        self.expr = expr

    def __call__(self, version: Optional[str] = None):
        if version is None:
            version = G.cv
        res = eval_expr(self.expr, version)
        ES[version][self.name] = res

        return res

    def __repr__(self):
        return f"{self.name} = {str(self.expr)}"

    __str__ = __repr__

    def display(self, evaluate: bool = True, version: Optional[str] = None):

        lhs = "\\text{" + self.name + "}"

        rhs = sympy.latex(self.expr)
        eq = lhs + " = " + rhs

        if not evaluate:
            return Math(eq)

        res = sympy.latex(self.__call__(version))

        if res == rhs:
            return Math(eq)

        eq += " = " + res

        return Math(eq)
