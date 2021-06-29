for name in dir():
    if not name.startswith("_"):
        del globals()[name]

import varius
from varius import *


def test_vr():

    x = vr("cost [usd]", 100)

    print(x)

    x.latex_repr

    show(x)

    assert x.value == 100

    x.value = 200

    assert x.value == 200

    y = vr("revenue [usd]", 200)

    print(y / x)

    vr.ls()

    varius.reset_all()


def test_ex():

    assert varius.MagicGlobals.cv == "default"

    x = vr("cost [usd]", 100)

    y = vr("revenue [usd]", 200)

    z = ex("profit [usd]", y - x)

    w = ex("margin", z / y)

    z()

    w()

    assert z.value.evalf() == 200 - 100
    assert w.value.evalf() == (200 - 100) / 200

    ex.ls()

    print(z - w, z * w, z / w, z ** 2, z ** w)

    varius.reset_all()


def test_scope():

    n = note()
    print(n)

    with note("new", "default") as n:
        print(n)


def test_grad():

    x = vr("cost [usd]", 100)

    y = vr("revenue [usd]", 200)

    z = ex("profit [usd]", y - x)

    w = ex("margin", z.expr / y)

    assert isinstance(z.grad(), dict)

    assert isinstance(w.grad(), dict)

    with note("new", "default") as s:
        x(200)
        y(300)
        z()
        w()
        z.grad()
        w.grad()
        show(*vr.ls())
        show(*ex.ls())
        show(s)
