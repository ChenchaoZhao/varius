from typing import *


class Ops:

    MUL = "·"
    DIV = "/"
    ADD = "+"
    SUB = "-"
    NEG = "-"
    POS = "+"
    POW = "^"
    MOD = "mod"


def bracket(expr: Any, *ops: str) -> str:
    expr = str(expr)
    if any((op in expr) for op in ops):
        return f"({expr})"

    return expr


def sadd(v1: Any, v2: Any):

    try:
        if isinstance(v1, str) or isinstance(v2, str):
            raise TypeError
        return repr(v1 + v2)
    except TypeError:

        if v1 == 0:
            return str(v2)

        if v2 == 0:
            return str(v1)

        if v1 == v2:
            return smul(2, v1)

        v1 = bracket(v1, Ops.NEG, Ops.POS)
        v2 = bracket(v2, Ops.NEG, Ops.POS)
        return f"{v1} {Ops.ADD} {v2}"


def sneg(v: Any):
    try:
        if isinstance(v, str):
            raise TypeError
        return repr(-v)
    except TypeError:

        if v == 0:
            return "0"

        if isinstance(v, str) and v.startswith("-"):
            return v[1:]

        v = bracket(v, Ops.NEG, Ops.POS)

        return f"{Ops.NEG}{v}"


def ssub(v1: Any, v2: Any):

    try:
        if isinstance(v1, str) or isinstance(v2, str):
            raise TypeError
        return repr(v1 - v2)
    except TypeError:

        if v1 == 0:
            return sneg(v2)

        if v2 == 0:
            return str(v1)

        if v1 == v2:
            return "0"

        v1 = bracket(v1, Ops.NEG, Ops.POS)
        v2 = bracket(v2, Ops.NEG, Ops.POS)
        return f"{v1} {Ops.SUB} {v2}"


def smul(v1: Any, v2: Any):
    try:
        if isinstance(v1, str) or isinstance(v2, str):
            raise TypeError

        return repr(v1 * v2)
    except TypeError:

        if v1 == 1.0:
            return str(v2)

        if v2 == 1.0:
            return str(v1)

        if v1 == 0 or v2 == 0:
            return "0"

        if v1 == v2:
            return spow(v1, 2)

        v1 = bracket(v1, Ops.NEG, Ops.POS, Ops.MOD)
        v2 = bracket(v2, Ops.NEG, Ops.POS, Ops.MOD)

        return f"{v1} {Ops.MUL} {v2}"


def sdiv(v1: Any, v2: Any):
    try:
        if isinstance(v1, str) or isinstance(v2, str):
            raise TypeError

        return repr(v1 / v2)
    except TypeError:
        if v2 == 0:
            raise ZeroDivisionError

        if v2 == 1:
            return str(v1)
        if v1 == 0:
            return "0"

        if v1 == v2:
            return "1"

        else:
            v1 = bracket(v1, Ops.NEG, Ops.POS)
            v2 = bracket(v2, Ops.NEG, Ops.POS)
            return f"{v1} {Ops.DIV} {v2}"


def spow(base: Any, exponent: Any):
    try:
        if isinstance(base, str) or isinstance(base, str):
            raise TypeError

        return repr(base ** exponent)
    except TypeError:

        if base == 0:
            raise ValueError("Power base cannot be zero.")

        if base == 1:
            return "1"

        if exponent == 0:
            return "1"

        if exponent == 1:
            return str(base)

        base = bracket(base, Ops.ADD, Ops.SUB, Ops.MUL, Ops.DIV, Ops.MOD)
        exponent = bracket(exponent, Ops.ADD, Ops.SUB, Ops.MUL, Ops.DIV, Ops.MOD)

        return f"{base}{Ops.POW}{exponent}"
