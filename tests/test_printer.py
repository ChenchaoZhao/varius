import varius


def test_ipython():

    assert not varius.is_ipython()


def test_latex_to_plain():

    assert varius.latex_to_plain(r"\text{abc}") == r"(abc)"

    assert varius.latex_to_plain(r"{\rm abc}") == r"(abc)"
