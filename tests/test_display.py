import varius.display as vd


def test_add():

    assert vd.sadd(1, 1) == "2"

    assert vd.sadd(1, "a") == "1 + a"

    assert vd.sadd("a", "b") == "a + b"

    assert vd.sadd("a", "a") == f"2 {vd.Ops.MUL} a"

    assert vd.sadd("a", 0) == "a"

    assert vd.sadd(0, "b") == "b"

    assert vd.sadd(0, 0) == "0"


def test_neg():

    assert vd.sneg(1) == "-1"

    assert vd.sneg("a") == "-a"
    assert vd.sneg("-a") == "a"
    assert vd.sneg(vd.sneg("a")) == "a"

    assert vd.sneg("a + b") == "-(a + b)"


def test_sub():

    assert vd.ssub(1, 1) == "0"

    assert vd.ssub(1, "a") == "1 - a"

    assert vd.ssub("a", "b") == "a - b"

    assert vd.ssub("a", "a") == "0"

    assert vd.ssub("a", 0) == "a"

    assert vd.ssub(0, "b") == "-b"

    assert vd.ssub(0, 0) == "0"


def test_mul():

    assert vd.smul(1, 1) == "1"

    assert vd.smul(1, 2) == "2"

    assert vd.smul(1, "a") == "a"

    assert vd.smul("a", "b") == f"a {vd.Ops.MUL} b"

    assert vd.smul("a", "a") == f"a{vd.Ops.POW}2"

    assert vd.smul(vd.sadd("a", 1), "b") == f"(a {vd.Ops.ADD} 1) {vd.Ops.MUL} b"

    assert vd.smul(vd.ssub("a", 1), "b") == f"(a {vd.Ops.SUB} 1) {vd.Ops.MUL} b"


def test_div():

    assert vd.sdiv(1, 1) == "1.0"

    assert vd.sdiv(0, 1) == "0.0"

    assert vd.sdiv(0, "a") == "0"

    assert vd.sdiv("a", "b") == f"a {vd.Ops.DIV} b"

    assert vd.sdiv("a", 1) == "a"

    assert vd.sdiv(vd.sadd("a", 1), "b") == f"(a {vd.Ops.ADD} 1) {vd.Ops.DIV} b"


def test_pow():

    assert vd.spow(1, 1) == "1"

    assert vd.spow(1, 0.5) == "1.0"

    assert vd.spow(1, "a") == "1"

    assert vd.spow("a", 1) == "a"

    assert vd.spow("a", 0) == "1"

    assert vd.spow("a", "b") == f"a{vd.Ops.POW}b"

    assert vd.spow("a+b-c", "d/e") == f"(a+b-c){vd.Ops.POW}(d/e)"
