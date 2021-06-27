import varius


def test_storage():

    assert varius.VARIABLE_STORAGE == {"default": dict()}

    varius.VARIABLE_STORAGE["v0"] = {"a": 0.1, "b": 0.1}

    assert varius.VARIABLE_STORAGE["v0"] == {"a": 0.1, "b": 0.1}


def test_version():

    assert varius.MagicGlobals.cv == "default"

    varius.MagicGlobals.cv = "v0"

    assert varius.MagicGlobals.cv == "v0"


def test_global_scope():

    assert varius.MagicGlobals.cv == "v0"
    assert varius.VARIABLE_STORAGE["v0"] == {"a": 0.1, "b": 0.1}
