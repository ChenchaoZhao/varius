def test_storage():

    import varius

    assert varius.VARIABLE_STORAGE == {"default": dict()}

    varius.VARIABLE_STORAGE["v0"] = {"a": 0.1, "b": 0.1}

    assert varius.VARIABLE_STORAGE["v0"] == {"a": 0.1, "b": 0.1}

    varius.MagicGlobals.cv = "default"


def test_version():

    import varius

    assert varius.MagicGlobals.cv == "default"

    varius.MagicGlobals.cv = "v0"

    assert varius.MagicGlobals.cv == "v0"

    varius.MagicGlobals.cv = "default"


for name in dir():
    if not name.startswith("_"):
        del globals()[name]


def test_global_scope():

    import varius

    varius.MagicGlobals.cv = "v0"
    varius.VARIABLE_STORAGE["v0"] = {"a": 0.1, "b": 0.1}

    assert varius.MagicGlobals.cv == "v0"
    assert varius.VARIABLE_STORAGE["v0"] == {"a": 0.1, "b": 0.1}

    varius.reset_all()
    varius.MagicGlobals.cv == "default"

    assert "v0" not in varius.VARIABLE_STORAGE
    assert varius.MagicGlobals.cv == "default"


for name in dir():
    if not name.startswith("_"):
        del globals()[name]
